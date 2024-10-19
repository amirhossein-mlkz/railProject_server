import os,sys,time

import Export_Constants
from PySide6.QtWidgets import QPushButton, QFileDialog, QApplication, QVBoxLayout, QWidget, QLabel, QProgressBar
import threading
from VideoCombiner import VideoCombiner
from pathConstans import pathConstants


os.system('pyside6-uic {} -o {}'.format(os.path.join('Export/ExportUIiFiles', 'export.ui'), os.path.join('Export/ExportUIiFiles', 'ui_export.py')))
os.system('pyside6-rcc {} -o {}'.format('Export/resources/assets.qrc','Export/assets_rc.py'))
os.system('pyside6-rcc {} -o {}'.format('Export/resources/assets.qrc','Export/assets_rc.py'))
# os.system('pyside6-rcc {} -o {}'.format('Export/ExportUIiFilesresources/assets.qrc','ExportUIiFiles/assets_rc.py'))

sys.path.append('Export')




from PySide6.QtWidgets import (
    QDialog, 
    QApplication,
    QWidget,
    QTableWidgetItem,
    QFrame,
    QStackedWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QComboBox
)
from PySide6.QtWidgets import QApplication as sQApplication
from PySide6.QtCore import Qt, QPoint


from ExportUIiFiles.ui_export import Ui_userProfile
from Calendar import JalaliCalendarDialog
from uiUtils.guiBackend import GUIBackend
from Tranform.transformModule import archiveManager





MKV_FORMAT = 'mkv'
MP4_FORMAT = 'mp4'




# ui class
class UIExport(QWidget):

    def __init__(self,archive_manager = None,train_name = None,date = None,selected_camera=None):
        super(UIExport, self).__init__()



        self.ui = Ui_userProfile()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.__center()
        self.offset = None



        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.btn_dst_path.clicked.connect(self.open_folder_dialog)
        self.ui.btn_start_copy.clicked.connect(self.get_available_files)
        
        self.ui.radioButton_mkv.toggled.connect(self.set_format)
        self.ui.radioButton_mp4.toggled.connect(self.set_format)

        self.archive_manager = archive_manager
        self.train_name = train_name
        self.date = date
        self.selected_camera = selected_camera


        # Connect signals
        self.ui.spinBox_hour_start.valueChanged.connect(self.adjust_end_time)
        self.ui.spinBox_minute_start.valueChanged.connect(self.adjust_end_time)
        self.ui.spinBox_hour_end.valueChanged.connect(self.validate_end_time)
        self.ui.spinBox_minute_end.valueChanged.connect(self.validate_end_time)





        self.set_init_details()


    def set_init_details(self):

        self.ui.lbl_train_name.setText(self.train_name)
        self.ui.lbl_date.setText(self.date.strftime("%Y/%m/%d"))

        self.set_format()




    def __center(self) -> None:
        """Centers the dialog on the screen based on the current primary screen's geometry."""
        primary_screen = QApplication.primaryScreen()
        if primary_screen:
            screen_geometry = primary_screen.geometry()
            center_point = screen_geometry.center()
            self.move(center_point.x() - self.frameGeometry().width() // 2,
                      center_point.y() - self.frameGeometry().height() // 2)



    def close_win(self) -> None:
        """Closes the window."""
        self.close()

    def mousePressEvent(self, event) -> None:
        """Enables the dialog to be moved by dragging."""
        if event.button() == Qt.LeftButton and event.position().y() < self.ui.top_frame.height():
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event) -> None:
        """Handles the dialog movement when dragged."""
        if not hasattr(self, 'move_refresh_time'):
            self.move_refresh_time = 0
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            if time.time() - self.move_refresh_time > Export_Constants.RefreshRates.WINDOW_MOVE:
                self.move_refresh_time = time.time()
                self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        """Finalizes the dragging operation by clearing the offset."""
        self.offset = None
        super().mouseReleaseEvent(event)




    def open_folder_dialog(self):
        # Open a folder selection dialog
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

        # If a folder is selected, update the label
        if folder_path:
            self.ui.lbl_selected_folder.setText(f"{folder_path}")


        else:
            self.ui.lbl_selected_folder.setText("No folder selected")




    def set_format(self):

        if self.ui.radioButton_mkv.isChecked():
            self.convert_mkv = True
            self.format_name = MKV_FORMAT
        elif self.ui.radioButton_mp4.isChecked():
            self.convert_mkv = False
            self.format_name = MP4_FORMAT
        else:
            print('Error in format')


    def creata_file_path(self):
        try:
            start_time = 's{}_{}'.format(str(self.ui.spinBox_hour_start.value()),str(self.ui.spinBox_minute_start.value()))
            finish_time = 'e{}_{}'.format(str(self.ui.spinBox_hour_end.value()),str(self.ui.spinBox_minute_end.value()))
            video_name = '{}_{}_{}_{}.{}'.format(self.train_name,self.date,start_time,finish_time,self.format_name)
            main_path = self.ui.lbl_selected_folder.text()
            if main_path =='' or main_path == "No folder selected":
                return None
            path = os.path.join(main_path,video_name)
            return path
        except:
            return None

    def create_dst_file(self):


        
        self.dst_path = self.creata_file_path()
        # dst_path = 'test.mkv'     ########################### TEMP

        if self.dst_path is None:
            self.show_message(1,'Error in Destination Path')
            self.finish_export()
            return None
        
        else:
            return self.dst_path

    def get_available_files(self):

        self.ui.btn_start_copy.setDisabled(True)

        if self.create_dst_file():

            self.show_message(0,'Collecting Videos')


            self.archive_manager.get_day_time_ranges(train_id=self.train_name, 
                                            date=self.date, 
                                            cameras=[self.selected_camera],
                                            finish_func=self.prepare_copy, 
                                            progress_func=self.date_ranges_progress)
            


    def filter_hour(self,pathes,start_time:list,end_time:list):

        filter_pathes = []

        for path in pathes:

            minute = int(path.split('\\')[-2])
            hour = int(path.split('\\')[-3])

            if start_time[0]<=hour<=end_time[0]:

                if start_time[0] == hour :
                    if minute< start_time[1]:
                        continue
                    else:
                        filter_pathes.append(path)

                
                elif end_time[0] == hour:
                    if minute> end_time[1]:
                        continue
                    else:
                        filter_pathes.append(path)        

                else:

                    filter_pathes.append(path)
        
        return filter_pathes







    def prepare_copy(self, date_ranges:dict[str, list]):
        try:




            self.date_ranges = date_ranges
            self.input_videos = date_ranges[self.selected_camera]['paths']

            start_time = [self.ui.spinBox_hour_start.value(),self.ui.spinBox_minute_start.value()]
            end_time = [self.ui.spinBox_hour_end.value(),self.ui.spinBox_minute_end.value()]

            if self.input_videos is not None:

                self.input_videos = self.filter_hour(pathes=self.input_videos,start_time=start_time,end_time=end_time)
                if len(self.input_videos)>0:

                    self.start_copy(self.input_videos,self.dst_path)
                else:
                    self.show_message(1,'No Video in This Filter')
                    self.finish_export()



            else:
                self.show_message(1,'Error in Read Videos')
                self.finish_export()
        except:
                self.show_message(1,'Error in Read Videos')
                self.finish_export()

    def date_ranges_progress(self, value:float):
        value = int(value * 1000) #denormal
        self.ui.progressBar.setValue(value)





    def start_copy(self,input_files,dst_path):



        if input_files is None:
            self.show_message(1,'Error in Read Videos')
            self.finish_export()
            return



        if dst_path:
            temp_output_file = 'temp_combined.mp4'  # Temporary MP4 file
            self.combine_videos(input_files, temp_output_file, dst_path)

    def combine_videos(self, input_videos, temp_output_file, final_output_file):
        self.worker = VideoCombiner(input_videos, temp_output_file, final_output_file,self.convert_mkv)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.conversion_progress_signal.connect(self.update_progress)
        self.worker.status_signal.connect(self.show_message)
        self.worker.finish_signal.connect(self.finish_export)
        self.worker.start()

        # self.worker.run()

    def update_progress(self, value):
        self.ui.progressBar.setValue(value)
    
    def show_message(self,mode:int,message:str):

        if mode==0:
            self.ui.lbl_msg.setStyleSheet("color:#2E2A3D")
        else:
            self.ui.lbl_msg.setStyleSheet("color:red")

        self.ui.lbl_msg.setText(message)




        
    def finish_export(self):

        self.ui.btn_start_copy.setDisabled(False)













    def adjust_end_time(self):
        start_hour = self.ui.spinBox_hour_start.value()
        start_minute = self.ui.spinBox_minute_start.value()

        end_hour = self.ui.spinBox_hour_end.value()
        end_minute = self.ui.spinBox_minute_end.value()

        # If end time is earlier than start time, adjust it
        if (end_hour < start_hour) or (end_hour == start_hour and end_minute < start_minute):
            self.ui.spinBox_hour_end.setValue(start_hour)
            self.ui.spinBox_minute_end.setValue(start_minute)

    def validate_end_time(self):
        # If end time is earlier than start time, reset end time
        start_hour = self.ui.spinBox_hour_start.value()
        start_minute = self.ui.spinBox_minute_start.value()

        end_hour = self.ui.spinBox_hour_end.value()
        end_minute = self.ui.spinBox_minute_end.value()

        if (end_hour < start_hour) or (end_hour == start_hour and end_minute < start_minute):
            self.ui.spinBox_hour_end.setValue(start_hour)
            self.ui.spinBox_minute_end.setValue(start_minute)





if __name__ == "__main__":


    # from uiUtils.Calendar import  JalaliCalendarDialog
    # from Calendar import JalaliCalendarDialog


    app = sQApplication()

    win = UIExport()

    # win.set_calendar_obj(JalaliCalendarDialog)
 
    win.show()
    sys.exit(app.exec())
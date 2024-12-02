import os,sys,time
from datetime import time as dt_time

from persiantools.jdatetime import JalaliDateTime

import Export_Constants
from PySide6.QtWidgets import QPushButton, QFileDialog, QApplication, QVBoxLayout, QWidget, QLabel, QProgressBar
import threading
from VideoCombiner import VideoCombiner
from pathsConstans import pathConstants


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


from ExportUIiFiles.ui_export import Ui_ExportDialog
from Calendar import JalaliCalendarDialog
from uiUtils.guiBackend import GUIBackend
from Tranform.transformModule import archiveManager





MKV_FORMAT = 'mkv'
MP4_FORMAT = 'mp4'




# ui class
class UIExport(QWidget):

    

    def __init__(self,archive_manager:archiveManager = None,train_name = None,date = None,selected_camera=None):
        super(UIExport, self).__init__()



        self.ui = Ui_ExportDialog()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.__center()
        self.offset = None



        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.btn_dst_path.clicked.connect(self.open_folder_dialog)
        self.ui.start_export_btn.clicked.connect(self.get_available_files)
        
        self.ui.radioButton_fasters.toggled.connect(self.set_format)
        self.ui.radioButton_best_compression.toggled.connect(self.set_format)

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
        defalt_dir = self.generate_default_export_folder()
        self.ui.lbl_selected_folder.setText(f"{defalt_dir}")


    def show_win(self,):
        self.setWindowModality(Qt.ApplicationModal)
        self.show()

    def generate_default_export_folder(self, folder_name='Radco Export'):
        documents_path = os.path.join(os.environ['USERPROFILE'], 'Documents')
        path =  os.path.join(documents_path, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path


    def set_init_details(self):

        self.ui.lbl_train_name.setText(self.train_name)
        self.ui.lbl_date.setText(self.date.strftime("%Y/%m/%d"))
        self.ui.spinBox_hour_end.setValue(23)
        self.ui.spinBox_minute_end.setValue(59)
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

        if self.ui.radioButton_fasters.isChecked():
            self.compression = False
        elif self.ui.radioButton_best_compression.isChecked():
            self.compression = True
        else:
            print('Error in format')


    def creata_file_path(self):
        try:
            start_time = 's{}_{}'.format(str(self.ui.spinBox_hour_start.value()),str(self.ui.spinBox_minute_start.value()))
            finish_time = 'e{}_{}'.format(str(self.ui.spinBox_hour_end.value()),str(self.ui.spinBox_minute_end.value()))
            video_name = '{}_{}_{}_{}'.format(self.train_name,self.date,start_time,finish_time)
            video_dir = self.ui.lbl_selected_folder.text()
            if video_dir =='' or video_dir == "No folder selected":
                return None
            return video_dir, video_name
        except:
            return None, None

    def create_dst_file(self):
        export_dir, export_fname = self.creata_file_path()

        if export_dir is None:
            self.show_message(1,'Please Select An Output Directory')
            self.finish_export()
            return None, None
        
        else:
            return export_dir, export_fname

    def get_available_files(self):

        self.ui.start_export_btn.setDisabled(True)
        export_dir, export_fname = self.create_dst_file()

        if export_dir is not None and export_fname is not None:

            self.show_message(0,'Collecting Videos')

            start_time, end_time = self.get_times_input()
            

            files_info = self.archive_manager.filter_files(
                                train_id=self.train_name,
                                date=self.date,
                                camera=self.selected_camera,
                                start_time=start_time,
                                end_time=end_time
                            )
            

            if len(files_info)>0:
                input_videos = list(map(lambda x:x['path'], files_info))
                if input_videos is None:
                    self.show_message(1,'Error in Read Videos')
                    self.finish_export()
                    return
                
                self.combine_videos(input_videos, export_dir, export_fname)
            else:
                self.show_message(1,'No Video in This Filter')
                self.finish_export()


            

    def get_times_input(self,)-> tuple[JalaliDateTime, JalaliDateTime]:
        start_h = self.ui.spinBox_hour_start.value()
        start_m = self.ui.spinBox_minute_start.value()
    
        end_h = self.ui.spinBox_hour_end.value()
        end_m = self.ui.spinBox_minute_end.value()

        start_time = dt_time(start_h, start_m, 0)
        end_time = dt_time(end_h, end_m, 59)

        return JalaliDateTime.combine(self.date, start_time), JalaliDateTime.combine(self.date, end_time)
    

    def date_ranges_progress(self, value:float):
        value = int(value * 1000) #denormal
        self.ui.progressBar.setValue(value)


    def combine_videos(self, input_videos, export_dir, export_fname):
        self.worker = VideoCombiner(input_videos, export_dir, export_fname, self.compression)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.status_signal.connect(self.show_message)
        self.worker.finish_signal.connect(self.finish_export)
        self.worker.start()

        # bself.worker.run()

    def update_progress(self, value):
        self.ui.progressBar.setValue(value)
    
    def show_message(self,mode:int,message:str):

        if mode==0:
            self.ui.lbl_msg.setStyleSheet("color:#2E2A3D")
        else:
            self.ui.lbl_msg.setStyleSheet("color:red")

        self.ui.lbl_msg.setText(message)




        
    def finish_export(self):
        self.ui.start_export_btn.setEnabled(True)


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

    app = sQApplication()
    win = UIExport()
 
    win.show()
    sys.exit(app.exec())
import os
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'calendar.ui'), os.path.join('UIFiles', 'calendar.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'main_UI.ui'), os.path.join('UIFiles', 'main_UI.py')))
os.system('CMD /C pyside6-rcc assets.qrc -o assets.py')#PySide
##############################################################################################################################

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as sQtCore
from PySide6.QtWidgets import QMainWindow as sQMainWindow
from PySide6.QtWidgets import QApplication as sQApplication
from PySide6.QtWidgets import QVBoxLayout, QWidget, QComboBox, QGridLayout, QLabel, QDialog,QDialogButtonBox,QPushButton,QFrame
import sys,os,platform,time,subprocess,threading
from copy_ping import ShareCopyWorker
from persiantools.jdatetime import JalaliDateTime
from guiBackend import GUIBackend
from PySide6.QtCore import QTimer
from login import LoginPage
from PySide6.QtCore import Qt
from UIFiles.main_UI import Ui_MainWindow

from PySide6.QtWidgets import QGraphicsBlurEffect
from PySide6.QtGui import QFont,QIcon
from timeLine import TimelineSlider
from PagesUI.settingPageUI import settingPageUI
from PagesUI.downloadPageUI import downloadPageUI
from PagesUI.playbackPageUI import playbackPageUI
import assets

from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QEvent


from constanst import ONE_HOUR
from uiUtils import GUIComponents


# ui class
class UI_main_window_org(sQMainWindow):

    def __init__(self):
        super(UI_main_window_org, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.all_style_repoblish()

        self.settingPageUI = settingPageUI(self.ui)
        self.downloadPageUI = downloadPageUI(self.ui)
        self.playbackPageUI = playbackPageUI(self.ui)

        self.setWindowTitle("Sepanta RailWay Monitoring")
        # window setup
        self.setWindowTitle("Iran RailWay Monitoring")
        # Set the window icon
        self.setWindowIcon(QIcon(":/icons/icons/download.png"))


        self.button_connector()
        
        # Create a central widget
        central_widget = self.ui.calendar_widget
        



        # timeline_widget = self.layout_timeline
        self.timeline = TimelineSlider(duration_ms=ONE_HOUR,played_color="green", unplayed_color="green",
                                     played_red_color="red", unplayed_red_color="red",
                                     show_dividers=False, groove_height=25,time_label=self.ui.time_label)


        self.timeline.set_minutes_segments([])
        # GUIBackend.add_widget(self.frame_timeline,self.timeline)
        GUIBackend.add_widget(self.ui.layout_timeline,self.timeline)



        self.preview_login = False



        # Create animations
        self.animation = QPropertyAnimation(self.ui.toggle_frame, b"geometry")
        self.animation.setDuration(1500)  # Duration in milliseconds (1.5 seconds)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)  # Easing curve for smooth animation

        # Connect the button's clicked event
        self.ui.btn_logo.clicked.connect(self.toggle_frame_visibility)
        self.ui.btn_logo.installEventFilter(self)  # Install an event filter to handle double clicks
        self.hide_all_messages()



    def all_style_repoblish(self,):
        #for widget in self.ui.
        
        for atr_name in dir(self):
            atr = getattr(self, atr_name)
            try:
                atr.style().unpolish(atr)
                atr.style().polish(atr)
            except:
                pass
        
        


    def hide_all_messages(self,):
        self.ui.add_station_message.hide()
        self.ui.modify_station_message.hide()
        self.ui.download_filter_message.hide()
        self.ui.refresh_image_db_message.hide()

    def toggle_frame_visibility(self):
        if self.ui.toggle_frame.isVisible():
            # Animate closing
            self.animation.setStartValue(self.ui.toggle_frame.geometry())
            self.animation.setEndValue(QRect(self.ui.toggle_frame.x(), self.ui.toggle_frame.y(), 0, self.ui.toggle_frame.height()))
            self.animation.start()
            self.ui.toggle_frame.setVisible(False)
        else:
            # Animate opening
            self.ui.toggle_frame.setVisible(True)
            self.animation.setStartValue(QRect(self.ui.toggle_frame.x(), self.ui.toggle_frame.y(), 0, self.ui.toggle_frame.height()))
            self.animation.setEndValue(QRect(self.ui.toggle_frame.x(), self.ui.toggle_frame.y(), 200, self.ui.toggle_frame.height()))
            self.animation.start()

    def eventFilter(self, source, event):
        if source == self.ui.btn_logo and event.type() == QEvent.MouseButtonDblClick:
            # Hide frame on double click with animation
            if self.ui.toggle_frame.isVisible():
                self.animation.setStartValue(self.ui.toggle_frame.geometry())
                self.animation.setEndValue(QRect(self.ui.toggle_frame.x(), self.ui.toggle_frame.y(), 0, self.ui.toggle_frame.height()))
                self.animation.start()
                self.ui.toggle_frame.setVisible(False)
            return True
        return super(UI_main_window_org, self).eventFilter(source, event)


    def open_calender(self, name:str):
        
        self.calenders[name].show()

    def button_connector(self):

        self.ui.btn_side_playback.clicked.connect(self.set_stack_widget)
        self.ui.btn_side_download.clicked.connect(self.set_stack_widget)
        self.ui.btn_side_settings.clicked.connect(self.set_stack_widget)
        self.ui.btn_side_aboutus.clicked.connect(self.set_stack_widget)


        



    def show_login(self):
        if not  self.preview_login:
            self.applyBlurEffect()
            self.login_ui = LoginPage(self)
            self.login_ui.show()
            self.preview_login = True
            self.login_ui.open_button.clicked.connect(self.check_password)
            self.login_ui.close_button.clicked.connect(self.close_login)

    def close_login(self):
            self.preview_login = False

    def check_password(self):

        password = self.login_ui.password
        self.preview_login = False
        if password != '':
            res = self.db.fetch_table_as_dict(table_name='password')
            if len(res)==1:
                res = res[0]
                if str(password) == str(res['password']):
                    self.login_ui.close()
                    self.update_log('Login Succussfully')
                    self.show_timeline(mode=True)

                else:
                    self.show_error('Password is Wrong')

    def time_line_copy(self):
        self.show_timeline(mode=False)

        if  self.start_date.text() !='' and  self.end_date.text() !='':

            start_time={}
            get_time = self.timeEdit_start.time()
            h = get_time.hour()
            m = get_time.minute()
            

            get_date = self.start_date.text().split('/')

            start_time = JalaliDateTime.now()
            start_time = start_time.replace(year=int(get_date[0]),month=int(get_date[1]),day = int(get_date[2]), hour=h,minute=m)
            print(start_time)


            get_time = self.timeEdit_end.time()
            h = get_time.hour()
            m = get_time.minute()

            get_date = self.end_date.text().split('/')


            end_time = JalaliDateTime.now()
            end_time = end_time.replace(year=int(get_date[0]),month=int(get_date[1]),day = int(get_date[2]), hour=h,minute=m)

            print(end_time)

            if end_time<start_time:
                print('End time should be bigger than start time')
                self.show_error('End time should be bigger than start time')



    def covert_date(self,jdatetime):
        date = jdatetime.strftime('%Y/%m/%d')
        return date
    
    def set_stack_widget(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "btn_side_playback":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_playback)
        if btnName == "btn_side_download":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_download)
        if btnName == "btn_side_settings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
        if btnName == "btn_side_aboutus":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_playback)


    def close_win(self):
        self.close()
        # pid = os.getpid()
        # os.kill(pid, SIGKILL)
        sys.exit()

    def minimize_win(self):
        self.showMinimized()



    def load_fields(self):
        res = self.db.fetch_table_as_dict()
        if len(res)==1:
            res = res[0]
            self.ui.ip_input.setText(res['ip'])
            self.ui.username_input.setText(res['username'])
            self.ui.password_input.setText(res['password'])

    


    def save_ip(self):
        self.db.update_row_by_id_zero(column_name='ip',new_value=self.ip_input.text())
    def save_username(self):
        self.db.update_row_by_id_zero(column_name='username',new_value=self.username_input.text())
    def save_password(self):
        self.db.update_row_by_id_zero(column_name='password',new_value=self.password_input.text())

    def load_pathes(self):
        res = self.db.fetch_table_as_dict(table_name='pathes')
        if len(res)==1:
            res = res[0]
            self.src_path = res['folder_to_copy']
            self.dst_path = res['destination_folder']


    def start_copy(self):
        ip = self.ui.ip_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        src_path = self.src_path
        dst_path = self.dst_path

        # if ip and username and password and src_path and dst_path:
        if self.ping_host(ip):
            conn_details = {
                'ip': ip,
                'username': username,
                'password': password,
                'share': src_path
            }
            self.worker = ShareCopyWorker(src_path, dst_path, conn_details)
            self.worker.progress.connect(self.update_progress)
            self.worker.log.connect(self.update_log)
            self.worker.completed.connect(self.copy_completed)
            self.worker.error.connect(self.show_error)
            self.worker.start()
            # self.worker.run()
        else:
            self.show_error("Ping failed. Check the IP address and try again.")
        # else:
        #     self.log_label.setText("Please fill all fields.")

    def ping_host(self, ip):

        try:
            # Determine the ping command based on the OS
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param, "1", ip]
            
            # Run the command
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if output.returncode == 0:
                self.update_log('1 packets transmitted, 1 packets received')
                return True
            # Display the result
            # if output.returncode == 0:
            #     self.result_area.setPlainText(f"Ping to {ip_address} successful!\n{output.stdout}")
            else:
                self.update_log(f"Ping to {ip} failed!\n{output.stderr}")

                return False
        except Exception as e:
            self.update_log(f"Ping to {ip} failed!\n{output.stderr}")

            return False


    def update_progress(self, value):
        print(value)
        self.ui.progress_bar.setValue(value)

    def update_log(self, message):
        self.ui.log_label.setText(message)
        QTimer.singleShot(3000, lambda: self.show_error(''))

    def copy_completed(self):
        self.ui.progress_bar.setValue(100)
        self.ui.log_label.setText("Copy Completed!")
        # threading.Timer(3,self.update_log,args=('',)).start()
        # threading.Timer(3,self.update_progress,args=(0,)).start()


    def show_error(self, error):
        if error !='':
            self.ui.log_label.setText(f"Error: {error}")
        else:
            self.ui.log_label.setText('')

        QTimer.singleShot(3000, lambda: self.show_error(''))



    def show_timeline(self,mode):
        self.frame_date.setVisible(mode) 

        



    def applyBlurEffect(self):
        current_effect = self.graphicsEffect()
        if current_effect:
            self.setGraphicsEffect(None)
        else:
            blur_effect = QGraphicsBlurEffect()
            blur_effect.setBlurRadius(10)
            self.setGraphicsEffect(blur_effect)


    def get_combo_values(self,combo_name):
        name = GUIBackend.get_combobox_selected(combo_name)
        return name



    

    def append_ping_result(self, result):
        """Append the ping result to the QTextEdit."""
        # print(result)
        self.ui.textEdit_ping_status.append(result)


    def clear_ping_result(self):
        self.ui.textEdit_ping_status.setText('')

    

    


    
            

    










    def set_item_combo_box(self,combo_name,items):

        GUIBackend.set_combobox_items(combo_name,items)
  

    def ret_current_value_combo_box(self,combo_name):
        return combo_name.currentText()
        


    def update_image(self, pixmap):
        # Resize the image to fit the label
        # self.show_image.setPixmap(pixmap.scaled(self.show_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.ui.show_image.setPixmap(pixmap.scaled(self.show_image.size()))#, Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def show_confirmbox(self, title:str, text:str, buttons:list[str]):
        confirmbox = GUIComponents.confirmMessageBox(title, text, buttons)
        return confirmbox.render()




if __name__ == "__main__":



    from api import API
    app = sQApplication()

    win = UI_main_window_org()
    api = API(win)
    win.show()
    sys.exit(app.exec())
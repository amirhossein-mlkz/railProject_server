##############################################################################################################################
import sys,os,platform,time,subprocess,threading

from PySide6.QtUiTools import loadUiType
from PySide6 import QtCore as sQtCore
from PySide6.QtWidgets import QMainWindow as sQMainWindow
from PySide6.QtWidgets import QVBoxLayout, QWidget, QComboBox, QGridLayout, QLabel, QDialog,QDialogButtonBox,QPushButton,QFrame , QStatusBar
from copy_ping import ShareCopyWorker
from persiantools.jdatetime import JalaliDateTime
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsBlurEffect
from PySide6.QtGui import QFont,QIcon

from PagesUI.settingPageUI import settingPageUI
from PagesUI.downloadPageUI import downloadPageUI
from PagesUI.playbackPageUI import playbackPageUI
from UIFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
import assets

from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QEvent
from Styles import SideBtnsStyle

from constanst import ONE_HOUR
from uiUtils import GUIComponents
from backend.utils.ShowQuestion import show_question
from backend.utils import texts
from login import LoginPage
from Export.export import UIExport

# ui class
class UI_main_window_org(sQMainWindow):

    def __init__(self):
        super(UI_main_window_org, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.all_style_repoblish()
        self.language = 'English'

        self.settingPageUI = settingPageUI(self.ui)
        self.downloadPageUI = downloadPageUI(self.ui)
        self.playbackPageUI = playbackPageUI(self.ui)

        self.setWindowTitle("Sepanta RailWay Monitoring")
        # window setup
        self.setWindowTitle("Iran RailWay Monitoring")
        # Set the window icon
        self.setWindowIcon(QIcon(":/icons/icons/download.png"))

        # window setup
        flags = sQtCore.Qt.WindowFlags(
            sQtCore.Qt.FramelessWindowHint
        )  # remove the windows frame of ui
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self._old_pos = None

        # Create a QStatusBar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Set the maximum height for the status bar (e.g., 30 pixels)
        self.status_bar.setMaximumHeight(10)


                # Set the background color and text color using a stylesheet
        self.status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #262632;  /* Background color */
            }
        """)

        self.button_connector()
        
        # Create a central widget
        central_widget = self.ui.calendar_widget


        self.side_btns = {
            'playback':self.ui.btn_side_playback,
            'download':self.ui.btn_side_download,
            'settings':self.ui.btn_side_settings
            }
        



        # timeline_widget = self.layout_timeline
        # self.timeline = TimelineSlider(duration_ms=ONE_HOUR,played_color="green", unplayed_color="green",
        #                              played_red_color="red", unplayed_red_color="red",
        #                              show_dividers=False, groove_height=25,time_label=self.ui.time_label)


        # self.timeline.set_minutes_segments([])
        # GUIBackend.add_widget(self.frame_timeline,self.timeline)
        # GUIBackend.add_widget(self.ui.layout_timeline,self.timeline)



        self.login_obj = LoginPage()




        # Create animations
        self.animation = QPropertyAnimation(self.ui.toggle_frame, b"geometry")
        self.animation.setDuration(1500)  # Duration in milliseconds (1.5 seconds)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)  # Easing curve for smooth animation

        self.ui.pages_stackwidget.setCurrentWidget(self.ui.page_playback)

        # Connect the button's clicked event
        # self.ui.btn_logo.clicked.connect(self.toggle_frame_visibility)
        # self.ui.btn_logo.installEventFilter(self)  # Install an event filter to handle double clicks
        self.hide_all_messages()


        self.ui.btn_side_playback.click()


    


    def mousePressEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton and not self.isMaximized():
            # accept event only on top bar
            if (
                event.position().y() <= self.ui.softeware_top_frame.height()
            ):
                self._old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = None



    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = sQtCore.QPoint(event.globalPosition().toPoint() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPosition().toPoint()




    def all_style_repoblish(self,):
        #for widget in self.ui.
        for atr_name in dir(self.ui):
            try:
                atr = getattr(self.ui, atr_name)
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

        
        # self.ui.btn_side_aboutus.clicked.connect(self.set_stack_widget)


        self.ui.close_btn.clicked.connect(self.close_win)
        self.ui.maximize_btn.clicked.connect(self.toggle_maximize)

        self.ui.minimize_btn.clicked.connect(self.minimize_win)



    



    

    def set_user(self,is_login=True,user_name = ''):

        if is_login:
            self.ui.btn_side_login.setText('User : '+user_name)
            self.ui.btn_side_login.setStyleSheet('icon: url(:/icons/icons/username.png);')
        else:             
            self.ui.btn_side_login.setText('  Login')
            self.ui.btn_side_login.setStyleSheet('icon: url(:/icons/icons/icons8-login-100 (3).png);')







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
            self.ui.pages_stackwidget.setCurrentWidget(self.ui.page_playback)
        elif btnName == "btn_side_download":
            self.ui.pages_stackwidget.setCurrentWidget(self.ui.page_download)
        elif btnName == "btn_side_settings":
            self.ui.pages_stackwidget.setCurrentWidget(self.ui.page_settings)
        elif btnName == "btn_side_aboutus":
            self.ui.pages_stackwidget.setCurrentWidget(self.ui.page_playback)



        self.clear_side_btns()

        self.set_side_click_btn(btn)


    def set_side_click_btn(self,btn):
        

        name = btn.objectName()
        name = name.split('_')[-1]
    
        style = SideBtnsStyle['click'][name]
        btn.setStyleSheet(style)

    def clear_side_btns(self):





        # for btn in self.side_btns:

        for btn,style in SideBtnsStyle['normal'].items():


            btn = self.side_btns[btn]
            btn.setStyleSheet(style)

            # current_style = btn.styleSheet()

            # # Check if the border is applied
            # if "border-left" in current_style:
            #     # If the border exists, clear it
            #     new_style = current_style.replace('border-left: 5px solid #D43D41;', '').strip()
            #     btn.setStyleSheet(new_style)
            


            




    def close_win(self):

        ret = show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['Close'][self.language])
        if ret:
            self.close()
            # pid = os.getpid()
            # os.kill(pid, SIGKILL)
            sys.exit()

    def minimize_win(self):
        self.showMinimized()


        
    def toggle_maximize(self):
        """Function to toggle between maximizing and restoring the window."""
        if self.isMaximized():
            self.showNormal()  # Restore the window to its original size
        else:
            self.showMaximized()  # Maximize the window


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





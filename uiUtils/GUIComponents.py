from PySide6.QtWidgets import QWidget, QFrame, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy,QPushButton, QMessageBox
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap, QIcon

TABEL_BUTTON_STYLE = """
    QPushButton{ 
        background-color: rgba(255,255,255,0);
        min-height:0px; min-width:0px; 
        width:auto;
        qproperty-iconSize: 24px;
        } 
    """


CONFIRMBOX_STYLESHEET = """
   QMessageBox{ 
        background-color: #ffffff;

    }
    
    QPushButton{
        border: none;
        font-weight: bold;
        color: #ffffff;
        background-color:rgb(6, 76, 130);
        min-height: 25px;
        border-radius: 5px;
        min-width:100px;
        font-size:12px;
	
        }

    QPushButton:hover{
	    background-color:rgb(22, 38, 76);
    }
"""

class MessageWidget(QWidget):
    # Constants for border colors
    SUCCESS_COLOR = "#00CB51"  # Green
    ERROR_COLOR = "#ff4444"    # Red
    INFO_COLOR = "#33B5E5"     # Blue
    BORDER_RADIUS = "10px"     # Border radius for the frame

    def __init__(self, parent=None):
        super().__init__(parent)

        # Main frame for the message
        self.frame = QFrame(self)
        # self.frame.setFixedHeight(80)
        # self.frame.setFixedWidth(280)

        # Set a unique object name (ID) for the frame to target it in the stylesheet
        self.frame.setObjectName("messageFrame")
        # Set border-radius and transparency for the frame
        self.frame.setStyleSheet(f"#{self.frame.objectName()} {{ border-radius: {self.BORDER_RADIUS}; background: transparent; }}")

        # Horizontal layout for icon and message text
        self.layout = QHBoxLayout(self.frame)

        # Icon label for message type
        self.icon_label = QLabel(self)
        self.icon_label.setFixedSize(30, 30)
        self.icon_label.setScaledContents(True)
        # Make icon label transparent
        self.icon_label.setStyleSheet("background: transparent;")

        # Text label for the message
        self.text_label = QLabel(self)
        self.text_label.setWordWrap(True)
        self.text_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # Align text to the left and vertically centered
        # Make text label transparent
        self.text_label.setStyleSheet("background: transparent;")

        # Adding widgets to the layout (icon and text label without spacer)
        self.layout.addWidget(self.icon_label)
        self.layout.addWidget(self.text_label)

        # Main layout for the widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.frame)
        self.setLayout(main_layout)

        # Timer to hide the widget after a certain period
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hide)

    def show_message(self, message: str, msg_type="info", display_time=3000):
        """
        Shows the message widget with the specified message and type.

        :param message: The message to display.
        :param msg_type: The type of the message ("success", "error", "info").
        :param display_time: The time in milliseconds to display the message before hiding it.
        """
        if not message:
            self.hide()
            return

        # Set message text
        self.text_label.setText(message)

        # Set the corresponding icon and border color based on message type
        if msg_type == "success":
            self.icon_label.setPixmap(QPixmap(":/icons/icons/success.png"))  # Use success icon from resources
            self.frame.setStyleSheet(f"#{self.frame.objectName()} {{ border: 2px solid {self.SUCCESS_COLOR}; border-radius: {self.BORDER_RADIUS}; background: transparent; }}")
        elif msg_type == "error":
            self.icon_label.setPixmap(QPixmap(":/icons/icons/error.png"))  # Use error icon from resources
            self.frame.setStyleSheet(f"#{self.frame.objectName()} {{ border: 2px solid {self.ERROR_COLOR}; border-radius: {self.BORDER_RADIUS}; background: transparent; }}")
        else:  # Default is "info"
            self.icon_label.setPixmap(QPixmap(":/icons/icons/info.png"))  # Use info icon from resources
            self.frame.setStyleSheet(f"#{self.frame.objectName()} {{ border: 2px solid {self.INFO_COLOR}; border-radius: {self.BORDER_RADIUS}; background: transparent; }}")

        # Show the widget
        self.show()
        if display_time>0:
            # Start the timer to hide the message after 'display_time' milliseconds
            self.timer.start(display_time)

    def hide(self):
        """
        Hides the message widget.
        """
        self.timer.stop()  # Stop the timer if it's running
        super().hide()     # Call the parent class's hide method



    



class deleteButton(QPushButton):

    def __init__(self, *a, **kw):
        super(deleteButton, self).__init__(*a, **kw)
        self._icon_normal = QIcon(':/icons/icons/icons8-remove-table-50.png')
        self._icon_over = QIcon(':/icons/icons/icons8-remove-hover-table-50.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(deleteButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(deleteButton, self).enterEvent(event)


class editButton(QPushButton):

    def __init__(self, *a, **kw):
        super(editButton, self).__init__(*a, **kw)
        self._icon_normal = QIcon(':/icons/icons/icons8-edit-table-50.png')
        self._icon_over = QIcon(':/icons/icons/icons8-edit-hover-table-50.png')
        self.setStyleSheet(TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)

    def enterEvent(self, event):
        self.setIcon(self._icon_over)
        #return super(editButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self._icon_normal)
        #return super(editButton, self).enterEvent(event)




class confirmMessageBox:
    def __init__(self, title, text, buttons, min_height=300, min_width=400, parent=None ):
        self.STANDARD_BUTTONS = {
            'yes': QMessageBox.Yes,
            'no': QMessageBox.No,
            'cancel': QMessageBox.Cancel,
            'save': QMessageBox.Save,
            'ok': QMessageBox.Ok,
            'ignore': QMessageBox.Ignore,
            

        }

        self.icon = QIcon(':/assets/icons/icons8-question-blue-50.png')
        self.buttons = buttons

        text = text + " " * 100 + "\n"

        self.msg = QMessageBox( text=text, parent=parent)
        self.msg.setWindowTitle(title)
        self.msg.setStyleSheet(CONFIRMBOX_STYLESHEET)
        self.msg.setWindowIcon(self.icon)
        #self.msg.setMinimumHeight(min_height)
        #self.msg.setStyleSheet("QLabel{ min-width:" + str(min_width) + " px; }" )
        #self.msg.setMinimumWidth(min_width)

        
        #---------------------------------------------------
        selected_buttons_obj = []
        for btn_name in buttons:
            btn = self.STANDARD_BUTTONS[btn_name]
            if isinstance(selected_buttons_obj, list):
                selected_buttons_obj = btn
            else:
                selected_buttons_obj = selected_buttons_obj | btn
        self.msg.setStandardButtons(selected_buttons_obj)
        #---------------------------------------------------

    def render(self) -> str:
        retval = self.msg.exec_()
        for btn_name in self.buttons:
            if self.STANDARD_BUTTONS[btn_name] == retval:
                return btn_name
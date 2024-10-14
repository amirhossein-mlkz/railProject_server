# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QToolButton,
    QVBoxLayout, QWidget)

from uiUtils.GUIComponents import MessageWidget
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1096, 777)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"QComboBox {\n"
"    background-color: #3b4252;\n"
"	background-color: rgb(180, 180, 180);\n"
"    border: 1px solid #4c566a;\n"
"    border-radius: 5px;\n"
"    padding: 6px 10px;\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #5e81ac;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/icons/icons8-drop-down-80.png);\n"
"\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"/****************************************************************/\n"
"QLabel{\n"
"	color: #404040;\n"
"}\n"
"\n"
"QLabel:disabled{\n"
"	color:#8D8D8D;\n"
"}\n"
"/****************************************************************/\n"
"QLineEdit\n"
"{\n"
"	color: #404040;\n"
"	background-color: #fff;\n"
"	/*border-bottom:2px solid rgba(6, 76, 130,120);\n"
"    border-radius: 0px;*/\n"
"	border:1px solid rgba(100, 100, 100,60);\n"
"	border-bottom:2px solid rgb(100, 100, 100);\n"
"    padding: 1px 8px 1px 8px;\n"
"	font-size: 16p"
                        "x;\n"
"	\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid rgba(100, 100, 100,60);\n"
"	border-bottom:2px solid rgb(100, 100, 100);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	selection-background-color: rgba(6, 76, 130,40);\n"
"	selection-color: #404040;\n"
"	border:1px solid rgba(6, 76, 130,60);\n"
"	border-bottom:2px solid rgb(6, 76, 130);\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgb(138, 138, 138); /* Placeholder text color */\n"
"    font-style: italic; /* Italicize placeholder text */\n"
"}\n"
"\n"
"/*******************************************/\n"
"\n"
"\n"
"\n"
"QToolButton {\n"
"    background-color: #4c566a; /* Dark background color */\n"
"    border: 1px solid #3b4252; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding around the text/icon */\n"
"    color: #eceff4; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: bold; /* Font weight */\n"
"    icon-size: 24px; /* Icon size */\n"
"}\n"
"\n"
"Q"
                        "ToolButton:hover {\n"
"    background-color: #5e81ac; /* Lighter background color on hover */\n"
"    border: 1px solid #4c566a; /* Border color on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #434c5e; /* Darker background color on press */\n"
"    border: 1px solid #3b4252; /* Border color on press */\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/icons/icons8-menu-24.png); /* Custom icon for the menu indicator */\n"
"    width: 16px; /* Width of the menu indicator */\n"
"    height: 16px; /* Height of the menu indicator */\n"
"}\n"
"\n"
"QToolButton::separator {\n"
"    width: 2px; /* Width of the separator */\n"
"    background-color: #3b4252; /* Color of the separator */\n"
"}\n"
"\n"
"QToolButton::toolbutton {\n"
"    padding: 5px; /* Padding for the toolbutton */\n"
"}\n"
"\n"
"\n"
"QCheckBox {\n"
"    spacing: 5px; /* Space between the checkbox and the text */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: 400; /* Font weight */\n"
"}\n"
"\n"
""
                        "QCheckBox::indicator {\n"
"    width: 20px; /* Width of the checkbox */\n"
"    height: 20px; /* Height of the checkbox */\n"
"    border: 1px solid #4c566a; /* Border color for the checkbox */\n"
"    border-radius: 3px; /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #2e3440; /* Default background color */\n"
"    border: 1px solid #81a1c1; /* Border color when checked */\n"
"    image: url(:/icons/icons/icons8-check-mark-48.png); /* Checkmark icon path */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 1px solid #5e81ac; /* Border color on hover */\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed {\n"
"    background-color: #434c5e; /* Background color when pressed */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background-color: #3b4252; /* Background color when checked and pressed */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: #3b4252; /* Background color when unchecked and pressed */\n"
"}\n"
"\n"
""
                        "QCheckBox::indicator:checked:disabled {\n"
"    background-color: #4c566a; /* Background color when disabled and checked */\n"
"    border: 1px solid #4c566a; /* Border color when disabled and checked */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"    background-color: #2e3440; /* Background color when disabled and unchecked */\n"
"    border: 1px solid #2e3440; /* Border color when disabled and unchecked */\n"
"}\n"
"\n"
"/*********************************************/\n"
"QHeaderView{\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    background-color: rgba(6, 76, 130,50);\n"
"	color: #404040;\n"
"	font-weight:bold;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:last \n"
"{\n"
"   border-top-right-radius: 12px;\n"
"	border-right: None;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:first \n"
"{\n"
"   border-top-left-radius: 12px;\n"
"	border-right: None;\n"
"}\n"
"\n"
"QTable"
                        "Widget::item:selected \n"
"{\n"
"    background-color: rgb(6, 76, 130,20);\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton[styleClass=\"fillBlueButton\"]{\n"
"	color: white;\n"
"    background-color:rgb(54, 90, 182);\n"
"	border: 2px solid rgb(54, 90, 182);\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:15px;\n"
"	min-height:18px;\n"
"}\n"
"\n"
"QPushButton[styleClass=\"fillBlueButton\"]:hover{\n"
"	background-color: rgb(70, 117, 235);\n"
"	border: 2px solid rgb(70, 117, 235);\n"
"}\n"
"\n"
"QPushButton[styleClass=\"fillBlueButton\"]:disabled {\n"
"		background-color:rgb(197, 197, 197);\n"
"		border: 2px solid rgb(197, 197, 197);	\n"
"}\n"
"\n"
"/******************************************************/\n"
"QPushButton[styleClass=\"borderBlueButton\"]{\n"
"    background-color:transparent;\n"
"	border: 2px solid rgb(54, 90, 182);\n"
"	color:rgb(54, 90, 182);\n"
"	paddi"
                        "ng: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	min-height:18px;\n"
"	border-radius:15px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton[styleClass=\"borderBlueButton\"]:hover{\n"
"	border: 2px solid rgb(70, 117, 235);\n"
"	color: rgb(70, 117, 235);\n"
"	background-color: rgba(70, 117, 235,5);\n"
"}\n"
"\n"
"QPushButton[styleClass=\"borderBlueButton\"]:disabled {\n"
"    color: #8D8D8D;\n"
"	border: 2px solid #8D8D8D;\n"
"}\n"
"\n"
"\n"
"QLabel[styleClass=\"h3\"]{\n"
"font-weight:bold;\n"
"font-size:14px;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.centralwidget)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"\n"
"background-color: rgb(170,170,170);")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btn_logo = QPushButton(self.frame_19)
        self.btn_logo.setObjectName(u"btn_logo")
        self.btn_logo.setMinimumSize(QSize(130, 0))
        self.btn_logo.setMaximumSize(QSize(130, 16777215))
        self.btn_logo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logo.setStyleSheet(u"QPushButton{\n"
"\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_logo.setIcon(icon)
        self.btn_logo.setIconSize(QSize(110, 50))

        self.horizontalLayout_22.addWidget(self.btn_logo)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_13)

        self.add_station_message_2 = MessageWidget(self.frame_19)
        self.add_station_message_2.setObjectName(u"add_station_message_2")
        self.add_station_message_2.setMinimumSize(QSize(0, 60))
        self.add_station_message_2.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.add_station_message_2)

        self.label_32 = QLabel(self.frame_19)
        self.label_32.setObjectName(u"label_32")
        font = QFont()
        font.setFamilies([u"Mongolian Baiti"])
        font.setPointSize(22)
        self.label_32.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_32)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_17 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_17)


        self.verticalLayout.addWidget(self.frame_19)

        self.middle = QFrame(self.centralwidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMaximumSize(QSize(16777215, 16777215))
        self.middle.setStyleSheet(u"")
        self.middle.setFrameShape(QFrame.Shape.NoFrame)
        self.middle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.middle)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame = QFrame(self.middle)
        self.toggle_frame.setObjectName(u"toggle_frame")
        self.toggle_frame.setMinimumSize(QSize(130, 0))
        self.toggle_frame.setMaximumSize(QSize(130, 16777215))
        self.toggle_frame.setStyleSheet(u"QFrame{\n"
"	background: #1b2c5a;\n"
"\n"
"}\n"
"\n"
"")
        self.toggle_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.toggle_frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.toggle_frame.setLineWidth(3)
        self.verticalLayout_36 = QVBoxLayout(self.toggle_frame)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 87, 0, 0)
        self.frame_7 = QFrame(self.toggle_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 82))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_side_playback = QPushButton(self.frame_7)
        self.btn_side_playback.setObjectName(u"btn_side_playback")
        self.btn_side_playback.setMinimumSize(QSize(120, 50))
        self.btn_side_playback.setMaximumSize(QSize(120, 50))
        self.btn_side_playback.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_playback.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color:#acb7cc;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8-playback-24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_playback.setIcon(icon1)
        self.btn_side_playback.setIconSize(QSize(51, 51))

        self.verticalLayout_2.addWidget(self.btn_side_playback, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_side_download = QPushButton(self.frame_7)
        self.btn_side_download.setObjectName(u"btn_side_download")
        self.btn_side_download.setMinimumSize(QSize(120, 50))
        self.btn_side_download.setMaximumSize(QSize(120, 50))
        self.btn_side_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_download.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color:#acb7cc;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8-file-download-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_download.setIcon(icon2)
        self.btn_side_download.setIconSize(QSize(23, 22))

        self.verticalLayout_2.addWidget(self.btn_side_download, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_side_settings = QPushButton(self.frame_7)
        self.btn_side_settings.setObjectName(u"btn_side_settings")
        self.btn_side_settings.setMinimumSize(QSize(120, 50))
        self.btn_side_settings.setMaximumSize(QSize(120, 50))
        self.btn_side_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_settings.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color:#acb7cc;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-settings-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_settings.setIcon(icon3)
        self.btn_side_settings.setIconSize(QSize(22, 22))

        self.verticalLayout_2.addWidget(self.btn_side_settings, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_side_aboutus = QPushButton(self.frame_7)
        self.btn_side_aboutus.setObjectName(u"btn_side_aboutus")
        self.btn_side_aboutus.setMinimumSize(QSize(120, 50))
        self.btn_side_aboutus.setMaximumSize(QSize(120, 50))
        self.btn_side_aboutus.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_aboutus.setStyleSheet(u"QPushButton{\n"
"	color: black;\n"
"	background-color:#acb7cc;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8-company-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_aboutus.setIcon(icon4)
        self.btn_side_aboutus.setIconSize(QSize(27, 51))

        self.verticalLayout_2.addWidget(self.btn_side_aboutus, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.verticalLayout_36.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.toggle_frame)

        self.main_frame = QFrame(self.middle)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(1, 1))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.main_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"#page_download,\n"
"#page_playback,\n"
"#page_settings {\n"
"	background-color: #F5F5F5;\n"
"	color: red;\n"
"}")
        self.stackedWidget.setFrameShape(QFrame.Shape.Box)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.stackedWidget.setLineWidth(2)
        self.page_playback = QWidget()
        self.page_playback.setObjectName(u"page_playback")
        self.horizontalLayout_7 = QHBoxLayout(self.page_playback)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.frame_6 = QFrame(self.page_playback)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_11)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_44)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_44)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 99))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background: #1b2c5a;\n"
"}\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_9.setLineWidth(3)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(16, 13, 9, 9)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(177, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_25.addWidget(self.frame_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_2)

        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(160, 100))
        self.label_2.setStyleSheet(u"font-size:30px;\n"
"color: white;\n"
"font: 23pt \"Mongolian Baiti\";")

        self.horizontalLayout_25.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addWidget(self.frame_9)

        self.frame_18 = QFrame(self.frame_44)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 60))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.playback_filter_frame = QFrame(self.frame_18)
        self.playback_filter_frame.setObjectName(u"playback_filter_frame")
        self.playback_filter_frame.setMinimumSize(QSize(340, 404))
        self.playback_filter_frame.setMaximumSize(QSize(340, 16777215))
        self.playback_filter_frame.setFrameShape(QFrame.Shape.Panel)
        self.playback_filter_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.playback_filter_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.playback_filter_frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(330, 0))
        self.frame_16.setMaximumSize(QSize(330, 16777215))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.frame_20)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_43.addWidget(self.label_6)

        self.refresh_btn = QPushButton(self.frame_20)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setMaximumSize(QSize(35, 16777215))
        self.refresh_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refresh_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: white;\n"
"\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"	background-color: rgb(161, 163, 159);\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8-refresh-26.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_btn.setIcon(icon5)

        self.horizontalLayout_43.addWidget(self.refresh_btn)

        self.refresh_image_database_log = QLabel(self.frame_20)
        self.refresh_image_database_log.setObjectName(u"refresh_image_database_log")
        self.refresh_image_database_log.setStyleSheet(u"color: rgb(34, 119, 255);")

        self.horizontalLayout_43.addWidget(self.refresh_image_database_log)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_5)


        self.verticalLayout_22.addLayout(self.horizontalLayout_43)

        self.refresh_image_db_message = MessageWidget(self.frame_20)
        self.refresh_image_db_message.setObjectName(u"refresh_image_db_message")
        self.refresh_image_db_message.setMinimumSize(QSize(0, 60))
        self.refresh_image_db_message.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.refresh_image_db_message)


        self.verticalLayout_6.addWidget(self.frame_20)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_3 = QLabel(self.frame_17)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(73, 16777215))

        self.horizontalLayout_15.addWidget(self.label_3)

        self.playback_combo_train_id = QComboBox(self.frame_17)
        self.playback_combo_train_id.setObjectName(u"playback_combo_train_id")
        self.playback_combo_train_id.setStyleSheet(u"QComboBox {\n"
"    background-color: #3b4252;\n"
"	background-color: rgb(180, 180, 180);\n"
"    border: 1px solid #4c566a;\n"
"    border-radius: 5px;\n"
"    padding: 6px 10px;\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #5e81ac;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/icons/icons8-drop-down-80.png);\n"
"\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}")
        self.playback_combo_train_id.setIconSize(QSize(41, 45))

        self.horizontalLayout_15.addWidget(self.playback_combo_train_id)

        self.btn_select_train = QPushButton(self.frame_17)
        self.btn_select_train.setObjectName(u"btn_select_train")
        self.btn_select_train.setMaximumSize(QSize(47, 16777215))
        self.btn_select_train.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_select_train.setStyleSheet(u"QPushButton{\n"
"\n"
"	color: white;\n"
"\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"	background-color: #1fbb8b\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icons8-railway-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_select_train.setIcon(icon6)
        self.btn_select_train.setIconSize(QSize(37, 30))

        self.horizontalLayout_15.addWidget(self.btn_select_train)


        self.verticalLayout_6.addWidget(self.frame_17)

        self.line = QFrame(self.frame_16)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.groupBox_6 = QGroupBox(self.frame_16)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(0, 300))
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.calendar_widget = QWidget(self.groupBox_6)
        self.calendar_widget.setObjectName(u"calendar_widget")
        self.calendar_widget.setMinimumSize(QSize(0, 50))
        self.calendar_widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.calendar_widget)

        self.frame_57 = QFrame(self.groupBox_6)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setStyleSheet(u"")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_date_2 = QLabel(self.frame_57)
        self.label_date_2.setObjectName(u"label_date_2")
        self.label_date_2.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_31.addWidget(self.label_date_2)

        self.label_date = QLabel(self.frame_57)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMaximumSize(QSize(16777215, 40))
        self.label_date.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"	padding: 5px;\n"
"	font-size:14px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_31.addWidget(self.label_date)


        self.verticalLayout_25.addWidget(self.frame_57)


        self.verticalLayout_6.addWidget(self.groupBox_6)


        self.verticalLayout_17.addWidget(self.frame_16, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.load_videos_progess_bar = QProgressBar(self.playback_filter_frame)
        self.load_videos_progess_bar.setObjectName(u"load_videos_progess_bar")
        self.load_videos_progess_bar.setValue(24)

        self.verticalLayout_17.addWidget(self.load_videos_progess_bar)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_17)


        self.horizontalLayout_12.addWidget(self.playback_filter_frame)

        self.video = QWidget(self.frame_18)
        self.video.setObjectName(u"video")

        self.horizontalLayout_12.addWidget(self.video)

        self.line_14 = QFrame(self.frame_18)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_14)


        self.verticalLayout_15.addWidget(self.frame_18)

        self.frame_12 = QFrame(self.frame_44)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 100))
        self.frame_12.setMaximumSize(QSize(16777215, 100))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.layout_timeline = QVBoxLayout()
        self.layout_timeline.setObjectName(u"layout_timeline")
        self.time_line_frame = QFrame(self.frame_12)
        self.time_line_frame.setObjectName(u"time_line_frame")
        self.time_line_frame.setMinimumSize(QSize(0, 50))
        self.time_line_frame.setMaximumSize(QSize(16777215, 50))
        self.time_line_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.time_line_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.time_line_frame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")

        self.layout_timeline.addWidget(self.time_line_frame)


        self.verticalLayout_16.addLayout(self.layout_timeline)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(1, 50))
        self.frame_13.setMaximumSize(QSize(16777211, 50))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"	background: #1b2c5a;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_28 = QLabel(self.frame_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"	color: white;")

        self.horizontalLayout_4.addWidget(self.label_28)

        self.playback_camera_combo = QComboBox(self.frame_13)
        self.playback_camera_combo.addItem("")
        self.playback_camera_combo.addItem("")
        self.playback_camera_combo.setObjectName(u"playback_camera_combo")
        self.playback_camera_combo.setMinimumSize(QSize(120, 0))
        self.playback_camera_combo.setMaximumSize(QSize(16777215, 16777215))
        self.playback_camera_combo.setStyleSheet(u"QComboBox {\n"
"    background-color:  transparent;\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"    padding: 6px 10px;\n"
"\n"
"	color: white;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #5e81ac;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #404040;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/icons/icons8-drop-down-80.png);\n"
"\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.playback_camera_combo)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.play_btn = QPushButton(self.frame_13)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMaximumSize(QSize(70, 30))
        self.play_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.play_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"    background-color:#F1F0E8;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/Live00.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_btn.setIcon(icon7)
        self.play_btn.setIconSize(QSize(60, 60))

        self.horizontalLayout_4.addWidget(self.play_btn)

        self.pause_btn = QPushButton(self.frame_13)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setToolTipDuration(-1)
        self.pause_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"    background-color:#F1F0E8;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/icons8-pause-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_btn.setIcon(icon8)
        self.pause_btn.setIconSize(QSize(29, 26))

        self.horizontalLayout_4.addWidget(self.pause_btn)

        self.line_4 = QFrame(self.frame_13)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.stop_btn = QPushButton(self.frame_13)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setToolTipDuration(-1)
        self.stop_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"    background-color:#F1F0E8;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/stop-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_btn.setIcon(icon9)
        self.stop_btn.setIconSize(QSize(29, 26))

        self.horizontalLayout_4.addWidget(self.stop_btn)

        self.line_2 = QFrame(self.frame_13)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color : rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.frame_58 = QFrame(self.frame_13)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_58)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"	color: white;")

        self.horizontalLayout_32.addWidget(self.label_25)

        self.speed_btn = QPushButton(self.frame_58)
        self.speed_btn.setObjectName(u"speed_btn")
        self.speed_btn.setToolTipDuration(-1)
        self.speed_btn.setStyleSheet(u"\n"
"QPushButton{\n"
"	color: white;\n"
"    background-color:#F1F0E8;\n"
"	padding: 5px;\n"
"	font-size: 11pt;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #a3a3a3;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        self.speed_btn.setIconSize(QSize(29, 26))

        self.horizontalLayout_32.addWidget(self.speed_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_4)

        self.frame_21 = QFrame(self.frame_58)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(100, 0))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label = QLabel(self.frame_21)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label)

        self.time_label = QLabel(self.frame_21)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.time_label)


        self.horizontalLayout_32.addWidget(self.frame_21)


        self.horizontalLayout_4.addWidget(self.frame_58)


        self.verticalLayout_16.addWidget(self.frame_13)


        self.verticalLayout_15.addWidget(self.frame_12)


        self.horizontalLayout_56.addWidget(self.frame_44)


        self.verticalLayout_9.addWidget(self.frame_11)

        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)


        self.horizontalLayout_7.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_playback)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.page_settings)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame_29 = QFrame(self.page_settings)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_24 = QVBoxLayout(self.frame_29)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(1, 1, 1, 21)
        self.frame_81 = QFrame(self.frame_29)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 100))
        self.frame_81.setMaximumSize(QSize(16777215, 16777215))
        self.frame_81.setTabletTracking(False)
        self.frame_81.setAutoFillBackground(False)
        self.frame_81.setFrameShape(QFrame.Shape.Panel)
        self.frame_81.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_81)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy2)
        self.frame_32.setMinimumSize(QSize(0, 0))
        self.frame_32.setMaximumSize(QSize(16777215, 16777215))
        self.frame_32.setStyleSheet(u"font-size:17px;")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_32)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 2, -1)
        self.frame_3 = QFrame(self.frame_32)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.frame_31 = QFrame(self.frame_3)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 80))
        self.frame_31.setMaximumSize(QSize(16777215, 80))
        self.frame_31.setStyleSheet(u"QFrame{\n"
"	background: #1b2c5a;\n"
"   border-radius:5px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(90, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_7)

        self.label_21 = QLabel(self.frame_31)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(300, 100))
        self.label_21.setStyleSheet(u"font-size:30px;\n"
"color: white;\n"
"font: 24pt \"Mongolian Baiti\";")

        self.horizontalLayout_17.addWidget(self.label_21)

        self.horizontalSpacer_14 = QSpacerItem(300, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)


        self.verticalLayout_4.addWidget(self.frame_31)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_3 = QGroupBox(self.frame_15)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"#modify,\n"
"#add {\n"
"	background-color: #F5F5F5;\n"
"}")
        self.add = QWidget()
        self.add.setObjectName(u"add")
        self.verticalLayout_27 = QVBoxLayout(self.add)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.scrollArea_2 = QScrollArea(self.add)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(500, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 199, 573))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_47 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_16 = QLabel(self.frame_47)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_20.addWidget(self.label_16)

        self.name_input = QLineEdit(self.frame_47)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMaximumSize(QSize(140, 16777215))
        self.name_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.name_input.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.name_input)


        self.verticalLayout_7.addWidget(self.frame_47)

        self.line_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_7)

        self.frame_48 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_17 = QLabel(self.frame_48)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_21.addWidget(self.label_17)

        self.city_input = QLineEdit(self.frame_48)
        self.city_input.setObjectName(u"city_input")
        self.city_input.setMaximumSize(QSize(140, 16777215))
        self.city_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.city_input.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.city_input)


        self.verticalLayout_7.addWidget(self.frame_48)

        self.line_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_5)

        self.frame_49 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_15 = QLabel(self.frame_49)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_19.addWidget(self.label_15)

        self.ip_input = QLineEdit(self.frame_49)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setMaximumSize(QSize(140, 16777215))
        self.ip_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.ip_input.setStyleSheet(u"")

        self.horizontalLayout_19.addWidget(self.ip_input)


        self.verticalLayout_7.addWidget(self.frame_49)

        self.line_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_6)

        self.frame_50 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_18 = QLabel(self.frame_50)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_24.addWidget(self.label_18)

        self.username_input = QLineEdit(self.frame_50)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMaximumSize(QSize(140, 16777215))
        self.username_input.setStyleSheet(u"")

        self.horizontalLayout_24.addWidget(self.username_input)


        self.verticalLayout_7.addWidget(self.frame_50)

        self.line_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_8)

        self.frame_51 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_19 = QLabel(self.frame_51)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_26.addWidget(self.label_19)

        self.password_input = QLineEdit(self.frame_51)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMaximumSize(QSize(140, 16777215))
        self.password_input.setStyleSheet(u"")

        self.horizontalLayout_26.addWidget(self.password_input)


        self.verticalLayout_7.addWidget(self.frame_51)

        self.add_station_message = MessageWidget(self.scrollAreaWidgetContents_2)
        self.add_station_message.setObjectName(u"add_station_message")
        self.add_station_message.setMinimumSize(QSize(0, 60))
        self.add_station_message.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.add_station_message)

        self.btn_add_check_connection = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_add_check_connection.setObjectName(u"btn_add_check_connection")
        self.btn_add_check_connection.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_add_check_connection)

        self.btn_save_add = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_save_add.setObjectName(u"btn_save_add")
        self.btn_save_add.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.btn_save_add)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.textEdit_ping_status = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_ping_status.setObjectName(u"textEdit_ping_status")

        self.verticalLayout_7.addWidget(self.textEdit_ping_status)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_27.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.add, "")
        self.modify = QWidget()
        self.modify.setObjectName(u"modify")
        self.horizontalLayout_33 = QHBoxLayout(self.modify)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.system_stations_table = QTableWidget(self.modify)
        if (self.system_stations_table.columnCount() < 3):
            self.system_stations_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.system_stations_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.system_stations_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.system_stations_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.system_stations_table.setObjectName(u"system_stations_table")
        self.system_stations_table.setStyleSheet(u"")
        self.system_stations_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.system_stations_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout_33.addWidget(self.system_stations_table)

        self.modify_form_frame = QFrame(self.modify)
        self.modify_form_frame.setObjectName(u"modify_form_frame")
        self.modify_form_frame.setMaximumSize(QSize(500, 16777215))
        self.modify_form_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.modify_form_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.modify_form_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.modify_form_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 199, 485))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_54 = QFrame(self.scrollAreaWidgetContents)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_22 = QLabel(self.frame_54)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_35.addWidget(self.label_22)

        self.name_input_modify = QLineEdit(self.frame_54)
        self.name_input_modify.setObjectName(u"name_input_modify")
        self.name_input_modify.setMaximumSize(QSize(140, 16777215))
        self.name_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.name_input_modify.setStyleSheet(u"")

        self.horizontalLayout_35.addWidget(self.name_input_modify)


        self.verticalLayout_5.addWidget(self.frame_54)

        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_10)

        self.frame_55 = QFrame(self.scrollAreaWidgetContents)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_20 = QLabel(self.frame_55)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_36.addWidget(self.label_20)

        self.city_input_modify = QLineEdit(self.frame_55)
        self.city_input_modify.setObjectName(u"city_input_modify")
        self.city_input_modify.setMaximumSize(QSize(140, 16777215))
        self.city_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.city_input_modify.setStyleSheet(u"")

        self.horizontalLayout_36.addWidget(self.city_input_modify)


        self.verticalLayout_5.addWidget(self.frame_55)

        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_11)

        self.frame_56 = QFrame(self.scrollAreaWidgetContents)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_26 = QLabel(self.frame_56)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_37.addWidget(self.label_26)

        self.ip_input_modify = QLineEdit(self.frame_56)
        self.ip_input_modify.setObjectName(u"ip_input_modify")
        self.ip_input_modify.setMaximumSize(QSize(140, 16777215))
        self.ip_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ip_input_modify.setStyleSheet(u"")

        self.horizontalLayout_37.addWidget(self.ip_input_modify)


        self.verticalLayout_5.addWidget(self.frame_56)

        self.line_12 = QFrame(self.scrollAreaWidgetContents)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_12)

        self.frame_59 = QFrame(self.scrollAreaWidgetContents)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_27 = QLabel(self.frame_59)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_38.addWidget(self.label_27)

        self.username_input_modify = QLineEdit(self.frame_59)
        self.username_input_modify.setObjectName(u"username_input_modify")
        self.username_input_modify.setMaximumSize(QSize(140, 16777215))
        self.username_input_modify.setStyleSheet(u"")

        self.horizontalLayout_38.addWidget(self.username_input_modify)


        self.verticalLayout_5.addWidget(self.frame_59)

        self.line_13 = QFrame(self.scrollAreaWidgetContents)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_13)

        self.frame_61 = QFrame(self.scrollAreaWidgetContents)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_29 = QLabel(self.frame_61)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_39.addWidget(self.label_29)

        self.password_input_modify = QLineEdit(self.frame_61)
        self.password_input_modify.setObjectName(u"password_input_modify")
        self.password_input_modify.setMaximumSize(QSize(140, 16777215))
        self.password_input_modify.setStyleSheet(u"")

        self.horizontalLayout_39.addWidget(self.password_input_modify)


        self.verticalLayout_5.addWidget(self.frame_61)

        self.ddddddd = QFrame(self.scrollAreaWidgetContents)
        self.ddddddd.setObjectName(u"ddddddd")
        self.ddddddd.setEnabled(True)
        self.ddddddd.setFrameShape(QFrame.Shape.StyledPanel)
        self.ddddddd.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.ddddddd)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, -1, 0, -1)
        self.modify_station_message = MessageWidget(self.ddddddd)
        self.modify_station_message.setObjectName(u"modify_station_message")
        self.modify_station_message.setMinimumSize(QSize(0, 60))
        self.modify_station_message.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.modify_station_message)

        self.btn_modify_save = QPushButton(self.ddddddd)
        self.btn_modify_save.setObjectName(u"btn_modify_save")
        self.btn_modify_save.setEnabled(True)
        self.btn_modify_save.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.btn_modify_save)

        self.btn_modify_cancel = QPushButton(self.ddddddd)
        self.btn_modify_cancel.setObjectName(u"btn_modify_cancel")
        self.btn_modify_cancel.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.btn_modify_cancel)


        self.verticalLayout_5.addWidget(self.ddddddd)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.horizontalLayout_33.addWidget(self.modify_form_frame)

        self.tabWidget.addTab(self.modify, "")

        self.verticalLayout_21.addWidget(self.tabWidget)


        self.horizontalLayout_3.addWidget(self.groupBox_3)


        self.verticalLayout_4.addWidget(self.frame_15)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_14 = QFrame(self.frame_32)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_10.addWidget(self.frame_14)


        self.horizontalLayout_28.addWidget(self.frame_32)


        self.verticalLayout_24.addWidget(self.frame_81)


        self.horizontalLayout.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_download = QWidget()
        self.page_download.setObjectName(u"page_download")
        self.horizontalLayout_6 = QHBoxLayout(self.page_download)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.frame_39 = QFrame(self.page_download)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMaximumSize(QSize(16777215, 16777215))
        self.frame_39.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_39.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_32 = QVBoxLayout(self.frame_39)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(1, 1, 1, 0)
        self.frame_82 = QFrame(self.frame_39)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(0, 0))
        self.frame_82.setMaximumSize(QSize(16777215, 16777215))
        self.frame_82.setFrameShape(QFrame.Shape.Panel)
        self.frame_82.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_82)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_42)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 2, -1)
        self.frame_41 = QFrame(self.frame_42)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 80))
        self.frame_41.setMaximumSize(QSize(16777215, 80))
        self.frame_41.setStyleSheet(u"QFrame{\n"
"	background: #1b2c5a;\n"
"   border-radius:5px;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_12 = QSpacerItem(90, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_12)

        self.label_31 = QLabel(self.frame_41)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(300, 100))
        self.label_31.setStyleSheet(u"font-size:30px;\n"
"color: white;\n"
"font: 24pt \"Mongolian Baiti\";")

        self.horizontalLayout_50.addWidget(self.label_31)

        self.horizontalSpacer_16 = QSpacerItem(300, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_16)


        self.verticalLayout_35.addWidget(self.frame_41)

        self.frame_4 = QFrame(self.frame_42)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.splitter = QSplitter(self.frame_4)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.download_filter_frame = QFrame(self.splitter)
        self.download_filter_frame.setObjectName(u"download_filter_frame")
        self.download_filter_frame.setMinimumSize(QSize(316, 0))
        self.download_filter_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.download_filter_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.download_filter_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.download_filter_stackWidget = QStackedWidget(self.download_filter_frame)
        self.download_filter_stackWidget.setObjectName(u"download_filter_stackWidget")
        self.step1 = QWidget()
        self.step1.setObjectName(u"step1")
        self.verticalLayout_14 = QVBoxLayout(self.step1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_8 = QLabel(self.step1)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_18.addWidget(self.label_8)

        self.download_filters_train_combobox = QComboBox(self.step1)
        self.download_filters_train_combobox.setObjectName(u"download_filters_train_combobox")

        self.horizontalLayout_18.addWidget(self.download_filters_train_combobox)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.download_filter_station_log = QTableWidget(self.step1)
        if (self.download_filter_station_log.columnCount() < 2):
            self.download_filter_station_log.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.download_filter_station_log.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.download_filter_station_log.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        if (self.download_filter_station_log.rowCount() < 1):
            self.download_filter_station_log.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.download_filter_station_log.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.download_filter_station_log.setObjectName(u"download_filter_station_log")
        self.download_filter_station_log.horizontalHeader().setCascadingSectionResizes(False)
        self.download_filter_station_log.horizontalHeader().setStretchLastSection(True)
        self.download_filter_station_log.verticalHeader().setVisible(False)
        self.download_filter_station_log.verticalHeader().setDefaultSectionSize(35)
        self.download_filter_station_log.verticalHeader().setHighlightSections(True)

        self.verticalLayout_14.addWidget(self.download_filter_station_log)

        self.download_filter_stackWidget.addWidget(self.step1)
        self.step0 = QWidget()
        self.step0.setObjectName(u"step0")
        self.verticalLayout_12 = QVBoxLayout(self.step0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_4 = QLabel(self.step0)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.label_4)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, -1, -1)
        self.download_all_stations_checkbox = QCheckBox(self.step0)
        self.download_all_stations_checkbox.setObjectName(u"download_all_stations_checkbox")

        self.horizontalLayout_34.addWidget(self.download_all_stations_checkbox)

        self.horizontalSpacer = QSpacerItem(36, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer)

        self.download_search_station = QLineEdit(self.step0)
        self.download_search_station.setObjectName(u"download_search_station")

        self.horizontalLayout_34.addWidget(self.download_search_station)


        self.verticalLayout_12.addLayout(self.horizontalLayout_34)

        self.download_stations_table = QTableWidget(self.step0)
        if (self.download_stations_table.columnCount() < 2):
            self.download_stations_table.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.download_stations_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.download_stations_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        if (self.download_stations_table.rowCount() < 3):
            self.download_stations_table.setRowCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.download_stations_table.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.download_stations_table.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.download_stations_table.setVerticalHeaderItem(2, __qtablewidgetitem10)
        self.download_stations_table.setObjectName(u"download_stations_table")
        self.download_stations_table.setMinimumSize(QSize(100, 100))
        self.download_stations_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.download_stations_table.horizontalHeader().setStretchLastSection(True)
        self.download_stations_table.verticalHeader().setVisible(False)
        self.download_stations_table.verticalHeader().setHighlightSections(True)

        self.verticalLayout_12.addWidget(self.download_stations_table)

        self.download_filter_stackWidget.addWidget(self.step0)

        self.verticalLayout_13.addWidget(self.download_filter_stackWidget)

        self.download_filter_message = MessageWidget(self.download_filter_frame)
        self.download_filter_message.setObjectName(u"download_filter_message")
        self.download_filter_message.setMinimumSize(QSize(0, 60))
        self.download_filter_message.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.download_filter_message)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(-1, 0, -1, -1)
        self.download_filter_prev_btn = QPushButton(self.download_filter_frame)
        self.download_filter_prev_btn.setObjectName(u"download_filter_prev_btn")
        self.download_filter_prev_btn.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.download_filter_prev_btn)

        self.download_filter_next_btn = QPushButton(self.download_filter_frame)
        self.download_filter_next_btn.setObjectName(u"download_filter_next_btn")
        self.download_filter_next_btn.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.download_filter_next_btn)


        self.verticalLayout_13.addLayout(self.horizontalLayout_41)

        self.splitter.addWidget(self.download_filter_frame)
        self.frame_45 = QFrame(self.splitter)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_45)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.groupBox_2 = QGroupBox(self.frame_45)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_23 = QFrame(self.groupBox_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 60))
        self.frame_23.setMaximumSize(QSize(16777215, 60))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_4 = QCheckBox(self.frame_23)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMaximumSize(QSize(23, 16777215))

        self.horizontalLayout_8.addWidget(self.checkBox_4)

        self.combo_download_all = QComboBox(self.frame_23)
        self.combo_download_all.setObjectName(u"combo_download_all")

        self.horizontalLayout_8.addWidget(self.combo_download_all)

        self.btn_add = QPushButton(self.frame_23)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(20, 20))
        self.btn_add.setMaximumSize(QSize(20, 20))
        self.btn_add.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color:#0C356A;\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"	background-color: rgb(0, 17, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(18, 3, 104);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.btn_add)

        self.combo_download_selected = QComboBox(self.frame_23)
        self.combo_download_selected.setObjectName(u"combo_download_selected")

        self.horizontalLayout_8.addWidget(self.combo_download_selected)

        self.btn_remove = QPushButton(self.frame_23)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setMinimumSize(QSize(20, 20))
        self.btn_remove.setMaximumSize(QSize(20, 20))
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color:#0C356A;\n"
"	padding: 5px;\n"
"	font-size:12px;\n"
"	font-weight: bold;\n"
"	border-radius:7px;\n"
"	background-color: rgb(0, 17, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(18, 3, 104);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.btn_remove)


        self.verticalLayout_8.addWidget(self.frame_23)

        self.line_15 = QFrame(self.groupBox_2)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_15)

        self.frame_25 = QFrame(self.groupBox_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 60))
        self.frame_25.setMaximumSize(QSize(16777215, 60))
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox = QCheckBox(self.frame_25)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(23, 16777215))

        self.horizontalLayout_9.addWidget(self.checkBox)

        self.label_5 = QLabel(self.frame_25)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_9.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.line_train_id = QLineEdit(self.frame_25)
        self.line_train_id.setObjectName(u"line_train_id")
        self.line_train_id.setMaximumSize(QSize(176, 16777215))
        self.line_train_id.setStyleSheet(u"QLineEdit {\n"
"\n"
"    border: 1px solid #4c566a; /* Subtle border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding inside the line edit */\n"
"    color: #d8dee9; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: 400; /* Font weight */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #81a1c1; /* Border color on focus */\n"
"    background-color: #3b4252; /* Slightly lighter background color on focus */\n"
"    selection-background-color: #81a1c1; /* Selection background color */\n"
"    selection-color: #2e3440; /* Selection text color */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #4c566a; /* Placeholder text color */\n"
"    font-style: italic; /* Italicize placeholder text */\n"
"}")

        self.horizontalLayout_9.addWidget(self.line_train_id)


        self.verticalLayout_8.addWidget(self.frame_25)

        self.line_16 = QFrame(self.groupBox_2)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_16)

        self.frame_26 = QFrame(self.groupBox_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_26)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.frame = QFrame(self.frame_26)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(23, 16777215))
        self.checkBox_2.setChecked(False)

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout_18.addWidget(self.frame)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, -1, -1, -1)
        self.label_10 = QLabel(self.frame_27)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.line_start_date = QLineEdit(self.frame_27)
        self.line_start_date.setObjectName(u"line_start_date")
        self.line_start_date.setStyleSheet(u"QLineEdit {\n"
"\n"
"    border: 1px solid #4c566a; /* Subtle border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding inside the line edit */\n"
"    color: #d8dee9; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: 400; /* Font weight */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #81a1c1; /* Border color on focus */\n"
"    background-color: #3b4252; /* Slightly lighter background color on focus */\n"
"    selection-background-color: #81a1c1; /* Selection background color */\n"
"    selection-color: #2e3440; /* Selection text color */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #4c566a; /* Placeholder text color */\n"
"    font-style: italic; /* Italicize placeholder text */\n"
"}")

        self.horizontalLayout_11.addWidget(self.line_start_date)

        self.toolButton = QToolButton(self.frame_27)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: #4c566a; /* Dark background color */\n"
"    border: 1px solid #3b4252; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding around the text/icon */\n"
"    color: #eceff4; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: bold; /* Font weight */\n"
"    icon-size: 24px; /* Icon size */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #5e81ac; /* Lighter background color on hover */\n"
"    border: 1px solid #4c566a; /* Border color on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #434c5e; /* Darker background color on press */\n"
"    border: 1px solid #3b4252; /* Border color on press */\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/icons/icons8-menu-24.png); /* Custom icon for the menu indicator */\n"
"    width: 16px; /* Width of the menu indicator */\n"
"    height: 16px; /* Height of the menu indicator */\n"
"}\n"
"\n"
"QToolB"
                        "utton::separator {\n"
"    width: 2px; /* Width of the separator */\n"
"    background-color: #3b4252; /* Color of the separator */\n"
"}\n"
"\n"
"QToolButton::toolbutton {\n"
"    padding: 5px; /* Padding for the toolbutton */\n"
"}")

        self.horizontalLayout_11.addWidget(self.toolButton)


        self.verticalLayout_18.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, -1, -1, -1)
        self.label_11 = QLabel(self.frame_28)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.line_end_date = QLineEdit(self.frame_28)
        self.line_end_date.setObjectName(u"line_end_date")
        self.line_end_date.setStyleSheet(u"QLineEdit {\n"
"\n"
"    border: 1px solid #4c566a; /* Subtle border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding inside the line edit */\n"
"    color: #d8dee9; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: 400; /* Font weight */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #81a1c1; /* Border color on focus */\n"
"    background-color: #3b4252; /* Slightly lighter background color on focus */\n"
"    selection-background-color: #81a1c1; /* Selection background color */\n"
"    selection-color: #2e3440; /* Selection text color */\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #4c566a; /* Placeholder text color */\n"
"    font-style: italic; /* Italicize placeholder text */\n"
"}")

        self.horizontalLayout_13.addWidget(self.line_end_date)

        self.toolButton_2 = QToolButton(self.frame_28)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setStyleSheet(u"QToolButton {\n"
"    background-color: #4c566a; /* Dark background color */\n"
"    border: 1px solid #3b4252; /* Border color */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding around the text/icon */\n"
"    color: #eceff4; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: bold; /* Font weight */\n"
"    icon-size: 24px; /* Icon size */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #5e81ac; /* Lighter background color on hover */\n"
"    border: 1px solid #4c566a; /* Border color on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #434c5e; /* Darker background color on press */\n"
"    border: 1px solid #3b4252; /* Border color on press */\n"
"}\n"
"\n"
"QToolButton::menu-indicator {\n"
"    image: url(:/icons/icons8-menu-24.png); /* Custom icon for the menu indicator */\n"
"    width: 16px; /* Width of the menu indicator */\n"
"    height: 16px; /* Height of the menu indicator */\n"
"}\n"
"\n"
"QToolB"
                        "utton::separator {\n"
"    width: 2px; /* Width of the separator */\n"
"    background-color: #3b4252; /* Color of the separator */\n"
"}\n"
"\n"
"QToolButton::toolbutton {\n"
"    padding: 5px; /* Padding for the toolbutton */\n"
"}")

        self.horizontalLayout_13.addWidget(self.toolButton_2)


        self.verticalLayout_18.addWidget(self.frame_28)


        self.verticalLayout_8.addWidget(self.frame_26)

        self.line_17 = QFrame(self.groupBox_2)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_17)

        self.frame_30 = QFrame(self.groupBox_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_30)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_5 = QFrame(self.frame_30)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.frame_5)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMaximumSize(QSize(27, 16777215))
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    spacing: 5px; /* Space between the checkbox and the text */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: 400; /* Font weight */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px; /* Width of the checkbox */\n"
"    height: 20px; /* Height of the checkbox */\n"
"    border: 1px solid #4c566a; /* Border color for the checkbox */\n"
"    border-radius: 3px; /* Rounded corners */\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: #2e3440; /* Default background color */\n"
"    border: 1px solid #81a1c1; /* Border color when checked */\n"
"    image: url(:/icons/icons/icons8-check-mark-48.png); /* Checkmark icon path */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 1px solid #5e81ac; /* Border color on hover */\n"
"}\n"
"\n"
"QCheckBox::indicator:pressed {\n"
"    background-color: #434c5e; /* Background color when pressed */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    background-color: #3b4252; /* Background color wh"
                        "en checked and pressed */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: #3b4252; /* Background color when unchecked and pressed */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    background-color: #4c566a; /* Background color when disabled and checked */\n"
"    border: 1px solid #4c566a; /* Border color when disabled and checked */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"    background-color: #2e3440; /* Background color when disabled and unchecked */\n"
"    border: 1px solid #2e3440; /* Border color when disabled and unchecked */\n"
"}")
        self.checkBox_3.setChecked(False)

        self.horizontalLayout_40.addWidget(self.checkBox_3)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_40.addWidget(self.label_12)


        self.verticalLayout_19.addWidget(self.frame_5)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.frame_33)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.time_start = QTimeEdit(self.frame_33)
        self.time_start.setObjectName(u"time_start")
        self.time_start.setStyleSheet(u"QTimeEdit {\n"
"    background-color: #2e3440; /* Dark background color */\n"
"    border: 1px solid #4c566a; /* Subtle border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding inside the line edit */\n"
"    color: #d8dee9; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: 400; /* Font weight */\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    background-color: #3b4252; /* Background color of the drop-down button */\n"
"    border: none; /* No border for the drop-down button */\n"
"    border-top-right-radius: 5px; /* Rounded corners for the drop-down button */\n"
"    border-bottom-right-radius: 5px; /* Rounded corners for the drop-down button */\n"
"}\n"
"\n"
"QTimeEdit::drop-down:hover {\n"
"    background-color: #434c5e; /* Hover background color for the drop-down button */\n"
"}\n"
"\n"
"QTimeEdit::drop-down::drop-down-button {\n"
"    image: url(:/icons/icons8-time-80.png); /* Set your icon path */\n"
"    width: 16px; /* Width of the dr"
                        "op-down arrow icon */\n"
"    height: 16px; /* Height of the drop-down arrow icon */\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 1px solid #81a1c1; /* Border color when focused */\n"
"    background-color: #3b4252; /* Slightly lighter background color when focused */\n"
"    selection-background-color: #81a1c1; /* Selection background color */\n"
"    selection-color: #2e3440; /* Selection text color */\n"
"}\n"
"\n"
"QTimeEdit::placeholder {\n"
"    color: #4c566a; /* Placeholder text color */\n"
"    font-style: italic; /* Italicize placeholder text */\n"
"}")
        self.time_start.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.horizontalLayout_14.addWidget(self.time_start)


        self.verticalLayout_19.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.frame_34)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.time_end = QTimeEdit(self.frame_34)
        self.time_end.setObjectName(u"time_end")
        self.time_end.setStyleSheet(u"QTimeEdit {\n"
"    background-color: #2e3440; /* Dark background color */\n"
"    border: 1px solid #4c566a; /* Subtle border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding: 5px 10px; /* Padding inside the line edit */\n"
"    color: #d8dee9; /* Text color */\n"
"    font-size: 14px; /* Font size */\n"
"    font-weight: 400; /* Font weight */\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    background-color: #3b4252; /* Background color of the drop-down button */\n"
"    border: none; /* No border for the drop-down button */\n"
"    border-top-right-radius: 5px; /* Rounded corners for the drop-down button */\n"
"    border-bottom-right-radius: 5px; /* Rounded corners for the drop-down button */\n"
"}\n"
"\n"
"QTimeEdit::drop-down:hover {\n"
"    background-color: #434c5e; /* Hover background color for the drop-down button */\n"
"}\n"
"\n"
"QTimeEdit::drop-down::drop-down-button {\n"
"    image: url(:/icons/icons8-time-80.png); /* Set your icon path */\n"
"    width: 16px; /* Width of the dr"
                        "op-down arrow icon */\n"
"    height: 16px; /* Height of the drop-down arrow icon */\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 1px solid #81a1c1; /* Border color when focused */\n"
"    background-color: #3b4252; /* Slightly lighter background color when focused */\n"
"    selection-background-color: #81a1c1; /* Selection background color */\n"
"    selection-color: #2e3440; /* Selection text color */\n"
"}\n"
"\n"
"QTimeEdit::placeholder {\n"
"    color: #4c566a; /* Placeholder text color */\n"
"    font-style: italic; /* Italicize placeholder text */\n"
"}")
        self.time_end.setLocale(QLocale(QLocale.Persian, QLocale.Iran))

        self.horizontalLayout_16.addWidget(self.time_end)


        self.verticalLayout_19.addWidget(self.frame_34)


        self.verticalLayout_8.addWidget(self.frame_30)


        self.verticalLayout_26.addWidget(self.groupBox_2)

        self.progressBar = QProgressBar(self.frame_45)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_26.addWidget(self.progressBar)

        self.splitter.addWidget(self.frame_45)

        self.verticalLayout_20.addWidget(self.splitter)


        self.verticalLayout_35.addWidget(self.frame_4)


        self.horizontalLayout_29.addWidget(self.frame_42)


        self.verticalLayout_32.addWidget(self.frame_82)


        self.horizontalLayout_6.addWidget(self.frame_39)

        self.stackedWidget.addWidget(self.page_download)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.frame_8 = QFrame(self.main_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 100))
        self.frame_8.setStyleSheet(u"background-color:#acb7cc;")
        self.frame_8.setFrameShape(QFrame.Shape.Box)
        self.frame_8.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_8.setLineWidth(2)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_10)

        self.label_24 = QLabel(self.frame_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(100, 16777215))
        self.label_24.setStyleSheet(u"font-size:18px;\n"
"font: 16pt \"Mongolian Baiti\";")

        self.horizontalLayout_23.addWidget(self.label_24)

        self.log_label = QLabel(self.frame_8)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setMinimumSize(QSize(300, 0))
        self.log_label.setMaximumSize(QSize(400, 16777215))
        self.log_label.setFrameShape(QFrame.Shape.Box)
        self.log_label.setFrameShadow(QFrame.Shadow.Raised)
        self.log_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.log_label.setMargin(4)

        self.horizontalLayout_23.addWidget(self.log_label)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addWidget(self.frame_8)


        self.horizontalLayout_27.addWidget(self.main_frame)


        self.verticalLayout.addWidget(self.middle)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.download_filter_stackWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_logo.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"RailWay Monitor Software - Arian Shabake", None))
#if QT_CONFIG(tooltip)
        self.btn_side_playback.setToolTip(QCoreApplication.translate("MainWindow", u"Live View", None))
#endif // QT_CONFIG(tooltip)
        self.btn_side_playback.setText(QCoreApplication.translate("MainWindow", u"  PlayBack", None))
#if QT_CONFIG(tooltip)
        self.btn_side_download.setToolTip(QCoreApplication.translate("MainWindow", u"Report", None))
#endif // QT_CONFIG(tooltip)
        self.btn_side_download.setText(QCoreApplication.translate("MainWindow", u" Download", None))
#if QT_CONFIG(tooltip)
        self.btn_side_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Defect Parameters", None))
#endif // QT_CONFIG(tooltip)
        self.btn_side_settings.setText(QCoreApplication.translate("MainWindow", u"    Settings", None))
#if QT_CONFIG(tooltip)
        self.btn_side_aboutus.setToolTip(QCoreApplication.translate("MainWindow", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.btn_side_aboutus.setText(QCoreApplication.translate("MainWindow", u"   AboutUs", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PlayBack", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Refresh Database :", None))
#if QT_CONFIG(tooltip)
        self.refresh_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_btn.setText("")
        self.refresh_image_database_log.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Train ID :", None))
#if QT_CONFIG(tooltip)
        self.btn_select_train.setToolTip(QCoreApplication.translate("MainWindow", u"Select", None))
#endif // QT_CONFIG(tooltip)
        self.btn_select_train.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.label_date_2.setText(QCoreApplication.translate("MainWindow", u"Selected Date :", None))
        self.label_date.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.playback_camera_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"test1", None))
        self.playback_camera_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"test2", None))

#if QT_CONFIG(tooltip)
        self.play_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Live", None))
#endif // QT_CONFIG(tooltip)
        self.play_btn.setText("")
#if QT_CONFIG(tooltip)
        self.pause_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Stop Live", None))
#endif // QT_CONFIG(tooltip)
        self.pause_btn.setText("")
#if QT_CONFIG(tooltip)
        self.stop_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Stop Live", None))
#endif // QT_CONFIG(tooltip)
        self.stop_btn.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Speed : ", None))
#if QT_CONFIG(tooltip)
        self.speed_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Stop Live", None))
#endif // QT_CONFIG(tooltip)
        self.speed_btn.setText(QCoreApplication.translate("MainWindow", u"1x", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Time : ", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Manage Stations", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Name * : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"City * : ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"IP Address * :", None))
        self.ip_input.setText("")
        self.ip_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: 192.168.1.50", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Username :", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Password : ", None))
        self.btn_add_check_connection.setText(QCoreApplication.translate("MainWindow", u"Check Connection", None))
        self.btn_add_check_connection.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"borderBlueButton", None))
        self.btn_save_add.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_save_add.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"fillBlueButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), QCoreApplication.translate("MainWindow", u"ADD", None))
        ___qtablewidgetitem = self.system_stations_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem1 = self.system_stations_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"city", None));
        ___qtablewidgetitem2 = self.system_stations_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ip", None));
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name * : ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"City * : ", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"IP Address *: ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Password : ", None))
        self.btn_modify_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_modify_save.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"fillBlueButton", None))
        self.btn_modify_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_modify_cancel.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"borderBlueButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.modify), QCoreApplication.translate("MainWindow", u"Modify", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Trains:", None))
        self.label_8.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"h3", None))
        ___qtablewidgetitem3 = self.download_filter_station_log.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem4 = self.download_filter_station_log.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem5 = self.download_filter_station_log.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select Stations:", None))
        self.label_4.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"h3", None))
        self.download_all_stations_checkbox.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.download_search_station.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search name", None))
        ___qtablewidgetitem6 = self.download_stations_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem7 = self.download_stations_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem8 = self.download_stations_table.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.download_stations_table.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.download_stations_table.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.download_filter_prev_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.download_filter_prev_btn.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"fillBlueButton", None))
        self.download_filter_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.download_filter_next_btn.setProperty("styleClass", QCoreApplication.translate("MainWindow", u"fillBlueButton", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.checkBox_4.setText("")
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_remove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.checkBox.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Train ID :", None))
        self.checkBox_2.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Start Date : ", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"End Date   : ", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_3.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Start Time  : ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"End Time    : ", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Message : ", None))
        self.log_label.setText("")
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_userProfile(object):
    def setupUi(self, userProfile):
        if not userProfile.objectName():
            userProfile.setObjectName(u"userProfile")
        userProfile.resize(431, 548)
        self.verticalLayout = QVBoxLayout(userProfile)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalStyleSheet = QWidget(userProfile)
        self.GlobalStyleSheet.setObjectName(u"GlobalStyleSheet")
        self.GlobalStyleSheet.setStyleSheet(u"/**************************QLineEdit***************************/\n"
"\n"
"QLineEdit\n"
"{\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	border: None;\n"
"	border-bottom: 2px solid rgba(105, 118, 132, 255);\n"
"	color: rgba(255, 255, 255, 230);\n"
"	padding-bottom: 7px;\n"
"	\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgba(151, 175, 201, 255);\n"
"}\n"
"\n"
"QLineEdit:disables {\n"
"	color: rgba(150, 150, 150, 230);\n"
"}\n"
"\n"
"/**************************QLabel***************************/\n"
"QLabel\n"
"{\n"
"	color: rgba(250, 250, 250, 200);\n"
"font : 18px;\n"
"}\n"
"\n"
"/**************************QComboBox***************************/\n"
"\n"
"QComboBox\n"
"{\n"
"	border:2px solid rgba(105, 118, 132, 255);\n"
"	background-color: transparent;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QComboBox:enabled{\n"
"	color: rgba(250, 250, 250, 140);\n"
"}\n"
"\n"
"QComboBox:disabled\n"
"{\n"
"	border: 2px solid rgba(61, 69, 77, 255);\n"
"	color: rgba(1"
                        "20, 120, 120, 140);\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled\n"
"{   \n"
"	image: url(:/resources/Icons/down_icon_gray.png);\n"
"	width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{   \n"
"	image: url(:/resources/Icons/down_icon_gray.png);\n"
"	width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding; \n"
"    subcontrol-position: bottom right;\n"
"    width: 30px; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px; \n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"    border-left: 3px solid rgba(151, 175, 201, 255);\n"
"	background-color: rgba(10, 14, 26, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgba(10, 14, 26, 255);\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"	border-bottom: 2px solid rgba(151, 175, 201, 255);\n"
"}\n"
"\n"
"/**************************QTableWidget***************************/\n"
"\n"
"QTableWidget {\n"
"    background-color: transparent"
                        ";\n"
"	gridline-color: #3C4D61;\n"
"	color: rgb(220, 220, 220);\n"
"	border: None;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #01011A;\n"
"    padding: 5px;\n"
"	border: None;\n"
"	border-bottom: 2px solid #3C4D61;\n"
"	/*border-left: 1px solid #3C4D61;*/\n"
"	font-weight: bold;\n"
"	color: rgb(220, 220, 220);\n"
"	min-height: 40px;\n"
"}\n"
"\n"
"QHeaderView::section:first {\n"
"   border-left: None;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	border-bottom: 1px solid #3C4D61;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #01011A;\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"\n"
"\n"
"/**************************QScrollBar***************************/\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #01011A;\n"
"    width: 7px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #3C4D61;\n"
"    min-height: 20px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: n"
                        "one;\n"
"    background: #01011A;\n"
"    height: 20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #01011A;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #01011A;\n"
"    height: 7px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #3C4D61;\n"
"    min-width: 20px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #01011A;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
""
                        "    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #01011A;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.GlobalStyleSheet)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LocalStyleSheet = QWidget(self.GlobalStyleSheet)
        self.LocalStyleSheet.setObjectName(u"LocalStyleSheet")
        self.verticalLayout_3 = QVBoxLayout(self.LocalStyleSheet)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PointStyleSheet = QWidget(self.LocalStyleSheet)
        self.PointStyleSheet.setObjectName(u"PointStyleSheet")
        self.PointStyleSheet.setStyleSheet(u"/**************************PmainFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PmainFrameStyle\"]\n"
"{\n"
"	border-image: url(:/icons/icons/back2.png);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/**************************PinnerFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PinnerFrameStyle\"]\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, 			y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0,100), stop:0.835227 rgba(0, 0, 0, 200));	\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/**************************PtopFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PtopFrameStyle\"]\n"
"{\n"
"	background-color: transparent;\n"
"	border: None;\n"
"}\n"
"\n"
"\n"
"/**************************PpagesFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PpagesFrameStyle\"]\n"
"{\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"/***********************PtempPushButtonStyle************************/\n"
""
                        "\n"
"*[styleSheet=\"PtempPushButtonStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"*[styleSheet=\"PtempPushButtonStyle\"]:pressed\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"/***********************PeyePushButtonStyle************************/\n"
"\n"
"*[styleSheet=\"PeyePushButtonStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"*[styleSheet=\"PeyePushButtonStyle\"]:pressed\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"/****************PpagesUnderLinePushButtonStyle*****************/\n"
"\n"
"*[styleSheet=\"PpagesUnderLinePushButtonStyle\"]\n"
"{\n"
"	color: rgba(250, 250, 250, 140);\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"*[styleSheet=\"PpagesUnderLinePushButtonStyle\"]:hover\n"
"{\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"*[styleSheet=\"PpagesUnderLinePushButtonStyle\"]:pressed\n"
"{\n"
"	color: rgba(250, 250, 250, 140);\n"
"	border: 0p"
                        "x;\n"
"	background-color: rgba(0,0,0,0);\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"/****************PpagesMainPushButtonStyle*****************/\n"
"\n"
"*[styleSheet=\"PpagesMainPushButtonStyle\"]\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color: rgba(255, 255, 255, 210);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"*[styleSheet=\"PpagesMainPushButtonStyle\"]:hover\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"\n"
"*[styleSheet=\"PpagesMainPushButtonStyle\"]:pressed\n"
"{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"/************************PmessageLabelStyle************************/\n"
"\n"
"*[styleSheet=\"PmessageLabelStyle\"]\n"
"{\n"
"	color:rgb(255, 99, 94);\n"
"}\n"
"\n"
"/*********************PmenuPushButt"
                        "onsStyle**********************/\n"
"\n"
"*[styleSheet=\"PmenuPushButtonsStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"	color: rgb(150, 150, 150);\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"}\n"
"\n"
"*[styleSheet=\"PmenuPushButtonsStyle\"]:hover\n"
"{\n"
"	background-color: rgba(224, 228, 236, 30);\n"
"	border-radius: 26px;\n"
"	color: rgb(250, 250, 250);\n"
"}\n"
"\n"
"/*********************PtransparentPushButtonStyle**********************/\n"
"\n"
"*[styleSheet=\"PtransparentPushButtonStyle\"]\n"
"{\n"
"	border: None;\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"/*********************PlineStyle**********************/\n"
"\n"
"*[styleSheet=\"PlineStyle\"]\n"
"{\n"
"	background-color: rgba(224, 228, 236, 20);\n"
"}\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.PointStyleSheet)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.PointStyleSheet)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"PmainFrameStyle")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"PinnerFrameStyle")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.top_frame = QFrame(self.frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 39))
        self.top_frame.setFrameShape(QFrame.NoFrame)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(14, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.top_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(26, 16777215))
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_btn.setStyleSheet(u"background-color:transparent;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-close-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout_5.addWidget(self.top_frame)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lbl_train_name = QLabel(self.frame_3)
        self.lbl_train_name.setObjectName(u"lbl_train_name")

        self.horizontalLayout_2.addWidget(self.lbl_train_name)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lbl_date = QLabel(self.frame_10)
        self.lbl_date.setObjectName(u"lbl_date")

        self.horizontalLayout_9.addWidget(self.lbl_date)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.spinBox_hour_start = QSpinBox(self.frame_8)
        self.spinBox_hour_start.setObjectName(u"spinBox_hour_start")
        self.spinBox_hour_start.setMinimumSize(QSize(60, 30))
        self.spinBox_hour_start.setMaximumSize(QSize(60, 30))
        self.spinBox_hour_start.setStyleSheet(u"QSpinBox {\n"
"    background-color: #2E2A3D; /* Background similar to top bar */\n"
"    color: white; /* Text color */\n"
"    font-size: 14px;\n"
"    padding: 0px;\n"
"    border: 2px solid #D43D41; /* Border with red color */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the up button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the down button */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #A93226; /* Darker red on hover */\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/ne"
                        "xt_gray.png); /* Path to custom up arrow image */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/prev_gray.png); /* Path to custom down arrow image */\n"
"}\n"
"")
        self.spinBox_hour_start.setMaximum(23)

        self.horizontalLayout_6.addWidget(self.spinBox_hour_start)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(6, 16777215))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.spinBox_minute_start = QSpinBox(self.frame_8)
        self.spinBox_minute_start.setObjectName(u"spinBox_minute_start")
        self.spinBox_minute_start.setMinimumSize(QSize(60, 30))
        self.spinBox_minute_start.setMaximumSize(QSize(60, 30))
        self.spinBox_minute_start.setStyleSheet(u"QSpinBox {\n"
"    background-color: #2E2A3D; /* Background similar to top bar */\n"
"    color: white; /* Text color */\n"
"    font-size: 14px;\n"
"    padding: 0px;\n"
"    border: 2px solid #D43D41; /* Border with red color */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the up button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the down button */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #A93226; /* Darker red on hover */\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/ne"
                        "xt_gray.png); /* Path to custom up arrow image */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/prev_gray.png); /* Path to custom down arrow image */\n"
"}\n"
"")
        self.spinBox_minute_start.setMaximum(59)

        self.horizontalLayout_6.addWidget(self.spinBox_minute_start)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spinBox_hour_end = QSpinBox(self.frame_9)
        self.spinBox_hour_end.setObjectName(u"spinBox_hour_end")
        self.spinBox_hour_end.setMinimumSize(QSize(60, 30))
        self.spinBox_hour_end.setMaximumSize(QSize(60, 30))
        self.spinBox_hour_end.setStyleSheet(u"QSpinBox {\n"
"    background-color: #2E2A3D; /* Background similar to top bar */\n"
"    color: white; /* Text color */\n"
"    font-size: 14px;\n"
"    padding: 0px;\n"
"    border: 2px solid #D43D41; /* Border with red color */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the up button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the down button */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #A93226; /* Darker red on hover */\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/ne"
                        "xt_gray.png); /* Path to custom up arrow image */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/prev_gray.png); /* Path to custom down arrow image */\n"
"}\n"
"")
        self.spinBox_hour_end.setMaximum(23)

        self.horizontalLayout_7.addWidget(self.spinBox_hour_end)

        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(6, 16777215))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.spinBox_minute_end = QSpinBox(self.frame_9)
        self.spinBox_minute_end.setObjectName(u"spinBox_minute_end")
        self.spinBox_minute_end.setMinimumSize(QSize(60, 30))
        self.spinBox_minute_end.setMaximumSize(QSize(60, 30))
        self.spinBox_minute_end.setStyleSheet(u"QSpinBox {\n"
"    background-color: #2E2A3D; /* Background similar to top bar */\n"
"    color: white; /* Text color */\n"
"    font-size: 14px;\n"
"    padding: 0px;\n"
"    border: 2px solid #D43D41; /* Border with red color */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the up button */\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    border-left: 1px solid white;\n"
"    background-color: #D43D41; /* Red background for the down button */\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #A93226; /* Darker red on hover */\n"
"}\n"
"\n"
"QSpinBox::up-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/ne"
                        "xt_gray.png); /* Path to custom up arrow image */\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"    border: none;\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    image: url(:/icons/icons/prev_gray.png); /* Path to custom down arrow image */\n"
"}\n"
"")
        self.spinBox_minute_end.setMaximum(59)

        self.horizontalLayout_7.addWidget(self.spinBox_minute_end)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lbl_selected_folder = QLineEdit(self.frame_7)
        self.lbl_selected_folder.setObjectName(u"lbl_selected_folder")
        self.lbl_selected_folder.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.lbl_selected_folder)

        self.btn_dst_path = QPushButton(self.frame_7)
        self.btn_dst_path.setObjectName(u"btn_dst_path")
        self.btn_dst_path.setMinimumSize(QSize(32, 20))
        self.btn_dst_path.setMaximumSize(QSize(43, 30))
        self.btn_dst_path.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_dst_path.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/icons/icons/icons8-browse-folder-100.png);\n"
"	border-radius: 20px;\n"
"}")
        self.btn_dst_path.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.btn_dst_path)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font:18px;\n"
"color:#D43D41;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_mp4 = QRadioButton(self.frame_2)
        self.radioButton_mp4.setObjectName(u"radioButton_mp4")
        self.radioButton_mp4.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radioButton_mp4)

        self.radioButton_mkv = QRadioButton(self.frame_2)
        self.radioButton_mkv.setObjectName(u"radioButton_mkv")
        self.radioButton_mkv.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_mkv)


        self.verticalLayout_5.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_start_copy = QPushButton(self.frame_4)
        self.btn_start_copy.setObjectName(u"btn_start_copy")
        self.btn_start_copy.setMinimumSize(QSize(200, 40))
        self.btn_start_copy.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setBold(True)
        self.btn_start_copy.setFont(font)
        self.btn_start_copy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_start_copy.setStyleSheet(u"QPushButton {\n"
"    background-color: #3A3F44; /* Dark gray background */\n"
"    color: white; /* White text color */\n"
"    border: 2px solid #D43D41; /* Blue border */\n"
"    border-radius: 5px;\n"
"    padding: 8px 16px; /* Padding for the button size */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4D9EFF; /* Lighter blue on hover */\n"
"    color: white; /* Keep the text white */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3A7CCC; /* Darker blue when pressed */\n"
"    border: 2px solid #3A7CCC; /* Change border color to match pressed state */\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #5A5A5A; /* Gray background when disabled */\n"
"    color: #A0A0A0; /* Lighter gray text when disabled */\n"
"    border: 2px solid #A0A0A0; /* Lighter gray border when disabled */\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.btn_start_copy, 0, Qt.AlignHCenter)

        self.lbl_msg = QLabel(self.frame_4)
        self.lbl_msg.setObjectName(u"lbl_msg")
        self.lbl_msg.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_6.addWidget(self.lbl_msg, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #D43D41; /* Red border */\n"
"    border-radius: 5px;\n"
"    background-color: #2E2A3D; /* Dark background similar to your top bar */\n"
"    text-align: center; /* Centers the percentage text */\n"
"    color: white; /* White text color */\n"
"    font-size: 14px; /* Font size for the percentage */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #D43D41; /* Red chunk (progress) color */\n"
"    width: 20px; /* Set a reasonable width for each chunk */\n"
"    border-radius: 5px; /* Rounded edges for smooth appearance */\n"
"}\n"
"\n"
"QProgressBar:horizontal {\n"
"    height: 20px; /* Height of the progress bar */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"}\n"
"\n"
"QProgressBar:vertical {\n"
"    width: 20px; /* Width for vertical progress bar */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.verticalLayout_6.addWidget(self.progressBar)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_29.addWidget(self.main_frame)


        self.verticalLayout_3.addWidget(self.PointStyleSheet)


        self.verticalLayout_2.addWidget(self.LocalStyleSheet)


        self.verticalLayout.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(userProfile)

        QMetaObject.connectSlotsByName(userProfile)
    # setupUi

    def retranslateUi(self, userProfile):
        userProfile.setWindowTitle(QCoreApplication.translate("userProfile", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("userProfile", u"Export Window", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("userProfile", u"Train Name :", None))
        self.lbl_train_name.setText(QCoreApplication.translate("userProfile", u"-", None))
        self.label_9.setText(QCoreApplication.translate("userProfile", u"Date :", None))
        self.lbl_date.setText(QCoreApplication.translate("userProfile", u"-", None))
        self.label_3.setText(QCoreApplication.translate("userProfile", u"Start :", None))
        self.label_6.setText(QCoreApplication.translate("userProfile", u":", None))
        self.label_4.setText(QCoreApplication.translate("userProfile", u"End  :", None))
        self.label_7.setText(QCoreApplication.translate("userProfile", u":", None))
        self.label_5.setText(QCoreApplication.translate("userProfile", u"Destination Path :", None))
        self.lbl_selected_folder.setPlaceholderText(QCoreApplication.translate("userProfile", u"C:/...", None))
        self.btn_dst_path.setText("")
        self.radioButton_mp4.setText(QCoreApplication.translate("userProfile", u"MP4", None))
        self.radioButton_mkv.setText(QCoreApplication.translate("userProfile", u"Mkv_x265", None))
        self.btn_start_copy.setText(QCoreApplication.translate("userProfile", u"Start Copy", None))
        self.lbl_msg.setText("")
    # retranslateUi


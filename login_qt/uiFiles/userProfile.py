# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userProfile.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_userProfile(object):
    def setupUi(self, userProfile):
        if not userProfile.objectName():
            userProfile.setObjectName(u"userProfile")
        userProfile.resize(372, 541)
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
"	color: rgba(250, 250, 250, 140)\n"
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
"	color: rgba(120, 120, 120, 140);\n"
""
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
"    background-color: transparent;\n"
"	gridline-color: #"
                        "3C4D61;\n"
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
"    border: none;\n"
"    background:"
                        " #01011A;\n"
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
"    subcontrol-origin: "
                        "margin;\n"
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
"	border-image: url(:/resources/Icons/Untitled.png);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/**************************PinnerFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PinnerFrameStyle\"]\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, 			y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 120), stop:0.835227 rgba(0, 0, 0, 150));	\n"
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
"/***********************PtempPushButtonStyle********************"
                        "****/\n"
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
"	"
                        "border: 0px;\n"
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
"/*********************Pme"
                        "nuPushButtonsStyle**********************/\n"
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
        self.inner_frame = QFrame(self.main_frame)
        self.inner_frame.setObjectName(u"inner_frame")
        self.inner_frame.setStyleSheet(u"PinnerFrameStyle")
        self.inner_frame.setFrameShape(QFrame.StyledPanel)
        self.inner_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.inner_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 9, 5, 0)
        self.top_frame = QFrame(self.inner_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 60))
        self.top_frame.setStyleSheet(u"PtopFrameStyle")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_btn.setStyleSheet(u"#close_btn{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"#forgot_btn:pressed{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resources/Icons/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.close_btn, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.top_frame)

        self.top_menu_frame = QFrame(self.inner_frame)
        self.top_menu_frame.setObjectName(u"top_menu_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_menu_frame.sizePolicy().hasHeightForWidth())
        self.top_menu_frame.setSizePolicy(sizePolicy1)
        self.top_menu_frame.setMinimumSize(QSize(0, 40))
        self.top_menu_frame.setMaximumSize(QSize(16777215, 40))
        self.top_menu_frame.setStyleSheet(u"PtopFrameStyle")
        self.top_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.top_menu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_menu_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 0, 9)
        self.menu_btn = QPushButton(self.top_menu_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.menu_btn.setStyleSheet(u"PtransparentPushButtonStyle")
        icon1 = QIcon()
        icon1.addFile(u":/resources/Icons/top_menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu_btn.setIcon(icon1)
        self.menu_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.menu_btn, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.top_menu_frame)

        self.stackedWidget = QStackedWidget(self.inner_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_menu = QWidget()
        self.page_menu.setObjectName(u"page_menu")
        self.verticalLayout_9 = QVBoxLayout(self.page_menu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.page_menu)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setStyleSheet(u"PpagesFrameStyle")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 20, -1, 50)
        self.show_change_username_btn = QPushButton(self.menu_frame)
        self.show_change_username_btn.setObjectName(u"show_change_username_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.show_change_username_btn.sizePolicy().hasHeightForWidth())
        self.show_change_username_btn.setSizePolicy(sizePolicy2)
        self.show_change_username_btn.setMinimumSize(QSize(0, 70))
        self.show_change_username_btn.setMaximumSize(QSize(16777215, 70))
        self.show_change_username_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_change_username_btn.setStyleSheet(u"PmenuPushButtonsStyle")
        icon2 = QIcon()
        icon2.addFile(u":/resources/Icons/username.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_change_username_btn.setIcon(icon2)
        self.show_change_username_btn.setIconSize(QSize(26, 26))

        self.verticalLayout_12.addWidget(self.show_change_username_btn)

        self.change_username_line = QFrame(self.menu_frame)
        self.change_username_line.setObjectName(u"change_username_line")
        self.change_username_line.setMinimumSize(QSize(300, 0))
        self.change_username_line.setMaximumSize(QSize(300, 16777215))
        self.change_username_line.setStyleSheet(u"PlineStyle")
        self.change_username_line.setFrameShape(QFrame.Shape.HLine)
        self.change_username_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.change_username_line, 0, Qt.AlignHCenter)

        self.show_change_password_btn = QPushButton(self.menu_frame)
        self.show_change_password_btn.setObjectName(u"show_change_password_btn")
        sizePolicy2.setHeightForWidth(self.show_change_password_btn.sizePolicy().hasHeightForWidth())
        self.show_change_password_btn.setSizePolicy(sizePolicy2)
        self.show_change_password_btn.setMinimumSize(QSize(0, 70))
        self.show_change_password_btn.setMaximumSize(QSize(16777215, 70))
        self.show_change_password_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_change_password_btn.setStyleSheet(u"PmenuPushButtonsStyle")
        icon3 = QIcon()
        icon3.addFile(u":/resources/Icons/password.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_change_password_btn.setIcon(icon3)
        self.show_change_password_btn.setIconSize(QSize(26, 26))

        self.verticalLayout_12.addWidget(self.show_change_password_btn)

        self.change_password_line = QFrame(self.menu_frame)
        self.change_password_line.setObjectName(u"change_password_line")
        self.change_password_line.setMinimumSize(QSize(300, 0))
        self.change_password_line.setMaximumSize(QSize(300, 16777215))
        self.change_password_line.setStyleSheet(u"PlineStyle")
        self.change_password_line.setFrameShape(QFrame.Shape.HLine)
        self.change_password_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.change_password_line, 0, Qt.AlignHCenter)

        self.show_all_users_btn = QPushButton(self.menu_frame)
        self.show_all_users_btn.setObjectName(u"show_all_users_btn")
        sizePolicy2.setHeightForWidth(self.show_all_users_btn.sizePolicy().hasHeightForWidth())
        self.show_all_users_btn.setSizePolicy(sizePolicy2)
        self.show_all_users_btn.setMinimumSize(QSize(0, 70))
        self.show_all_users_btn.setMaximumSize(QSize(16777215, 70))
        self.show_all_users_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_all_users_btn.setStyleSheet(u"PmenuPushButtonsStyle")
        icon4 = QIcon()
        icon4.addFile(u":/resources/Icons/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_all_users_btn.setIcon(icon4)
        self.show_all_users_btn.setIconSize(QSize(40, 40))

        self.verticalLayout_12.addWidget(self.show_all_users_btn)

        self.all_users_line = QFrame(self.menu_frame)
        self.all_users_line.setObjectName(u"all_users_line")
        self.all_users_line.setMinimumSize(QSize(300, 0))
        self.all_users_line.setMaximumSize(QSize(300, 16777215))
        self.all_users_line.setStyleSheet(u"PlineStyle")
        self.all_users_line.setFrameShape(QFrame.Shape.HLine)
        self.all_users_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.all_users_line, 0, Qt.AlignHCenter)

        self.show_signup_btn = QPushButton(self.menu_frame)
        self.show_signup_btn.setObjectName(u"show_signup_btn")
        sizePolicy2.setHeightForWidth(self.show_signup_btn.sizePolicy().hasHeightForWidth())
        self.show_signup_btn.setSizePolicy(sizePolicy2)
        self.show_signup_btn.setMinimumSize(QSize(0, 70))
        self.show_signup_btn.setMaximumSize(QSize(16777215, 70))
        self.show_signup_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_signup_btn.setStyleSheet(u"PmenuPushButtonsStyle")
        icon5 = QIcon()
        icon5.addFile(u":/resources/Icons/add_user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_signup_btn.setIcon(icon5)
        self.show_signup_btn.setIconSize(QSize(34, 34))

        self.verticalLayout_12.addWidget(self.show_signup_btn)

        self.signup_line = QFrame(self.menu_frame)
        self.signup_line.setObjectName(u"signup_line")
        self.signup_line.setMinimumSize(QSize(300, 0))
        self.signup_line.setMaximumSize(QSize(300, 16777215))
        self.signup_line.setStyleSheet(u"PlineStyle")
        self.signup_line.setFrameShape(QFrame.Shape.HLine)
        self.signup_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.signup_line, 0, Qt.AlignHCenter)

        self.show_logout_btn = QPushButton(self.menu_frame)
        self.show_logout_btn.setObjectName(u"show_logout_btn")
        sizePolicy2.setHeightForWidth(self.show_logout_btn.sizePolicy().hasHeightForWidth())
        self.show_logout_btn.setSizePolicy(sizePolicy2)
        self.show_logout_btn.setMinimumSize(QSize(0, 70))
        self.show_logout_btn.setMaximumSize(QSize(16777215, 70))
        self.show_logout_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_logout_btn.setStyleSheet(u"PmenuPushButtonsStyle")
        icon6 = QIcon()
        icon6.addFile(u":/resources/Icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.show_logout_btn.setIcon(icon6)
        self.show_logout_btn.setIconSize(QSize(34, 34))

        self.verticalLayout_12.addWidget(self.show_logout_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)


        self.verticalLayout_9.addWidget(self.menu_frame)

        self.stackedWidget.addWidget(self.page_menu)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.verticalLayout_10 = QVBoxLayout(self.page_login)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(self.page_login)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setStyleSheet(u"PpagesFrameStyle")
        self.login_frame.setFrameShape(QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.login_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(13, 124, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.login_username_icon = QLabel(self.login_frame)
        self.login_username_icon.setObjectName(u"login_username_icon")
        sizePolicy.setHeightForWidth(self.login_username_icon.sizePolicy().hasHeightForWidth())
        self.login_username_icon.setSizePolicy(sizePolicy)
        self.login_username_icon.setMaximumSize(QSize(25, 25))
        self.login_username_icon.setPixmap(QPixmap(u":/resources/Icons/username.png"))
        self.login_username_icon.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.login_username_icon)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.login_username_lineEdit = QLineEdit(self.login_frame)
        self.login_username_lineEdit.setObjectName(u"login_username_lineEdit")
        self.login_username_lineEdit.setMinimumSize(QSize(200, 40))
        self.login_username_lineEdit.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.login_username_lineEdit.setFont(font)
        self.login_username_lineEdit.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.login_username_lineEdit)

        self.login_temp_btn = QPushButton(self.login_frame)
        self.login_temp_btn.setObjectName(u"login_temp_btn")
        self.login_temp_btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.login_temp_btn.sizePolicy().hasHeightForWidth())
        self.login_temp_btn.setSizePolicy(sizePolicy)
        self.login_temp_btn.setMinimumSize(QSize(20, 16))
        self.login_temp_btn.setMaximumSize(QSize(20, 16))
        self.login_temp_btn.setStyleSheet(u"PtempPushButtonStyle")

        self.horizontalLayout_3.addWidget(self.login_temp_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.login_password_icon = QLabel(self.login_frame)
        self.login_password_icon.setObjectName(u"login_password_icon")
        sizePolicy.setHeightForWidth(self.login_password_icon.sizePolicy().hasHeightForWidth())
        self.login_password_icon.setSizePolicy(sizePolicy)
        self.login_password_icon.setMaximumSize(QSize(25, 25))
        self.login_password_icon.setPixmap(QPixmap(u":/resources/Icons/password.png"))
        self.login_password_icon.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.login_password_icon)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.login_password_lineEdit = QLineEdit(self.login_frame)
        self.login_password_lineEdit.setObjectName(u"login_password_lineEdit")
        self.login_password_lineEdit.setMinimumSize(QSize(200, 40))
        self.login_password_lineEdit.setMaximumSize(QSize(200, 40))
        self.login_password_lineEdit.setFont(font)
        self.login_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.login_password_lineEdit)

        self.login_eye_btn = QPushButton(self.login_frame)
        self.login_eye_btn.setObjectName(u"login_eye_btn")
        sizePolicy.setHeightForWidth(self.login_eye_btn.sizePolicy().hasHeightForWidth())
        self.login_eye_btn.setSizePolicy(sizePolicy)
        self.login_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        icon7 = QIcon()
        icon7.addFile(u":/resources/Icons/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.login_eye_btn.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.login_eye_btn)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_10 = QSpacerItem(13, 124, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(16)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.login_btn = QPushButton(self.login_frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(200, 40))
        self.login_btn.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.login_btn.setFont(font1)
        self.login_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.login_btn.setStyleSheet(u"PpagesMainPushButtonStyle")

        self.verticalLayout_36.addWidget(self.login_btn, 0, Qt.AlignHCenter)

        self.login_message_label = QLabel(self.login_frame)
        self.login_message_label.setObjectName(u"login_message_label")
        sizePolicy1.setHeightForWidth(self.login_message_label.sizePolicy().hasHeightForWidth())
        self.login_message_label.setSizePolicy(sizePolicy1)
        self.login_message_label.setStyleSheet(u"PmessageLabelStyle")
        self.login_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.login_message_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_36)


        self.verticalLayout_10.addWidget(self.login_frame)

        self.stackedWidget.addWidget(self.page_login)
        self.page_change_password = QWidget()
        self.page_change_password.setObjectName(u"page_change_password")
        self.verticalLayout_17 = QVBoxLayout(self.page_change_password)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.change_password_frame = QFrame(self.page_change_password)
        self.change_password_frame.setObjectName(u"change_password_frame")
        self.change_password_frame.setStyleSheet(u"PpagesFrameStyle")
        self.change_password_frame.setFrameShape(QFrame.StyledPanel)
        self.change_password_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.change_password_frame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(30)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.change_current_password_lineEdit = QLineEdit(self.change_password_frame)
        self.change_current_password_lineEdit.setObjectName(u"change_current_password_lineEdit")

        self.horizontalLayout_21.addWidget(self.change_current_password_lineEdit)

        self.change_current_password_eye_btn = QPushButton(self.change_password_frame)
        self.change_current_password_eye_btn.setObjectName(u"change_current_password_eye_btn")
        sizePolicy.setHeightForWidth(self.change_current_password_eye_btn.sizePolicy().hasHeightForWidth())
        self.change_current_password_eye_btn.setSizePolicy(sizePolicy)
        self.change_current_password_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.change_current_password_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        self.change_current_password_eye_btn.setIcon(icon7)

        self.horizontalLayout_21.addWidget(self.change_current_password_eye_btn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.change_new_password_lineEdit = QLineEdit(self.change_password_frame)
        self.change_new_password_lineEdit.setObjectName(u"change_new_password_lineEdit")
        self.change_new_password_lineEdit.setMinimumSize(QSize(0, 0))
        self.change_new_password_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.change_new_password_lineEdit.setFont(font)
        self.change_new_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_22.addWidget(self.change_new_password_lineEdit)

        self.change_new_password_eye_btn = QPushButton(self.change_password_frame)
        self.change_new_password_eye_btn.setObjectName(u"change_new_password_eye_btn")
        sizePolicy.setHeightForWidth(self.change_new_password_eye_btn.sizePolicy().hasHeightForWidth())
        self.change_new_password_eye_btn.setSizePolicy(sizePolicy)
        self.change_new_password_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.change_new_password_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        self.change_new_password_eye_btn.setIcon(icon7)

        self.horizontalLayout_22.addWidget(self.change_new_password_eye_btn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.change_confirm_password_lineEdit = QLineEdit(self.change_password_frame)
        self.change_confirm_password_lineEdit.setObjectName(u"change_confirm_password_lineEdit")
        self.change_confirm_password_lineEdit.setMinimumSize(QSize(0, 0))
        self.change_confirm_password_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.change_confirm_password_lineEdit.setFont(font)
        self.change_confirm_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_23.addWidget(self.change_confirm_password_lineEdit)

        self.change_confirm_password_eye_btn = QPushButton(self.change_password_frame)
        self.change_confirm_password_eye_btn.setObjectName(u"change_confirm_password_eye_btn")
        sizePolicy.setHeightForWidth(self.change_confirm_password_eye_btn.sizePolicy().hasHeightForWidth())
        self.change_confirm_password_eye_btn.setSizePolicy(sizePolicy)
        self.change_confirm_password_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.change_confirm_password_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        self.change_confirm_password_eye_btn.setIcon(icon7)

        self.horizontalLayout_23.addWidget(self.change_confirm_password_eye_btn)


        self.verticalLayout_19.addLayout(self.horizontalLayout_23)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(16)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.change_password_btn = QPushButton(self.change_password_frame)
        self.change_password_btn.setObjectName(u"change_password_btn")
        self.change_password_btn.setMinimumSize(QSize(200, 40))
        self.change_password_btn.setMaximumSize(QSize(200, 40))
        self.change_password_btn.setFont(font1)
        self.change_password_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.change_password_btn.setStyleSheet(u"PpagesMainPushButtonStyle")

        self.verticalLayout_30.addWidget(self.change_password_btn, 0, Qt.AlignHCenter)

        self.change_password_message_label = QLabel(self.change_password_frame)
        self.change_password_message_label.setObjectName(u"change_password_message_label")
        sizePolicy1.setHeightForWidth(self.change_password_message_label.sizePolicy().hasHeightForWidth())
        self.change_password_message_label.setSizePolicy(sizePolicy1)
        self.change_password_message_label.setStyleSheet(u"PmessageLabelStyle")
        self.change_password_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.change_password_message_label)


        self.verticalLayout_20.addLayout(self.verticalLayout_30)


        self.verticalLayout_17.addWidget(self.change_password_frame)

        self.stackedWidget.addWidget(self.page_change_password)
        self.page_change_username = QWidget()
        self.page_change_username.setObjectName(u"page_change_username")
        self.verticalLayout_26 = QVBoxLayout(self.page_change_username)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.change_username_frame = QFrame(self.page_change_username)
        self.change_username_frame.setObjectName(u"change_username_frame")
        self.change_username_frame.setStyleSheet(u"PpagesFrameStyle")
        self.change_username_frame.setFrameShape(QFrame.StyledPanel)
        self.change_username_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.change_username_frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(40)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.change_current_username_lineEdit = QLineEdit(self.change_username_frame)
        self.change_current_username_lineEdit.setObjectName(u"change_current_username_lineEdit")
        self.change_current_username_lineEdit.setEnabled(False)
        self.change_current_username_lineEdit.setMinimumSize(QSize(0, 0))
        self.change_current_username_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.change_current_username_lineEdit.setFont(font)
        self.change_current_username_lineEdit.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_24.addWidget(self.change_current_username_lineEdit)


        self.verticalLayout_25.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.change_new_username_lineEdit = QLineEdit(self.change_username_frame)
        self.change_new_username_lineEdit.setObjectName(u"change_new_username_lineEdit")
        self.change_new_username_lineEdit.setMinimumSize(QSize(0, 0))
        self.change_new_username_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.change_new_username_lineEdit.setFont(font)
        self.change_new_username_lineEdit.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_28.addWidget(self.change_new_username_lineEdit)


        self.verticalLayout_25.addLayout(self.horizontalLayout_28)


        self.verticalLayout_24.addLayout(self.verticalLayout_25)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(16)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.change_username_btn = QPushButton(self.change_username_frame)
        self.change_username_btn.setObjectName(u"change_username_btn")
        self.change_username_btn.setMinimumSize(QSize(200, 40))
        self.change_username_btn.setMaximumSize(QSize(200, 40))
        self.change_username_btn.setFont(font1)
        self.change_username_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.change_username_btn.setStyleSheet(u"PpagesMainPushButtonStyle")

        self.verticalLayout_31.addWidget(self.change_username_btn, 0, Qt.AlignHCenter)

        self.change_username_message_label = QLabel(self.change_username_frame)
        self.change_username_message_label.setObjectName(u"change_username_message_label")
        sizePolicy1.setHeightForWidth(self.change_username_message_label.sizePolicy().hasHeightForWidth())
        self.change_username_message_label.setSizePolicy(sizePolicy1)
        self.change_username_message_label.setStyleSheet(u"PmessageLabelStyle")
        self.change_username_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.change_username_message_label)


        self.verticalLayout_24.addLayout(self.verticalLayout_31)


        self.verticalLayout_26.addWidget(self.change_username_frame)

        self.stackedWidget.addWidget(self.page_change_username)
        self.page_all_users = QWidget()
        self.page_all_users.setObjectName(u"page_all_users")
        self.verticalLayout_8 = QVBoxLayout(self.page_all_users)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.all_users_frame = QFrame(self.page_all_users)
        self.all_users_frame.setObjectName(u"all_users_frame")
        self.all_users_frame.setStyleSheet(u"PpagesFrameStyle")
        self.all_users_frame.setFrameShape(QFrame.StyledPanel)
        self.all_users_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.all_users_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.all_users_table = QTableWidget(self.all_users_frame)
        if (self.all_users_table.columnCount() < 2):
            self.all_users_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.all_users_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.all_users_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.all_users_table.setObjectName(u"all_users_table")
        self.all_users_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.all_users_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.all_users_table.setShowGrid(False)
        self.all_users_table.horizontalHeader().setStretchLastSection(True)
        self.all_users_table.verticalHeader().setVisible(False)
        self.all_users_table.verticalHeader().setCascadingSectionResizes(False)
        self.all_users_table.verticalHeader().setDefaultSectionSize(50)

        self.horizontalLayout_6.addWidget(self.all_users_table)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(16)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.all_users_message_label = QLabel(self.all_users_frame)
        self.all_users_message_label.setObjectName(u"all_users_message_label")
        sizePolicy1.setHeightForWidth(self.all_users_message_label.sizePolicy().hasHeightForWidth())
        self.all_users_message_label.setSizePolicy(sizePolicy1)
        self.all_users_message_label.setStyleSheet(u"PmessageLabelStyle")
        self.all_users_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.all_users_message_label)


        self.verticalLayout_11.addLayout(self.verticalLayout_32)


        self.verticalLayout_8.addWidget(self.all_users_frame)

        self.stackedWidget.addWidget(self.page_all_users)
        self.page_signup = QWidget()
        self.page_signup.setObjectName(u"page_signup")
        self.verticalLayout_18 = QVBoxLayout(self.page_signup)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.signup_frame = QFrame(self.page_signup)
        self.signup_frame.setObjectName(u"signup_frame")
        self.signup_frame.setStyleSheet(u"PpagesFrameStyle")
        self.signup_frame.setFrameShape(QFrame.StyledPanel)
        self.signup_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.signup_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(18)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.signup_username_lineEdit = QLineEdit(self.signup_frame)
        self.signup_username_lineEdit.setObjectName(u"signup_username_lineEdit")
        self.signup_username_lineEdit.setMinimumSize(QSize(0, 0))
        self.signup_username_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.signup_username_lineEdit.setFont(font)

        self.horizontalLayout_14.addWidget(self.signup_username_lineEdit)

        self.signup_temp_btn = QPushButton(self.signup_frame)
        self.signup_temp_btn.setObjectName(u"signup_temp_btn")
        sizePolicy.setHeightForWidth(self.signup_temp_btn.sizePolicy().hasHeightForWidth())
        self.signup_temp_btn.setSizePolicy(sizePolicy)
        self.signup_temp_btn.setMinimumSize(QSize(20, 16))
        self.signup_temp_btn.setMaximumSize(QSize(20, 16))
        self.signup_temp_btn.setStyleSheet(u"PtempPushButtonStyle")

        self.horizontalLayout_14.addWidget(self.signup_temp_btn)


        self.verticalLayout_28.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.signup_password_lineEdit = QLineEdit(self.signup_frame)
        self.signup_password_lineEdit.setObjectName(u"signup_password_lineEdit")
        self.signup_password_lineEdit.setMinimumSize(QSize(0, 0))
        self.signup_password_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.signup_password_lineEdit.setFont(font)
        self.signup_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_16.addWidget(self.signup_password_lineEdit)

        self.signup_password_eye_btn = QPushButton(self.signup_frame)
        self.signup_password_eye_btn.setObjectName(u"signup_password_eye_btn")
        sizePolicy.setHeightForWidth(self.signup_password_eye_btn.sizePolicy().hasHeightForWidth())
        self.signup_password_eye_btn.setSizePolicy(sizePolicy)
        self.signup_password_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signup_password_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        self.signup_password_eye_btn.setIcon(icon7)

        self.horizontalLayout_16.addWidget(self.signup_password_eye_btn)


        self.verticalLayout_28.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.signup_confirm_password_lineEdit = QLineEdit(self.signup_frame)
        self.signup_confirm_password_lineEdit.setObjectName(u"signup_confirm_password_lineEdit")
        self.signup_confirm_password_lineEdit.setMinimumSize(QSize(0, 0))
        self.signup_confirm_password_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.signup_confirm_password_lineEdit.setFont(font)
        self.signup_confirm_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_18.addWidget(self.signup_confirm_password_lineEdit)

        self.signup_confirm_password_eye_btn = QPushButton(self.signup_frame)
        self.signup_confirm_password_eye_btn.setObjectName(u"signup_confirm_password_eye_btn")
        sizePolicy.setHeightForWidth(self.signup_confirm_password_eye_btn.sizePolicy().hasHeightForWidth())
        self.signup_confirm_password_eye_btn.setSizePolicy(sizePolicy)
        self.signup_confirm_password_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signup_confirm_password_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        self.signup_confirm_password_eye_btn.setIcon(icon7)

        self.horizontalLayout_18.addWidget(self.signup_confirm_password_eye_btn)


        self.verticalLayout_28.addLayout(self.horizontalLayout_18)

        self.signup_role_comboBox = QComboBox(self.signup_frame)
        self.signup_role_comboBox.addItem("")
        self.signup_role_comboBox.setObjectName(u"signup_role_comboBox")
        self.signup_role_comboBox.setEnabled(True)
        self.signup_role_comboBox.setMinimumSize(QSize(0, 35))
        self.signup_role_comboBox.setMaximumSize(QSize(290, 16777215))

        self.verticalLayout_28.addWidget(self.signup_role_comboBox)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(16)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 5, -1, -1)
        self.signup_btn = QPushButton(self.signup_frame)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setMinimumSize(QSize(200, 40))
        self.signup_btn.setMaximumSize(QSize(200, 40))
        self.signup_btn.setFont(font1)
        self.signup_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.signup_btn.setStyleSheet(u"PpagesMainPushButtonStyle")

        self.verticalLayout_35.addWidget(self.signup_btn, 0, Qt.AlignHCenter)

        self.signup_message_label = QLabel(self.signup_frame)
        self.signup_message_label.setObjectName(u"signup_message_label")
        sizePolicy1.setHeightForWidth(self.signup_message_label.sizePolicy().hasHeightForWidth())
        self.signup_message_label.setSizePolicy(sizePolicy1)
        self.signup_message_label.setStyleSheet(u"PmessageLabelStyle")
        self.signup_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.signup_message_label)


        self.verticalLayout_27.addLayout(self.verticalLayout_35)


        self.verticalLayout_18.addWidget(self.signup_frame)

        self.stackedWidget.addWidget(self.page_signup)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.inner_frame)


        self.verticalLayout_29.addWidget(self.main_frame)


        self.verticalLayout_3.addWidget(self.PointStyleSheet)


        self.verticalLayout_2.addWidget(self.LocalStyleSheet)


        self.verticalLayout.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(userProfile)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(userProfile)
    # setupUi

    def retranslateUi(self, userProfile):
        userProfile.setWindowTitle(QCoreApplication.translate("userProfile", u"Form", None))
        self.close_btn.setText("")
        self.menu_btn.setText("")
        self.show_change_username_btn.setText(QCoreApplication.translate("userProfile", u"      Change Username", None))
        self.show_change_password_btn.setText(QCoreApplication.translate("userProfile", u"      Change Password", None))
        self.show_all_users_btn.setText(QCoreApplication.translate("userProfile", u"      All Users", None))
        self.show_signup_btn.setText(QCoreApplication.translate("userProfile", u"      Signup", None))
        self.show_logout_btn.setText(QCoreApplication.translate("userProfile", u"      Logout", None))
        self.login_username_icon.setText("")
        self.login_username_lineEdit.setText("")
        self.login_username_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Username", None))
        self.login_temp_btn.setText("")
        self.login_password_icon.setText("")
        self.login_password_lineEdit.setText("")
        self.login_password_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Password", None))
        self.login_eye_btn.setText("")
        self.login_btn.setText(QCoreApplication.translate("userProfile", u"LOGIN", None))
        self.login_message_label.setText("")
        self.change_current_password_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Current Password", None))
        self.change_current_password_eye_btn.setText("")
        self.change_new_password_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"New Password", None))
        self.change_new_password_eye_btn.setText("")
        self.change_confirm_password_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Confirm Password", None))
        self.change_confirm_password_eye_btn.setText("")
        self.change_password_btn.setText(QCoreApplication.translate("userProfile", u"CHANGE", None))
        self.change_password_message_label.setText("")
        self.change_current_username_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Current Username", None))
        self.change_new_username_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"New Username", None))
        self.change_username_btn.setText(QCoreApplication.translate("userProfile", u"CHANGE", None))
        self.change_username_message_label.setText("")
        self.all_users_message_label.setText("")
        self.signup_username_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Username", None))
        self.signup_temp_btn.setText("")
        self.signup_password_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Password", None))
        self.signup_password_eye_btn.setText("")
        self.signup_confirm_password_lineEdit.setPlaceholderText(QCoreApplication.translate("userProfile", u"Confirm Password", None))
        self.signup_confirm_password_eye_btn.setText("")
        self.signup_role_comboBox.setItemText(0, QCoreApplication.translate("userProfile", u"Role", None))

        self.signup_btn.setText(QCoreApplication.translate("userProfile", u"SIGNUP", None))
        self.signup_message_label.setText("")
    # retranslateUi


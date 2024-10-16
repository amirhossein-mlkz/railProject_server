# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editUser.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc
import resource_rc

class Ui_editUser(object):
    def setupUi(self, editUser):
        if not editUser.objectName():
            editUser.setObjectName(u"editUser")
        editUser.resize(276, 325)
        self.verticalLayout = QVBoxLayout(editUser)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.GlobalStyleSheet = QWidget(editUser)
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
"\n"
"	\n"
"background-color:rgb(65, 59, 71);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/**************************PinnerFrameStyle***************************/\n"
"\n"
"*[styleSheet=\"PinnerFrameStyle\"]\n"
"{\n"
"	background-color: transparent;\n"
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
"	background-color: transparent;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"/***********************PtempPushButtonStyle************************/\n"
"\n"
"*[styleSheet=\"PtempPushButtonStyle\"]\n"
"{\n"
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"*[styleSheet=\"PtempPush"
                        "ButtonStyle\"]:pressed{\n"
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
"	border: 0px;\n"
"	background-color: rgba(0,0,0,0);\n"
"	text-decoration: underline;\n"
"}\n"
"\n"
"/****************PpagesMainPushButtonStyle*****************/\n"
""
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
"/**************************PmessageLabelStyle***************************/\n"
"\n"
"*[styleSheet=\"PmessageLabelStyle\"]\n"
"{\n"
"	color:rgb(255, 99, 94);\n"
"}")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setMinimumSize(QSize(0, 30))
        self.top_frame.setStyleSheet(u"PtopFrameStyle")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
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

        self.page_frame = QFrame(self.inner_frame)
        self.page_frame.setObjectName(u"page_frame")
        self.page_frame.setStyleSheet(u"PpagesFrameStyle")
        self.page_frame.setFrameShape(QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.page_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 12)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(18)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.edituser_username_lineEdit = QLineEdit(self.page_frame)
        self.edituser_username_lineEdit.setObjectName(u"edituser_username_lineEdit")
        self.edituser_username_lineEdit.setMinimumSize(QSize(0, 0))
        self.edituser_username_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        self.edituser_username_lineEdit.setFont(font)

        self.horizontalLayout_14.addWidget(self.edituser_username_lineEdit)

        self.edituser_temp_btn = QPushButton(self.page_frame)
        self.edituser_temp_btn.setObjectName(u"edituser_temp_btn")
        sizePolicy1.setHeightForWidth(self.edituser_temp_btn.sizePolicy().hasHeightForWidth())
        self.edituser_temp_btn.setSizePolicy(sizePolicy1)
        self.edituser_temp_btn.setMinimumSize(QSize(20, 16))
        self.edituser_temp_btn.setMaximumSize(QSize(20, 16))
        self.edituser_temp_btn.setStyleSheet(u"PtempPushButtonStyle")

        self.horizontalLayout_14.addWidget(self.edituser_temp_btn)


        self.verticalLayout_28.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.edituser_password_lineEdit = QLineEdit(self.page_frame)
        self.edituser_password_lineEdit.setObjectName(u"edituser_password_lineEdit")
        self.edituser_password_lineEdit.setMinimumSize(QSize(0, 0))
        self.edituser_password_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.edituser_password_lineEdit.setFont(font)
        self.edituser_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_16.addWidget(self.edituser_password_lineEdit)

        self.edituser_password_eye_btn = QPushButton(self.page_frame)
        self.edituser_password_eye_btn.setObjectName(u"edituser_password_eye_btn")
        sizePolicy1.setHeightForWidth(self.edituser_password_eye_btn.sizePolicy().hasHeightForWidth())
        self.edituser_password_eye_btn.setSizePolicy(sizePolicy1)
        self.edituser_password_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edituser_password_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        icon1 = QIcon()
        icon1.addFile(u":/resources/Icons/eye.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edituser_password_eye_btn.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.edituser_password_eye_btn)


        self.verticalLayout_28.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.edituser_confirm_password_lineEdit = QLineEdit(self.page_frame)
        self.edituser_confirm_password_lineEdit.setObjectName(u"edituser_confirm_password_lineEdit")
        self.edituser_confirm_password_lineEdit.setMinimumSize(QSize(0, 0))
        self.edituser_confirm_password_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.edituser_confirm_password_lineEdit.setFont(font)
        self.edituser_confirm_password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_18.addWidget(self.edituser_confirm_password_lineEdit)

        self.edituser_confirm_password_eye_btn = QPushButton(self.page_frame)
        self.edituser_confirm_password_eye_btn.setObjectName(u"edituser_confirm_password_eye_btn")
        sizePolicy1.setHeightForWidth(self.edituser_confirm_password_eye_btn.sizePolicy().hasHeightForWidth())
        self.edituser_confirm_password_eye_btn.setSizePolicy(sizePolicy1)
        self.edituser_confirm_password_eye_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edituser_confirm_password_eye_btn.setStyleSheet(u"PeyePushButtonStyle")
        self.edituser_confirm_password_eye_btn.setIcon(icon1)

        self.horizontalLayout_18.addWidget(self.edituser_confirm_password_eye_btn)


        self.verticalLayout_28.addLayout(self.horizontalLayout_18)

        self.edituser_role_comboBox = QComboBox(self.page_frame)
        self.edituser_role_comboBox.addItem("")
        self.edituser_role_comboBox.setObjectName(u"edituser_role_comboBox")
        self.edituser_role_comboBox.setEnabled(True)
        self.edituser_role_comboBox.setMinimumSize(QSize(0, 35))
        self.edituser_role_comboBox.setMaximumSize(QSize(290, 16777215))

        self.verticalLayout_28.addWidget(self.edituser_role_comboBox)

        self.apply_btn = QPushButton(self.page_frame)
        self.apply_btn.setObjectName(u"apply_btn")
        self.apply_btn.setMinimumSize(QSize(150, 40))
        self.apply_btn.setMaximumSize(QSize(150, 40))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.apply_btn.setFont(font1)
        self.apply_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.apply_btn.setStyleSheet(u"PpagesMainPushButtonStyle")

        self.verticalLayout_28.addWidget(self.apply_btn, 0, Qt.AlignHCenter)

        self.edit_user_message_label = QLabel(self.page_frame)
        self.edit_user_message_label.setObjectName(u"edit_user_message_label")
        sizePolicy.setHeightForWidth(self.edit_user_message_label.sizePolicy().hasHeightForWidth())
        self.edit_user_message_label.setSizePolicy(sizePolicy)
        self.edit_user_message_label.setStyleSheet(u"PmessageLabelStyle")
        self.edit_user_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.edit_user_message_label)


        self.verticalLayout_6.addLayout(self.verticalLayout_28)


        self.verticalLayout_5.addWidget(self.page_frame)


        self.verticalLayout_4.addWidget(self.inner_frame)


        self.verticalLayout_29.addWidget(self.main_frame)


        self.verticalLayout_3.addWidget(self.PointStyleSheet)


        self.verticalLayout_2.addWidget(self.LocalStyleSheet)


        self.verticalLayout.addWidget(self.GlobalStyleSheet)


        self.retranslateUi(editUser)

        QMetaObject.connectSlotsByName(editUser)
    # setupUi

    def retranslateUi(self, editUser):
        editUser.setWindowTitle(QCoreApplication.translate("editUser", u"Dialog", None))
        self.close_btn.setText("")
        self.edituser_username_lineEdit.setPlaceholderText(QCoreApplication.translate("editUser", u"Username", None))
        self.edituser_temp_btn.setText("")
        self.edituser_password_lineEdit.setPlaceholderText(QCoreApplication.translate("editUser", u"Password", None))
        self.edituser_password_eye_btn.setText("")
        self.edituser_confirm_password_lineEdit.setPlaceholderText(QCoreApplication.translate("editUser", u"Confirm Password", None))
        self.edituser_confirm_password_eye_btn.setText("")
        self.edituser_role_comboBox.setItemText(0, QCoreApplication.translate("editUser", u"Role", None))

        self.apply_btn.setText(QCoreApplication.translate("editUser", u"APPLY", None))
        self.edit_user_message_label.setText("")
    # retranslateUi


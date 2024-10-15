# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

from uiUtils.GUIComponents import MessageWidget
import assets_rc
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1153, 749)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet(u"QLabel{\n"
"	color: #e0e0e0;\n"
"	font-size:14px;\n"
"}\n"
"\n"
"\n"
"*[styleClass=\"page\"]{\n"
"	background-color:rgb(36, 32, 39);\n"
"}\n"
"\n"
"*[styleClass=\"page-light\"]{\n"
"	background-color:rgb(65, 59, 71);\n"
"}\n"
"\n"
"\n"
"*[styleClass=\"hide\"]{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"/****************************************************************************/\n"
"/****************************************************************************/\n"
"\n"
"QPushButton[styleClass=\"fill_gradient_purple_btn\"]{\n"
"border-radius:15px;\n"
"padding:5px 10px;\n"
"font-weight:bold;\n"
"color:#fff;\n"
"\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 255), stop:1 rgba(118, 22, 228, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton[styleClass=\"fill_gradient_purple_btn\"]:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 255), stop:0.516484 rgba(118, 22, 228, 255));\n"
"}\n"
"/**********************"
                        "******************************************************/\n"
"/****************************************************************************/\n"
"QPushButton[styleClass=\"border_gradient_purple_btn\"]{\n"
"border-radius:15px;\n"
"padding:5px 10px;\n"
"font-weight:bold;\n"
"color:#fff;\n"
"\n"
"border: 3px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 255), stop:1 rgba(118, 22, 228, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton[styleClass=\"border_gradient_purple_btn\"]:hover{\n"
"border: 5px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 255), stop:1 rgba(118, 22, 228, 255));\n"
"border: 3px solid rgba(118, 22, 228, 255);\n"
"}\n"
"\n"
"/****************************************************************************/\n"
"/****************************************************************************/\n"
"\n"
" QTabWidget::pane { \n"
"        border: 1px solid #444; /* \u0631\u0646\u06af \u062d\u0627\u0634\u06cc\u0647 \u062f\u0648\u0631 TabWidget */\n"
""
                        "        background-color: #2b2b2b; /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u06a9\u0644 TabWidget */\n"
"    }\n"
"\n"
"    QTabBar::tab {\n"
"        background-color: rgb(65, 59, 71); /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u062a\u0628\u200c\u0647\u0627 \u062f\u0631 \u062d\u0627\u0644\u062a \u0639\u0627\u062f\u06cc */\n"
"        color: #ffffff;  /* \u0631\u0646\u06af \u0645\u062a\u0646 \u062a\u0628\u200c\u0647\u0627 */\n"
"        padding: 10px;  /* \u0641\u0636\u0627\u06cc \u062f\u0627\u062e\u0644\u06cc \u062a\u0628\u200c\u0647\u0627 */\n"
"        border: 1px solid #444; /* \u0631\u0646\u06af \u062d\u0627\u0634\u06cc\u0647 \u062f\u0648\u0631 \u062a\u0628\u200c\u0647\u0627 */\n"
"        border-bottom-color: #2b2b2b; /* \u0647\u0645\u200c\u0631\u0627\u0633\u062a\u0627\u06cc\u06cc \u062a\u0628\u200c\u0647\u0627 \u0628\u0627 \u067e\u0646\u0644 */\n"
"    }\n"
"\n"
"    QTabBar::tab:selected {\n"
"        background-color: #6327E8; /* \u0631\u0646"
                        "\u06af \u062a\u0628 \u0627\u0646\u062a\u062e\u0627\u0628 \u0634\u062f\u0647 */\n"
"        color: #ffffff;  /* \u0631\u0646\u06af \u0645\u062a\u0646 \u062a\u0628 \u0627\u0646\u062a\u062e\u0627\u0628 \u0634\u062f\u0647 */\n"
"        border-bottom-color: #2b2b2b; /* \u0628\u062f\u0648\u0646 \u062d\u0627\u0634\u06cc\u0647 \u062f\u0631 \u067e\u0627\u06cc\u06cc\u0646 \u062a\u0628 \u0627\u0646\u062a\u062e\u0627\u0628 \u0634\u062f\u0647 */\n"
"    }\n"
"\n"
"    QTabBar::tab:hover {\n"
"        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 			255), stop:0.516484 rgba(118, 22, 228, 255));\n"
"    }\n"
"\n"
"    QTabWidget::tab-bar {\n"
"        left: 5px; /* \u0641\u0627\u0635\u0644\u0647\u200c\u06cc \u062a\u0628\u200c\u0647\u0627 \u0627\u0632 \u067e\u0646\u0644 */\n"
"    }\n"
"/****************************************************************************/\n"
"/****************************************************************************/\n"
"QLineEdit{\n"
"	background-c"
                        "olor: transparent;\n"
"	border:1px solid rgba(255, 255, 255, 50);\n"
"	border-bottom: 2px solid rgb(247, 240, 255);\n"
"	min-height: 25px;\n"
"	color: #f0e0e0;\n"
"	font-size: 14px;\n"
"	padding: 2px 10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"        border-bottom: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 255), stop:0.516484 rgba(118, 22, 228, 255));\n"
"        \n"
"    }\n"
"\n"
"QLineEdit:disabled{\n"
"	border-bottom: 2px solid #a0a0a0;\n"
"	color: #a0a0a0;\n"
"}\n"
"\n"
"/****************************************************************************/\n"
"/****************************************************************************/\n"
"   QTableWidget, QTableView {\n"
"       \n"
"	background-color: rgba(74, 74, 74, 50);\n"
"\n"
"    text-align:centre;\n"
"        \n"
"	color: : rgb(83, 83, 83);\n"
"        border: 1px solid #444444;  /* \u062d\u0627\u0634\u06cc\u0647 \u062f\u0648\u0631 \u062c\u062f\u0648\u0644 */\n"
"        gridline-color: #555555;  /* \u0631\u0646"
                        "\u06af \u062e\u0637\u0648\u0637 \u0634\u0628\u06a9\u0647 \u0628\u06cc\u0646 \u0633\u0644\u0648\u0644\u200c\u0647\u0627 */\n"
"        font-size: 14px;  /* \u0627\u0646\u062f\u0627\u0632\u0647 \u0641\u0648\u0646\u062a */\n"
"    }\n"
"\n"
"    QHeaderView {\n"
"        background-color: qlineargradient(spread:pad, x1:0.454, y1:0, x2:0.514495, y2:1, stop:0 rgba(77, 77, 104, 255), stop:1 rgba(77, 77, 104, 128));\n"
"        border-top-left-radius: 10px;   /* \u0634\u0639\u0627\u0639 \u06af\u0648\u0634\u0647 \u0628\u0627\u0644\u0627 \u0633\u0645\u062a \u0686\u067e */\n"
"        border-top-right-radius: 10px;  /* \u0634\u0639\u0627\u0639 \u06af\u0648\u0634\u0647 \u0628\u0627\u0644\u0627 \u0633\u0645\u062a \u0631\u0627\u0633\u062a */\n"
"        border: none;  /* \u062d\u0627\u0634\u06cc\u0647 \u0647\u062f\u0631 */\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: transparent;  /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u0633\u0631\u0633\u062a\u0648\u0646\u200c"
                        "\u0647\u0627 */\n"
"        color: #ffffff;  /* \u0631\u0646\u06af \u0645\u062a\u0646 \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"        padding: 5px;  /* \u0641\u0636\u0627\u06cc \u062f\u0627\u062e\u0644\u06cc \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"        border: none;  /* \u062d\u0630\u0641 \u062d\u0627\u0634\u06cc\u0647 \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"        font-weight: bold;  /* \u0628\u0648\u0644\u062f \u06a9\u0631\u062f\u0646 \u0641\u0648\u0646\u062a \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"    }\n"
"\n"
"/****************************************************************************/\n"
"/****************************************************************************/\n"
"\n"
"QCheckBox {\n"
"        spacing: 5px;  /* \u0641\u0627\u0635\u0644\u0647 \u0628\u06cc\u0646 \u062a\u06cc\u06a9 \u0648 \u0645\u062a\u0646 */\n"
"        font-size: 16px;  /* \u0627\u0646\u062f\u0627\u0632\u0647 \u0641\u0648\u0646\u062a */\n"
""
                        "        color: #ffffff;  /* \u0631\u0646\u06af \u0645\u062a\u0646 */\n"
"    }\n"
"\n"
"    QCheckBox::indicator {\n"
"        width: 18px;  /* \u0639\u0631\u0636 \u0686\u06a9 \u0628\u0627\u06a9\u0633 */\n"
"        height: 18px;  /* \u0627\u0631\u062a\u0641\u0627\u0639 \u0686\u06a9 \u0628\u0627\u06a9\u0633 */\n"
"        border: 2px solid rgb(192, 197, 217);  /* \u062d\u0627\u0634\u06cc\u0647 \u0686\u06a9 \u0628\u0627\u06a9\u0633 */\n"
"        border-radius: 0px;  /* \u0634\u0639\u0627\u0639 \u06af\u0648\u0634\u0647 \u0686\u06a9 \u0628\u0627\u06a9\u0633 */\n"
"        background-color: transparent;  /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u0686\u06a9 \u0628\u0627\u06a9\u0633 */\n"
"    }\n"
"\n"
"    QCheckBox::indicator:checked {\n"
"        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 255), stop:0.516484 rgba(118, 22, 228, 255));  /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u0686\u06a9 \u0628\u0627"
                        "\u06a9\u0633 \u062f\u0631 \u062d\u0627\u0644\u062a \u062a\u06cc\u06a9 \u062e\u0648\u0631\u062f\u0647 */\n"
"        border: 2px solid rgb(192, 197, 217);  /* \u062d\u0627\u0634\u06cc\u0647 \u0686\u06a9 \u0628\u0627\u06a9\u0633 \u062f\u0631 \u062d\u0627\u0644\u062a \u062a\u06cc\u06a9 \u062e\u0648\u0631\u062f\u0647 */\n"
"\n"
"		background-image: url(:/icons/icons/check-wight-24.png);  /* \u0645\u0633\u06cc\u0631 \u0622\u06cc\u06a9\u0648\u0646 \u0686\u06a9 */\n"
"        background-repeat: no-repeat;  /* \u062c\u0644\u0648\u06af\u06cc\u0631\u06cc \u0627\u0632 \u062a\u06a9\u0631\u0627\u0631 \u0622\u06cc\u06a9\u0648\u0646 */\n"
"        background-position: center;  /* \u062a\u0631\u0627\u0632 \u06a9\u0631\u062f\u0646 \u0622\u06cc\u06a9\u0648\u0646 \u062f\u0631 \u0648\u0633\u0637 */\n"
"		border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(39, 83, 237, 255), stop:0.516484 rgba(118, 22, 228, 255));\n"
"    }\n"
"\n"
"    QCheckBox::indicator:unchecked:hover {\n"
"        border: 2px so"
                        "lid rgb(99, 39, 232);  /* \u062d\u0627\u0634\u06cc\u0647 \u0686\u06a9 \u0628\u0627\u06a9\u0633 \u062f\u0631 \u062d\u0627\u0644\u062a \u063a\u06cc\u0631\u0641\u0639\u0627\u0644 \u0648 \u0647\u0646\u06af\u0627\u0645\u06cc \u06a9\u0647 \u0645\u0627\u0648\u0633 \u0631\u0648\u06cc \u0622\u0646 \u0627\u0633\u062a */\n"
"    }\n"
"\n"
"    QCheckBox::indicator:checked:hover {\n"
"          /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u0686\u06a9 \u0628\u0627\u06a9\u0633 \u062f\u0631 \u062d\u0627\u0644\u062a \u062a\u06cc\u06a9 \u062e\u0648\u0631\u062f\u0647 \u0648 \u0645\u0627\u0648\u0633 \u0631\u0648\u06cc \u0622\u0646 \u0627\u0633\u062a */\n"
"    }\n"
"\n"
"/****************************************************************************/\n"
"/****************************************************************************/")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.softeware_top_frame = QFrame(self.centralwidget)
        self.softeware_top_frame.setObjectName(u"softeware_top_frame")
        self.softeware_top_frame.setMaximumSize(QSize(16777215, 35))
        self.softeware_top_frame.setStyleSheet(u"\n"
"background-color: #262632")
        self.softeware_top_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_22 = QHBoxLayout(self.softeware_top_frame)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.softeware_top_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(120, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame)

        self.label_32 = QLabel(self.softeware_top_frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 37))
        font = QFont()
        font.setFamilies([u"Mongolian Baiti"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"color: #f0f0f0;\n"
"font: 16pt ;")

        self.horizontalLayout_22.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.softeware_top_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(120, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minimize_btn = QPushButton(self.frame_2)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy)
        self.minimize_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"background-color:none;\n"
"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8-subtract-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame_2)
        self.maximize_btn.setObjectName(u"maximize_btn")
        sizePolicy.setHeightForWidth(self.maximize_btn.sizePolicy().hasHeightForWidth())
        self.maximize_btn.setSizePolicy(sizePolicy)
        self.maximize_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.maximize_btn.setStyleSheet(u"background-color:none;\n"
"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8-maximize-button-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximize_btn.setIcon(icon1)
        self.maximize_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.frame_2)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_btn.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8-close-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.horizontalLayout_22.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.softeware_top_frame)

        self.middle = QFrame(self.centralwidget)
        self.middle.setObjectName(u"middle")
        self.middle.setMaximumSize(QSize(16777215, 16777215))
        self.middle.setStyleSheet(u"")
        self.middle.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_27 = QHBoxLayout(self.middle)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame = QFrame(self.middle)
        self.toggle_frame.setObjectName(u"toggle_frame")
        self.toggle_frame.setMinimumSize(QSize(130, 0))
        self.toggle_frame.setMaximumSize(QSize(130, 16777215))
        self.toggle_frame.setStyleSheet(u"QFrame{\n"
"	background: #413B47;\n"
"	padding:0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	color: #fff;\n"
"	background-color:transparent;\n"
"	padding: 0px;\n"
"	font-size: 10pt;\n"
"	font-weight: normal;\n"
"	border-radius:0px;\n"
"	min-width:120px;\n"
"	text-align: left; \n"
"	padding-left:10px;\n"
"}\n"
"\n"
"QPushButton::icon {\n"
"        subcontrol-position: left center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #D43D41;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #8D8D8D;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: rgb(0, 0, 0);\n"
"}")
        self.toggle_frame.setFrameShape(QFrame.NoFrame)
        self.toggle_frame.setLineWidth(3)
        self.verticalLayout_36 = QVBoxLayout(self.toggle_frame)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.toggle_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 82))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_side_playback = QPushButton(self.frame_7)
        self.btn_side_playback.setObjectName(u"btn_side_playback")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_side_playback.sizePolicy().hasHeightForWidth())
        self.btn_side_playback.setSizePolicy(sizePolicy1)
        self.btn_side_playback.setMinimumSize(QSize(130, 50))
        self.btn_side_playback.setMaximumSize(QSize(120, 50))
        self.btn_side_playback.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_playback.setStyleSheet(u"\n"
"    icon: url(:/icons/icons/playback-white.png);\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icons8-playback-24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_playback.setIcon(icon3)
        self.btn_side_playback.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.btn_side_playback)

        self.btn_side_download = QPushButton(self.frame_7)
        self.btn_side_download.setObjectName(u"btn_side_download")
        self.btn_side_download.setMinimumSize(QSize(130, 50))
        self.btn_side_download.setMaximumSize(QSize(120, 50))
        self.btn_side_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_download.setStyleSheet(u"\n"
"icon:url(:/icons/icons/download-white.png);\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8-file-download-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_download.setIcon(icon4)
        self.btn_side_download.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.btn_side_download)

        self.btn_side_settings = QPushButton(self.frame_7)
        self.btn_side_settings.setObjectName(u"btn_side_settings")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_side_settings.sizePolicy().hasHeightForWidth())
        self.btn_side_settings.setSizePolicy(sizePolicy2)
        self.btn_side_settings.setMinimumSize(QSize(130, 50))
        self.btn_side_settings.setMaximumSize(QSize(120, 50))
        self.btn_side_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_side_settings.setStyleSheet(u"icon: url(:/icons/icons/setting-white.png);\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8-settings-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_side_settings.setIcon(icon5)
        self.btn_side_settings.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.btn_side_settings)


        self.verticalLayout_36.addWidget(self.frame_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_3)


        self.horizontalLayout_27.addWidget(self.toggle_frame)

        self.line_3 = QFrame(self.middle)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setMaximumSize(QSize(1, 16777215))
        self.line_3.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_27.addWidget(self.line_3)

        self.main_frame = QFrame(self.middle)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setMinimumSize(QSize(1, 1))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"*[styleClass=\"page\"]{\n"
"	background-color:rgb(36, 32, 39);\n"
"}\n"
"")
        self.main_frame.setFrameShape(QFrame.NoFrame)
        self.main_frame.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.main_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pages_stackwidget = QStackedWidget(self.main_frame)
        self.pages_stackwidget.setObjectName(u"pages_stackwidget")
        self.pages_stackwidget.setStyleSheet(u"")
        self.pages_stackwidget.setFrameShape(QFrame.NoFrame)
        self.pages_stackwidget.setLineWidth(2)
        self.page_playback = QWidget()
        self.page_playback.setObjectName(u"page_playback")
        self.page_playback.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.page_playback)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.frame_18 = QFrame(self.page_playback)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 60))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.playback_filter_frame = QFrame(self.frame_18)
        self.playback_filter_frame.setObjectName(u"playback_filter_frame")
        self.playback_filter_frame.setMinimumSize(QSize(350, 404))
        self.playback_filter_frame.setMaximumSize(QSize(350, 16777215))
        self.playback_filter_frame.setStyleSheet(u"/*#playback_filter_frame{*/\n"
"QFrame{\n"
"background-color:rgb(49, 44, 53);\n"
"}\n"
"\n"
"")
        self.playback_filter_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.playback_filter_frame)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.playback_filter_frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(330, 0))
        self.frame_16.setMaximumSize(QSize(330, 16777215))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_22 = QVBoxLayout(self.frame_20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.refresh_btn = QPushButton(self.frame_20)
        self.refresh_btn.setObjectName(u"refresh_btn")
        sizePolicy1.setHeightForWidth(self.refresh_btn.sizePolicy().hasHeightForWidth())
        self.refresh_btn.setSizePolicy(sizePolicy1)
        self.refresh_btn.setMinimumSize(QSize(0, 30))
        self.refresh_btn.setMaximumSize(QSize(16777215, 16777215))
        self.refresh_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refresh_btn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/refresh_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_btn.setIcon(icon6)

        self.verticalLayout_8.addWidget(self.refresh_btn)

        self.refresh_image_database_log = QLabel(self.frame_20)
        self.refresh_image_database_log.setObjectName(u"refresh_image_database_log")
        self.refresh_image_database_log.setStyleSheet(u"color: rgb(34, 119, 255);")

        self.verticalLayout_8.addWidget(self.refresh_image_database_log, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addLayout(self.verticalLayout_8)

        self.refresh_image_db_message = MessageWidget(self.frame_20)
        self.refresh_image_db_message.setObjectName(u"refresh_image_db_message")
        self.refresh_image_db_message.setMinimumSize(QSize(0, 40))
        self.refresh_image_db_message.setStyleSheet(u"")

        self.verticalLayout_22.addWidget(self.refresh_image_db_message)


        self.verticalLayout_6.addWidget(self.frame_20, 0, Qt.AlignHCenter)

        self.line_6 = QFrame(self.frame_16)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_3 = QLabel(self.frame_17)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(110, 16777215))

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


        self.verticalLayout_6.addWidget(self.frame_17, 0, Qt.AlignHCenter)

        self.line_7 = QFrame(self.frame_16)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_7)

        self.line = QFrame(self.frame_16)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.calender_frame = QFrame(self.frame_16)
        self.calender_frame.setObjectName(u"calender_frame")
        self.calender_frame.setMinimumSize(QSize(317, 349))
        self.calender_frame.setStyleSheet(u"#calender_frame{\n"
"	border: 1px solid rgb(99, 39, 232);\n"
"	border: 1px solid #f0f0f0;\n"
"	border-radius: 20px;\n"
"}")
        self.calender_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_28 = QVBoxLayout(self.calender_frame)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_7 = QLabel(self.calender_frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_28.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.calendar_widget = QWidget(self.calender_frame)
        self.calendar_widget.setObjectName(u"calendar_widget")
        self.calendar_widget.setMinimumSize(QSize(0, 50))
        self.calendar_widget.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_28.addWidget(self.calendar_widget)

        self.frame_57 = QFrame(self.calender_frame)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setStyleSheet(u"")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_date_2 = QLabel(self.frame_57)
        self.label_date_2.setObjectName(u"label_date_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_date_2.sizePolicy().hasHeightForWidth())
        self.label_date_2.setSizePolicy(sizePolicy4)
        self.label_date_2.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_31.addWidget(self.label_date_2)

        self.label_date = QLabel(self.frame_57)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMaximumSize(QSize(16777215, 40))
        self.label_date.setStyleSheet(u"QLabel{\n"
"	color: rgb(135, 88, 255);\n"
"	padding: 5px;\n"
"	font-size:14px;\n"
"	font-weight: normal;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_31.addWidget(self.label_date)


        self.verticalLayout_28.addWidget(self.frame_57, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.calender_frame, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_16, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)


        self.horizontalLayout_12.addWidget(self.playback_filter_frame)

        self.line_5 = QFrame(self.frame_18)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(2, 16777215))
        self.line_5.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_5)

        self.frame_4 = QFrame(self.frame_18)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background: #413B47;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(6)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.video = QWidget(self.frame_4)
        self.video.setObjectName(u"video")
        self.video.setStyleSheet(u"background-color: rgb(102, 102, 102);")

        self.verticalLayout_15.addWidget(self.video)


        self.horizontalLayout_12.addWidget(self.frame_4)

        self.line_14 = QFrame(self.frame_18)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setMaximumSize(QSize(1, 16777215))
        self.line_14.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_14)


        self.horizontalLayout.addWidget(self.frame_18)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.line_8 = QFrame(self.page_playback)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMaximumSize(QSize(16777215, 1))
        self.line_8.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_8)

        self.playback_bottom_frame = QFrame(self.page_playback)
        self.playback_bottom_frame.setObjectName(u"playback_bottom_frame")
        self.playback_bottom_frame.setMinimumSize(QSize(0, 100))
        self.playback_bottom_frame.setMaximumSize(QSize(16777215, 100))
        self.playback_bottom_frame.setStyleSheet(u"#playback_bottom_frame{\n"
"	\n"
"background-color: rgb(30, 27, 33);\n"
"\n"
"}")
        self.playback_bottom_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_16 = QVBoxLayout(self.playback_bottom_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.time_line_frame = QFrame(self.playback_bottom_frame)
        self.time_line_frame.setObjectName(u"time_line_frame")
        self.time_line_frame.setMaximumSize(QSize(16777215, 16777215))
        self.time_line_frame.setStyleSheet(u"QFrame{\n"
"	background-color:transparent;\n"
"}")
        self.time_line_frame.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.time_line_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_16.addWidget(self.time_line_frame)

        self.frame_13 = QFrame(self.playback_bottom_frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(1, 50))
        self.frame_13.setMaximumSize(QSize(16777211, 50))
        self.frame_13.setStyleSheet(u"background-color:transparent;\n"
"")
        self.frame_13.setFrameShape(QFrame.NoFrame)
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
"QPushButton[status=\"play\"]{\n"
"	icon: url(:/icons/icons/play-white.png);\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QPushButton[status=\"play\"]:hover{\n"
"	icon: url(:/icons/icons/play_purple.png);\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"\n"
"QPushButton[status=\"stop\"]{\n"
"	icon: url(:/icons/icons/stop-white.png);\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QPushButton[status=\"stop\"]:hover{\n"
"	icon: url(:/icons/icons/stop-purple.png);\n"
"	background-color:transparent;\n"
"}")
        self.play_btn.setIconSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.play_btn)

        self.line_4 = QFrame(self.frame_13)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.line_2 = QFrame(self.frame_13)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color : rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.frame_58 = QFrame(self.frame_13)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.NoFrame)
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
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label = QLabel(self.frame_21)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label)

        self.playback_time_label = QLabel(self.frame_21)
        self.playback_time_label.setObjectName(u"playback_time_label")
        self.playback_time_label.setMinimumSize(QSize(0, 20))
        self.playback_time_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.playback_time_label)


        self.horizontalLayout_32.addWidget(self.frame_21)


        self.horizontalLayout_4.addWidget(self.frame_58)


        self.verticalLayout_16.addWidget(self.frame_13)


        self.verticalLayout_9.addWidget(self.playback_bottom_frame)

        self.pages_stackwidget.addWidget(self.page_playback)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page_settings)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.setting_tab_widget = QTabWidget(self.page_settings)
        self.setting_tab_widget.setObjectName(u"setting_tab_widget")
        self.setting_tab_widget.setStyleSheet(u"")
        self.system_station_tab = QWidget()
        self.system_station_tab.setObjectName(u"system_station_tab")
        self.verticalLayout_10 = QVBoxLayout(self.system_station_tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.system_station_tabwidget = QTabWidget(self.system_station_tab)
        self.system_station_tabwidget.setObjectName(u"system_station_tabwidget")
        self.system_station_tabwidget.setStyleSheet(u"")
        self.add = QWidget()
        self.add.setObjectName(u"add")
        self.add.setStyleSheet(u"")
        self.verticalLayout_27 = QVBoxLayout(self.add)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.scrollArea_2 = QScrollArea(self.add)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_2.setMaximumSize(QSize(500, 16777215))
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 481, 588))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(-1, 30, -1, -1)
        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 1, 1, 1)

        self.password_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMaximumSize(QSize(140, 16777215))
        self.password_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.password_input, 4, 2, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 4, 1, 1, 1)

        self.username_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMaximumSize(QSize(140, 16777215))
        self.username_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.username_input, 3, 2, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 1, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.city_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.city_input.setObjectName(u"city_input")
        self.city_input.setMaximumSize(QSize(140, 16777215))
        self.city_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.city_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.city_input, 1, 2, 1, 1)

        self.ip_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setMaximumSize(QSize(140, 16777215))
        self.ip_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.ip_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.ip_input, 2, 2, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.name_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setEnabled(True)
        self.name_input.setMaximumSize(QSize(140, 16777215))
        self.name_input.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.name_input.setStyleSheet(u"")

        self.gridLayout.addWidget(self.name_input, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.add_station_message = MessageWidget(self.scrollAreaWidgetContents_2)
        self.add_station_message.setObjectName(u"add_station_message")
        self.add_station_message.setMinimumSize(QSize(0, 60))
        self.add_station_message.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.add_station_message)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.btn_add_check_connection = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_add_check_connection.setObjectName(u"btn_add_check_connection")
        self.btn_add_check_connection.setMinimumSize(QSize(150, 30))
        self.btn_add_check_connection.setMaximumSize(QSize(150, 16777215))
        self.btn_add_check_connection.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.btn_add_check_connection)

        self.btn_save_add = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_save_add.setObjectName(u"btn_save_add")
        self.btn_save_add.setMinimumSize(QSize(150, 30))
        self.btn_save_add.setMaximumSize(QSize(150, 16777215))
        self.btn_save_add.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.btn_save_add)


        self.verticalLayout_7.addLayout(self.verticalLayout_21)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.textEdit_ping_status = QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_ping_status.setObjectName(u"textEdit_ping_status")

        self.verticalLayout_7.addWidget(self.textEdit_ping_status)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_27.addWidget(self.scrollArea_2)

        self.system_station_tabwidget.addTab(self.add, "")
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
        if (self.system_stations_table.rowCount() < 3):
            self.system_stations_table.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.system_stations_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.system_stations_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.system_stations_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.system_stations_table.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.system_stations_table.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.system_stations_table.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.system_stations_table.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.system_stations_table.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.system_stations_table.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.system_stations_table.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.system_stations_table.setItem(2, 2, __qtablewidgetitem13)
        self.system_stations_table.setObjectName(u"system_stations_table")
        self.system_stations_table.setStyleSheet(u"border:none;")
        self.system_stations_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.system_stations_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.system_stations_table.setAlternatingRowColors(True)
        self.system_stations_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.system_stations_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.system_stations_table.horizontalHeader().setStretchLastSection(True)
        self.system_stations_table.verticalHeader().setVisible(False)

        self.horizontalLayout_33.addWidget(self.system_stations_table)

        self.modify_form_frame = QFrame(self.modify)
        self.modify_form_frame.setObjectName(u"modify_form_frame")
        self.modify_form_frame.setMaximumSize(QSize(500, 16777215))
        self.modify_form_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.modify_form_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.modify_form_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 468, 555))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(20)
        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 1)

        self.username_input_modify = QLineEdit(self.scrollAreaWidgetContents)
        self.username_input_modify.setObjectName(u"username_input_modify")
        self.username_input_modify.setMaximumSize(QSize(140, 16777215))
        self.username_input_modify.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.username_input_modify, 3, 1, 1, 1)

        self.city_input_modify = QLineEdit(self.scrollAreaWidgetContents)
        self.city_input_modify.setObjectName(u"city_input_modify")
        self.city_input_modify.setMaximumSize(QSize(140, 16777215))
        self.city_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.city_input_modify.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.city_input_modify, 1, 1, 1, 1)

        self.ip_input_modify = QLineEdit(self.scrollAreaWidgetContents)
        self.ip_input_modify.setObjectName(u"ip_input_modify")
        self.ip_input_modify.setMaximumSize(QSize(140, 16777215))
        self.ip_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.ip_input_modify.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.ip_input_modify, 2, 1, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)

        self.name_input_modify = QLineEdit(self.scrollAreaWidgetContents)
        self.name_input_modify.setObjectName(u"name_input_modify")
        self.name_input_modify.setMaximumSize(QSize(140, 16777215))
        self.name_input_modify.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.name_input_modify.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.name_input_modify, 0, 1, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 4, 0, 1, 1)

        self.password_input_modify = QLineEdit(self.scrollAreaWidgetContents)
        self.password_input_modify.setObjectName(u"password_input_modify")
        self.password_input_modify.setMaximumSize(QSize(140, 16777215))
        self.password_input_modify.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.password_input_modify, 4, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.modify_station_message = MessageWidget(self.scrollAreaWidgetContents)
        self.modify_station_message.setObjectName(u"modify_station_message")
        self.modify_station_message.setMinimumSize(QSize(0, 60))
        self.modify_station_message.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.modify_station_message)

        self.btn_modify_save = QPushButton(self.scrollAreaWidgetContents)
        self.btn_modify_save.setObjectName(u"btn_modify_save")
        self.btn_modify_save.setEnabled(True)
        self.btn_modify_save.setMinimumSize(QSize(200, 32))
        self.btn_modify_save.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_modify_save)

        self.btn_modify_cancel = QPushButton(self.scrollAreaWidgetContents)
        self.btn_modify_cancel.setObjectName(u"btn_modify_cancel")
        self.btn_modify_cancel.setMinimumSize(QSize(200, 32))
        self.btn_modify_cancel.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_modify_cancel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)


        self.horizontalLayout_33.addWidget(self.modify_form_frame)

        self.system_station_tabwidget.addTab(self.modify, "")

        self.verticalLayout_10.addWidget(self.system_station_tabwidget)

        self.setting_tab_widget.addTab(self.system_station_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.setting_tab_widget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.setting_tab_widget)

        self.pages_stackwidget.addWidget(self.page_settings)
        self.page_download = QWidget()
        self.page_download.setObjectName(u"page_download")
        self.page_download.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.page_download)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, -1)
        self.splitter = QSplitter(self.page_download)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"/****************************************************************************/\n"
"/****************************************************************************/\n"
"   QTableWidget, QTableView {\n"
"        background-color: transparent;  /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u06a9\u0644 \u062c\u062f\u0648\u0644 */\n"
"        \n"
"        color: #ffffff;  /* \u0631\u0646\u06af \u0645\u062a\u0646 \u0633\u0644\u0648\u0644\u200c\u0647\u0627 */\n"
"        border: 1px solid #444444;  /* \u062d\u0627\u0634\u06cc\u0647 \u062f\u0648\u0631 \u062c\u062f\u0648\u0644 */\n"
"        gridline-color: #555555;  /* \u0631\u0646\u06af \u062e\u0637\u0648\u0637 \u0634\u0628\u06a9\u0647 \u0628\u06cc\u0646 \u0633\u0644\u0648\u0644\u200c\u0647\u0627 */\n"
"        font-size: 14px;  /* \u0627\u0646\u062f\u0627\u0632\u0647 \u0641\u0648\u0646\u062a */\n"
"    }\n"
"\n"
"    QHeaderView {\n"
"        background-color: qlineargradient(spread:pad, x1:0.454, y1:0, x2:0.514495, y2:1, stop:0 rgba(77, 77, "
                        "104, 255), stop:1 rgba(77, 77, 104, 128));\n"
"        border-top-left-radius: 10px;   /* \u0634\u0639\u0627\u0639 \u06af\u0648\u0634\u0647 \u0628\u0627\u0644\u0627 \u0633\u0645\u062a \u0686\u067e */\n"
"        border-top-right-radius: 10px;  /* \u0634\u0639\u0627\u0639 \u06af\u0648\u0634\u0647 \u0628\u0627\u0644\u0627 \u0633\u0645\u062a \u0631\u0627\u0633\u062a */\n"
"        border: none;  /* \u062d\u0627\u0634\u06cc\u0647 \u0647\u062f\u0631 */\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: transparent;  /* \u0631\u0646\u06af \u067e\u0633\u200c\u0632\u0645\u06cc\u0646\u0647 \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"        color: #ffffff;  /* \u0631\u0646\u06af \u0645\u062a\u0646 \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"        padding: 5px;  /* \u0641\u0636\u0627\u06cc \u062f\u0627\u062e\u0644\u06cc \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"        border: none;  /* \u062d\u0630\u0641 \u062d\u0627\u0634\u06cc\u0647 \u0633"
                        "\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"        font-weight: bold;  /* \u0628\u0648\u0644\u062f \u06a9\u0631\u062f\u0646 \u0641\u0648\u0646\u062a \u0633\u0631\u0633\u062a\u0648\u0646\u200c\u0647\u0627 */\n"
"    }")
        self.download_filter_frame = QFrame(self.splitter)
        self.download_filter_frame.setObjectName(u"download_filter_frame")
        self.download_filter_frame.setMinimumSize(QSize(316, 0))
        self.download_filter_frame.setMaximumSize(QSize(500, 16777215))
        self.download_filter_frame.setStyleSheet(u"#download_filter_frame{\n"
"background-color:rgb(49, 44, 53);\n"
"}\n"
"\n"
"")
        self.download_filter_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.download_filter_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.download_filter_stackWidget = QStackedWidget(self.download_filter_frame)
        self.download_filter_stackWidget.setObjectName(u"download_filter_stackWidget")
        self.download_filter_stackWidget.setStyleSheet(u"")
        self.step1 = QWidget()
        self.step1.setObjectName(u"step1")
        self.verticalLayout_14 = QVBoxLayout(self.step1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_8 = QLabel(self.step1)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_18.addWidget(self.label_8)

        self.download_filters_train_combobox = QComboBox(self.step1)
        self.download_filters_train_combobox.setObjectName(u"download_filters_train_combobox")

        self.horizontalLayout_18.addWidget(self.download_filters_train_combobox)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.download_filter_station_log = QTableWidget(self.step1)
        if (self.download_filter_station_log.columnCount() < 2):
            self.download_filter_station_log.setColumnCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.download_filter_station_log.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.download_filter_station_log.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        if (self.download_filter_station_log.rowCount() < 1):
            self.download_filter_station_log.setRowCount(1)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.download_filter_station_log.setVerticalHeaderItem(0, __qtablewidgetitem16)
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
        self.download_all_stations_checkbox.setStyleSheet(u"")
        self.download_all_stations_checkbox.setChecked(False)

        self.horizontalLayout_34.addWidget(self.download_all_stations_checkbox)

        self.horizontalSpacer = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer)

        self.download_search_station = QLineEdit(self.step0)
        self.download_search_station.setObjectName(u"download_search_station")

        self.horizontalLayout_34.addWidget(self.download_search_station)


        self.verticalLayout_12.addLayout(self.horizontalLayout_34)

        self.verticalSpacer_2 = QSpacerItem(11, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.download_stations_table = QTableWidget(self.step0)
        if (self.download_stations_table.columnCount() < 2):
            self.download_stations_table.setColumnCount(2)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.download_stations_table.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.download_stations_table.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        if (self.download_stations_table.rowCount() < 3):
            self.download_stations_table.setRowCount(3)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.download_stations_table.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.download_stations_table.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.download_stations_table.setVerticalHeaderItem(2, __qtablewidgetitem21)
        self.download_stations_table.setObjectName(u"download_stations_table")
        self.download_stations_table.setMinimumSize(QSize(100, 100))
        self.download_stations_table.setStyleSheet(u"border:none;")
        self.download_stations_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
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
        self.download_filter_prev_btn.setMinimumSize(QSize(0, 30))
        self.download_filter_prev_btn.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.download_filter_prev_btn)

        self.download_filter_next_btn = QPushButton(self.download_filter_frame)
        self.download_filter_next_btn.setObjectName(u"download_filter_next_btn")
        self.download_filter_next_btn.setMinimumSize(QSize(0, 30))
        self.download_filter_next_btn.setStyleSheet(u"")

        self.horizontalLayout_41.addWidget(self.download_filter_next_btn)


        self.verticalLayout_13.addLayout(self.horizontalLayout_41)

        self.splitter.addWidget(self.download_filter_frame)
        self.download_results_frame = QFrame(self.splitter)
        self.download_results_frame.setObjectName(u"download_results_frame")
        self.download_results_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_26 = QVBoxLayout(self.download_results_frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.splitter.addWidget(self.download_results_frame)

        self.horizontalLayout_6.addWidget(self.splitter)

        self.pages_stackwidget.addWidget(self.page_download)

        self.verticalLayout_3.addWidget(self.pages_stackwidget)


        self.horizontalLayout_27.addWidget(self.main_frame)


        self.verticalLayout.addWidget(self.middle)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.name_input, self.city_input)
        QWidget.setTabOrder(self.city_input, self.ip_input)
        QWidget.setTabOrder(self.ip_input, self.username_input)
        QWidget.setTabOrder(self.username_input, self.password_input)
        QWidget.setTabOrder(self.password_input, self.download_all_stations_checkbox)
        QWidget.setTabOrder(self.download_all_stations_checkbox, self.download_search_station)
        QWidget.setTabOrder(self.download_search_station, self.download_stations_table)
        QWidget.setTabOrder(self.download_stations_table, self.download_filter_prev_btn)
        QWidget.setTabOrder(self.download_filter_prev_btn, self.download_filter_next_btn)
        QWidget.setTabOrder(self.download_filter_next_btn, self.playback_combo_train_id)
        QWidget.setTabOrder(self.playback_combo_train_id, self.playback_camera_combo)
        QWidget.setTabOrder(self.playback_camera_combo, self.play_btn)
        QWidget.setTabOrder(self.play_btn, self.speed_btn)
        QWidget.setTabOrder(self.speed_btn, self.setting_tab_widget)
        QWidget.setTabOrder(self.setting_tab_widget, self.system_station_tabwidget)
        QWidget.setTabOrder(self.system_station_tabwidget, self.system_stations_table)
        QWidget.setTabOrder(self.system_stations_table, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.name_input_modify)
        QWidget.setTabOrder(self.name_input_modify, self.city_input_modify)
        QWidget.setTabOrder(self.city_input_modify, self.ip_input_modify)
        QWidget.setTabOrder(self.ip_input_modify, self.username_input_modify)
        QWidget.setTabOrder(self.username_input_modify, self.password_input_modify)
        QWidget.setTabOrder(self.password_input_modify, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.btn_add_check_connection)
        QWidget.setTabOrder(self.btn_add_check_connection, self.btn_save_add)
        QWidget.setTabOrder(self.btn_save_add, self.textEdit_ping_status)
        QWidget.setTabOrder(self.textEdit_ping_status, self.btn_side_playback)
        QWidget.setTabOrder(self.btn_side_playback, self.btn_side_download)
        QWidget.setTabOrder(self.btn_side_download, self.btn_side_settings)
        QWidget.setTabOrder(self.btn_side_settings, self.download_filters_train_combobox)
        QWidget.setTabOrder(self.download_filters_train_combobox, self.download_filter_station_log)

        self.retranslateUi(MainWindow)

        self.pages_stackwidget.setCurrentIndex(0)
        self.setting_tab_widget.setCurrentIndex(0)
        self.system_station_tabwidget.setCurrentIndex(1)
        self.download_filter_stackWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"IRAN RailWay Monitor Software - Arian Shabake", None))
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
#if QT_CONFIG(tooltip)
        self.btn_side_playback.setToolTip(QCoreApplication.translate("MainWindow", u"Live View", None))
#endif // QT_CONFIG(tooltip)
        self.btn_side_playback.setText(QCoreApplication.translate("MainWindow", u"   PlayBack", None))
#if QT_CONFIG(tooltip)
        self.btn_side_download.setToolTip(QCoreApplication.translate("MainWindow", u"Report", None))
#endif // QT_CONFIG(tooltip)
        self.btn_side_download.setText(QCoreApplication.translate("MainWindow", u"   Download", None))
#if QT_CONFIG(tooltip)
        self.btn_side_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Defect Parameters", None))
#endif // QT_CONFIG(tooltip)
        self.btn_side_settings.setText(QCoreApplication.translate("MainWindow", u"   Settings", None))
#if QT_CONFIG(tooltip)
        self.pages_stackwidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.refresh_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"Rshresh Dtabase", None))
        self.refresh_btn.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"fill_gradient_purple_btn", None))
        self.refresh_image_database_log.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Train ID :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.label_date_2.setText(QCoreApplication.translate("MainWindow", u"Selected Date :", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"14/04/02", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.playback_camera_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"test1", None))
        self.playback_camera_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"test2", None))

#if QT_CONFIG(tooltip)
        self.play_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Live", None))
#endif // QT_CONFIG(tooltip)
        self.play_btn.setText("")
        self.play_btn.setProperty(u"status", QCoreApplication.translate("MainWindow", u"stop", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Speed : ", None))
#if QT_CONFIG(tooltip)
        self.speed_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Stop Live", None))
#endif // QT_CONFIG(tooltip)
        self.speed_btn.setText(QCoreApplication.translate("MainWindow", u"1x", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Time : ", None))
        self.playback_time_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.page_settings.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"page", None))
        self.system_station_tab.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"page", None))
        self.add.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"page-light", None))
        self.scrollArea_2.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"hide", None))
        self.scrollAreaWidgetContents_2.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"hide", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"IP Address * :", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Password : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"City * : ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Username :", None))
        self.ip_input.setText("")
        self.ip_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: 192.168.1.50", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Name * : ", None))
        self.name_input.setText("")
        self.btn_add_check_connection.setText(QCoreApplication.translate("MainWindow", u"Check Connection", None))
        self.btn_add_check_connection.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"fill_gradient_purple_btn", None))
        self.btn_save_add.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_save_add.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"fill_gradient_purple_btn", None))
        self.system_station_tabwidget.setTabText(self.system_station_tabwidget.indexOf(self.add), QCoreApplication.translate("MainWindow", u"Add", None))
        self.modify.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"page-light", None))
        ___qtablewidgetitem = self.system_stations_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem1 = self.system_stations_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"city", None));
        ___qtablewidgetitem2 = self.system_stations_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ip", None));
        ___qtablewidgetitem3 = self.system_stations_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"fdsf", None));
        ___qtablewidgetitem4 = self.system_stations_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"sdfsf", None));
        ___qtablewidgetitem5 = self.system_stations_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.system_stations_table.isSortingEnabled()
        self.system_stations_table.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.system_stations_table.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"dsfs", None));
        ___qtablewidgetitem7 = self.system_stations_table.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"dfsfsdf", None));
        ___qtablewidgetitem8 = self.system_stations_table.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"sdfsf", None));
        ___qtablewidgetitem9 = self.system_stations_table.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"dfsf", None));
        ___qtablewidgetitem10 = self.system_stations_table.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"sfs", None));
        ___qtablewidgetitem11 = self.system_stations_table.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"sfsf", None));
        ___qtablewidgetitem12 = self.system_stations_table.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"sf", None));
        ___qtablewidgetitem13 = self.system_stations_table.item(2, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"sdfs", None));
        self.system_stations_table.setSortingEnabled(__sortingEnabled)

        self.modify_form_frame.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"hide", None))
        self.scrollArea.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"hide", None))
        self.scrollAreaWidgetContents.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"hide", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"IP Address *: ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Name * : ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"City * : ", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"User Name :", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Password : ", None))
        self.btn_modify_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_modify_save.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"fill_gradient_purple_btn", None))
        self.btn_modify_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_modify_cancel.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"border_gradient_purple_btn", None))
        self.system_station_tabwidget.setTabText(self.system_station_tabwidget.indexOf(self.modify), QCoreApplication.translate("MainWindow", u"Modify", None))
        self.setting_tab_widget.setTabText(self.setting_tab_widget.indexOf(self.system_station_tab), QCoreApplication.translate("MainWindow", u"system Stations", None))
        self.setting_tab_widget.setTabText(self.setting_tab_widget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"General", None))
        self.page_download.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"page", None))
        self.download_filter_frame.setProperty(u"styleClass", "")
        self.step1.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"hide", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Trains:", None))
        self.label_8.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"h3", None))
        ___qtablewidgetitem14 = self.download_filter_station_log.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem15 = self.download_filter_station_log.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem16 = self.download_filter_station_log.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.step0.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"hide", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Select Stations:", None))
        self.label_4.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"h3", None))
        self.download_all_stations_checkbox.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.download_search_station.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search name", None))
        ___qtablewidgetitem17 = self.download_stations_table.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem18 = self.download_stations_table.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem19 = self.download_stations_table.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.download_stations_table.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.download_stations_table.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.download_filter_prev_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.download_filter_prev_btn.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"fill_gradient_purple_btn", None))
        self.download_filter_next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.download_filter_next_btn.setProperty(u"styleClass", QCoreApplication.translate("MainWindow", u"fill_gradient_purple_btn", None))
    # retranslateUi


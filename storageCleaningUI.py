from persiantools.jdatetime import JalaliDateTime

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QIcon, QColor
from PySide6.QtCore import Qt

from UIFiles.stationDownload_UI import Ui_stationdownloadMainUI
from uiUtils.guiBackend import GUIBackend
from uiUtils.Clock import ClockWidget

class storageCleaningDialog(QWidget):

    def __init__(self,) -> None:
        super().__init__()
        self.ui = Ui_stationdownloadMainUI()
        self.ui.setupUi(self)

        GUIBackend.set_win_frameless(self)
        
    
    def set_progess_value(self, value):
        GUIBackend.set_progressbar_value(self.ui.prograssbar, value)


    def show_win(self,):
        self.set_progess_value(0)
        self.setWindowModality(Qt.ApplicationModal)
        super().show()
from persiantools.jdatetime import JalaliDateTime

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QIcon, QColor
from PySide6.QtCore import Qt

from UIFiles.stationDownload_UI import Ui_stationdownloadMainUI
from uiUtils.guiBackend import GUIBackend
from uiUtils.Clock import ClockWidget

class downloadSection(QWidget):

    def __init__(self, _id, name:str, dt:JalaliDateTime) -> None:
        super().__init__()
        self.ui = Ui_stationdownloadMainUI()
        self.ui.setupUi(self)

        self.Clocks:dict[str, ClockWidget] = {'pm':None, 'am':None}
        for key in self.Clocks.keys():
            self.Clocks[key] = ClockWidget(is_am=(key=='am'), 
                                           show_all_hours=False,
                                           show_main_hours=True,
                                           outline_color=QColor('#fff'),
                                           guide_line_color=QColor('#fff'),
                                           avaiable_color=QColor(99, 39, 232),
                                           w=150,
                                           h=150,
                                           )

        
        self.ui.download_filter_am_lock_wgt.layout().addWidget(self.Clocks['am'],  alignment=Qt.AlignCenter)
        self.ui.download_filter_pm_lock_wgt.layout().addWidget(self.Clocks['pm'],  alignment=Qt.AlignCenter)

        self.id = _id

        if name:
            self.set_station_name(name)
        if dt:
            self.set_date(dt)

        self.set_progess_value(0)

    def set_station_name(self, name:str):
        GUIBackend.set_label_text(self.ui.station_lbl, name)

    def set_date(self, dt:JalaliDateTime):
        txt = dt.strftime('%Y/%d/%m')
        GUIBackend.set_label_text(self.ui.date_lbl, txt)
    
    def set_progess_value(self, value):
        GUIBackend.set_progressbar_value(self.ui.prograssbar, value)

    def download_btn_connector(self, func):
        GUIBackend.button_connector_argument_pass(self.ui.download_btn, 
                                                  func,
                                                  args=(self.id) )
from persiantools.jdatetime import JalaliDateTime

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QIcon, QColor
from PySide6.QtCore import Qt

from UIFiles.stationDownload_UI import Ui_stationdownloadMainUI
from uiUtils.guiBackend import GUIBackend
from uiUtils.Clock import ClockWidget
from Tranform.transformModule import transformModule
class downloadSection(QWidget):

    def __init__(self, station_info:str, train:str, camera:str, dt:JalaliDateTime) -> None:
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

        self.date_time = dt

        self.id = id(self)
        self.station_info = station_info
        self.transformer:transformModule = None
        self.files_paths:list[str] = []
        self.files_sizes:list[int] = []

        self.is_during_download = False

        self.set_station_name(station_info['name'])
        if train:
            self.set_train(train)
        if camera:
            self.set_camera_name(camera)
        if dt:
            self.set_date(dt)

        self.set_progess_value(0)

    def set_station_name(self, name:str):
        GUIBackend.set_label_text(self.ui.station_lbl, name)

    def set_date(self, dt:JalaliDateTime):
        txt = dt.strftime('%Y/%d/%m')
        GUIBackend.set_label_text(self.ui.date_lbl, txt)
    
    def set_train(self, train:str):
        GUIBackend.set_label_text(self.ui.train_lbl, train)

    def set_camera_name(self, camera:str):
        GUIBackend.set_label_text(self.ui.camera_lbl, camera)
    
    def set_progess_value(self, value):
        GUIBackend.set_progressbar_value(self.ui.prograssbar, value)

    def download_btn_connector(self, func,):
        
        GUIBackend.button_connector_argument_pass(self.ui.download_btn,  
                                                  func,
                                                  args=(self.id,) )
        
    def close_btn_connector(self, func, args):
        GUIBackend.button_connector_argument_pass(self.ui.close_btn, 
                                                  func,
                                                  args=args )
        
    def set_during_download(self, flag):
        self.is_during_download = flag
        GUIBackend.set_disable_enable(self.ui.download_btn, not(self.is_during_download))
        GUIBackend.set_disable_enable(self.ui.close_btn, not(self.is_during_download) )
        
    def set_time_ranges(self, time_rangs:list[tuple[JalaliDateTime, JalaliDateTime]]):
        for clock in self.Clocks.values():
            clock.set_time_ranges(time_rangs, self.date_time)

    def set_transformer(self, transformer:transformModule):
        self.transformer = transformer

    def set_download_files(self, files:list[str], sizes:list[int]):
        self.files_paths = files
        self.files_sizes = sizes


    def write_msg(self, txt):
        GUIBackend.set_label_text(self.ui.msg_lbl, txt)


    def reset(self,):
        self.set_during_download(False)
        self.set_progess_value(0)
        GUIBackend.set_disable_enable(self.ui.download_btn, True)
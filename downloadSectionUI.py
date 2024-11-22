from persiantools.jdatetime import JalaliDateTime

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QIcon, QColor
from PySide6.QtCore import Qt

from UIFiles.stationDownload_UI import Ui_stationdownloadMainUI
from uiUtils.guiBackend import GUIBackend
from uiUtils.Clock import ClockWidget

class downloadSection(QWidget):

    def __init__(self, _id, name:str, train:str, camera:str, dt:JalaliDateTime) -> None:
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

        if _id is None:
            self.id = name
        else:
            self.id = _id

        if name:
            self.set_station_name(name)
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

    def download_btn_connector(self, func, args):
        GUIBackend.button_connector_argument_pass(self.ui.download_btn, 
                                                  func,
                                                  args=args )
        
    def set_time_ranges(self, time_rangs:list[tuple[JalaliDateTime, JalaliDateTime]]):
        for clock in self.Clocks.values():
            clock.set_time_ranges(time_rangs)

    # def show_msg(self,txt, msg_type, display_time=3000):
    #     self.ui.download_message.show_message(txt, msg_type, display_time )

    def write_msg(self, txt):
        GUIBackend.set_label_text(self.ui.msg_lbl, txt)

    def disable_download_btn(self,):
        GUIBackend.set_disable_enable(self.ui.download_btn, False)

    def reset(self,):
        self.set_progess_value(0)
        GUIBackend.set_disable_enable(self.ui.download_btn, True)
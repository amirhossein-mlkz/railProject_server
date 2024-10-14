from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QIcon
from persiantools.jdatetime import JalaliDateTime, timedelta

from uiUtils.Calendar import  JalaliCalendarDialog
from UIFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents


class playbackPageUI:

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui

        self.calendar_dialog = JalaliCalendarDialog(self.ui.label_date)
        self.calendar_dialog.setParent(self.ui.calendar_widget)
        self.ui.load_videos_progess_bar.setMaximum(1000)
        self.timeLineSlider = GUIComponents.timeLineSlider(JalaliDateTime.now(), JalaliDateTime.now() - timedelta(1))
        GUIBackend.add_widget(self.ui.time_line_frame, self.timeLineSlider)
        self.trainLoading = GUIComponents.trainLoading(0,1000)


    def set_timelines(self, time_ranges:list, start:JalaliDateTime, end:JalaliDateTime):
        self.timeLineSlider.set_min_max(start, end)
        self.timeLineSlider.set_avaiable_segments(time_ranges)
            
    

    def set_avaiable_trains(self, trains:list[str]):
        GUIBackend.set_combobox_items(self.ui.playback_combo_train_id, trains)

    def get_selected_train(self,):
        return GUIBackend.get_combobox_selected(self.ui.playback_combo_train_id)
    


    def set_cameras(self, items:list):
        GUIBackend.set_combobox_items(self.ui.playback_camera_combo, items)
    
    def get_current_camera(self,)->str:
        return GUIBackend.get_combobox_selected(self.ui.playback_camera_combo)
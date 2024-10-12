from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QIcon

from Calendar import  JalaliCalendarDialog
from UIFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents


class playbackPageUI:

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui

        self.calendar_dialog = JalaliCalendarDialog(self.ui.label_date)
        self.calendar_dialog.setParent(self.ui.calendar_widget)


    def set_avaiable_trains(self, trains:list[str]):
        GUIBackend.set_combobox_items(self.ui.playback_combo_train_id, trains)

    def get_selected_train(self,):
        return GUIBackend.get_combobox_selected(self.ui.playback_combo_train_id)
    

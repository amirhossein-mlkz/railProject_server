from datetime import time

from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QIcon, QColor
from PySide6.QtCore import Qt

from UIFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from uiUtils.Calendar import  JalaliCalendarDialog
from uiUtils.Clock import ClockWidget
from uiUtils import GUIComponents

class downloadPageUI:

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui
        self.calendar_dialog = JalaliCalendarDialog(self.ui.download_filter_label_date)
        self.calendar_dialog.setParent(self.ui.download_filter_calendar_widget)

        self.Clocks:dict[str, ClockWidget] = {'pm':None, 'am':None}
        for key in self.Clocks.keys():
            self.Clocks[key] = ClockWidget(is_am=(key=='am'), 
                                           show_all_hours=False,
                                           outline_color=QColor('#fff'),
                                           guide_line_color=QColor('#fff'),
                                           avaiable_color=QColor(99, 39, 232),
                                           )
            
        

        
        self.ui.download_filter_am_lock_wgt.layout().addWidget(self.Clocks['am'],  alignment=Qt.AlignCenter)
        self.ui.download_filter_pm_lock_wgt.layout().addWidget(self.Clocks['pm'],  alignment=Qt.AlignCenter)

        time_ranges = [
        (time(3, 0), time(5, 30)),
        (time(9, 15), time(10, 45)),
    ]
        self.Clocks['am'].set_time_ranges(time_ranges)


    def set_download_stations_list(self, datas:list[dict], event_func, selected_ids:list):
        headers = ['-', 'name', 'city']
        GUIBackend.set_table_dim(self.ui.download_stations_table, len(datas), len(headers))
        GUIBackend.set_table_cheaders(self.ui.download_stations_table, headers)
        GUIBackend.set_cell_width_content_adjust(self.ui.download_stations_table)
        
        for row_idx, row_info in enumerate(datas):
            for cell_name, cell_value in row_info.items():
                if cell_name in headers:
                    col_idx = headers.index(cell_name)
                    GUIBackend.set_table_cell_value(table=self.ui.download_stations_table,
                                                    index=(row_idx, col_idx),
                                                    value=cell_value
                                                    )
            
            checkbox = GUIComponents.tabelCheckbox()
            GUIBackend.checkbox_connector_argument_pass(checkbox, event_func, args=(row_info['id'],))

            GUIBackend.set_table_cell_widget(table=self.ui.download_stations_table,
                                             index=(row_idx, headers.index('-')),
                                             widget=checkbox
                                            )
            
            if row_info['id'] in selected_ids:
                GUIBackend.set_checkbox_value(checkbox, True, block_signal=True)
            else:
                GUIBackend.set_checkbox_value(checkbox, False, block_signal=False)
    
    
    def handle_filter_navigation_btns(self, curent_step, final_step):
        if curent_step == 0:
            GUIBackend.set_disable_enable(self.ui.download_filter_prev_btn, False)
        else:
            GUIBackend.set_disable_enable(self.ui.download_filter_prev_btn, True)
        
        if curent_step == final_step:
            GUIBackend.set_button_text(self.ui.download_filter_next_btn, "Finish")
        else:
            GUIBackend.set_button_text(self.ui.download_filter_next_btn, "Next")

    def set_filter_form_step(self, step, final_step):
        steps_page= {
            0:self.ui.step0,
            1:self.ui.step1,
            2:self.ui.step2,
            3:self.ui.step3,

        }

        GUIBackend.set_stack_widget_page(self.ui.download_filter_stackWidget, steps_page[step])
        self.handle_filter_navigation_btns(step, final_step)
    
    def set_filter_trains(self, trains:list[str]):
        GUIBackend.set_combobox_items(self.ui.download_filters_train_combobox, trains, block_signal=True)

    def get_selected_train(self,):
        return GUIBackend.get_combobox_selected(self.ui.download_filters_train_combobox)

    def train_filter_change_connector(self, func):
        GUIBackend.combobox_changeg_connector(self.ui.download_filters_train_combobox, func)

    def set_filter_cameras(self, cameras:list[str]):
        GUIBackend.set_combobox_items(self.ui.download_filters_cameras_combobox, cameras, block_signal=True)

    def get_selected_camera(self,):
        return GUIBackend.get_combobox_selected(self.ui.download_filters_cameras_combobox)


    def set_filter_stations_logs(self, logs:list[dict]):
        headers = ['status', 'name', 'message']
        GUIBackend.set_table_dim(self.ui.download_filter_station_log, len(logs), len(headers))
        GUIBackend.set_table_cheaders(self.ui.download_filter_station_log, headers)
        GUIBackend.set_table_cwidth(self.ui.download_filter_station_log, headers.index('status'), 30)
        GUIBackend.set_table_cwidth(self.ui.download_filter_station_log, headers.index('name'), 60)

        for row_idx, log in enumerate(logs):
            icon_label = QLabel()
            icon_label.setFixedSize(24,24)
            icon_label.setScaledContents(True)

            if log['status']:
                icon_label.setPixmap(QPixmap(":/icons/icons/success.png"))  # Use success icon from resources
            else:
                icon_label.setPixmap(QPixmap(":/icons/icons/error.png"))  # Use success icon from resources

            GUIBackend.set_table_cell_widget(self.ui.download_filter_station_log,
                                             index=(row_idx, headers.index('status')),
                                             widget=icon_label,
                                             layout=True)
            
            GUIBackend.set_table_cell_value(self.ui.download_filter_station_log,
                                             index=(row_idx, headers.index('message')),
                                             value=log['message'])
            
            GUIBackend.set_table_cell_value(self.ui.download_filter_station_log,
                                             index=(row_idx, headers.index('name')),
                                             value=log['info']['name'])
            
        
      
    def show_confirmbox(self, title:str, text:str, buttons:list[str]):
        confirmbox = GUIComponents.confirmMessageBox(title, text, buttons)
        return confirmbox.render()
    
    

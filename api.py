import os
from threading import Thread, Event
import threading
import platform,subprocess

from PySide6.QtWidgets import QMessageBox

from backend.database.databaseManager import DataBaseManager
from backend.database.mainDatabase import mainDatabase
from main_ui import UI_main_window_org
from constanst import MAX_SPEED,COLUMN_DESTINATION,TABLE_PATHES
from backend.utils.threadWorker import threadWorkers
from Tranform.Network import pingWorker
from Tranform.sharingConstans import StatusCodes
from uiUtils.GUIComponents import MessageWidget
from PagesAPI.settingPageAPI import settingPageAPI
from PagesAPI.downloadPageAPI import downloadPageAPI
from PagesAPI.playbackPageAPI import playbackPageAPI
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames

class API:
    def __init__(self, ui_obj:UI_main_window_org):

        self.ui_obj = ui_obj
        self.create_db_obj()
        # self.load_base_parms()
        self.button_connector()
        self.speed_rate = 1
        self.check_available_trains()
        self.train_id_selected = False

        self.stop_event = Event()

        self.Mediator = Mediator()
        self.Mediator.register_events(eventNames.MODIFY_SYSTEM_STATIONS)

        self.settingPageAPI = settingPageAPI(self.ui_obj.settingPageUI, self.db)
        self.downloadPageAPI = downloadPageAPI(self.ui_obj.downloadPageUI, self.db)
        self.playbackPageAPI = playbackPageAPI(self.ui_obj.playbackPageUI, self.db)

        self.settingPageAPI.refresh_system_stations()


        
        
        



    def button_connector(self):
        self.ui_obj.ui.btn_side_download.clicked.connect(self.load_download_base_params)

        self.ui_obj.ui.btn_add.clicked.connect(self.add_name)
        self.ui_obj.ui.btn_remove.clicked.connect(self.remove_name)
        self.ui_obj.ui.btn_select_train.clicked.connect(self.set_train_id)
       
        #--------------------------------------------------------------------
        

    def create_db_obj(self):
        self.db_manager = DataBaseManager('data.db')
        self.db = mainDatabase(self.db_manager)



    

    
        

    
    
    
    def load_system_spec_column(self,column_name):
        configs = self.db_manager.fetch_table_as_dict(table_name='system_config')
        self.system_datas = configs
        names = []
        if len(configs)>=1:
            for config in configs:
                names.append(config[column_name])
        else:
            names=None
        return names
    

    
    









    def load_download_base_params(self):

        self.condidate_names = []

        self.download_systems_names = self.load_system_spec_column(column_name='name')
        self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.ui.combo_download_all, items=self.download_systems_names)


    def add_name(self):

        text = self.ui_obj.ret_current_value_combo_box(self.ui_obj.ui.combo_download_all)
        if text !='':
            self.download_systems_names.remove(text)

            self.condidate_names.append(text)

            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.ui.combo_download_selected,items=self.condidate_names)
            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.ui.combo_download_all,items=self.download_systems_names)


    def remove_name(self):
        text = self.ui_obj.ret_current_value_combo_box(self.ui_obj.ui.combo_download_selected)
        if text!='':
            self.condidate_names.remove(text)

            self.download_systems_names.append(text)

            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.ui.combo_download_all,items=self.download_systems_names)
            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.ui.combo_download_selected,items=self.condidate_names)







    def get_main_path(self):


        des_path = self.db_manager.fetch_table_as_dict(table_name=TABLE_PATHES)
        if des_path !=[]:
            self.des_path = des_path[0][COLUMN_DESTINATION]
            return self.des_path





    def check_available_trains(self):

        des_path =  self.get_main_path()
        self.des_path = des_path
        if des_path and os.path.exists(des_path):
            trains = os.listdir(des_path)
            self.ui_obj.set_item_combo_box(self.ui_obj.combo_train_id,trains)


    def set_train_id(self):
        self.train_id = self.ui_obj.get_combo_values(self.ui_obj.combo_train_id)
        if self.train_id =='':
            print('Train id is none')
            return
        try:
            self.path_train_id = os.path.join(self.des_path,self.train_id)
        except:
            print('Error in get path train id not exist')
            return 


        days = self.get_days(train_path=self.path_train_id)
        print(days)

        self.ui_obj.calendar_dialog.set_spec_days(days)

        self.ui_obj.calendar_dialog.updateCalendar()

        self.train_id_selected = True
    




    def get_days(self,train_path):

        days = []
        if os.path.exists(train_path) and os.path.isdir(train_path):
            for year in os.listdir(train_path):
                year_path = os.path.join(train_path,year)
                if os.path.exists(year_path) and os.path.isdir(year_path):
                    for month in os.listdir(year_path):
                        month_path = os.path.join(year_path,month)
                        if os.path.exists(month_path) and os.path.isdir(month_path):
                            for day in os.listdir(month_path):
                                days.append(f'{year}_{month}_{day}')


                        else:
                            print(f"{month_path} is not a directory or does not exist.")
                else:
                    print(f"{year_path} is not a directory or does not exist.")
        else:
            print(f"{train_path} is not a directory or does not exist.")




        return days


  




    def get_path_selected_date(self):

        if not self.train_id_selected:
            print('First Set/Select train')
            return
        
        selected_date = self.ui_obj.calendar_dialog.path_selected_date
        self.path_selected_day = os.path.join(self.des_path,self.train_id,selected_date)
        return self.path_selected_day





    def calendar_day_click(self,date):
        print('clcik',date)
        str_date = date.strftime("%Y/%m/%d")
        
        path_day = self.generate_path(date)

        available_times = self.get_available_times(path_day=path_day)

        self.set_timeline_exist(available_times)


    def generate_path(self,date):

        path = os.path.join( self.path_train_id,
                                    str(date.year),
                                    str(date.month),
                                    str(date.day),
                                    )
        return path   

    def get_available_times(self,path_day):
        available_times = []
        for h in os.listdir(path_day):
            hour_path = os.path.join(path_day,h)
            for m in os.listdir(hour_path):
                minute_path = os.path.join(hour_path,m)
                if len(os.listdir(minute_path))>1:

                    available_times.append((int(h)*60)+int(m))
        

        return available_times



    def set_timeline_exist(self,available_times):

        self.ui_obj.timeline.set_minutes_segments(available_times)





if __name__ == '__main__':

    obj = API('test')

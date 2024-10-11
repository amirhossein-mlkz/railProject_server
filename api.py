import os
from threading import Thread, Event
import threading
import platform,subprocess

from PySide6.QtWidgets import QMessageBox

from backend.database.databaseManager import DataBaseManager
from backend.database.mainDatabase import mainDatabase
from main_ui import UI_main_window_org
from constanst import MAX_SPEED,COLUMN_DESTINATION,TABLE_PATHES
from loading_train import LoadingWindow
from ImageLoader import ImageLoader
from backend.utils.threadWorker import threadWorkers
from Tranform.Network import pingWorker
from Tranform.sharingConstans import StatusCodes
from uiUtils.GUIComponents import MessageWidget

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
        self.image_loader = ImageLoader(self.stop_event,'', self.speed_rate)

        self.ui_obj.calendar_dialog.set_parent_function(self.calendar_day_click)


        self.systems_stations = []
        self.current_system_staion_modify_id = None
        
        self.pingThreadWorker = threadWorkers(None, None)
        self.ui_obj.show_modify_system_station_form(False)
        self.refresh_system_stations()



    def button_connector(self):
        self.ui_obj.btn_modify_cancel.clicked.connect(self.cancel_editing_systems_station)
        self.ui_obj.btn_modify_save.clicked.connect(self.save_systems_station_change)

        self.ui_obj.btn_save_add.clicked.connect(self.add_system_station)
        self.ui_obj.btn_add_check_connection.clicked.connect(self.check_system_connection)

        self.ui_obj.speed_btn.clicked.connect(self.set_speed)
        self.ui_obj.btn_side_download.clicked.connect(self.load_download_base_params)

        self.ui_obj.btn_add.clicked.connect(self.add_name)
        self.ui_obj.btn_remove.clicked.connect(self.remove_name)
        self.ui_obj.refresh_btn.clicked.connect(self.check_available_trains)
        self.ui_obj.btn_select_train.clicked.connect(self.set_train_id)
        self.ui_obj.play_btn.clicked.connect(self.play_images)
        self.ui_obj.stop_btn.clicked.connect(self.stop_show_image)



    



        


    def create_db_obj(self):
        self.db_manager = DataBaseManager('data.db')
        self.db = mainDatabase(self.db_manager)

    def refresh_system_stations(self,):
        self.systems_stations = self.db.load_all_system_stations()
        self.ui_obj.set_system_stations_table(self.systems_stations, event_func=self.ststem_station_table_event)

    def ststem_station_table_event(self, name:str, id:str):
        if name == 'delete':
            self.remove_system_station(id)
        
        elif name == 'edit':
            self.edit_system_station(id)
        
        else:
            print("BUG:ststem_station_table_event", name, id)



    def remove_system_station(self, id:int):
        res = self.ui_obj.show_confirmbox('remove', 'Are You Sure to remove?', buttons=['yes', 'no'])
        if res =='no':
            return
        ret = self.db.remove_system_station_by_id(id)
        self.refresh_system_stations()

    def edit_system_station(self, id):
        system_info = self.db.load_system_station_by_id(id)
        if len(system_info) == 0:
            return
        
        self.current_system_staion_modify_id = id
        
        system_info = system_info[0]
        self.ui_obj.set_modify_system_station_fields(system_info)
        self.ui_obj.show_modify_system_station_form(True)

    def cancel_editing_systems_station(self,):
        self.ui_obj.clear_modify_system_station_fields()
        self.ui_obj.show_modify_system_station_form(False)

    def save_systems_station_change(self,):
        input_fields = self.ui_obj.get_modify_system_station_fields()
        verfiy = self.verify_system_station(input_fields, 
                                         self.ui_obj.modify_station_message , 
                                         id=self.current_system_staion_modify_id)
        
        if verfiy:

            ret = self.db.update_system_station_by_id(input_fields, id=self.current_system_staion_modify_id)
            if ret:
                self.ui_obj.modify_station_message.show_message('Changes Saved Cusscess', msg_type='success', display_time=3000)
                self.refresh_system_stations()
                self.ui_obj.show_modify_system_station_form(False)

            else:
                self.ui_obj.modify_station_message.show_message('Failed to save', msg_type='error', display_time=3000)


 


    def add_system_station(self):
        input_fields = self.ui_obj.get_add_system_station()
        verfiy = self.verify_system_station(input_fields, msg_wgt=self.ui_obj.add_station_message)
        if verfiy:
            ret = self.db.save_system_station(input_fields)
            if ret:
                self.refresh_system_stations()
                self.ui_obj.clear_add_system_station()
                self.ui_obj.add_station_message.show_message("Saved Success", msg_type='success', display_time=3000)
            else:
                self.ui_obj.add_station_message.show_message("failed to save", msg_type='error', display_time=3000)


    def verify_system_station(self, data:dict, msg_wgt:MessageWidget, id=None,):
        if data is None:
            msg_wgt.show_message('Please Fill All Requierd Fields', msg_type='error', display_time=3000)
            return False

        for system_info in self.systems_stations:
            if id is None or id != system_info['id']:
                if system_info['name'] == data['name']:
                    msg_wgt.show_message("this name is already exists", msg_type='error', display_time=3000)
                    return False
            
                if system_info['ip'] == data['ip']:
                    msg_wgt.show_message("this IP is already exists", msg_type='error', display_time=3000)
                    return False
        return True
    
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
    

    def check_system_connection(self):
        input_fields = self.ui_obj.get_add_ip()
        if self.pingThreadWorker.is_alive():
            self.ui_obj.add_station_message.show_message("Please wait for Response", msg_type='info', display_time=3000)
            return

        if input_fields['ip']:
            ip = input_fields['ip']
            worker = pingWorker(ip)
            worker.result_signal.connect(self.ping_result_event)
            thread = threading.Thread(target=worker.run, daemon=True)
            self.pingThreadWorker = threadWorkers(thread=thread, worker=worker)
            self.pingThreadWorker.start()
        else:
            self.ui_obj.add_station_message.show_message("IP filed can't be empty", msg_type='error', display_time=3000)



    def ping_result_event(self, status):
        if status == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            self.ui_obj.add_station_message.show_message("connection failed", msg_type='error', display_time=3000)
            return
        
        if status == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            self.ui_obj.add_station_message.show_message("connection success", msg_type='success', display_time=3000)
            return



    def set_speed(self):
        speed = self.ui_obj.speed_btn.text()
        speed = int(speed[:-1])
        speed = speed*2
        if speed> MAX_SPEED:
            speed = 1
        self.speed_rate = speed
        self.ui_obj.speed_btn.setText(str(speed)+'x')

        if self.image_loader is not None:
            self.image_loader.update_fps(speed_rate=self.speed_rate)









    def load_download_base_params(self):

        self.condidate_names = []

        self.download_systems_names = self.load_system_spec_column(column_name='name')
        self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_all, items=self.download_systems_names)


    def add_name(self):

        text = self.ui_obj.ret_current_value_combo_box(self.ui_obj.combo_download_all)
        if text !='':
            self.download_systems_names.remove(text)

            self.condidate_names.append(text)

            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_selected,items=self.condidate_names)
            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_all,items=self.download_systems_names)


    def remove_name(self):
        text = self.ui_obj.ret_current_value_combo_box(self.ui_obj.combo_download_selected)
        if text!='':
            self.condidate_names.remove(text)

            self.download_systems_names.append(text)

            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_all,items=self.download_systems_names)
            self.ui_obj.set_item_combo_box(combo_name=self.ui_obj.combo_download_selected,items=self.condidate_names)







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
        

        self.loading = LoadingWindow(self.ui_obj)
        self.loading.show()


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


    def play_images(self):

        if not self.image_loader.playing:

            if  self.image_loader.is_alive():
                text = 'Thread is already running.'
                print(text)
                self.ui_obj.show_error(text)
                return


            path_selected_day = self.get_path_selected_date()

                
            # Create a new Worker instance and start it
            self.stop_event.clear()  # Reset the stop event
            # self.image_loader = ImageLoader(self.stop_event)
            self.image_loader = ImageLoader(self.stop_event,path_selected_day, self.speed_rate)
            
            # ImageLoader runs in a separate thread
            self.image_loader.update_folder_path(path_selected_day)
            self.image_loader.image_signal.connect(self.ui_obj.update_image)  # Connect the signal to the update_image slot

            self.image_loader.start()
            
            text = 'Start Playing'
            self.ui_obj.update_log(text)


        else:
            text = 'First Stop Playing'
            print(text)
            self.ui_obj.show_error(text)


    def stop_show_image(self, event):
        # Stop the image loader thread when closing the window
        self.stop_event.set()
        self.image_loader.stop()
        text = 'Stop Playing'
        self.ui_obj.update_log(text)


  




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

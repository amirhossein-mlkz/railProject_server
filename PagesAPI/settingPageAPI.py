import threading


from PagesUI.settingPageUI import settingPageUI
from backend.database.mainDatabase import mainDatabase
from uiUtils.GUIComponents import MessageWidget
from Tranform.Network import pingAndCreateWorker
from Tranform.transformUtils import transormUtils
from backend.utils.threadWorker import threadWorkers
from Tranform.sharingConstans import StatusCodes
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames
from pathsConstans import pathConstants


class settingPageAPI:

    def __init__(self, uiHandler:settingPageUI, db:mainDatabase):
        self.uiHandler = uiHandler
        self.db = db
        self.mediator = Mediator()

        self.systems_stations = []
        self.pingThreadWorker = threadWorkers(None, None)
        self.current_system_staion_modify_id = None

        self.uiHandler.ui.btn_modify_cancel.clicked.connect(self.cancel_editing_systems_station)
        self.uiHandler.ui.btn_modify_save.clicked.connect(self.save_systems_station_change)
        self.uiHandler.ui.storage_clean_save_btn.clicked.connect(self.save_storage_setting)
        self.uiHandler.ui.storage_clean_cancel_btn.clicked.connect(self.load_storage_setting)



        self.uiHandler.ui.btn_save_add.clicked.connect(self.add_system_station)
        self.uiHandler.ui.btn_add_check_connection.clicked.connect(self.check_system_connection)

        self.uiHandler.show_modify_system_station_form(False)
        self.refresh_system_stations()

        self.load_storage_setting()


    def system_station_table_event(self, name:str, id:str):
        if name == 'delete':
            self.remove_system_station(id)
        
        elif name == 'edit':
            self.edit_system_station(id)
        
        else:
            print("BUG:system_station_table_event", name, id)

    
    def refresh_system_stations(self,):
        self.systems_stations = self.db.load_all_system_stations()
        self.uiHandler.set_system_stations_table(self.systems_stations, 
                                              event_func=self.system_station_table_event)
        
        self.mediator.start_event(eventNames.MODIFY_SYSTEM_STATIONS, args=(self.systems_stations,))


    def remove_system_station(self, id:int):
        res = self.uiHandler.show_confirmbox('remove', 'Are You Sure to remove?', buttons=['yes', 'no'])
        if res =='no':
            return
        ret = self.db.remove_system_station_by_id(id)
        self.refresh_system_stations()

    def edit_system_station(self, id):
        system_info = self.db.load_system_station_by_id(id)
        if system_info is None:
            return
        
        self.current_system_staion_modify_id = id
        
        self.uiHandler.set_modify_system_station_fields(system_info)
        self.uiHandler.show_modify_system_station_form(True)

    def cancel_editing_systems_station(self,):
        self.uiHandler.clear_modify_system_station_fields()
        self.uiHandler.show_modify_system_station_form(False)

    def save_systems_station_change(self,):
        input_fields = self.uiHandler.get_modify_system_station_fields()
        verfiy = self.verify_system_station(input_fields, 
                                         self.uiHandler.ui.modify_station_message , 
                                         id=self.current_system_staion_modify_id)
        
        if verfiy:

            ret = self.db.update_system_station_by_id(input_fields, id=self.current_system_staion_modify_id)
            if ret:
                self.uiHandler.ui.modify_station_message.show_message('Changes Saved Cusscess', 
                                                                      msg_type='success', 
                                                                      display_time=3000)
                self.refresh_system_stations()
                self.uiHandler.show_modify_system_station_form(False)

            else:
                self.uiHandler.ui.modify_station_message.show_message('Failed to save', 
                                                                      msg_type='error', 
                                                                      display_time=3000)


 


    def add_system_station(self):
        input_fields = self.uiHandler.get_add_system_station()
        verfiy = self.verify_system_station(input_fields, msg_wgt=self.uiHandler.ui.add_station_message)
        if verfiy:
            ret = self.db.save_system_station(input_fields)
            if ret:
                self.refresh_system_stations()
                self.uiHandler.clear_add_system_station()
                self.uiHandler.ui.add_station_message.show_message("Saved Success", 
                                                                   msg_type='success', 
                                                                   display_time=3000)
            else:
                self.uiHandler.ui.add_station_message.show_message("failed to save", 
                                                                msg_type='error', 
                                                                display_time=3000)


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
    

    def check_system_connection(self):
        ip = self.uiHandler.get_add_ip()
        username = self.uiHandler.get_add_username()
        password  = self.uiHandler.get_add_password()
        if self.pingThreadWorker.is_alive():
            self.uiHandler.ui.add_station_message.show_message("Please wait for Response", 
                                                               msg_type='info', 
                                                               display_time=3000)
            return

        if ip:
            path = transormUtils.build_share_path(ip, pathConstants.OTHER_SHARE_NAME)
            worker = pingAndCreateWorker(ip=ip,
                                         src_path=path, 
                                         username=username,
                                         password=password
                                         )
            worker.result_signal.connect(self.ping_result_event)
            thread = threading.Thread(target=worker.run, daemon=True)
            self.pingThreadWorker = threadWorkers(thread=thread, worker=worker)
            self.pingThreadWorker.start()
        else:
            self.uiHandler.ui.add_station_message.show_message("IP filed can't be empty", 
                                                               msg_type='error', 
                                                               display_time=3000)


    def ping_result_event(self, status, msg):
        if status == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            self.uiHandler.ui.add_station_message.show_message(msg, 
                                                            msg_type='error', 
                                                            display_time=3000)
            return
        
        if status == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            self.uiHandler.ui.add_station_message.show_message("connection success", 
                                                               msg_type='success', 
                                                               display_time=3000)
            return

    def save_storage_setting(self, ):
        parms = self.uiHandler.get_storage_setting()
        ret = self.db.save_storage_settings(data=parms)
        if ret:
            self.uiHandler.ui.storage_manager_msg.show_message('Changes Saved Cusscess', 
                                                                msg_type='success', 
                                                                display_time=3000)
            self.mediator.start_event(eventNames.STORAGE_SETTING_CHANGED, args=())
        else:
            self.uiHandler.ui.modify_station_message.show_message('Faild to save in Database', 
                                                                      msg_type='error', 
                                                                      display_time=3000)

    def load_storage_setting(self):
        parms = self.db.load_storage_settings()
        self.uiHandler.set_storage_setting(parms)



    
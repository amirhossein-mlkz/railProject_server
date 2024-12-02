import os
from threading import Thread, Event
import threading
import platform,subprocess

from PySide6.QtWidgets import QMessageBox

from backend.database.databaseManager import DataBaseManager
from backend.database.mainDatabase import mainDatabase
from main_ui import UI_main_window_org
from constanst import MAX_SPEED,COLUMN_DESTINATION,TABLE_PATHES
from Tranform.Network import pingWorker, Sharing
from Tranform.sharingConstans import StatusCodes
from Tranform.storgeManager import storageManager, Space
from PagesAPI.settingPageAPI import settingPageAPI
from PagesAPI.downloadPageAPI import downloadPageAPI
from PagesAPI.playbackPageAPI import playbackPageAPI
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames
from accessHandler import accessHandler
from login_qt.Constants import Constants as userConstants
import constanst
from pathsConstans import pathConstants
from storageCleaningUI import storageCleaningDialog
from backend import FirewallRules

class API:
    def __init__(self, uiHandler:UI_main_window_org):

        self.mkdirs()
        try:
            FirewallRules.enable_file_sharing()
            FirewallRules.ensure_network_discovery_enabled()
        except:
            pass

        try:
            Sharing.remove_share(pathConstants.SELF_SHARE_NAME)
            Sharing.create_and_share_folder(pathConstants.SELF_SHARE_PATH,
                                            pathConstants.SELF_SHARE_NAME)
        except:
            pass




        self.uiHandler = uiHandler
        self.create_db_obj()
        # self.load_base_parms()
        self.button_connector()
        self.speed_rate = 1
        self.check_available_trains()
        self.train_id_selected = False
        self.preview_login = False


        self.stop_event = Event()

        self.Mediator = Mediator()
        self.Mediator.register_events(eventNames.MODIFY_SYSTEM_STATIONS)
        self.Mediator.register_events(eventNames.STORAGE_SETTING_CHANGED)
        self.Mediator.register_events(eventNames.NAV_KEY_PRESS_KEYBOARD)

  

        self.settingPageAPI = settingPageAPI(self.uiHandler.settingPageUI, self.db)
        self.downloadPageAPI = downloadPageAPI(self.uiHandler.downloadPageUI, self.db)
        self.playbackPageAPI = playbackPageAPI(self.uiHandler.playbackPageUI, self.db)

        self.accessHandler = accessHandler(self.uiHandler)

        self.settingPageAPI.refresh_system_stations()
        self.login_logout_evet(None)

        # #------------------------
        # self.storageManager = None
        # self.storageManager_thread = None
        # self.storageCleaningDialog = storageCleaningDialog()
        # #-----------------------

        


        
        
    def mkdirs(self,):
        if not os.path.exists(pathConstants.SELF_SHARE_PATH):
            os.makedirs(pathConstants.SELF_SHARE_PATH)
        
        if not os.path.exists(pathConstants.SELF_SHARE_PATH):
            os.makedirs(pathConstants.SELF_SHARE_PATH)


        if not os.path.exists(pathConstants.SELF_UTILS_DIR):
            os.makedirs(pathConstants.SELF_UTILS_DIR)

        # if not os.path.exists(pathConstants.SELF_UPD ATES_PATH):
        #     os.makedirs(pathConstants.SELF_UPDATES_PATH)

        # if not os.path.exists(pathConstants.SELF_UPDATE_IMAGEGRABBER_PATH):
        #     os.makedirs(pathConstants.SELF_UPDATE_IMAGEGRABBER_PATH)    

    

    def button_connector(self):
        self.uiHandler.ui.btn_side_download.clicked.connect(self.load_download_base_params)
        self.uiHandler.ui.btn_side_login.clicked.connect(self.check_user_loggedin)


        # self.uiHandler.ui.btn_select_train.clicked.connect(self.set_train_id)
       
    def check_user_loggedin(self):
        loggedin_user = self.uiHandler.login_obj.login_API.get_logined_user()
        if loggedin_user is None:
            self.show_login()
        else:
            self.show_user_managment_page(loggedin_user)




    def show_user_managment_page(self,loggedin_user):
        role = loggedin_user['role']
        if role == 'Admin':
            accessibity = [userConstants.UIPages.CHANGE_PASSWORD,
                           userConstants.UIPages.CHANGE_USERNAME,
                           userConstants.UIPages.ALL_USERS,
                           userConstants.UIPages.SIGNUP,
                           userConstants.UIPages.LOGIN]
        else:
            accessibity = [userConstants.UIPages.CHANGE_PASSWORD,
                           userConstants.UIPages.CHANGE_USERNAME,
                           userConstants.UIPages.LOGIN]

        if self.uiHandler.login_obj.login_API.get_logined_user() is not None:
            ret= self.uiHandler.login_obj.show_page(userConstants.UIPages.MENU, accessibity)
            
            #user logout
            if self.uiHandler.login_obj.login_API.get_logined_user() is None:
                self.login_logout_evet(None)
                self.uiHandler.set_user(is_login=False)


    def login_logout_evet(self, role):
        print(f'role:{role}')
        self.accessHandler.set_role(role)



    def show_login(self):
        self.uiHandler.applyBlurEffect()
        self.uiHandler.login_obj.show_page()
        # self.preview_login = False
        loggedin_user = self.uiHandler.login_obj.login_API.get_logined_user()
        if loggedin_user is not None:
            self.uiHandler.set_user(is_login=True,user_name= loggedin_user['username'])
            self.login_logout_evet(loggedin_user['role'])
            

        else:
            self.uiHandler.set_user(is_login=False)

        

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
        pass
    
    def add_name(self):

        text = self.uiHandler.ret_current_value_combo_box(self.uiHandler.ui.combo_download_all)
        if text !='':
            self.download_systems_names.remove(text)

            self.condidate_names.append(text)

            self.uiHandler.set_item_combo_box(combo_name=self.uiHandler.ui.combo_download_selected,items=self.condidate_names)
            self.uiHandler.set_item_combo_box(combo_name=self.uiHandler.ui.combo_download_all,items=self.download_systems_names)


    def remove_name(self):
        text = self.uiHandler.ret_current_value_combo_box(self.uiHandler.ui.combo_download_selected)
        if text!='':
            self.condidate_names.remove(text)

            self.download_systems_names.append(text)

            self.uiHandler.set_item_combo_box(combo_name=self.uiHandler.ui.combo_download_all,items=self.download_systems_names)
            self.uiHandler.set_item_combo_box(combo_name=self.uiHandler.ui.combo_download_selected,items=self.condidate_names)


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
            self.uiHandler.set_item_combo_box(self.uiHandler.combo_train_id,trains)


    

    def storage_cleaning_progress_event(self, deleted:Space, total:Space):
        percent = deleted.bytes / total.bytes * 100
        self.storageCleaningDialog.set_progess_value(percent)

    def storage_cleaning_finish_event(self, ):
        self.storageCleaningDialog.close()


if __name__ == '__main__':

    obj = API('test')

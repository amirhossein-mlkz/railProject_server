import threading


from PagesUI.downloadPageUI import downloadPageUI
from backend.database.mainDatabase import mainDatabase
from uiUtils.GUIComponents import MessageWidget
from Tranform.Network import pingWorker
from backend.utils.threadWorker import threadWorkers
from Tranform.sharingConstans import StatusCodes
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames



class downloadPageAPI:
    FILTER_STEP_FINAL = 3
    def __init__(self, uiHandler:downloadPageUI, db:mainDatabase):
        self.uiHandler = uiHandler
        self.db = db
        self.mediator = Mediator()

        self.filter_step = 0

        self.mediator.add_event_listener(event_name=eventNames.MODIFY_SYSTEM_STATIONS, 
                                         priority=5,
                                         func=self.update_stations_event)
        
        self.systems_stations = []
        self.selected_stations_id_for_download = []
        

        self.uiHandler.ui.download_search_station.textChanged.connect(self.update_download_stations_list)
        self.uiHandler.ui.download_all_stations_checkbox.checkStateChanged.connect(self.select_all_staions_for_download)
        self.uiHandler.ui.download_filter_next_btn.clicked.connect(self.next_filter_step)
        self.uiHandler.ui.download_filter_prev_btn.clicked.connect(self.prev_filter_step)

        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)



    def update_stations_event(self, systems_stations:list[dict] ):
        self.systems_stations = systems_stations
        self.update_download_stations_list()


    def update_download_stations_list(self,  ):
        search_q = self.uiHandler.ui.download_search_station.text()
        if search_q:
            resluts = list(filter( lambda x:search_q.lower() in x['name'], self.systems_stations))
        else:
            resluts = self.systems_stations
        
        self.uiHandler.set_download_stations_list(resluts, 
                                                  event_func=self.download_system_station_select_event,
                                                  selected_ids=self.selected_stations_id_for_download)


    def download_system_station_select_event(self, state, id):
        if state:
            if id not in self.selected_stations_id_for_download:
                self.selected_stations_id_for_download.append(id)
        else:
            if id in self.selected_stations_id_for_download:
                self.selected_stations_id_for_download.remove(id)

    
    def select_all_staions_for_download(self, state):
        if state.value:
            self.selected_stations_id_for_download = list(map(lambda x:x['id'], self.systems_stations))
        else:
            self.selected_stations_id_for_download = []
        
        self.update_download_stations_list()

    def next_filter_step(self,):
        if self.filter_step == 0:
            self.step0_filter()

    def prev_filter_step(self,):
        self.filter_step = max(self.filter_step-1, 0)
        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)


    
    def step0_filter(self,):
        if len(self.selected_stations_id_for_download) == 0:
            self.uiHandler.ui.download_filter_message.show_message("Please select at least 1 station",
                                                                   msg_type='error',
                                                                   display_time=4000)
            return
        
        #load_all_configs
        self.fetch_stations_db_event()
    
    def fetch_stations_db_event(self, ):
        datas:dict[str, dict] = {
            'milad': {
                '11BG12': [],
                '13CF00': [],
            }
        }
        
        all_trains = []
        for station in datas.keys():
            all_trains = all_trains + list(datas[station].keys())
        all_trains = set(all_trains)

        self.uiHandler.set_filter_trains(all_trains)

        if len(all_trains) == 0:
            self.uiHandler.ui.download_filter_message.show_message("No Trains Found", msg_type='error', display_time=4000)

        self.filter_step +=1
        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)


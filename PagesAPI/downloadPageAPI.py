import threading

from persiantools.jdatetime import JalaliDateTime, timedelta

from PagesUI.downloadPageUI import downloadPageUI
from backend.database.mainDatabase import mainDatabase
from uiUtils.GUIComponents import MessageWidget
from Tranform.Network import pingWorker, pingAndCreateWorker
from Tranform.transformUtils import transormUtils
from Tranform.transformModule import archiveManager
from backend.utils.threadWorker import threadWorkers
from Tranform.sharingConstans import StatusCodes
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames
from pathConstans import pathConstants
from uiUtils.guiBackend import GUIBackend
from downloadSectionUI import downloadSection


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
        self.selected_train = None
        self.selected_camera = None
        self.selected_date = None
        self.station_logs  = []
        self.stations_archives:dict[str, archiveManager] = {}
        self.stations_passed_train_filter = []
        self.station_passed_date_filter = []

        self.pingThreadWorker = threadWorkers(None,None)
        

        self.uiHandler.ui.download_search_station.textChanged.connect(self.update_download_stations_list)
        self.uiHandler.ui.download_all_stations_checkbox.checkStateChanged.connect(self.select_all_staions_for_download)
        self.uiHandler.ui.download_filter_next_btn.clicked.connect(self.next_filter_step)
        self.uiHandler.ui.download_filter_prev_btn.clicked.connect(self.prev_filter_step)
        self.uiHandler.train_filter_change_connector(self.train_changed)
        self.uiHandler.calendar_dialog.set_calender_event(self.date_select_event)


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
        
        elif self.filter_step == 1:
            self.step1_filter()

        elif self.filter_step == 2:
            self.step2_filter()

        elif self.filter_step == 3:
            self.step3_filter()

    def prev_filter_step(self,):
        self.filter_step = max(self.filter_step-1, 0)
        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)
    
    def step0_filter(self,):
        if len(self.selected_stations_id_for_download) == 0:
            self.uiHandler.ui.download_filter_message.show_message("Please select at least 1 station",
                                                                   msg_type='error',
                                                                   display_time=4000)
            return
        
        self.uiHandler.ui.download_filter_frame.setDisabled(True)
        self.station_logs = []

        GUIBackend.cursor_changer('wait')


        for id in self.selected_stations_id_for_download:
            system_info = self.db.load_system_station_by_id(id)
            if system_info is None:
                continue
            
            path = transormUtils.build_share_path(system_info['ip'], pathConstants.OTHER_IMAGES_SHARE_FOLDER)# SHOULD BE CHANGE
            worker = pingAndCreateWorker(system_info['ip'],
                                         src_path=path,
                                         username=system_info['username'],
                                         password=system_info['password'])
            event_func = transormUtils.pass_extra_arg_event(self.step0_check_connection_event, (id,))
            worker.result_signal.connect(event_func)
            thread = threading.Thread(target=worker.run, daemon=True)
            thread.start()


        
    
    def step0_check_connection_event(self, status, msg, id ):
        station_system = self.db.load_system_station_by_id(int(id))
        if status == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            self.station_logs.append( { 'info':station_system,
                                        'status' : False,
                                        'message':  msg
                                    }
                                )
        
        
        elif status == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            pass
        
        #check if result of all station got
        print(station_system)
        self.check_for_finish()

    def check_for_finish(self,):
        if len(self.station_logs) == len(self.selected_stations_id_for_download):
            self.step0_finish()

    
    def step0_finish(self,):
        GUIBackend.cursor_changer(None)
        
        #-----------------------------------------------------------------  
        self.stations_archives= {}
        for log in self.station_logs:
            archive = archiveManager(pathConstants.UTILS_DIR)
            archive.load()
            name = log['info']['name']
            self.stations_archives[name] = archive
        #-----------------------------------------------------------------

                
        self.uiHandler.ui.download_filter_frame.setEnabled(True)
        self.uiHandler.set_filter_stations_logs(self.station_logs)
        #---------------------------------
        all_trains = []
        for station in self.stations_archives.keys():
            all_trains = all_trains + self.stations_archives [station].get_available_trains()
        all_trains = set(all_trains)
        #---------------------------------

        self.uiHandler.set_filter_trains(all_trains)
        self.train_changed()

        if len(all_trains) == 0:
            self.uiHandler.ui.download_filter_message.show_message("No Trains Found", msg_type='error', display_time=4000)

        self.filter_step =1
        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)


    def train_changed(self,):
        GUIBackend.cursor_changer('wait')
        selected_train = self.uiHandler.get_selected_train()
        cameras = []
        for name, archive in self.stations_archives.items():
            cams = archive.get_available_cameras(selected_train)
            cameras.extend(cams)
        cameras = list(set(cameras))
        self.uiHandler.set_filter_cameras(cameras)
        GUIBackend.cursor_changer(None)


    def step1_filter(self, ):
        self.selected_train = self.uiHandler.get_selected_train()
        self.selected_camera = self.uiHandler.get_selected_camera()


        self.stations_passed_train_filter = []
        available_dates = []
        for name, archive in self.stations_archives.items():
            dates = archive.get_avaiable_dates(train_id=self.selected_train)
            if len(dates):
                if self.selected_camera in dates.keys():
                    self.stations_passed_train_filter.append(name)
                    available_dates.extend( dates[self.selected_camera] )
        available_dates = list(set(available_dates))
        self.uiHandler.calendar_dialog.set_avaiable_date_ranges(available_dates)

        self.selected_date = None
        self.uiHandler.calendar_dialog.set_date(self.selected_date)

        self.filter_step =2
        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)


    
    def step2_filter(self,):
        #select date
        if not self.selected_date:
            self.uiHandler.ui.download_filter_message.show_message("Please Select A Date", msg_type='error', display_time=4000)
            return
        
        self.station_passed_date_filter = []
        all_times = []

        for name in self.stations_passed_train_filter:
            arcihve = self.stations_archives[name]
            avaialbe_dates = arcihve.get_avaiable_dates(self.selected_train)

            #check date exist in archive
            if self.selected_date in avaialbe_dates[self.selected_camera]:
                self.station_passed_date_filter.append(name)
                times = arcihve.get_day_times(self.selected_train, self.selected_date, self.selected_camera)
                all_times.extend(times)
        
        self.times_ranges = transormUtils.times2ranges(all_times, step_lenght_sec=600)
        for clock in self.uiHandler.Clocks.values():
            clock.set_time_ranges(self.times_ranges)

        self.filter_step = 3
        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)

    def date_select_event(self, date:JalaliDateTime):
        self.selected_date = date

    
    def step3_filter(self,):
        self.uiHandler.clear_download_sections()

        start_time , end_time = self.uiHandler.get_selected_time_range()
        start_datetime = JalaliDateTime.combine(self.selected_date, start_time)
        end_datetime   = JalaliDateTime.combine(self.selected_date, end_time)

        if start_datetime > end_datetime:
            self.uiHandler.ui.download_filter_message.show_message("Start time Can't be bigger than end time", msg_type='error', display_time=4000)
        

        for station in self.stations_archives.keys():
            results = self.stations_archives[station].filter_files(
                                                    train_id=self.selected_train,
                                                    date=self.selected_date,
                                                    camera=self.selected_camera,
                                                    start_time=start_datetime,
                                                    end_time=end_datetime
                                                )
            if len(results):
                times = list(map(lambda x:x['datetime'], results))
                times_rangs =  transormUtils.times2ranges(times, step_lenght_sec=600)
                sec = downloadSection(  _id=1,
                                        name=station,
                                        dt=self.selected_date
                                        )
                
                sec.set_time_ranges(times_rangs)
                self.uiHandler.add_download_section(sec)

                                            
import threading

from persiantools.jdatetime import JalaliDateTime, timedelta

from PagesUI.downloadPageUI import downloadPageUI
from backend.database.mainDatabase import mainDatabase
from uiUtils.GUIComponents import MessageWidget
from Tranform.Network import pingWorker, pingAndCreateWorker
from Tranform.transformUtils import transormUtils
from Tranform.transformModule import archiveManager, transformModule
from backend.utils.threadWorker import threadWorkers
from Tranform.sharingConstans import StatusCodes
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames
from pathsConstans import pathConstants
from uiUtils.guiBackend import GUIBackend
from downloadSectionUI import downloadSection
from Tranform.storgeManager import storageManager, Space
from Tranform.idList import idList

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
        self.selected_datetime_range = None
        self.station_logs  = []
        self.stations_archives:dict[str, archiveManager] = {}
        self.stations_passed_train_filter = []
        self.station_passed_date_filter = []
        self.download_sections = idList()

        



        self.pingThreadWorker = threadWorkers(None,None)
        

        self.uiHandler.ui.download_search_station.textChanged.connect(self.update_download_stations_list)
        self.uiHandler.ui.download_all_stations_checkbox.checkStateChanged.connect(self.select_all_staions_for_download)
        self.uiHandler.ui.download_filter_next_btn.clicked.connect(self.next_filter_step)
        self.uiHandler.ui.download_filter_prev_btn.clicked.connect(self.prev_filter_step)
        self.uiHandler.train_filter_change_connector(self.train_changed)
        self.uiHandler.calendar_dialog.set_calender_event(self.date_select_event)


        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)
        self.uiHandler.set_station_archive_progress_visible(False)

        #-------------------------
        self.storageManager_worker:storageManager = storageManager(path=pathConstants.SELF_IMAGES_DIR,
                                            logs_path=None,
                                            max_usage=0.9,
                                            logger=None,
                                            )
        self.storageManager_worker.finish_cleaning_signal.connect(self.storage_cleaning_finish)
        self.storageManager_worker.progress_signal.connect(self.storage_cleaning_progress)
        self.storageManager_thread:threading.Thread = threading.Thread(target=self.storageManager_worker.run,
                                                                       daemon=True)
        self.storageManager_thread.start()
        #-------------------------
        



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

        self.complete_archive_count = 0
        self.uiHandler.set_station_archive_progress(self.complete_archive_count, 
                                                    len(self.selected_stations_id_for_download))
        self.uiHandler.set_station_archive_progress_visible(True)

        for id in self.selected_stations_id_for_download:
            system_info = self.db.load_system_station_by_id(id)
            if system_info is None:
                self.complete_archive_count +=1
                continue
            
            path = transormUtils.build_share_path(system_info['ip'], pathConstants.OTHER_IMAGES_SHARE_FOLDER)
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
            self.station_logs.append( { 'info':station_system,
                                        'status' : True,
                                        'message':  msg
                                    }
                                )
        
        #check if result of all station got
        self.complete_archive_count +=1
        self.uiHandler.set_station_archive_progress(self.complete_archive_count)
        self.check_for_finish()

    def check_for_finish(self,):
        if len(self.station_logs) == len(self.selected_stations_id_for_download):
            self.step0_finish()

    
    def step0_finish(self,):
        GUIBackend.cursor_changer(None)
        
        
        #-----------------------------------------------------------------  
        #ONLY FOR TEST
        self.stations_archives= {}
        for log in self.station_logs:
            archive_path = transormUtils.build_share_path(ip=log['info']['ip'],
                                                          share_name=pathConstants.OTHER_UTILS_SHARE_FOLDER)
            
            archive = archiveManager(archive_path)
            flag = archive.load()
            if flag:
                name = log['info']['name']
                self.stations_archives[name] = archive
            else:
                log['status'] = False
                log['message'] = f"Couldn't open archive"
        #ONLY FOR TEST
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
            self.uiHandler.ui.download_filter_message.show_message("No Trains Found", msg_type='error', display_time=8000)

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
        if self.selected_train == '':
            self.uiHandler.ui.download_filter_message.show_message("Train Is Empty", msg_type='error', display_time=4000)
            return

        if self.selected_camera == '':
            self.uiHandler.ui.download_filter_message.show_message("Camera Is Empty", msg_type='error', display_time=4000)
            return



        self.stations_passed_train_filter = []
        available_dates = []
        for name, archive in self.stations_archives.items():
            dates = archive.get_avaiable_dates(train_id=self.selected_train, camera=self.selected_camera)
            if len(dates):
                self.stations_passed_train_filter.append(name)
                available_dates.extend( dates )
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
            avaialbe_dates = arcihve.get_avaiable_dates(self.selected_train, self.selected_camera)

            #check date exist in archive
            if self.selected_date in avaialbe_dates:
                self.station_passed_date_filter.append(name)
                times = arcihve.get_day_times(self.selected_train, self.selected_date, self.selected_camera)
                all_times.extend(times)
        
        self.times_ranges = transormUtils.times2ranges(all_times, step_lenght_sec=600)
        for clock in self.uiHandler.Clocks.values():
            clock.set_time_ranges(self.times_ranges, self.selected_date)

        self.filter_step = 3
        self.uiHandler.set_filter_form_step(self.filter_step, self.FILTER_STEP_FINAL)

    def date_select_event(self, date:JalaliDateTime):
        self.selected_date = date

    
    def step3_filter(self,):
        i = 0
        while i < len(self.download_sections):
            dowload_sec:downloadSection = self.download_sections[i]
            if dowload_sec.is_during_download:
                i+=1
                continue

            self.download_sections.remove_by_id(dowload_sec.id)
            self.uiHandler.remove_download_section(dowload_sec)



        start_time , end_time = self.uiHandler.get_selected_time_range()
        start_datetime = JalaliDateTime.combine(self.selected_date, start_time)
        end_datetime   = JalaliDateTime.combine(self.selected_date, end_time)

        self.selected_datetime_range = (start_datetime, end_datetime)

        if start_datetime > end_datetime:
            self.uiHandler.ui.download_filter_message.show_message("Start time Can't be bigger than end time", msg_type='error', display_time=4000)
        

        for station in self.station_passed_date_filter:
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
                station_info = self.db.load_system_station_by_name(station)
                if station_info is None:
                    self.uiHandler.show_confirmbox('Error', 
                                                   f'Error happend in load {station} staion info, it may removed from database',
                                                   buttons=['ok'])
                    return

                sec = downloadSection(  
                                        station_info=station_info,
                                        train=self.selected_train,
                                        camera=self.selected_camera,
                                        dt=self.selected_date
                                        )
                

                
                sec.download_btn_connector(self.start_download,)
                sec.close_btn_connector(self.close_download_section, args=(station,))
                
                sec.set_time_ranges(times_rangs)
                self.uiHandler.add_download_section(sec)
                self.download_sections.append( sec, sec.id)


    def start_download(self, sec_id):
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)
        download_sec.set_during_download(True)
            
        tf = transformModule(download_sec.station_info['ip'],
                        src_path=pathConstants.OTHER_IMAGES_SHARE_FOLDER,
                        dst_path=pathConstants.SELF_IMAGES_DIR,
                        username=download_sec.station_info['username'],
                        password=download_sec.station_info['password']
                        )
        
        download_sec.set_transformer(tf)
        event_func = transormUtils.pass_extra_arg_event(self.station_download_file_check_connection, 
                                                        (sec_id,))
        tf.check_connection_and_create_connection(event_func)


    
    def station_download_file_check_connection(self, status, msg, sec_id ):
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)

        if status == StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT:
            download_sec.write_msg(
                txt=msg,
                )
            download_sec.reset()
            return
    
        if status == StatusCodes.pingAndConnectionStatusCodes.SUCCESS:
            finish_func = transormUtils.pass_extra_arg_event(self.find_files_finish, (sec_id,))
            log_func = transormUtils.pass_extra_arg_event(self.find_files_station_log, (sec_id,))

            download_sec.transformer.find_files(
                trains=[self.selected_train],
                dates_tange=self.selected_datetime_range,
                status=None,
                finish_event_func=finish_func,
                log_event_func=log_func,
                log_search=False
            )
        
        
        
    def find_files_station_log(self, log:str, sec_id):
        txt = f'Searching Files: {log}'
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)
        download_sec.write_msg(txt)

    def find_files_finish(self, 
                          status_code, 
                          paths:list[str], 
                          sizes:list[int],
                          sec_id,
                          ):
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)
        
        if status_code == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            path = download_sec.transformer.src_path
            download_sec.write_msg(f"Path dosen't exists: {path}", )
            download_sec.reset()
            return
        


        if len(paths) == 0:
            download_sec.write_msg(f"No Files Found to Copy", )
            download_sec.reset()
            return
        
        download_sec.set_download_files(paths, sizes)
        

        res, space_need_clean = self.storageManager_worker.has_enough_space_for_files(
                                                              files_path=paths,
                                                              sizes=sizes,
                                                              src_dir=download_sec.transformer.src_path,
                                                              dst_dir=download_sec.transformer.dst_path
                                                              )
        space_need_clean:Space
        
        if not res:
            ans = self.uiHandler.show_confirmbox('Error Memory',
                                           f'''not enough space for download, {space_need_clean.toMB()} MB should be remove. 
                                           do you want remove old files automative?''',
                                           buttons=['yes', 'no'])
            if ans == 'no':
                download_sec.reset()
                return
            
            download_sec.write_msg('Wait for cleaninig Storage...')
            
            self.storageManager_worker.send_clean_request(name=str(sec_id),
                                                          size= space_need_clean)
            
        else:
            self.storage_cleaning_finish(str(sec_id), True)


    def storage_cleaning_progress(self, sec_id, remove_path, deleted:Space, total:Space):
        if sec_id != '':
            sec_id = int(sec_id) #storageManager signals work with str so we should retun id into int
            download_sec:downloadSection = self.download_sections.get_by_id(sec_id)
            download_sec.write_msg(
                f"Delete {deleted.toMB()}/{total.toMB()} - Removed {remove_path}"
            )


    

    def storage_cleaning_finish(self, sec_id, status):
        sec_id = int(sec_id) #storageManager signals work with str so we should retun id into int
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)

        if not status:
            download_sec.write_msg('There is not enough video for delete')
            download_sec.reset()
            return

        download_sec.set_progess_value(0)
        finish_func = transormUtils.pass_extra_arg_event(self.station_download_finish, (sec_id,))
        log_func = transormUtils.pass_extra_arg_event(self.station_download_log, (sec_id,))
        progress_func = transormUtils.pass_extra_arg_event(self.station_download_progress, (sec_id,))
        download_sec.transformer.start_copy( download_sec.files_paths, 
                                             download_sec.files_sizes, 
                                             finish_func=finish_func,
                                             speed_func=None,
                                             progress_func=progress_func,
                                             msg_callback=log_func,
                                             rename_src=False,
                                             move=False)
        

    

    def station_download_log(self, msg, sec_id):
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)
        download_sec.write_msg(msg)


    def station_download_progress(self,completed:int, total:int, sec_id):
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)

        if total<1:
            total = 1 
        percent = int(completed/total * 100)
        download_sec.set_progess_value(percent)


    def station_download_finish(self, status_code, sec_id):
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)
        
        if status_code == StatusCodes.copyStatusCodes.DISCONNECT:
            download_sec.write_msg("Dissconnected!")
            download_sec.reset()
            return
        
        download_sec.write_msg("Download Videos Finish Success")    
        download_sec.reset()

        

    def close_download_section(self, sec_id):
        download_sec:downloadSection = self.download_sections.get_by_id(sec_id)
        self.uiHandler.remove_download_section(section=download_sec)

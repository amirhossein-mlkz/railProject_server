import threading

from persiantools.jdatetime import JalaliDateTime, timedelta
from datetime import time as Time
from PySide6.QtCore import Qt, QTimer


from PagesUI.playbackPageUI import playbackPageUI
from backend.database.mainDatabase import mainDatabase
from uiUtils.GUIComponents import MessageWidget
from Tranform.Network import pingWorker
from backend.utils.threadWorker import threadWorkers
from Tranform.sharingConstans import StatusCodes
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames
# from Tranform.filesScanners import filesFinderWorker
from Tranform.transformModule import archiveManager
from Tranform.sharingConstans import DIRECTORY_TREE
from Tranform.transformUtils import transormUtils
from backend.mediaPlayer.player import MediaPlayer
from pathConstans import pathConstants




class playbackPageAPI:
    def __init__(self, uiHandler:playbackPageUI, db:mainDatabase):
        self.uiHandler = uiHandler
        self.db = db
        self.mediator = Mediator()

        self.filesFinderThreadWorker = threadWorkers(None,None)
        self.videos_avaiabilities:dict[str, dict[str,list]] = {}

        self.selected_camera = None
        self.selected_date = None
        self.selected_train = None
        self.curent_video_idx = 0

        self.Player = MediaPlayer(self.uiHandler.ui.video)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshing_ui)
        self.timer.start(500)  # Update every second

        self.uiHandler.ui.refresh_btn.clicked.connect(self.update_archive)
        self.uiHandler.calendar_dialog.set_calender_event(self.date_select_event)
        self.uiHandler.ui.play_btn.clicked.connect(self.play_video)
        self.uiHandler.ui.pause_btn.clicked.connect(self.pause_video)
        self.uiHandler.ui.speed_btn.clicked.connect(self.change_video_speed)
        self.uiHandler.ui.playback_camera_combo.currentTextChanged.connect(self.camera_change_event)
        self.uiHandler.ui.playback_combo_train_id.currentTextChanged.connect(self.select_train_event)
        self.uiHandler.timeLineSlider.timeSelected.connect(self.timline_change_event)
        
        self.archiveManager = archiveManager(pathConstants.UTILS_DIR)
        self.archiveManager.load()
        self.load_archive()

        self.uiHandler.ui.refresh_image_database_log.hide()


    def update_archive(self,):
        if self.archiveManager.is_during_updating():
            return
        
        self.archiveManager.update_archive(src_path=pathConstants.SELF_IMAGES_DIR,
                                           finish_func=self.images_database_refresh_event,
                                           log_func=self.availability_logs_event)

    

    def availability_logs_event(self, txt):
        self.uiHandler.ui.refresh_image_database_log.show()
        txt = f'Founded:{txt}'
        self.uiHandler.ui.refresh_image_database_log.setText(txt)

    def images_database_refresh_event(self, status,):
        self.uiHandler.ui.refresh_image_database_log.hide()
        
        if status == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            self.uiHandler.ui.refresh_image_db_message.show_message('Directory not found',
                                                                    msg_type='error',
                                                                    display_time=3000)
            
                
        elif status == StatusCodes.findFilesStatusCodes.SUCCESS:
            self.uiHandler.ui.refresh_image_db_message.show_message('Database updated',
                                                                    msg_type='success',
                                                                    display_time=2000)
            self.load_archive()

    def load_archive(self,):
        trains = self.archiveManager.get_available_trains()            
        self.uiHandler.set_avaiable_trains(trains)

    # def merge_dates(self,):
    #     for train in self.videos_avaiabilities:
    #         for cam in self.videos_avaiabilities[train]:
    #             self.videos_avaiabilities[train][cam] = transormUtils.dateTimeRanges(self.videos_avaiabilities[train][cam], 600)


    def select_train_event(self,):    
        train_id = self.uiHandler.get_selected_train()        
        if not train_id:
            return
        
        self.selected_train = train_id
        
        dates = self.archiveManager.get_avaiable_dates(train_id)

        all_dates = []

        for cam in dates.keys():
            all_dates = all_dates + dates[cam]
        
        self.uiHandler.calendar_dialog.set_avaiable_date_ranges(all_dates)
    

    def date_select_event(self, date:JalaliDateTime):
        self.uiHandler.ui.playback_filter_frame.setDisabled(True)
        self.selected_date = date

        cameras = self.archiveManager.get_available_cameras(self.selected_train)
        self.uiHandler.set_cameras(cameras)

    
    def camera_change_event(self,):
        self.selected_camera = self.uiHandler.get_current_camera()
        if not self.selected_camera:
            return

        # self.uiHandler.set_load_video_progress(0)
        self.uiHandler.trainLoading.set_value(0)
        self.uiHandler.trainLoading.show()
        self.archiveManager.get_day_time_ranges(train_id=self.selected_train, 
                                                date=self.selected_date, 
                                                cameras=[self.selected_camera],
                                                finish_func=self.date_ranges_event, 
                                                progress_func=self.date_ranges_progress)

    def date_ranges_event(self, date_ranges:dict[str, list]):
        self.date_ranges = date_ranges
        self.uiHandler.ui.playback_filter_frame.setDisabled(False)
        start = JalaliDateTime.combine(self.selected_date, Time.min)
        end = start + timedelta(days=1)

        self.uiHandler.set_timelines(date_ranges[self.selected_camera]['ranges'], start=start, end=end)
        self.Player.load_video(date_ranges[self.selected_camera]['paths'][self.curent_video_idx])
    
    def date_ranges_progress(self, value:float):
        value = int(value * 1000) #denormal
        self.uiHandler.trainLoading.set_value(value)

    def play_video(self,):
        self.Player.play_video()

    def pause_video(self,):
        self.Player.pause_video()

    def change_video_speed(self, ):
        speed = self.Player.change_speed()
        self.uiHandler.ui.speed_btn.setText(f'{speed}x')
    
    def refreshing_ui(self,):
        if self.Player.is_finished():
            #move to next video
            self.curent_video_idx+=1
            if self.curent_video_idx > len(self.date_ranges[self.selected_camera]):
                self.curent_video_idx = 0
            self.Player.load_video(self.date_ranges[self.selected_camera]['paths'][self.curent_video_idx])
            self.Player.play_video()


        if self.Player.is_playing():
            sec = self.Player.get_time()
            start_datetime, end_datetime = self.date_ranges[self.selected_camera]['ranges'][self.curent_video_idx]
            current_datetime:JalaliDateTime = start_datetime + timedelta(seconds=sec)
            
            self.uiHandler.timeLineSlider.set_time_by_jdatetime(current_datetime)

            time_string = current_datetime.strftime('%Y/%m/%d  %H:%M:%S')
            marquee_text = f"{self.selected_train} | {self.selected_camera} {time_string}"
            self.Player.update_marquee(marquee_text, position=6, font_size=48)

    def timline_change_event(self, date_time:JalaliDateTime):
        date_ranges = self.date_ranges[self.selected_camera]['ranges']
        paths = self.date_ranges[self.selected_camera]['paths']

        for i,(start, end) in enumerate(date_ranges):
            if start<=date_time<=end:
                self.curent_video_idx = i
                secs:timedelta = date_time - start
                secs = secs.total_seconds()
                self.Player.load_video(paths[self.curent_video_idx])
                self.play_video()
                self.Player.set_time(secs)
                break

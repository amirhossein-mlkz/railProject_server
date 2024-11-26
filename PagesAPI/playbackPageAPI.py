import threading
import time

from persiantools.jdatetime import JalaliDateTime, timedelta
from datetime import time as Time
from PySide6.QtCore import Qt, QTimer


from Export.export import UIExport
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
from pathsConstans import pathConstants
from uiUtils.Calendar import  JalaliCalendarDialog




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
        self.date_ranges = {}
        self.is_playing = False


        self.Player = MediaPlayer(self.uiHandler.ui.video)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refreshing_ui)
        self.timer.start(500)  # Update every second


        self.uiHandler.ui.refresh_btn.clicked.connect(self.update_archive)
        self.uiHandler.calendar_dialog.set_calender_event(self.date_select_event)
        self.uiHandler.ui.play_btn.clicked.connect(self.play_video)
        self.uiHandler.ui.speed_btn.clicked.connect(self.change_video_speed)
        self.uiHandler.ui.btn_export.clicked.connect(self.show_export)
        self.uiHandler.ui.left_rotate_btn.clicked.connect(lambda : self.rotate_video(-1))
        self.uiHandler.ui.right_rotate_btn.clicked.connect(lambda : self.rotate_video(+1))
        self.uiHandler.ui.flip_horizontal_btn.clicked.connect(self.flip_h)
        self.uiHandler.ui.flip_vertical_btn.clicked.connect(self.flip_v)


        self.uiHandler.ui.playback_camera_combo.currentTextChanged.connect(self.select_camera_event)
        self.uiHandler.ui.playback_combo_train_id.currentTextChanged.connect(self.select_train_event)
        self.uiHandler.timeLineSlider.timeSelected.connect(self.timline_change_event)
        
        self.archiveManager = archiveManager(pathConstants.SELF_UTILS_DIR)
        self.archiveManager.load()
        self.load_archive()
        
        self.uiHandler.ui.refresh_image_database_log.hide()
        self.uiHandler.setplaying_button(self.is_playing)


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
        if trains:        
            self.uiHandler.set_avaiable_trains(trains)
            self.select_train_event()
        else:
            print('No Train Detect')
    # def merge_dates(self,):
    #     for train in self.videos_avaiabilities:
    #         for cam in self.videos_avaiabilities[train]:
    #             self.videos_avaiabilities[train][cam] = transormUtils.dateTimeRanges(self.videos_avaiabilities[train][cam], 600)


    def select_train_event(self,):    
        train_id = self.uiHandler.get_selected_train()        
        if not train_id:
            return
        
        self.selected_train = train_id
        cameras = self.archiveManager.get_available_cameras(train_id)
        self.uiHandler.set_cameras(cameras)
        self.select_camera_event()

    def select_camera_event(self,):
        self.selected_camera = self.uiHandler.get_current_camera()
        if not self.selected_camera:
            return
        
        dates = self.archiveManager.get_avaiable_dates(self.selected_train, self.selected_camera)
        self.uiHandler.calendar_dialog.set_avaiable_date_ranges(dates)


    

    def date_select_event(self, date:JalaliDateTime):
        self.uiHandler.ui.playback_filter_frame.setDisabled(True)
        self.selected_date = date

        self.curent_video_idx = 0

        # self.uiHandler.set_load_video_progress(0)
        self.uiHandler.trainLoading.set_value(0)
        self.uiHandler.trainLoading.show()
        self.archiveManager.get_day_time_ranges(train_id=self.selected_train, 
                                                date=self.selected_date, 
                                                camera=self.selected_camera,
                                                finish_func=self.date_ranges_event, 
                                                progress_func=self.date_ranges_progress)


        

    
    
    

    def date_ranges_event(self, date_ranges:dict[str, list]):
        self.date_ranges = date_ranges
        self.uiHandler.ui.playback_filter_frame.setDisabled(False)
        start = JalaliDateTime.combine(self.selected_date, Time.min)
        end = start + timedelta(days=1)

        
        self.uiHandler.set_timelines(date_ranges['ranges'], start=start, end=end)
            
        #check if any video exists
        if len(date_ranges['paths']):
            self.Player.load_video(date_ranges['paths'][self.curent_video_idx])
            self.Player.update_frame()
            self.refreshing_ui(force=True)
        else:
            self.Player.load_video(None)

        
        self.is_playing = False
        self.uiHandler.setplaying_button(self.is_playing)
        

    
    def date_ranges_progress(self, value:float):
        value = int(value * 1000) #denormal
        self.uiHandler.trainLoading.set_value(value)

    def play_video(self,):

        if self.is_playing:
            self.is_playing = False
            self.Player.pause_video()
        else:
            self.Player.play_video()
            if self.Player.will_play():
                self.is_playing = True
        
        self.uiHandler.setplaying_button(self.is_playing)


    def pause_video(self,):
        self.Player.pause_video()

    def change_video_speed(self, ):
        speed = self.Player.change_speed()
        self.uiHandler.ui.speed_btn.setText(f'{speed}x')

    def rotate_video(self, direction):
        self.Player.rotate_video(90)
    
    def flip_h(self,):
        self.Player.toggle_flip_horizontal()

    def flip_v(self,):
        self.Player.toggle_flip_vertical()
    
    def refreshing_ui(self, force=False):
        if not self.date_ranges:
            return
        
        if self.Player.is_finished():
            #move to next video
            self.curent_video_idx+=1
            if self.curent_video_idx > len(self.date_ranges):
                self.curent_video_idx = 0
            
            
            self.Player.load_video(self.date_ranges['paths'][self.curent_video_idx])
            self.Player.play_video()


        if self.Player.is_playing() or force:
            sec = self.Player.get_time()
            start_datetime, end_datetime = self.date_ranges['ranges'][self.curent_video_idx]
            current_datetime:JalaliDateTime = start_datetime + timedelta(seconds=sec)
            
            self.uiHandler.timeLineSlider.set_time_by_jdatetime(current_datetime)

            time_string = current_datetime.strftime('%Y/%m/%d  %H:%M:%S')
            marquee_text = f"{self.selected_train} | {self.selected_camera} {time_string}"
            self.Player.update_marquee(marquee_text, position=6, font_size=48)
            self.uiHandler.ui.playback_time_label.setText(time_string)



    def timline_change_event(self, date_time:JalaliDateTime):
        date_ranges = self.date_ranges['ranges']
        paths = self.date_ranges['paths']

        prev_video_idx = self.curent_video_idx
        for i,(start, end) in enumerate(date_ranges):
            if start<=date_time<=end:
                self.curent_video_idx = i
                secs:timedelta = date_time - start
                secs = secs.total_seconds()
                #--------------------------------------------------------------
                if prev_video_idx == i:
                    #vidoe loaded befor we can use set_time function
                    self.Player.set_time(secs)
                else:
                    #video should load so we should use set_start_time function
                    self.Player.load_video(paths[self.curent_video_idx])
                    self.Player.set_start_time(secs)
                #--------------------------------------------------------------
                if self.is_playing:
                    self.Player.play_video()
                else:
                    self.Player.update_frame()
                break








    def show_export(self):

        if self.archiveManager is not None and self.selected_date is not None and self.selected_camera is not None and self.selected_train is not None:
            self.export_obj = UIExport(archive_manager = self.archiveManager, date=self.selected_date,train_name=self.selected_train,selected_camera=self.selected_camera)
            self.export_obj.ui.close_btn.clicked.connect(self.close_export)
            self.uiHandler.set_export_btn_mode(mode=True)
            self.export_window_is_open = True
            self.export_obj.show()
        
        else:
            self.uiHandler.show_message('Check Selected Date/Camera')

    def close_export(self):


        self.uiHandler.set_export_btn_mode(mode=False)
        self.export_window_is_open = False

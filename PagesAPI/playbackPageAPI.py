import threading


from PagesUI.playbackPageUI import playbackPageUI
from backend.database.mainDatabase import mainDatabase
from uiUtils.GUIComponents import MessageWidget
from Tranform.Network import pingWorker
from backend.utils.threadWorker import threadWorkers
from Tranform.sharingConstans import StatusCodes
from Mediator.mainMediator import Mediator
from Mediator.mediatorNames import eventNames
from Tranform.filesScanners import filesFinderWorker
from Tranform.sharingConstans import DIRECTORY_TREE
from Tranform.transformUtils import transormUtils
from pathConstans import pathConstants



class playbackPageAPI:
    def __init__(self, uiHandler:playbackPageUI, db:mainDatabase):
        self.uiHandler = uiHandler
        self.db = db
        self.mediator = Mediator()

        self.filesFinderThreadWorker = threadWorkers(None,None)
        self.videos_avaiabilities:dict[str, dict[str,list]] = {}

        self.uiHandler.ui.refresh_btn.clicked.connect(self.get_availability)
        self.uiHandler.ui.playback_combo_train_id.currentTextChanged.connect(self.select_train_event)
        # self.uiHandler.calendar_dialog.set_parent_function(self.calendar_day_click)        

        self.uiHandler.ui.refresh_image_database_log.hide()


    def get_availability(self,):
        if self.filesFinderThreadWorker.is_alive():
            return
        
        worker = filesFinderWorker(main_path=pathConstants.SELF_IMAGES_DIR,
                                   struct=DIRECTORY_TREE,
                                   trains=None,
                                   date_ranges=None,
                                   return_avaiability=True)
        worker.log_signal.connect(self.availability_logs_event)
        worker.finish_signal.connect(self.images_database_refresh_event)
        thread = threading.Thread(target=worker.run, daemon=True)
        self.filesFinderThreadWorker = threadWorkers(worker, thread)
        self.filesFinderThreadWorker.start()
    

    def availability_logs_event(self, txt):
        self.uiHandler.ui.refresh_image_database_log.show()
        txt = f'Founded:{txt}'
        self.uiHandler.ui.refresh_image_database_log.setText(txt)

    def images_database_refresh_event(self, status, res_paths, res_sizes, avaiabilities):
        self.uiHandler.ui.refresh_image_database_log.hide()
        
        if status == StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS:
            self.uiHandler.ui.refresh_image_db_message.show_message('Directory not found',
                                                                    msg_type='error',
                                                                    display_time=3000)
            
                
        elif status == StatusCodes.findFilesStatusCodes.SUCCESS:
            self.uiHandler.ui.refresh_image_db_message.show_message('Database updated',
                                                                    msg_type='success',
                                                                    display_time=2000)
            
            self.videos_avaiabilities = avaiabilities
            self.merge_dates()
            
            trains = list(self.videos_avaiabilities.keys())
            self.uiHandler.set_avaiable_trains(trains)

    def merge_dates(self,):
        for train in self.videos_avaiabilities:
            for cam in self.videos_avaiabilities[train]:
                self.videos_avaiabilities[train][cam] = transormUtils.dateTimeRanges(self.videos_avaiabilities[train][cam], 600)


    def select_train_event(self,):
        train_id = self.uiHandler.get_selected_train()
        
        dates = []
        for cam in self.videos_avaiabilities[train_id].keys():
            dates = dates + self.videos_avaiabilities[train_id][cam]
        
        self.uiHandler.calendar_dialog.set_avaiable_date_ranges(dates)
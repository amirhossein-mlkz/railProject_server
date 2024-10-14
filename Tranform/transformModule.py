import sys
import pickle
import time
import threading
import os



from persiantools.jdatetime import JalaliDateTime, timedelta
# from PySide6.QtCore import Signal, QObject

try:
    from Tranform.Network import pingAndCreateWorker
    from Tranform.Network import pingWorker, shareMapping
    from Tranform.transformUtils import transormUtils, timeRangeWorker
    from Tranform.sharingConstans import DIRECTORY_TREE, STRUCT_PARTS
    from Tranform.filesScanners import filesFinderWorker, updateArchiveWorker
    from Tranform.filesActionWorker import CopyWorker
    from Tranform.sharingConstans import StatusCodes
    

except:

    # from Network import pingWorker, shareMapping
    from transformUtils import transormUtils
    # from sharingConstans import DIRECTORY_TREE, STRUCT_PARTS
    # from filesScanners import filesFinderWorker
    # from filesActionWorker import CopyWorker




import subprocess


class transformModule:
    def __init__(self, 
                 ip:str, 
                 src_path:str, 
                 dst_path:str,
                 username:str,
                 password:str
                 ) -> None:
        self.ip = ip
        if self.ip is not None:

            

            self.src_path = transormUtils.build_share_path(ip, src_path)

            self.dst_path = dst_path
            self.username = username
            self.password = password


        else:
            self.src_path = src_path

            self.dst_path = None
            self.username = None
            self.password = None



        self.msg_callback = None

        self.ping_thread = None
        self.ping_worker = None

        self.searcher_thread = None
        self.searcher_worker = None

        self.move_flag = False
        



    def check_connection(self, event_func, ):
        # self.ping_worker = pingWorker(self.ip, self.username, self.password)
        self.ping_worker = pingWorker(self.ip)
        self.ping_worker.result_signal.connect(event_func)
        self.ping_thread = threading.Thread(target=self.ping_worker.run, daemon=True)
        self.ping_thread.start()

    

    def check_connection_and_create_connection(self,event_func):



        self.ping_worker = pingAndCreateWorker(self.ip,self.src_path,self.username,self.password)
        self.ping_worker.result_signal.connect(event_func)
        self.ping_thread = threading.Thread(target=self.ping_worker.run, daemon=True)
        self.ping_thread.start()
        


    def find_files(self, trains, dates_tange, finish_event_func, log_event_func=None,log_search=False):
        
        
        self.searcher_worker = filesFinderWorker(self.src_path,
                                                 trains=trains,
                                                 date_ranges=dates_tange,
                                                 struct=DIRECTORY_TREE,
                                                 log_search=log_search)
        if log_event_func is not None:
            self.searcher_worker.log_signal.connect(log_event_func)

        self.searcher_worker.finish_signal.connect(finish_event_func)
        self.searcher_thread = threading.Thread( target=self.searcher_worker.run, daemon=True )
        self.searcher_thread.start()
        
    def start_copy(self, paths:list[str], sizes:list[int], finish_func, speed_func, progress_func, msg_callback, move=False):
        # a = transormUtils.dateTimeRanges( avaiabilities['11BG21']['right'], 600 )
        self.copy_worker = CopyWorker(self.src_path,
                                      dst_path=self.dst_path,
                                      files_paths=paths,
                                      sizes=sizes,
                                      move=move
                                      )
        
        self.copy_worker.log_signal.connect(msg_callback)
        self.copy_worker.progress_signal.connect(progress_func)
        self.copy_worker.speed_singnal.connect(speed_func)
        self.copy_worker.finish_signal.connect(finish_func)
        self.copy_thread = threading.Thread( target=self.copy_worker.run, daemon=True )
        self.copy_thread.start()
        





class archiveManager:
    FILE_NAME = 'archive.molmal'
    def __init__(self, db_dir):
        self.db_path = os.path.join(db_dir, self.FILE_NAME)
        
        self.archive = None

        self.update_worker = None
        self.update_thread:threading.Thread = None

        self.time_range_worker = None
        self.time_range_thread:threading.Thread = None
        self.external_update_finish_func = None

        

    def update_archive(self,src_path, finish_func, log_func=None):        
        self.external_update_finish_func = finish_func

        self.update_worker = updateArchiveWorker(src_path, DIRECTORY_TREE)
        self.update_worker.finish_signal.connect(self.__update_archive_finish)

        if log_func is not None:
            self.update_worker.log_signal.connect(log_func)
        
        self.update_thread = threading.Thread(target=self.update_worker.run, daemon=True)
        self.update_thread.start()
    
    def is_during_updating(self):
        if self.update_thread is None:
            return False
        
        if self.update_thread.is_alive():
            return True
        else:
            return False
    
    def __update_archive_finish(self, status_code:int, archive:dict[str,dict[str, dict[str, dict[str, dict]]]]):
        if status_code == StatusCodes.findFilesStatusCodes.SUCCESS:
            self.archive = archive
            self.save()

        if self.external_update_finish_func is not None:
            self.external_update_finish_func(status_code)

    def get_day_time_ranges(self, train_id, date:JalaliDateTime, cameras, finish_func, progress_func):
        if self.time_range_thread is not None and self.time_range_thread.is_alive():
            return
        
        self.time_range_worker = timeRangeWorker(self.archive, train_id, date, cameras)
        self.time_range_worker.finish_signal.connect(finish_func)
        self.time_range_worker.progress_signal.connect(progress_func)
        self.time_range_thread = threading.Thread(target=self.time_range_worker.run, daemon=True)
        self.time_range_thread.start()

    
    def get_available_trains(self,):
        return list( self.archive.keys())
    
    def get_available_cameras(self, train_id:str):
        return list( self.archive[train_id].keys())
    
    def get_avaiable_dates(self, train_id:str):
        res = {}
        if train_id not in self.archive:
            return {}
        
        for camera in self.archive[train_id].keys():
            dates = self.archive[train_id][camera].keys()
            dates = list(
                map( lambda x:JalaliDateTime.strptime(x, '%Y-%m-%d').jdate(), dates)
            )
            res[camera] = dates
        return res

        
    def load(self,):
        if not os.path.exists(self.db_path):
            return False
        try:
            with open(self.db_path, 'rb') as f:
                self.archive = pickle.load(f)
            return True
        except Exception as e:
            print(e)
            return False

    def save(self,):
        _dir,_ = os.path.split(self.db_path)
        if not os.path.exists(_dir):
            os.makedirs(_dir)

        #remove old file
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        try:
            with open(self.db_path, 'wb') as f:
                pickle.dump(self.archive, f)
            return True
        except Exception as e:
            return False




if __name__=='__main__':
    from PySide6.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)


    # nmap = shareMapping('','','')
    # drives = nmap.get_mapped_drives()
    # res = nmap.check_drived_is_mapped('192.168.1.60')
    # if res is None and False:
    #     nmap.map_network('192.168.1.60','image_share',username='rail',password= '1', )
    
    
    # def msg_callback1(txt):
    #     print(txt)

    ip = '192.168.43.63'                    # IP address of the remote system
    share_path = 'test'                      # Shared folder on the remote system
    username = "MMM"                         # Your username
    password = "PHK"   


    obj = transformModule(ip=ip,src_path='test',dst_path='asd',username=username,password=password)
    ret = obj.create_connection()
    print(ret)
    app.exec()
    
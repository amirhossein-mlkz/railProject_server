import os
import sys
import time
import threading
import shutil

from PySide6.QtCore import QObject, Signal

from persiantools.jdatetime import JalaliDateTime , timedelta
import dorsa_logger

class Space:
    def __init__(self, bytes) -> None:
        self.bytes = int(bytes)

    def toGB(self,):
        return round(self.bytes / pow(1024,3),2)
    
    def toMB(self,):
        return round(self.bytes / pow(1024,2),2)
    
    def toKB(self,):
        return round(self.bytes / pow(1024,1),2)
    
    def toByte(self,):
        return self.bytes
    
    def __add__(self, other):
        return Space(self.bytes + other.bytes)
    
    def __sub__(self, other):
        return Space(self.bytes - other.bytes)
    
    def __eq__(self, other):
        return self.bytes == other.bytes

    def __lt__(self, other):
        return self.bytes < other.bytes

    def __gt__(self, other):
        return self.bytes > other.bytes


    def __str__(self) -> str:
        return f'GB: {self.toGB()}'
    







class storageManager(QObject):

    finish_cleaning_signal = Signal(str, bool)
    progress_signal = Signal(str,str, Space, Space)
    stop_signal = Signal()

    def __init__(self, path, logs_path, max_usage=0.8,  max_log_count=100, logger:None|dorsa_logger.logger=None) -> None:
        super().__init__()
        """if cleaning_evry_sec be negative, storageMnage run one time
        """

        self.path = path
        self.logs_path = logs_path
        self.max_log_count = max_log_count
        self.max_usage = max_usage
        self.logger = logger
        self.__is_running = True
        self.clean_requsts = []
    
    def set_max_usage(self, max_usage):
        self.max_usage = max_usage

    
    def get_disk_usage(self, path):
        total, used, free = shutil.disk_usage(path)
        total = Space(total)
        used = Space(used)
        free = Space(free)
        max_allowed = Space( total.toByte() * self.max_usage)
        return total, used, free, max_allowed
    
    def has_enough_space_for(self, size:Space):
        total, used, free, max_allowed = self.get_disk_usage(self.path)
        final_used = used + size
        if final_used < max_allowed:
            return True
        else:
            return False
        
    def has_enough_space_for_files(self, files_path:list[str], sizes:list[int], src_dir=None, dst_dir=None)-> tuple[bool, Space]:
        files_path_after_download = files_path.copy()
        sizes = sizes.copy()
        if src_dir is not None and dst_dir is not None:
            files_path_after_download = list(map( lambda x: x.replace(src_dir, dst_dir),
                                                 files_path_after_download))
            
            
            
        #check for duplicate files
        for i, path in enumerate(files_path_after_download):
            if os.path.exists(path):
                exist_size = os.path.getsize(path)
                sizes[i] = sizes[i] - exist_size

        total_need_size = sum(sizes)
        total_need_size = Space(total_need_size)
        total, used, free, max_allowed = self.get_disk_usage(self.path)
        final_used = used + total_need_size
        if final_used < max_allowed:
            return True, Space(0)
        else:
            return False, total_need_size
    
    def send_clean_request(self, name:str, size:Space):
        self.clean_requsts.append( {'name':name, 'size':size} )
    

    def remove_empty_dirs(self, directory, depth):
        is_empty = True
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            
            if os.path.isdir(item_path):
                if not self.remove_empty_dirs(item_path, depth+1):
                    is_empty = False 
            else:
                is_empty = False
        
        if is_empty and depth > 0:
            os.rmdir(directory)
            #-----------------------------------------------------------
            if self.logger is not None:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"remove empty folder {directory}", 
                                            code="SMRED000")
                self.logger.create_new_log(message=log_msg)
            #-----------------------------------------------------------
            return True
        else:
            return False
        
    def remove_logs(self,):
        if self.logs_path is None:
            return
        
        logs = []
        for day_folder in os.listdir(self.logs_path):
            day_log_path = os.path.join(self.logs_path, day_folder)
            for fname in os.listdir(day_log_path):
                slog_path = os.path.join(day_log_path, fname)
                logs.append(slog_path)

        logs.sort()
        #-----------------------------------------------------------
        if self.logger is not None:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"found {len(logs)} logs", 
                                            code="SMRL000")
            self.logger.create_new_log(message=log_msg)
        #-----------------------------------------------------------
        
        if len(logs)> self.max_log_count:
            #-----------------------------------------------------------
            if self.logger is not None:
                log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"start remove logs", 
                                            code="SMRL001")
                self.logger.create_new_log(message=log_msg)
            #-----------------------------------------------------------

            for log_path in logs[:-self.max_log_count]:                
                #-----------------------------------------------------------
                if self.logger is not None:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"try remove log {log_path}", 
                                            code="SMRL002")
                    self.logger.create_new_log(message=log_msg)
                #----------------------------------------------------------

                try:
                    os.remove(log_path)
                except Exception as e:
                    #-----------------------------------------------------------
                    if self.logger is not None:
                        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                            text=f"error occur during remove log {log_path}: {e}", 
                                                            code="SMRL003")
                        self.logger.create_new_log(message=log_msg)
                    #----------------------------------------------------------





            
    

    def __sort_file_number(self, files:list[str]):
        def key(x):
            try:
                return int(x)
            except:
                return 0
        files.sort(key=key)
        return files


    def get_oldets_files(self, path, n=1) -> list[list[str]]:
        results = []
        for train in os.listdir(path):
            train_path = os.path.join(self.path, train)
            if not os.path.isdir(train_path):
                continue

            for cam in os.listdir(train_path):
                cam_path = os.path.join(train_path, cam)
                if not os.path.isdir(cam_path):
                    continue
                
                years = os.listdir(cam_path)
                years = self.__sort_file_number(years)

                last_hours_paths_per_cam = []

                for year in years:
                    year_path = os.path.join(cam_path, year)
                    if not os.path.isdir(year_path):
                        continue
                    months = os.listdir(year_path)
                    months = self.__sort_file_number(months)
                    for month in months:
                        month_path = os.path.join(year_path, month)
                        if not os.path.isdir(month_path):
                            continue
                        days = os.listdir(month_path)
                        days = self.__sort_file_number(days)
                        for day in days:
                            day_path = os.path.join(month_path, day)
                            if not os.path.isdir(day_path):
                                continue
                            hours = os.listdir(day_path)
                            hours = self.__sort_file_number(hours)

                            for hour in hours:
                                houre_path = os.path.join(day_path, hour)
                                if not os.path.isdir(houre_path):
                                    continue
                                last_hours_paths_per_cam.append(houre_path)
                                if len(last_hours_paths_per_cam) >= n:
                                    break
                            if len(last_hours_paths_per_cam) >= n:
                                break
                        if len(last_hours_paths_per_cam) >= n:
                                break
                    if len(last_hours_paths_per_cam) >= n:
                                break
                
                results.append(last_hours_paths_per_cam)
        return results
                
                
    def remove(self, path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)

    def stop(self,):
        self.__is_running = False


    def run(self,):
        #-----------------------------------------------------------
        if self.logger is not None:
            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                            text=f"StorageManager thread run", 
                                            code="SMR000")
            self.logger.create_new_log(message=log_msg)
        #-----------------------------------------------------------

        while self.__is_running:
            try:
                total, used, free, max_allowed= self.get_disk_usage(self.path)

                aditional_space = Space(0)
                name = ''
                if len(self.clean_requsts):
                    aditional_space = self.clean_requsts[0]['size']
                    name = self.clean_requsts[0]['name']
                
                used = aditional_space  + used
                #-----------------------------------------------------------
                if self.logger is not None:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                    text=f"total: {total.toGB()} ---- used: {used.toGB()} ---- free:{free.toGB()}  ----- allowed: {max_allowed.toGB()}", 
                                                    code="SMR002")
                    self.logger.create_new_log(message=log_msg)
                #-----------------------------------------------------------
                total_should_clean = max(used - max_allowed, Space(0))

                while used > max_allowed and self.__is_running:
                    #-----------------------------------------------------------
                    if self.logger is not None:
                        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                    text=f"storage need cleaning", 
                                                    code="SMR003")
                        self.logger.create_new_log(message=log_msg)
                    #-----------------------------------------------------------
                    
                    try:
                        res = self.get_oldets_files(self.path, 1) #get first 50 hours folder of each camera
                        #-----------------------------------------------------------
                        if self.logger is not None:
                            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                    text=f"oldest files: {res}", 
                                                    code="SMR004")
                            self.logger.create_new_log(message=log_msg)
                        #-----------------------------------------------------------
                    except Exception as e:
                        #-----------------------------------------------------------
                        if self.logger is not None:
                            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR,
                                                    text=f"ERROR Happend in storage Manger get_oldest_files: {e}", 
                                                    code="SMR005")
                            self.logger.create_new_log(message=log_msg)
                        #-----------------------------------------------------------
                        break
                    
                    #is_any_file_to_remove flag show is there any files to remove or storage is full beacuse of other files in system
                    is_any_file_to_remove = False
                    for camera_last_hours in res:
                        if len(camera_last_hours):
                            is_any_file_to_remove = True

                        for path in camera_last_hours:
                            try:
                                #-----------------------------------------------------------
                                if self.logger is not None:
                                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                    text=f"storageManager try remove {path}", 
                                                    code="SMR006")
                                    self.logger.create_new_log(message=log_msg)
                                #-----------------------------------------------------------
                                self.remove(path)
                                
                                self.progress_signal.emit( name, 
                                                           path,
                                                           used - max_allowed, 
                                                           total_should_clean)
                                
                                #-----------------------------------------------------------
                                if self.logger is not None:
                                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                    text=f"success remove {path}", 
                                                    code="SMR007")
                                    self.logger.create_new_log(message=log_msg)
                                #-----------------------------------------------------------
                            except Exception as e:
                                #-----------------------------------------------------------
                                if self.logger is not None:
                                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR,
                                                    text=f"storageManager remove failed: {e}", 
                                                    code="SMR008")
                                    self.logger.create_new_log(message=log_msg)
                                #-----------------------------------------------------------   

                    if not is_any_file_to_remove:
                        #-----------------------------------------------------------
                        if self.logger is not None:
                            log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.WARNING,
                                                            text=f"there is not any file to remove this means storge is full beacuse of other files", 
                                                            code="SMR009")
                            self.logger.create_new_log(message=log_msg)
                        #-----------------------------------------------------------
                        break
                    total, used, free, max_allowed= self.get_disk_usage(self.path)
                    used = used + aditional_space
                    
                
                    #end while remove
                #-------------------------------------------------------------------------------------------
                total, used, free, max_allowed= self.get_disk_usage(self.path)
                used = used + aditional_space

                
                #-----------------------------------------------------------
                if self.logger is not None:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.DEBUG,
                                                    text=f"Statistics after cleaning: total: {total.toGB()} ---- used: {used.toGB()} ---- free:{free.toGB()}  ----- allowed: {max_allowed.toGB()}", 
                                                    code="SMR010")
                    self.logger.create_new_log(message=log_msg)
                #-----------------------------------------------------------
                #-------------------------------------------------------------------------------------------
                try:
                    self.remove_empty_dirs(self.path, 0)
                except Exception as e:
                    #-----------------------------------------------------------
                    if self.logger is not None:
                        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR,
                                                        text=f"error happend in cleaning empty folders: {e}", 
                                                        code="SMR011")
                        self.logger.create_new_log(message=log_msg)
                    #-----------------------------------------------------------

                try:
                    self.remove_empty_dirs(self.logs_path,0)
                except Exception as e:
                    #-----------------------------------------------------------
                    if self.logger is not None:
                        log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR,
                                                        text=f"error happend in cleaning empty folders logs: {e}", 
                                                        code="SMR011")
                        self.logger.create_new_log(message=log_msg)
                    #-----------------------------------------------------------

                #-------------------------------------------------------------------------------------------
                self.remove_logs()
                #-------------------------------------------------------------------------------------------


            except Exception as e:
                #-----------------------------------------------------------
                if self.logger is not None:
                    log_msg = dorsa_logger.log_message(level=dorsa_logger.log_levels.ERROR,
                                                    text=f"error happend in StorageManager: {e}", 
                                                    code="SMR012")
                    self.logger.create_new_log(message=log_msg)
                #-----------------------------------------------------------
            total, used, free, max_allowed= self.get_disk_usage(self.path)
            used = used + aditional_space

            if len(self.clean_requsts) > 0:
                request = self.clean_requsts.pop()
                if used.bytes <= max_allowed.bytes:
                    self.finish_cleaning_signal.emit(request['name'], True)
                else:
                    self.finish_cleaning_signal.emit(request['name'], False)
        
            time.sleep(1)
            


if __name__ == '__main__':
    sm = storageManager('C:\image_share', max_usage=0.17)
    sm.daemon = True
    sm.start()
    while True:
        pass
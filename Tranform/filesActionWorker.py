import time
import os
import shutil

from persiantools.jdatetime import JalaliDateTime, timedelta
from PySide6.QtCore import Signal, QObject
from Tranform.sharingConstans import StatusCodes



class CopyWorker(QObject):
    progress_signal = Signal(int, int)
    speed_singnal = Signal(int)
    log_signal = Signal(str)
    finish_signal = Signal(int)
    error_signal = Signal(str)

    def __init__(self, src_path, dst_path, files_paths:list[str], sizes:list[int], move = False):
        super().__init__()
        self.src_path = src_path
        self.dst_path = dst_path
        self.files_paths = files_paths
        self.sizes = sizes
        self.move = move
        self.speeds = []


    def run(self):
        total = sum(self.sizes)
        total = int(total/(1024**2))
        total_copied = 0
        self.speeds = []

        self.log_signal.emit('Start Copy')
        self.progress_signal.emit(0, total)

        time.sleep(0.5)

        for i in range(len(self.files_paths)):
            t = time.time()

            file_src_path = self.files_paths[i]
            file_dst_path = file_src_path.replace(self.src_path, self.dst_path)
            file_dst_dir, fname = os.path.split(file_dst_path)

            if not os.path.exists(file_dst_dir):
                os.makedirs(file_dst_dir)

            self.log_signal.emit(f'Copy {fname}')

            try:
                if self.move:
                    shutil.move(file_src_path, file_dst_path)

                else:
                    shutil.copy2(file_src_path, file_dst_path)

                t = time.time() - t
                self.calc_speed(self.sizes[i], t)
            
            except Exception as e:
                #if src path not exist means 
                if not os.path.exists(self.src_path):
                    self.finish_signal.emit(StatusCodes.copyStatusCodes.DISCONNECT)
                    return
                print(e)
                self.log_signal.emit(f'Failed Copy {fname}: {e}')
                

            
            
            total_copied += self.sizes[i]
            self.progress_signal.emit(int(total_copied/(1024**2)), total)
        
        else:
            self.log_signal.emit(f'Finish Success')
        
        self.finish_signal.emit(StatusCodes.copyStatusCodes.SUCCESS)


    def calc_speed(self, size, t, avg=5):
        speed = int(size / t)
        self.speeds.append(speed)
        if len(self.speeds)>avg:
            self.speeds.pop(0)
        
        curent_speed = int( sum(self.speeds) / len(self.speeds) )
        self.speed_singnal.emit(curent_speed)
        return curent_speed
    



class removeWorker(QObject):
    progress_signal = Signal(int, int)
    speed_singnal = Signal(int)
    log_signal = Signal(str)
    finish_signal = Signal()
    error_signal = Signal(str)

    def __init__(self,main_path, files_paths, sizes,):
        super().__init__()
        self.files_paths = files_paths
        self.main_path = main_path
        self.sizes = sizes
        self.speeds = []
        


    def run(self):
        self.speeds = []

        self.log_signal.emit('Start Removing Old datas')
        time.sleep(0.5)

        self.remove_files(self.files_paths, self.sizes)
        self.log_signal.emit('Old Files Removed')
        time.sleep(1)

        self.log_signal.emit('Start Removing Empty Folders')
        self.remove_empty_dirs(self.main_path)
        self.log_signal.emit(f'Finish Success')
        self.finish_signal.emit()


    
    def remove_files(self, files_paths, sizes):
        total = sum(sizes)
        total_removed = 0

        for i in range(len(files_paths)):
            t = time.time()

            path = files_paths[i]
            dir, fname = os.path.split(path)


            self.log_signal.emit(f'Remove {fname}')

            try:
                os.remove(path)
                t = time.time() - t
                self.calc_speed(sizes[i], t)
            
            except Exception as e:
                print(e)
                self.log_signal.emit(f'Failed Remove {fname}: {e}')
            
            total_removed += sizes[i]
            self.progress_signal.emit(total_removed, total)

    def remove_empty_dirs(self, directory):
        is_empty = True
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            
            if os.path.isdir(item_path):
                if not self.remove_empty_dirs(item_path):
                    is_empty = False  
            else:
                is_empty = False 
        
        if is_empty:
            self.log_signal.emit(f'Remove {directory}')
            os.rmdir(directory)
            return True  
        else:
            return False 
        
    def calc_speed(self, size, t, avg=5):
        speed = int(size / t)
        self.speeds.append(speed)
        if len(self.speeds)>avg:
            self.speeds.pop(0)
        
        curent_speed = int( sum(self.speeds) / len(self.speeds) )
        self.log_signal.emit('Removing Empty Directories')
        self.speed_singnal.emit(curent_speed)
        return curent_speed
    
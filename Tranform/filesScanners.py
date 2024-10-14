import os
import threading
import time
import pickle


from persiantools.jdatetime import JalaliDateTime, timedelta
from PySide6.QtCore import Signal, QObject

from Tranform.transformUtils import transormUtils
from Tranform.sharingConstans import DIRECTORY_TREE, STRUCT_PARTS, StatusCodes


class filesFinderWorker(QObject):
    #this class returns list of files that pass filters

    finish_signal = Signal(int, list, list)#status_code, paths, sizes, availability
    log_signal = Signal(str)
    def __init__(self, 
                 main_path:str, 
                 struct:list[str],
                 trains:list[str] = None, 
                 date_ranges:tuple[JalaliDateTime] = None,
                 log_search = False) -> None:
        super().__init__()    
        self.trains = trains
        self.date_ranges = date_ranges
        self.temp_date_ranges = None
        if date_ranges is not None:
            self.temp_date_ranges = date_ranges[0], date_ranges[1]
        self.main_path = main_path
        self.struct = struct
        self.log_search = log_search
        #choose filter trains by folder name or by directory name
        # self.check_train_by_filename = True
        # if STRUCT_PARTS.TRAIN in self.struct:
        #     self.check_train_by_filename = False


    def __init_flags(self,):
        self.is_train_checked = False
        self.is_year_checked = False
        self.is_month_checked = False
        self.is_day_checked = False
        self.is_hour_checked = False
        self.is_minute_checked = False
        
  

    def run(self, ):
        if not os.path.exists(self.main_path):
            # self.log_signal.emit('Directory not Exist')
            self.finish_signal.emit(StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS, 
                                    [], 
                                    [], 
                                    )
            return
        self.__init_flags()
        self.res_paths = []
        self.res_sizes = []
        self.total_size = 0
        self.searcher(self.main_path, pos_index=0)
        self.finish_signal.emit(StatusCodes.findFilesStatusCodes.SUCCESS,
                                self.res_paths, 
                                self.res_sizes, 
        )

    def __sort_number_folder(self, names:list[str]):
        def key_func(x:str):
            if x.isdigit():
                return int(x)
            else:
                return 10*6
        
        names.sort(key=key_func)
        return names

    def searcher(self, path, pos_index, date=None):
        #pos_index show we are in which level of directory
        if pos_index >= len(self.struct):
            return
        

        step_name = self.struct[pos_index]
        subs = os.listdir(path)
        if not self.log_search:
            if step_name in [STRUCT_PARTS.YEAR,STRUCT_PARTS.MONTH,STRUCT_PARTS.DAY,STRUCT_PARTS.HOUR,STRUCT_PARTS.MINUTE]:
                subs = self.__sort_number_folder(subs)

        if not self.log_search:
            for sub in subs:
                sub_path = os.path.join(path, sub)
                #check if we arent in last level of tree
                if pos_index != (len(self.struct) -1):
                    if not os.path.isdir(sub_path):
                        continue
                else:
                    if not os.path.isfile(sub_path):
                        continue
                #-----------------------------------
                flag, date = self.check_filters(path, sub, step_name, date)

                if flag:
                    if pos_index == (len(self.struct) -1):
                        size = os.path.getsize(sub_path)
                        self.res_paths.append(sub_path)
                        self.res_sizes.append(size)
                        self.total_size += size
                        self.log_signal.emit(f'Size f{int(self.total_size)}')
                    else:
                        self.searcher(sub_path, pos_index+1, date)
                        
        else:
            if os.path.exists(path):
                for sub in subs:
                    sub_path = os.path.join(path, sub)
                    if os.path.exists(sub_path):
                        for log_name in os.listdir(sub_path):
                            new_path = os.path.join(sub_path,log_name)
                            self.res_paths.append(new_path)
                            size = os.path.getsize(new_path)
                            self.res_sizes.append(size)
                            self.total_size += size
                            self.log_signal.emit(f'Size f{int(self.total_size)}')


    

    def check_filters(self, dir:str, sub:str, step_name:str, date:JalaliDateTime):
        if step_name == STRUCT_PARTS.TRAIN:
            self.is_train_checked = True
            if self.trains is None:
                return True, date
            if sub in self.trains:
                return True, date
            return False, date
        #------------------------------check year------------------------- 
        elif step_name == STRUCT_PARTS.YEAR:
            self.is_year_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            year = int(sub)
            if self.date_ranges[0].year <= year <= self.date_ranges[1].year:
                date = JalaliDateTime(year,month=1,day=1)
                start_date = JalaliDateTime(self.date_ranges[0].year,month=1,day=1, hour=0,minute=0)
                last_day =  transormUtils.last_day_of_month(self.date_ranges[1].year, 12)
                end_date = JalaliDateTime(self.date_ranges[1].year,month=12,day=last_day, hour=23, minute=59)
                self.temp_date_ranges = (start_date, end_date)
                return True, date
            else:
                return False, date
        #------------------------------check month-------------------------
        elif step_name == STRUCT_PARTS.MONTH:
            #we coudnt check month if year dose not check befor
            if not( self.is_year_checked):
                return True, date
            
            self.is_month_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            
            month = int(sub)
            date = date.replace(month=month)
            last_day =  transormUtils.last_day_of_month(self.date_ranges[1].year, self.date_ranges[1].month)
            start_date = self.temp_date_ranges[0].replace( month=self.date_ranges[0].month, day=1, hour=0, minute=0)
            end_date = self.temp_date_ranges[1].replace( month=self.date_ranges[1].month, day=last_day, hour=23, minute=59)
            self.temp_date_ranges = start_date, end_date
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:                
                return True, date
            else:
                return False, date
        
        #------------------------------check day-------------------------
        elif step_name == STRUCT_PARTS.DAY:
            #we coudnt check day if year and month dose not check befor
            if not( self.is_year_checked and
                    self.is_month_checked):
                return True, date
            
            self.is_day_checked = True
            if self.date_ranges is None:

                return True, date
            if not sub.isdigit():
                return False, date
            
            day = int(sub)
            date = date.replace(day=day)
            start_date = self.temp_date_ranges[0].replace( day=self.date_ranges[0].day, hour=0, minute=0)
            end_date = self.temp_date_ranges[1].replace( day=self.date_ranges[1].day, hour=23, minute=59)
            self.temp_date_ranges = (start_date, end_date)
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:
                
                return True, date
            else:
                return False, date
            
        #------------------------------check hour-------------------------
        elif step_name == STRUCT_PARTS.HOUR:
            #we couldnt check day if year and month dose not check befor
            if not( self.is_year_checked and
                    self.is_month_checked and
                    self.is_day_checked):
                return True, date
            
            self.is_hour_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            
            hour = int(sub)
            date = date.replace(hour=hour)
            start_date = self.temp_date_ranges[0].replace( hour=self.date_ranges[0].hour, minute=0)
            end_date = self.temp_date_ranges[1].replace( hour=self.date_ranges[1].hour, minute=59)
            self.temp_date_ranges = (start_date, end_date)
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:
                return True, date
            else:
                return False, date
            
        #------------------------------check minute-------------------------
        elif step_name == STRUCT_PARTS.MINUTE:
            #we couldnt check day if year and month dose not check befor
            if not( self.is_year_checked and
                    self.is_month_checked and
                    self.is_day_checked and
                    self.is_hour_checked):
                return True, date
            
            self.is_minute_checked = True
            if self.date_ranges is None:
                return True, date
            if not sub.isdigit():
                return False, date
            
            minute = int(sub)
            date = date.replace(minute=minute)
            start_date = self.temp_date_ranges[0].replace( minute=self.date_ranges[0].minute)
            end_date = self.temp_date_ranges[1].replace( minute=self.date_ranges[1].minute)
            self.temp_date_ranges = (start_date, end_date)
            if self.temp_date_ranges[0] <= date <= self.temp_date_ranges[1]:
                
                return True, date
            else:
                return False, date
        #------------------------------check FILE-------------------------
         
        elif step_name == STRUCT_PARTS.FILE:
            if self.date_ranges is None and self.trains is None:
                return True, date
            
            date, train_id, camera = transormUtils.extract_file_name_info(sub)            

            
            if self.trains is not None:
                if not self.is_train_checked:
                    if train_id not in self.trains:
                        return False, date
                
            if self.date_ranges is not None:
                if not (self.is_year_checked and
                        self.is_month_checked and
                        self.is_day_checked and
                        self.is_hour_checked and
                        self.is_minute_checked):
                    if not( self.date_ranges[0] <= date <= self.date_ranges[1] ):
                        return False, date
            
            return True, date
        
        else:
            return True, date
        










class updateArchiveWorker(QObject):
    #this class returns list of files that pass filters

    finish_signal = Signal(int, dict)#status_code, paths, sizes, availability
    log_signal = Signal(str)
    def __init__(self, 
                 main_path:str, 
                 struct:list[str],
                 ) -> None:
        super().__init__()    
        
        self.main_path = main_path
        self.struct = struct


    def run(self, ):
        if not os.path.exists(self.main_path):
            # self.log_signal.emit('Directory not Exist')
            self.finish_signal.emit(StatusCodes.findFilesStatusCodes.DIR_NOT_EXISTS, 
                                    {})
            return
        self.avaiabilities:dict[str, dict[str, dict[str, list]]] = {} #train -> camera -> date_str ->  [dates ranges]
        
        self.searcher(self.main_path, pos_index=0)
        self.finish_signal.emit(StatusCodes.findFilesStatusCodes.SUCCESS,
                                self.avaiabilities)

    def __sort_number_folder(self, names:list[str]):
        def key_func(x:str):
            if x.isdigit():
                return int(x)
            else:
                return 10*6
        
        names.sort(key=key_func)
        return names

    def searcher(self, dir, pos_index,):
        #pos_index show we are in which level of directory
        if pos_index >= len(self.struct):
            return
        

        step_name = self.struct[pos_index]
        subs = os.listdir(dir)
        if step_name in [STRUCT_PARTS.YEAR,STRUCT_PARTS.MONTH,STRUCT_PARTS.DAY,STRUCT_PARTS.HOUR,STRUCT_PARTS.MINUTE]:
            subs = self.__sort_number_folder(subs)

        for sub in subs:
            sub_path = os.path.join(dir, sub)
            #check if we arent in last level of tree
            if pos_index != (len(self.struct) -1):
                if not os.path.isdir(sub_path):
                    continue
            else:
                if not os.path.isfile(sub_path):
                    continue
            #-----------------------------------

            if step_name == STRUCT_PARTS.FILE:
                self.log_signal.emit(f'Findes: {sub}')
                self.append_to_avaiability(sub_path, sub)
            
            if pos_index < len(self.struct):
                self.searcher(sub_path, pos_index+1)
                        

    

    def append_to_avaiability(self, path:str, fname:str):
        date_time, train_id, camera = transormUtils.extract_file_name_info(fname)
        date_str = date_time.strftime('%Y-%m-%d')
        time_str = date_time.strftime('%H-%M-%S')
        
        
        if train_id not in self.avaiabilities:
            self.avaiabilities[train_id] = {}
            
        if camera not in self.avaiabilities[train_id]:
            self.avaiabilities[train_id][camera] = {}
        
        if date_str not in self.avaiabilities[train_id][camera]:
            self.avaiabilities[train_id][camera][date_str] = {}
        
        if time_str not in self.avaiabilities[train_id][camera][date_str]:
            self.avaiabilities[train_id][camera][date_str][time_str] = {}

            
        self.avaiabilities[train_id][camera][date_str][time_str] = {
            'path':path,
            'datetime':date_time
        }
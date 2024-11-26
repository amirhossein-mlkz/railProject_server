import time

from PySide6.QtCore import QObject, Signal
from datetime import datetime, timedelta

class timerThread(QObject):
    finish_signal = Signal()
    counter_signal = Signal(int)

    def __init__(self, t:int, sleep_time=1, name='') -> None:
        super().__init__()
        self.time = t
        self.pass_time = 0
        self.sleep_time = sleep_time
        self.name = name
        self.__start_time = 0
        self.__running_flag = True

    
    def stop(self,):
        self.__running_flag = False


    def get_pass_time(self,):
        return self.pass_time
    

    def run_single(self,):
        self.__running_flag = True
        self.__start_time = time.time()
        self.pass_time = 0
        while  self.pass_time < self.time:
            time.sleep(self.sleep_time)
            self.pass_time = time.time() - self.__start_time
            self.counter_signal.emit( self.pass_time )
            if not self.__running_flag:
                break
        
        if self.__running_flag:
            self.finish_signal.emit()

    
    def run_loop(self,):
        while True:
            self.__running_flag = True
            self.__start_time = time.time()
            self.pass_time = 0
            while  self.pass_time < self.time:
                time.sleep(self.sleep_time)
                self.pass_time = time.time() - self.__start_time
                self.counter_signal.emit( self.pass_time )
                if not self.__running_flag:
                    break
        
            if self.__running_flag:
                self.finish_signal.emit()


    def reset(self,):
        self.__start_time = time.time()



class recurringThreadTimer(QObject):
    finish_signal = Signal()
    counter_signal = Signal(int)

    def __init__(self,recurring_timer , min_time = 0, limit_timer=0, sleep_time=1, name='') -> None:
        assert limit_timer > recurring_timer or limit_timer==0, "limit timer should be greater than recurring_timer"
        super().__init__()
        
        self.name = name
        self.recurring_timer = recurring_timer
        self.limit_timer = limit_timer
        self.min_time = min_time
        self.sleep_time = sleep_time
        self.__start_time = 0
        self.__running_flag = True


    def run_single(self,):
        self.__start_time = time.time()
        pass_time = 0
        total_pass_time = 0
        self.__running_flag = True
        self.__start_time_fix = self.__start_time

        while  pass_time < self.recurring_timer or total_pass_time < self.min_time:
            # print(pass_time, total_pass_time)
            time.sleep(self.sleep_time)
            t = time.time()
            total_pass_time = t - self.__start_time_fix
            pass_time = t - self.__start_time

            self.counter_signal.emit( total_pass_time )
            if not self.__running_flag:
                #break and no emit signal
                break

            if self.limit_timer!=0 and total_pass_time > self.limit_timer:
                #break and emit signal
                break
        
        if self.__running_flag:
            self.finish_signal.emit()

    def stop(self,):
        self.__running_flag = False


    def recurring(self,):
        self.__start_time = time.time()






class clockThread(QObject):
    alarm_signal = Signal(str)
    # counter_signal = Signal(int)

    def __init__(self, sleep_time=1, name='') -> None:
        super().__init__()
        self.sleep_time = sleep_time
        self.name = name
        self.alarms:dict[str, datetime] = {}
        self.__running_flag = True


    def add_alarm(self, h, m, name:str):
        now = datetime.now()
        target_time = now.replace(hour=h, minute=m, second=0, microsecond=0)
        if target_time < now:
            target_time = self.__to_next_day(target_time)
        
        self.alarms[name] = target_time
        
    
    def __to_next_day(self, target_time):
        target_time += timedelta(days=1)
        return target_time
    

    def stop(self,):
        self.__running_flag = False

    def run(self,):
        self.__running_flag = True

        while  self.__running_flag:
            now = datetime.now()
            
            for name, clock in self.alarms.items():
                delta:timedelta = now - clock
                delta = delta.total_seconds()
                if 0 <= delta <=60:
                    self.alarms[name] = self.__to_next_day(self.alarms[name])
                    self.alarm_signal.emit(name)
                
            time.sleep(self.sleep_time)
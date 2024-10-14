import os
import subprocess

import cv2
from PySide6.QtCore import Signal, QObject
from persiantools.jdatetime import JalaliDateTime, timedelta
# from moviepy.editor import VideoFileClip


class transormUtils:

    @staticmethod
    def extract_file_name_info(name:str) -> tuple[JalaliDateTime, str, str]:
        name, extention = os.path.splitext(name)
        date, clock, train_id, camera_name = name.split('_')
        dc_str = date + '_' + clock
        dt = JalaliDateTime.strptime(dc_str,'%Y-%m-%d_%H-%M-%S-%f')
        return dt, train_id, camera_name
    
    @staticmethod
    def build_share_path( ip:str, share_name:str, path:str=''):
        res = f"\\\\{ip}\\{share_name}"
        if path:
            res = res + f"\\{path}"
        return res

    @staticmethod
    def last_day_of_month(year, month):
        if month == 12:
            next_month = JalaliDateTime(year+1, 1, 1)
        else:
            next_month = JalaliDateTime(year, month+1, 1)
        last_day_of_month:JalaliDateTime = next_month - timedelta(days=1)
        return last_day_of_month.day
    
    @staticmethod
    def get_video_duration(path):
        video = cv2.VideoCapture(path)
        fps = video.get(cv2.CAP_PROP_FPS)  # Frames per second
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames
        if frame_count == 0 or fps == 0:
            return 0
        duration = frame_count / fps
        return duration
    
    # @staticmethod
    # def dateTimeRanges(date_times:list[JalaliDateTime], step_lenght_sec:int, max_gap_sec=1):
    #     date_times.sort()


    #     start = date_times[0]
    #     end = date_times[0]
    #     res = []
    #     for i in range(1, len(date_times)):
    #         dif:timedelta = date_times[i] - end

    #         #check if next video distance is more than each video lengh, than means thay arent continues
    #         if dif.total_seconds() > (step_lenght_sec + max_gap_sec):
    #             end = timedelta(seconds=step_lenght_sec) + end
    #             res.append((start, end))
                
    #             start = date_times[i]
    #             end = date_times[i]
    #         else:
    #             end = date_times[i]
    #             if i==len(date_times)-1:
    #                 end = timedelta(seconds=step_lenght_sec) + end
    #                 res.append((start, end))

    #     return res


            

class timeRangeWorker(QObject):
    finish_signal = Signal(dict)
    progress_signal = Signal(float)
    def __init__(self, arcihve:dict[str,dict[str,dict]], train_id, date:JalaliDateTime, cameras):
        super().__init__()
        self.archive = arcihve
        self.train_id = train_id
        self.date = date
        self.date_str =  self.date.strftime("%Y-%m-%d")
        self.cameras = cameras

    def run(self,):
        total_count = self.get_total_count()
        count = 0
        result:dict[str, dict[str, list]] = {}
        for cam in self.archive[self.train_id].keys():
            if self.cameras is None or cam in self.cameras:
                result[cam] = {'ranges':[], 'paths':[]}

                if cam not in self.archive[self.train_id]:
                    continue

                if self.date_str not in self.archive[self.train_id][cam]:
                    continue

                for dict_info in self.archive[self.train_id][cam][self.date_str].values():
                    start_date_time = dict_info['datetime']
                    path = dict_info['path']
                    if os.path.exists(path):
                        
                        duration = transormUtils.get_video_duration(path)
                        if duration>0:
                            end_date_time = timedelta(seconds=duration) + start_date_time
                            result[cam]['ranges'].append((start_date_time, end_date_time))
                            result[cam]['paths'].append(path)
                    count+=1
                    progress = count/total_count
                    self.progress_signal.emit(progress)

        self.finish_signal.emit(result)

    
    def get_total_count(self,):
        count = 0
        for cam in self.archive[self.train_id].keys():
            if cam not in self.archive[self.train_id]:
                continue
            if self.date_str not in self.archive[self.train_id][cam]:
                continue

            if self.cameras is None or cam in self.cameras:
                
                count += len(self.archive[self.train_id][cam][self.date_str])
        return count
        
    # @staticmethod
    # def get_video_duration(video_path):
    #     try:
    #         clip = VideoFileClip(video_path)
    #         duration = clip.duration  # مدت زمان به ثانیه
    #         return duration
    #     except Exception as e:
    #         print(e)
    #         return None
        
# import vlc
# def get_video_duration_vlc(file_path):
#     # ایجاد یک شیء MediaPlayer برای دریافت متادیتا
#     instance = vlc.Instance()
#     media = instance.media_new(file_path)
    
#     # پردازش و بارگذاری متادیتا
#     media.parse()  # صبر می‌کند تا متادیتا بارگذاری شود
    
#     # مدت زمان را بدست آورید
#     duration = media.get_duration() / 1000  # مدت زمان به میلی‌ثانیه است، تبدیل به ثانیه
    
#     return duration

# import subprocess
# import concurrent.futures

# def get_video_duration(file_path):
#     result = subprocess.run(
#         ["ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", file_path],
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE
#     )
    
#     return float(result.stdout)

# def get_video_duration_cv(path):
#     video = cv2.VideoCapture(path)
#     fps = video.get(cv2.CAP_PROP_FPS)  # Frames per second
#     frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # Total number of frames
#     duration = frame_count / fps
#     return duration

# def get_multiple_video_durations(file_paths):
#     durations = {}
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         # ارسال هر فایل به تابع get_video_duration و اجرا به صورت همزمان
#         future_to_file = {executor.submit(get_video_duration, file): file for file in file_paths}
        
#         for future in concurrent.futures.as_completed(future_to_file):
#             file = future_to_file[future]
#             try:
#                 duration = future.result()
#                 durations[file] = duration
#             except Exception as exc:
#                 durations[file] = None
#                 print(f"{file} generated an exception: {exc}")
    
#     return durations

if __name__ == '__main__':
    import time
    import cv2
    import threading
    def test():
        for i in range(250):
            t=time.time()
            path = r'C:\rail_share\images\11BG21\cam1\1403\7\19\8\47\1403-07-19_08-47-22-043542_11BG21_cam1.mp4'
              # Duration in seconds
            duration = transormUtils.get_video_duration(path)
            # duration = get_video_duration(path)
            # get_video_duration_cv(path)
            # get_video_duration_vlc(path)
            t = time.time() - t
    t = time.time()

    threads = []
    for i in range(2):
        th1 = threading.Thread(target=test)
        threads.append(th1)
    
    for i in range(2):
        threads[i].start()

    for i in range(2):
        threads[i].join()


    
    print(time.time()- t)

import os
import subprocess

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
    def get_video_duration(video_path):
        try:
            # دستور ffprobe برای استخراج مدت زمان
            result = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", video_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
            # مدت زمان ویدیو به ثانیه
            return float(result.stdout)
        except Exception as e:
            print(e)
            return None
    
    @staticmethod
    def dateTimeRanges(date_times:list[JalaliDateTime], step_lenght_sec:int, max_gap_sec=1):
        date_times.sort()


        start = date_times[0]
        end = date_times[0]
        res = []
        for i in range(1, len(date_times)):
            dif:timedelta = date_times[i] - end

            #check if next video distance is more than each video lengh, than means thay arent continues
            if dif.total_seconds() > (step_lenght_sec + max_gap_sec):
                end = timedelta(seconds=step_lenght_sec) + end
                res.append((start, end))
                
                start = date_times[i]
                end = date_times[i]
            else:
                end = date_times[i]
        return res

            


        
    # @staticmethod
    # def get_video_duration(video_path):
    #     try:
    #         clip = VideoFileClip(video_path)
    #         duration = clip.duration  # مدت زمان به ثانیه
    #         return duration
    #     except Exception as e:
    #         print(e)
    #         return None
        

if __name__ == '__main__':
    import time

    t=time.time()
    lenght = transormUtils.get_video_duration('test_data1\\11BG21\\right\\1403\\7\9\\17\\21\\1403-07-09_17-21-42-236194_11BG21_right.mp4')
    t = time.time() - t
    print(t)

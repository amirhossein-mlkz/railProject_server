import cv2
import os
import subprocess
import re

from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QProgressBar, QFileDialog
from PySide6.QtCore import QThread, Signal
from Tranform.transformUtils import transormUtils
from datetime import timedelta
from persiantools.jdatetime import JalaliDateTime

class VideoCombiner(QThread):
    progress_signal = Signal(int)
    status_signal = Signal(int,str)
    finish_signal = Signal(int)

    FILES_LIST = "file_list.txt"
    SUBTITLE_EXTENTION = ".srt"
    VIDEO_EXTENTION = '.mp4'


    def __init__(self, input_videos, export_dir, export_fname,compression=True):
        super().__init__()
        self.input_videos = input_videos
        self.export_dir = export_dir
        self.export_fname = export_fname
        self.total_frames = 0
        self.compression=compression

        # #-----------------------------------------------------------
        # dir_path = 'C:\\Users\\amirh\\Downloads\\test'
        # self.input_videos = os.listdir(dir_path)
        # self.input_videos = list(map( lambda x:os.path.join(dir_path,x), self.input_videos))
        # #-----------------------------------------------------------


        
    def create_subtitle(self, video_paths):
        subtitle_path = os.path.join(self.export_dir, self.export_fname + self.SUBTITLE_EXTENTION)
        if os.path.exists(subtitle_path):
            os.remove(subtitle_path)

        subtitle_time = JalaliDateTime.now().replace(hour=0,minute=0,second=0, microsecond=0)
        videos_duration = list(map(lambda x:transormUtils.get_video_duration(x), video_paths))
        total_duration = sum(videos_duration)
        complete_duration = 0

        with open(subtitle_path, 'w', encoding='utf-8') as f:
        
            for idx, path in enumerate(video_paths):
                fdir, fname = os.path.split(path)
                video_datetime, train_id, camera_name, status, extention = transormUtils.extract_file_name_info(fname)
                durarion = videos_duration[idx]
                
                date_str = video_datetime.strftime('%Y/%m/%d')
                subtitle_file_text = ""
                for i in range(int(durarion)):
                    start_time = subtitle_time
                    end_time = start_time + timedelta(seconds=1)
                    subtitle_time = subtitle_time + timedelta(seconds=1)

                    start_time_str = start_time.strftime('%H:%M:%S')
                    end_time_str = end_time.strftime('%H:%M:%S')

                    current_real_time = video_datetime + timedelta(seconds=i)
                    current_real_time_str = current_real_time.strftime('%H:%M:%S')
                    text = f"Train: {train_id}  Camera:{camera_name}  {date_str}  {current_real_time_str}"

                    subtitle_file_text = subtitle_file_text + f"{i + 1}\n"
                    subtitle_file_text = subtitle_file_text + f"{start_time_str},000 --> {end_time_str},000\n"
                    subtitle_file_text = subtitle_file_text + f"{text}\n\n"

                    #---------------progressbar-------------------
                    complete_duration+=1
                    if complete_duration%10 == 0:
                        progress = (complete_duration/total_duration)*100
                        progress = int(progress)
                        self.progress_signal.emit(progress)

                f.write(subtitle_file_text)
                    
                
        return subtitle_path

    
    def create_file_list(self, video_paths:list[str], output_file):
        """
        یک فایل متنی برای لیست فایل‌های ویدیو ایجاد می‌کند.

        :param video_paths: لیستی از مسیر فایل‌های ویدیو
        :param output_file: نام فایل لیست (پیش‌فرض: file_list.txt)
        """
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except:
                return False
        
        res = []
        with open(output_file, "w", encoding="utf-8") as file:
            for path in video_paths:
                duration = transormUtils.get_video_duration(path)
                if duration > 0:
                    res.append(path)
                    file.write(f"file '{path}'\n")
        
        return True, res



    def run(self):
        self.status_signal.emit(0,'Get Videos')
        # First, calculate the total number of frames across all videos
        

        try:
            ret, good_files_Path = self.create_file_list(self.input_videos, self.FILES_LIST)

            if len(good_files_Path) == 0:
                self.status_signal.emit(0,"No Videos Exist For Export")
                self.finish_signal.emit(1)
                return

            self.status_signal.emit(0,'Generate Subtitle')
            subtitle_path = self.create_subtitle(self.input_videos)
            self.merge(good_files_Path)
            
            file_list = self.FILES_LIST  # فایل لیست ویدیوها
            output_file = os.path.join(self.export_dir, self.export_fname + self.VIDEO_EXTENTION)  # فایل خروجی
            file_list_path = os.path.join(os.getcwd(), file_list)

            total_frame_count = 0
            for path in good_files_Path:
                count, fps = transormUtils.get_video_frames_count(path)
                total_frame_count += count

            if not self.compression:
                command = [
                    "ffmpeg",
                    "-f", "concat",
                    "-safe", "0",
                    "-i", file_list_path,
                    "-c", "copy",
                    '-y',  # Overwrite the output file if it exists
                    output_file
                ]

                # command = [
                #     "ffmpeg",
                #     "-f", "concat",
                #     "-safe", "0",
                #     "-i", file_list_path,  # List of input files
                #     "-i", subtitle_path,  # Input subtitle file
                #     "-c", "copy",  # Copy streams without re-encoding
                #     "-map", "0",  # Map all streams from the video input
                #     "-map", "1",  # Map the subtitle stream
                #     "-y",  # Overwrite the output file if it exists
                #     output_file  # Output file with subtitle included
                # ]

            else:
                command = [
                    'ffmpeg', 
                    "-f", "concat",
                    "-safe", "0",
                    '-i', file_list,  # Input temporary MP4 file
                    '-c:v', 'libx265',  # Use H.265 codec
                    '-preset', 'fast',  # Medium encoding speed
                    '-y',  # Overwrite the output file if it exists
                    output_file  # Output file in MKV format
                ]

                # command = [
                #     'ffmpeg',
                #     '-f', 'concat',
                #     '-safe', '0',
                #     '-i', file_list,  # Input temporary MP4 file
                #     '-c:v', 'libx265',  # Use H.265 codec
                #     '-preset', 'medium',  # Medium encoding speed
                #     '-scodec', 'mov_text',  # Subtitle codec for soft subtitles
                #     '-i', subtitle_path,  # Input subtitle file
                #     '-map', '0',  # Map all streams from the video
                #     '-map', '1',  # Map the subtitle stream
                #     '-y',  # Overwrite the output file if it exists
                #     output_file  # Output file in MKV format
                # ]

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            self.status_signal.emit(0,'Merge Videos')

            current_progress = 0
            frame_pattern = r'frame=\s*(\d+)'
            for line in process.stdout:
                match = re.search(frame_pattern, line)
                if match:
                    frame_count = int(match.group(1))
                    current_progress = int(frame_count / total_frame_count * 100)
                    self.progress_signal.emit(current_progress)

            process.wait()
            self.status_signal.emit(0,'Progress Completed')
            self.finish_signal.emit(1)
            os.startfile(self.export_dir)
        
        except Exception as e:
            self.status_signal.emit(0,f'Error:{e}')
            self.finish_signal.emit(1)


    def merge(self, files_path):
        file_list = self.FILES_LIST  # فایل لیست ویدیوها
        output_file = os.path.join(self.export_dir, self.export_fname + self.VIDEO_EXTENTION)  # فایل خروجی
        file_list_path = os.path.join(os.getcwd(), file_list)

        total_frame_count = 0
        for path in files_path:
            count, fps = transormUtils.get_video_frames_count(path)
            total_frame_count += count

        if not self.compression:
            command = [
                "ffmpeg",
                "-f", "concat",
                "-safe", "0",
                "-i", file_list_path,
                "-c", "copy",
                '-y',  # Overwrite the output file if it exists
                output_file
            ]

            # command = [
            #     "ffmpeg",
            #     "-f", "concat",
            #     "-safe", "0",
            #     "-i", file_list_path,  # List of input files
            #     "-i", subtitle_path,  # Input subtitle file
            #     "-c", "copy",  # Copy streams without re-encoding
            #     "-map", "0",  # Map all streams from the video input
            #     "-map", "1",  # Map the subtitle stream
            #     "-y",  # Overwrite the output file if it exists
            #     output_file  # Output file with subtitle included
            # ]

        else:
            command = [
                'ffmpeg', 
                "-f", "concat",
                "-safe", "0",
                '-i', file_list,  # Input temporary MP4 file
                '-c:v', 'libx264',  # Use H.265 codec
                '-preset', 'medium',  # Medium encoding speed
                '-y',  # Overwrite the output file if it exists
                output_file  # Output file in MKV format
            ]

            # command = [
            #     'ffmpeg',
            #     '-f', 'concat',
            #     '-safe', '0',
            #     '-i', file_list,  # Input temporary MP4 file
            #     '-c:v', 'libx265',  # Use H.265 codec
            #     '-preset', 'medium',  # Medium encoding speed
            #     '-scodec', 'mov_text',  # Subtitle codec for soft subtitles
            #     '-i', subtitle_path,  # Input subtitle file
            #     '-map', '0',  # Map all streams from the video
            #     '-map', '1',  # Map the subtitle stream
            #     '-y',  # Overwrite the output file if it exists
            #     output_file  # Output file in MKV format
            # ]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        self.status_signal.emit(0,'Merge Videos')

        current_progress = 0
        frame_pattern = r'frame=\s*(\d+)'
        for line in process.stdout:
            match = re.search(frame_pattern, line)
            if match:
                frame_count = int(match.group(1))
                current_progress = int(frame_count / total_frame_count * 100)
                self.progress_signal.emit(current_progress)

        process.wait()
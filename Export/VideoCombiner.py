import cv2
import os
import subprocess
import re
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QProgressBar, QFileDialog
from PySide6.QtCore import QThread, Signal


class VideoCombiner(QThread):
    progress_signal = Signal(int)
    status_signal = Signal(int,str)
    finish_signal = Signal(int)

    FILES_LIST = "file_list.txt"

    def __init__(self, input_videos, temp_output_file, final_output_file,convert_mkv=True):
        super().__init__()
        convert_mkv = False

        self.input_videos = input_videos
        self.temp_output_file = temp_output_file  # Temporary MP4 file from OpenCV
        self.final_output_file = final_output_file  # Final MKV file with H.265 codec
        self.total_frames = 0
        self.convert_mkv=convert_mkv

        if not self.convert_mkv:
            if self.final_output_file.split('.')[-1] != 'mp4':
                self.temp_output_file = self.final_output_file+'.mp4'
            else:
                self.temp_output_file = self.final_output_file
        if self.convert_mkv:
            if self.final_output_file.split('.')[-1] != 'mkv':

                self.temp_output_file = self.final_output_file+'.mkv'

    
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
        
        with open(output_file, "w", encoding="utf-8") as file:
            for path in video_paths:
                file.write(f"file '{path}'\n")
        
        return True



    def run(self):
        self.status_signal.emit(0,'Get Videos')
        # First, calculate the total number of frames across all videos
        self.create_file_list(self.input_videos, self.FILES_LIST)

        try:
            file_list = self.FILES_LIST  # فایل لیست ویدیوها
            output_file = self.final_output_file  # فایل خروجی

            if not self.convert_mkv:
                command = [
                    "ffmpeg",
                    "-f", "concat",
                    "-safe", "0",
                    "-i", file_list,
                    "-c", "copy",
                    '-y',  # Overwrite the output file if it exists
                    output_file
                ]

            else:
                command = [
                    'ffmpeg', 
                    "-f", "concat",
                    "-safe", "0",
                    '-i', file_list,  # Input temporary MP4 file
                    '-c:v', 'libx265',  # Use H.265 codec
                    '-preset', 'medium',  # Medium encoding speed
                    #'-crf', '28',  # Quality setting
                    '-y',  # Overwrite the output file if it exists
                    output_file  # Output file in MKV format
                ]

            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            self.status_signal.emit(0,'Merge Videos')

            total_duration = 0
            current_progress = 0

            for line in process.stdout:
                # استخراج مدت زمان کل از خروجی FFmpeg
                if "Duration" in line:
                    parts = line.split(",")[0].split("Duration:")[-1].strip()
                    h, m, s = map(float, parts.replace(":", " ").split())
                    total_duration = h * 3600 + m * 60 + s

                # استخراج زمان فعلی از پیشرفت
                if "time=" in line:
                    time_part = line.split("time=")[-1].split(" ")[0]
                    h, m, s = map(float, time_part.replace(":", " ").split())
                    current_time = h * 3600 + m * 60 + s

                    # محاسبه درصد پیشرفت
                    current_progress = int((current_time / total_duration) * 100)
                    self.progress_signal.emit(current_progress)

            process.wait()
            self.status_signal.emit(0,'Progress Completed')
            self.finish_signal.emit(1)

        except Exception as e:
            self.status_signal.emit(1,'Error in Converting to mkv x265')
            self.finish_signal.emit(1)




            

class VideoCombinerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Add widgets to layout
        self.progress = QProgressBar(self)
        self.progress.setMaximum(100)
        self.layout.addWidget(self.progress)

        self.conversion_progress = QProgressBar(self)
        self.conversion_progress.setMaximum(100)
        self.layout.addWidget(self.conversion_progress)

        self.label = QLabel('Video combining progress:', self)
        self.layout.addWidget(self.label)

        self.button = QPushButton('Select Videos and Combine', self)
        self.button.clicked.connect(self.select_videos)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.setWindowTitle('Video Combiner')
        self.show()

    def select_videos(self):
        # Open file dialog to select multiple video files
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, 'Select Video Files', '', 'Video Files (*.mp4 *.avi *.mkv)', options=options)
        if files:
            output_file, _ = QFileDialog.getSaveFileName(self, 'Save Combined Video', '', 'MKV Files (*.mkv)')
            if output_file:
                temp_output_file = 'temp_combined.mp4'  # Temporary MP4 file
                # Start combining videos in the background
                self.combine_videos(files, temp_output_file, output_file)

    def combine_videos(self, input_videos, temp_output_file, final_output_file):
        self.worker = VideoCombiner(input_videos, temp_output_file, final_output_file)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.start()

    def update_progress(self, value):
        self.progress.setValue(value)



if __name__ == '__main__':
    app = QApplication([])
    window = VideoCombinerUI()
    app.exec_()

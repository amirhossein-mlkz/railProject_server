import cv2
import os
import subprocess
import re
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QLabel, QProgressBar, QFileDialog
from PySide6.QtCore import QThread, Signal

class VideoCombiner(QThread):
    progress_signal = Signal(int)
    conversion_progress_signal = Signal(int)  # For conversion progress
    status_signal = Signal(int,str)
    finish_signal = Signal(int)

    def __init__(self, input_videos, temp_output_file, final_output_file,convert_mkv=True):
        super().__init__()
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



    def run(self):
        # First, calculate the total number of frames across all videos
        for video_path in self.input_videos:
            cap = cv2.VideoCapture(video_path)
            self.total_frames += int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            cap.release()
            self.status_signal.emit(0,'Get Videos')

        # Open temporary output video writer (MP4 format)
        first_video = cv2.VideoCapture(self.input_videos[0])
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # OpenCV doesn't directly support MKV, so use MP4 here
        fps = first_video.get(cv2.CAP_PROP_FPS)
        width = int(first_video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(first_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(self.temp_output_file, fourcc, fps, (width, height))
        first_video.release()

        processed_frames = 0

        # Loop through each video and write their frames to the temporary MP4 file
        try:
            self.status_signal.emit(0,'Merge Videos')

            for video_path in self.input_videos:
                cap = cv2.VideoCapture(video_path)
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    out.write(frame)
                    processed_frames += 1
                    progress = int((processed_frames / self.total_frames) * 100)
                    self.progress_signal.emit(progress)  # Emit progress signal to update the UI
                cap.release()

            out.release()
        except:
            self.status_signal.emit(1,'Error in Read Videos')
            self.finish_signal.emit(1)


        # After combining, convert to MKV using FFmpeg

        if self.convert_mkv:
            self.convert_to_mkv()

        else:
            self.status_signal.emit(0,'Progress Completed')
            self.finish_signal.emit(1)


    def convert_to_mkv(self):
        try:
            # FFmpeg command to convert MP4 to MKV with H.265 (HEVC) codec
            self.status_signal.emit(0,'Start to converting mkv x265')

            command = [
                'ffmpeg', '-i', self.temp_output_file,  # Input temporary MP4 file
                '-c:v', 'libx265',  # Use H.265 codec
                '-preset', 'medium',  # Medium encoding speed
                '-crf', '28',  # Quality setting
                '-y',  # Overwrite the output file if it exists
                self.final_output_file  # Output file in MKV format
            ]

            # Run FFmpeg and capture the output in real-time
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            total_duration = 0
            for line in process.stderr:
                # Extract the total duration of the video from the FFmpeg output
                if 'Duration:' in line:
                    match = re.search(r'Duration: (\d+):(\d+):(\d+)\.(\d+)', line)
                    if match:
                        hours = int(match.group(1))
                        minutes = int(match.group(2))
                        seconds = int(match.group(3))
                        total_duration = hours * 3600 + minutes * 60 + seconds

                # Track encoding progress by parsing the `time=` field from FFmpeg output
                if 'time=' in line:
                    time_match = re.search(r'time=(\d+):(\d+):(\d+)\.(\d+)', line)
                    if time_match:
                        current_hours = int(time_match.group(1))
                        current_minutes = int(time_match.group(2))
                        current_seconds = int(time_match.group(3))
                        current_time = current_hours * 3600 + current_minutes * 60 + current_seconds

                        if total_duration > 0:
                            progress = int((current_time / total_duration) * 100)
                            self.conversion_progress_signal.emit(progress)  # Emit conversion progress

            process.wait()
            print(progress)
            print(f"Conversion to MKV with H.265 completed: {self.final_output_file}")
            if progress<100:
                self.conversion_progress_signal.emit(100)
                self.status_signal.emit(0,'Progress Completed')
                self.finish_signal.emit(1)

        except:
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
        self.worker.conversion_progress_signal.connect(self.update_conversion_progress)
        self.worker.start()

    def update_progress(self, value):
        self.progress.setValue(value)

    def update_conversion_progress(self, value):
        self.conversion_progress.setValue(value)

if __name__ == '__main__':
    app = QApplication([])
    window = VideoCombinerUI()
    app.exec_()

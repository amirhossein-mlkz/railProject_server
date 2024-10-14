import sys
import os
import ctypes

# Set the full path to VLC libraries


def LocalVlc():
    vlc_path = r"backend\mediaPlayer\vlc_path"  # Adjust this path based on where VLC is installed
    # Load VLC libraries manually
    ctypes.CDLL(os.path.join(vlc_path, "libvlc.dll"))
    ctypes.CDLL(os.path.join(vlc_path, "libvlccore.dll"))
LocalVlc()
import vlc

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QSlider, QHBoxLayout
from PySide6.QtCore import Qt, QTimer


class MediaPlayer:
    def __init__(self, video_widget):

        self.playback_speed = 1  # Initial playback speed
        # Create VLC instance and media player
        self.instance = vlc.Instance()
        self.media_player:vlc.MediaPlayer = self.instance.media_player_new()

        # Set VLC to render in the widget
        if sys.platform == "linux":
            self.media_player.set_xwindow(video_widget.winId())
        elif sys.platform == "win32":
            self.media_player.set_hwnd(video_widget.winId())


        # Load the video

    def load_video(self, video_path):
        """Load the video from the given path."""
        if video_path:
            media = self.instance.media_new(video_path)
            self.media_player.set_media(media)

    def play_video(self):
        """Play the video."""
        self.media_player.play()

    def pause_video(self):
        """Pause the video."""
        self.media_player.pause()

    def stop_video(self):
        """Stop the video."""
        self.media_player.stop()

    def set_position(self, position):
        """Set the position of the video based on the slider."""
        self.media_player.set_position(position / 1000)

    def set_time(self, t_sec):
        t_sec = int(t_sec * 1000)
        self.media_player.set_time(t_sec)

    def change_speed(self):
        """Cycle through video playback speeds from 1x to 32x."""
        if self.playback_speed < 32:
            self.playback_speed *= 2
        else:
            self.playback_speed = 1

        # Update VLC playback rate
        self.media_player.set_rate(self.playback_speed)
        return self.playback_speed

    def update_marquee(self, text, position=5, font_size=100, color=0x00FF00):
        """Update marquee text on the video.

                # Position Value	Position Description
                # 0	                    Center
                # 1	                    Left
                # 2	                    Right
                # 3	                    Top-center
                # 4	                    Bottom-center
                # 5	                    Top-left
                # 6	                    Top-right
                # 7	                    Bottom-left
                # 8	                    Bottom-right

                SAMPLE COLORS :

                Black:                  #000000
                Dark Gray:              #333333
                White:                  #FFFFFF
                Navy Blue:              #001F3F
                Dark Green:             #006400

        """



        self.media_player.video_set_marquee_string(vlc.VideoMarqueeOption.Text, text)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Enable, 1)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Position, position)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Size, font_size)
        self.media_player.video_set_marquee_int(vlc.VideoMarqueeOption.Color, color)






    def set_start_time(self, time_in_seconds):
        """Set the start time of the video."""
        self.media_player.set_time(time_in_seconds * 1000)

    def is_playing(self):
        """Return whether the media player is currently playing."""
        return self.media_player.is_playing()
    
    def is_finished(self,):
        return self.media_player.get_state() == vlc.State.Ended

    def get_time(self):
        """Get the current time in the video in seconds."""
        return self.media_player.get_time() // 1000

    def get_position(self):
        """Get the current position of the video (from 0 to 1)."""
        return self.media_player.get_position()


class PlayerUI(QMainWindow):
    def __init__(self, camera_number="Camera 1", video_path=""):
        super().__init__()

        self.camera_number = camera_number  # Store the camera number

        # Set up the video output widget
        self.video_widget = QWidget(self)
        # self.video_widget.setAttribute(Qt.WidgetAttribute.WA_OpaquePaintEvent)

        # Create MediaPlayer instance
        self.media_player = MediaPlayer(self.video_widget, video_path)

        # Layout for the video and controls
        layout = QVBoxLayout()

        # Add video widget to layout
        layout.addWidget(self.video_widget)

        # Slider for video timeline
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 1000)  # This will be updated later based on video length
        self.slider.sliderMoved.connect(self.set_position)
        layout.addWidget(self.slider)

        # Buttons for play, pause, stop, and speed
        button_layout = QHBoxLayout()
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_video)
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.pause_video)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_video)
        self.speed_button = QPushButton(f"Speed: {self.media_player.playback_speed}x")
        self.speed_button.clicked.connect(self.change_speed)

        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.speed_button)

        layout.addLayout(button_layout)

        # Set layout to central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Timer for updating the slider and checking video state
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_ui)
        self.timer.start(1000)  # Update every second

    def play_video(self):
        """Play the video."""
        self.media_player.play_video()

    def pause_video(self):
        """Pause the video."""
        self.media_player.pause_video()

    def stop_video(self):
        """Stop the video."""
        self.media_player.stop_video()

    def set_position(self, position):
        """Set the position of the video based on the slider."""
        self.media_player.set_position(position)

    def change_speed(self):
        """Change the video speed."""
        self.media_player.change_speed()
        self.speed_button.setText(f"Speed: {self.media_player.playback_speed}x")

    def update_ui(self):
        """Update the slider and the video playback UI."""
        if self.media_player.is_playing():
            position = self.media_player.get_position() * 1000
            self.slider.setValue(int(position))

            # Display the current time and update the top marquee
            current_time = self.media_player.get_time()
            minutes, seconds = divmod(current_time, 60)
            time_string = f"{minutes:02}:{seconds:02}"
            marquee_text = f"{self.camera_number} | Time: {time_string}"
            self.media_player.update_marquee(marquee_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Single video path to play
    video_path = r"intro001.mp4"  # Replace with your video path

    # Create the UI
    player_ui = PlayerUI(camera_number="Camera 1", video_path=video_path)
    player_ui.resize(800, 600)
    player_ui.show()

    sys.exit(app.exec())

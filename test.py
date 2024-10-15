from PySide6.QtCore import Qt, QPoint, QEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window as frameless
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Track mouse positions for dragging
        self.is_dragging = False
        self.drag_position = QPoint()

        # Initial height of the top bar
        self.top_bar_default_height = 30
        self.top_bar_maximized_height = 50  # Height when maximized/fullscreen

        # Create a basic UI
        self.init_ui()

        # Set the initial window size
        self.setWindowSize(800, 600)

    def init_ui(self):
        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a top bar (for dragging the window)
        self.top_bar = QLabel("Drag me!", self)
        self.top_bar.setFixedHeight(self.top_bar_default_height)
        self.top_bar.setStyleSheet("background-color: #333; color: white;")
        layout.addWidget(self.top_bar)

        # Example content
        content = QLabel("Content goes here...", self)
        layout.addWidget(content)

    def setWindowSize(self, width, height):
        """Set the window size."""
        self.setGeometry(100, 100, width, height)  # Set x=100, y=100, width, height

    # Handle mouse press event (start dragging)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.top_bar.underMouse():
            self.is_dragging = True
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    # Handle mouse move event (dragging the window)
    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    # Handle mouse release event (stop dragging)
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False

            # Check if the window is dragged to the top of the screen
            if self.y() <= 0:  # If dragged to the top of the screen
                if self.isFullScreen():
                    self.showNormal()  # Exit fullscreen
                    self.setWindowSize(800, 600)  # Reset to desired size
                else:
                    self.showMaximized()  # Maximize the window

    # Detect changes in window state (fullscreen, maximized, normal)
    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
                self.top_bar.setFixedHeight(self.top_bar_maximized_height)  # Increase top bar size
            else:
                self.top_bar.setFixedHeight(self.top_bar_default_height)  # Reset top bar size
                self.setWindowSize(800, 600)  # Reset to your desired size

        super().changeEvent(event)

    # Override the keyPressEvent to toggle fullscreen with the 'F11' key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()  # Exit fullscreen
                self.setWindowSize(800, 600)  # Reset to desired size
            else:
                self.showFullScreen()  # Enter fullscreen

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()

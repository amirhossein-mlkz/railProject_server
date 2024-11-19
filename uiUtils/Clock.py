import math
from datetime import time, datetime
from persiantools.jdatetime import JalaliDateTime

from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QPainter, QColor, QMouseEvent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow, QApplication
from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QPainter, QColor, QMouseEvent
from PySide6.QtWidgets import QWidget


class ClockWidget(QWidget):
    def __init__(self, 
                 is_am=True, 
                 time_ranges=None, 
                 show_all_hours=False, 
                 show_main_hours = True,
                 hour_text_color=QColor("black"),
                 guide_line_color=QColor("gray"),
                 outline_color=QColor("black"),
                 avaiable_color=QColor("green"),
                 w=200,
                 h=200,
                 parent=None):
        super().__init__(parent)
        self.is_am = is_am
        self.time_ranges = time_ranges if time_ranges else []
        self.show_all_hours = show_all_hours
        self.show_main_hours = show_main_hours
        self.hour_text_color = hour_text_color
        self.guide_line_color = guide_line_color
        self.outline_color = outline_color
        self.avaiable_color = avaiable_color
        self.external_click_event_func = None
        self.setMinimumSize(w,h)
        self.setMouseTracking(True)  # Enable tracking for mouseMoveEvent
        self.setFocusPolicy(Qt.StrongFocus)  # Ensure widget can receive focus for events

    def set_time_ranges(self, time_ranges):
        self.time_ranges = []
        for start, end in time_ranges:
            if isinstance(start, datetime) or isinstance(start, JalaliDateTime):
                start = start.time()
                end = end.time()

            if self.is_am:
                if end >= time(12,0):
                    end = time(11,59,59)
                if time(0,0) <= start < time(12,0) and time(0,0) <= end < time(12,0):
                    self.time_ranges.append((start, end))
                else:
                    continue
            else:
                if time(0,0) <= end < time(12,0):
                    end = time(23,59,59)
                if time(0,0) <= start < time(12,0) and time(0,0) <= end < time(12,0):
                    continue
                else:
                    self.time_ranges.append((start, end))

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        size = min(self.width(), self.height()) - 20
        rect = QRectF(10, 10, size, size)
        
        # Draw the clock outline
        painter.setPen(self.outline_color)
        painter.drawEllipse(rect)

        # Draw time ranges with highlight color
        for start, end in self.time_ranges:
            if (self.is_am and 0 <= start.hour < 12 and 0 <= end.hour < 12) or \
               (not self.is_am and 12 <= start.hour < 24 and 12 <= end.hour < 24):
                self.draw_time_range(painter, rect, start, end, self.avaiable_color)

        # Draw hour labels and guide lines
        center = rect.center()
        painter.setPen(self.hour_text_color)
        for hour in range(1, 13):
            angle = (hour - 3) * 30
            x = center.x() + (rect.width() / 2 - 30) * math.cos(math.radians(angle))
            y = center.y() + (rect.height() / 2 - 30) * math.sin(math.radians(angle))
            if self.show_all_hours or ( hour in {3, 6, 9, 12} and self.show_main_hours):
                painter.drawText(x - 10, y + 10, f"{hour}{' AM' if self.is_am else ' PM'}")

            # Draw small guide lines next to each hour
            painter.setPen(self.guide_line_color)
            line_start_x = center.x() + (rect.width() / 2 - 15) * math.cos(math.radians(angle))
            line_start_y = center.y() + (rect.height() / 2 - 15) * math.sin(math.radians(angle))
            line_end_x = center.x() + (rect.width() / 2 - 5) * math.cos(math.radians(angle))
            line_end_y = center.y() + (rect.height() / 2 - 5) * math.sin(math.radians(angle))
            painter.drawLine(QPointF(line_start_x, line_start_y), QPointF(line_end_x, line_end_y))

    def time_range2angle(self, start, end):
        start_minutes = (start.hour % 12) * 60 + start.minute
        end_minutes = (end.hour % 12) * 60 + end.minute

        start_angle = int(start_minutes / 720 * 360)
        end_angle = int(end_minutes / 720 * 360)
        
        return start_angle, end_angle

    def draw_time_range(self, painter, rect, start, end, color):
        painter.setBrush(color)
        painter.setPen(Qt.NoPen)

        start_angle, end_angle = self.time_range2angle(start, end)
        start_angle = self.from_clockwise_angle(start_angle)
        end_angle = self.from_clockwise_angle(end_angle)

        if start_angle * end_angle <0:
            if start_angle > 0:
                span_angle = start_angle + abs(end_angle)
            else:
                span_angle = (180 - end_angle) + (180 + start_angle)
            
            span_angle  = span_angle * -1
   
        else:
            span_angle = end_angle - start_angle

        painter.drawPie(rect, start_angle * 16, span_angle * 16)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(self.outline_color)

    def connect_click(self, func):
        self.external_click_event_func = func

    def mousePressEvent(self, event: QMouseEvent):
        clicked_angle = self.get_angle_from_position(event.position().toPoint())
        for start, end in self.time_ranges:
            start_angle, end_angle = self.time_range2angle(start, end)
            if start_angle <= clicked_angle <= end_angle:
                # print(f"Clicked Time Range: {start.strftime('%H:%M')} - {end.strftime('%H:%M')}")
                if self.external_click_event_func:
                    self.external_click_event_func(start, end)
                break

    def mouseMoveEvent(self, event: QMouseEvent):
        hovered_angle = self.get_angle_from_position(event.position().toPoint())
        for start, end in self.time_ranges:
            start_angle, end_angle = self.time_range2angle(start, end)
            if start_angle <= hovered_angle <= end_angle:
                self.setToolTip(f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}")
                break
        else:
            self.setToolTip("")

    def to_clockwise_angle(self, angle):
        angle = angle % 360
        return (450 - angle) % 360

    def from_clockwise_angle(self, angle):
        angle = angle % 360
        new_angle = (90 - angle) % 360
        return new_angle if new_angle <= 180 else new_angle - 360

    def get_angle_from_position(self, pos):
        center = self.rect().center()
        dx = pos.x() - center.x()
        dy = center.y() - pos.y()
        angle = math.degrees(math.atan2(dy, dx))
        return (self.to_clockwise_angle(angle) + 360) % 360


# Example Usage
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Centered Clock Widget")

        clock_widget = ClockWidget(is_am=True, show_all_hours=False)
        time_ranges = [(time(3, 0), time(5, 30)), (time(9, 15), time(10, 45))]
        clock_widget.set_time_ranges(time_ranges)

        layout = QVBoxLayout()
        layout.addWidget(clock_widget, alignment=Qt.AlignCenter)  # Center the clock in layout

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

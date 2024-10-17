import os,sys,time

import Export_Constants


os.system('pyside6-uic {} -o {}'.format(os.path.join('Export/ExportUIiFiles', 'export.ui'), os.path.join('Export/ExportUIiFiles', 'ui_export.py')))
os.system('pyside6-rcc {} -o {}'.format('Expor/resources/assets.qrc','Export/resources/assets_rc.py'))


from resources import assets_rc


from PySide6.QtWidgets import (
    QDialog, 
    QApplication,
    QWidget,
    QTableWidgetItem,
    QFrame,
    QStackedWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QComboBox
)
from PySide6.QtWidgets import QApplication as sQApplication
from PySide6.QtCore import Qt, QPoint


from ExportUIiFiles.ui_export import Ui_userProfile



# ui class
class UIExport(QWidget):

    def __init__(self):
        super(UIExport, self).__init__()

        self.ui = Ui_userProfile()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.__center()
        self.offset = None




    def __center(self) -> None:
        """Centers the dialog on the screen based on the current primary screen's geometry."""
        primary_screen = QApplication.primaryScreen()
        if primary_screen:
            screen_geometry = primary_screen.geometry()
            center_point = screen_geometry.center()
            self.move(center_point.x() - self.frameGeometry().width() // 2,
                      center_point.y() - self.frameGeometry().height() // 2)



    def close_win(self) -> None:
        """Closes the window."""
        self.close()

    def mousePressEvent(self, event) -> None:
        """Enables the dialog to be moved by dragging."""
        if event.button() == Qt.LeftButton and event.position().y() < self.ui.top_frame.height():
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event) -> None:
        """Handles the dialog movement when dragged."""
        if not hasattr(self, 'move_refresh_time'):
            self.move_refresh_time = 0
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            if time.time() - self.move_refresh_time > Export_Constants.RefreshRates.WINDOW_MOVE:
                self.move_refresh_time = time.time()
                self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        """Finalizes the dragging operation by clearing the offset."""
        self.offset = None
        super().mouseReleaseEvent(event)


if __name__ == "__main__":




    app = sQApplication()

    win = UIExport()
 
    win.show()
    sys.exit(app.exec())
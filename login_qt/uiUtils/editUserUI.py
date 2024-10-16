import sys, os
import time
import threading
from typing import Union
from PySide6.QtWidgets import (
    QDialog,
    QApplication,
    QFrame,
    QPushButton,
    QLineEdit,
    QComboBox,
)
from PySide6.QtCore import Qt, QPoint

# Append the directory containing resources to system path for easier imports
sys.path.append(os.path.join('uiFiles', 'resources'))
from uiFiles.editUser import Ui_editUser
from Constants import Constants
from Constants import Messages
from uiUtils.eyeButtonHandler import eyeButtonHandler

class editUser_UI(QDialog):
    """
    A dialog window class for editing user information, extending QDialog.

    Provides comprehensive UI components for interacting with user data such as username,
    password, role, and message displays with validations and updates.
    """
    
    def __init__(self) -> None:
        super(editUser_UI, self).__init__()

        self.edited_user_info = {}  # Store modified user information

        # Load and set up the user interface from a Designer file
        self.ui = Ui_editUser()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Define and connect UI components
        self.__define_ui_components()
        self.__connect_ui_components()

        # Center the dialog on screen
        self.__center()

        # To manage window dragging
        self.offset = None

        # Initialize role options
        self.set_role_comboBox_items()

    def __center(self) -> None:
        """Centers the window on the screen."""
        primary_screen = QApplication.primaryScreen()
        if primary_screen:
            screen_geometry = primary_screen.geometry()
            center_point = screen_geometry.center()
            self.move(center_point.x() - self.frameGeometry().width() // 2,
                      center_point.y() - self.frameGeometry().height() // 2)

    def __define_ui_components(self) -> None:
        """
        Maps UI components from the Ui_editUser to more accessible attributes,
        simplifying further interactions.
        """
        self.ui_components: dict[str, Union[QFrame, QPushButton, QLineEdit, QComboBox]] = {
            'top_frame': self.ui.top_frame,
            'close_btn': self.ui.close_btn,
            'password_eye_btn': self.ui.edituser_password_eye_btn,
            'confirm_password_eye_btn': self.ui.edituser_confirm_password_eye_btn,
            'apply_btn': self.ui.apply_btn,
            'username_lineEdit': self.ui.edituser_username_lineEdit,
            'password_lineEdit': self.ui.edituser_password_lineEdit,
            'confirm_password_lineEdit': self.ui.edituser_confirm_password_lineEdit,
            'role_comboBox': self.ui.edituser_role_comboBox,
            'message_label': self.ui.edit_user_message_label,
        }

    def __connect_ui_components(self) -> None:
        """Connects UI components to their respective functions or handlers."""
        self.ui_components['close_btn'].clicked.connect(self.close_win)
        # Eye button handlers for password visibility toggling
        self.password_eye_handler = eyeButtonHandler(
            self.ui_components['password_eye_btn'],
            self.ui_components['password_lineEdit']
        )
        self.confirm_password_eye_handler = eyeButtonHandler(
            self.ui_components['confirm_password_eye_btn'],
            self.ui_components['confirm_password_lineEdit']
        )
        self.ui_components['apply_btn'].clicked.connect(self.apply)

    def show_win(self, user_info: dict = None) -> None:
        """
        Displays the window and initializes fields if user_info is provided.

        Args:
            user_info (dict, optional): Dictionary containing user data to initialize the form.

        Returns:
            The edited user information if changes were made and the dialog was closed properly.
        """
        if user_info:
            self.set_fields(user_info)
        ret = self.exec()
        if ret and self.edited_user_info:
            if self.edited_user_info[Constants.Keys.PASSWORD_KEY] == Constants.ReservedPassword.RESERVED_PASSWORD:
                self.edited_user_info[Constants.Keys.PASSWORD_KEY] = user_info[Constants.Keys.PASSWORD_KEY]
                self.edited_user_info[Constants.Keys.CONFIRM_PASSWORD_KEY] = user_info[Constants.Keys.PASSWORD_KEY]
            return self.edited_user_info

    def close_win(self) -> None:
        """Closes the window."""
        self.close()

    def mousePressEvent(self, event) -> None:
        """
        Handles mouse press events for dragging the window.

        Args:
            event: The mouse event.
        """
        if event.button() == Qt.LeftButton and event.position().y() < self.ui.top_frame.height():
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event) -> None:
        """
        Handles the window dragging if the left mouse button is held down.

        Args:
            event: The mouse event.
        """
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            if not hasattr(self, 'move_refresh_time'):
                self.move_refresh_time = 0
            if time.time() - self.move_refresh_time > Constants.RefreshRates.WINDOW_MOVE:
                self.move_refresh_time = time.time()
                self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        """Releases the dragging mechanism."""
        self.offset = None
        super().mouseReleaseEvent(event)

    def set_role_comboBox_items(self) -> None:
        """
        Populates the role combobox with roles retrieved from the Constants.
        """
        items = [v for k, v in vars(Constants.Roles).items() if not k.startswith('__')]
        self.ui_components['role_comboBox'].clear()
        self.ui_components['role_comboBox'].addItems(items)

    def set_message(self, message: str, level: int = 0) -> None:
        """
        Displays a message in the message label with appropriate styling based on the level of importance.

        Args:
            message (str): The message to display.
            level (int): The severity level of the message.
        """
        if level == Constants.MessagesLevels.INFO:
            self.ui_components['message_label'].setStyleSheet('color:rgb(84, 156, 86);')
        elif level == Constants.MessagesLevels.WARNING:
            self.ui_components['message_label'].setStyleSheet('color:rgb(255, 255, 94);')
        elif level == Constants.MessagesLevels.ERROR:
            self.ui_components['message_label'].setStyleSheet('color:rgb(255, 99, 94);')

        self.ui_components['message_label'].setText(message)
        if message:
            threading.Timer(Constants.RefreshRates.MESSAGES_TIME, self.set_message, args=('',)).start()

    def highlight_field(self, field: str, level: int = 0):
        """
        Highlights an input field to indicate an issue, using colors and styles based on the message level.

        Args:
            field (str): The field to highlight.
            level (int): The severity level of the issue.
        """
        if level == Constants.MessagesLevels.INFO:
            self.ui_components[field].setStyleSheet('color:rgb(84, 156, 86); border-bottom: 2px solid rgb(84, 156, 86);')
        elif level == Constants.MessagesLevels.WARNING:
            self.ui_components[field].setStyleSheet('color:rgb(255, 255, 94); border-bottom: 2px solid rgb(255, 255, 94);')
        elif level == Constants.MessagesLevels.ERROR:
            self.ui_components[field].setStyleSheet('color:rgb(255, 99, 94); border-bottom: 2px solid rgb(255, 99, 94);')

        threading.Timer(Constants.RefreshRates.MESSAGES_TIME, self.highlight_field, args=(field, -1)).start()

    def clear_fields(self) -> None:
        """Clears all input fields in the form."""
        self.ui_components['username_lineEdit'].clear()
        self.ui_components['password_lineEdit'].clear()
        self.ui_components['confirm_password_lineEdit'].clear()

    def get_fields(self) -> dict:
        """
        Retrieves and validates the input data from all form fields.

        Returns:
            dict: A dictionary of the validated form data, or None if any field is missing.
        """
        flag = True
        username = self.ui_components['username_lineEdit'].text()
        if not username:
            self.highlight_field(field='username_lineEdit', level=Constants.MessagesLevels.ERROR)
            flag = False

        password = self.ui_components['password_lineEdit'].text()
        if not password:
            self.highlight_field(field='password_lineEdit', level=Constants.MessagesLevels.ERROR)
            flag = False

        confirm_password = self.ui_components['confirm_password_lineEdit'].text()
        if not confirm_password:
            self.highlight_field(field='confirm_password_lineEdit', level=Constants.MessagesLevels.ERROR)
            flag = False

        role = self.ui_components['role_comboBox'].currentText()
        if not role:
            self.highlight_field(field='role_comboBox', level=Constants.MessagesLevels.ERROR)
            flag = False

        if not flag:
            self.set_message(message=Messages.Messages.EMPTY_FIELD, level=Constants.MessagesLevels.ERROR)
            return

        return {
            Constants.Keys.USERNAME_KEY: username,
            Constants.Keys.PASSWORD_KEY: password,
            Constants.Keys.CONFIRM_PASSWORD_KEY: confirm_password,
            Constants.Keys.ROLE_KEY: role
        }

    def set_fields(self, user_info: dict) -> None:
        """
        Sets the input fields based on provided user information.

        Args:
            user_info (dict): A dictionary containing user details to populate the form.
        """
        self.ui_components['username_lineEdit'].setText(user_info[Constants.Keys.USERNAME_KEY])
        self.ui_components['password_lineEdit'].setText(Constants.ReservedPassword.RESERVED_PASSWORD)
        self.ui_components['confirm_password_lineEdit'].setText(Constants.ReservedPassword.RESERVED_PASSWORD)
        self.ui_components['role_comboBox'].setCurrentText(user_info[Constants.Keys.ROLE_KEY])

    def apply(self):
        """
        Processes the changes and validates the input before accepting the edits.
        """
        edited_user_info = self.get_fields()
        if edited_user_info:
            self.edited_user_info = edited_user_info
            self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_ui = editUser_UI()
    ret = main_ui.show_win()
    print(ret)

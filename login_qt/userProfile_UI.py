import time
from typing import Callable, Union
import threading

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
from PySide6.QtCore import Qt, QPoint
from LoginUIFiles.userProfile import Ui_userProfile
from LoginuiUtils.eyeButtonHandler import eyeButtonHandler
from LoginuiUtils.editButton import editButton
from LoginuiUtils.deleteButton import deleteButton
from LoginuiUtils.messageBox import messageBox
from LoginuiUtils.editUserUI import editUser_UI
from LoginConstants import Constants
from LoginConstants import Messages

class userProfile_UI(QDialog):
    """
    A user interface for managing user profiles, providing functionalities like login,
    password change, username change, viewing all users, and signup through a single dialog window.
    """

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_userProfile()
        self.ui.setupUi(self)

        # Set up the window with no frame and a translucent background
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Initialize UI components and connect actions
        self.__define_ui_components()
        self.__connect_ui_components()

        # Set up additional pages and their respective callbacks
        self.__define_pages_ui_obj()
        self.__set_accept_callback()
        self.__set_change_page_callback()

        # Center the dialog on the screen
        self.__center()

        # Variables to handle window dragging
        self.offset = None
        self.change_page_external_callback = None
        self.logined_user = None

    def __center(self) -> None:
        """Centers the dialog on the screen based on the current primary screen's geometry."""
        primary_screen = QApplication.primaryScreen()
        if primary_screen:
            screen_geometry = primary_screen.geometry()
            center_point = screen_geometry.center()
            self.move(center_point.x() - self.frameGeometry().width() // 2,
                      center_point.y() - self.frameGeometry().height() // 2)

    def __define_ui_components(self) -> None:
        """
        Defines core components of the UI, mapping them for easy access and interaction.
        """
        self.ui_components: dict[str, Union[QFrame, QStackedWidget, QPushButton]] = {
            'top_frame': self.ui.top_frame,
            'main_stackedWidget': self.ui.stackedWidget,
            'close_btn': self.ui.close_btn,
            'menu_btn': self.ui.menu_btn,
            'login_btn': self.ui.login_btn,
            'change_username_btn': self.ui.change_username_btn,
            'change_password_btn': self.ui.change_password_btn,
            'signup_btn': self.ui.signup_btn,
        }

    def __connect_ui_components(self) -> None:
        """Connects signals to their corresponding slots for interaction handling."""
        self.ui_components['close_btn'].clicked.connect(self.close_win)
        self.ui_components['menu_btn'].clicked.connect(lambda: self.change_page(Constants.UIPages.MENU))

    def __define_pages_ui_obj(self) -> None:
        """Initializes objects for each page managed by the main stacked widget."""
        self.menu_ui = menuUI(self.ui)
        self.login_ui = loginUI(self.ui)
        self.change_password_ui = changePasswordUI(self.ui)
        self.change_username_ui = changeUsernameUI(self.ui)
        self.all_users_ui = allUsersUI(self.ui)
        self.signup_ui = signupUI(self.ui)

    def __set_accept_callback(self) -> None:
        """
        Sets accept callbacks for each UI component that might issue an accept command.
        Typically, this is used for handling successful operations or confirmations.
        """
        self.menu_ui.set_accept_callback(self.accept)
        self.login_ui.set_accept_callback(self.accept)
        self.change_password_ui.set_accept_callback(self.accept)
        self.change_username_ui.set_accept_callback(self.accept)
        self.signup_ui.set_accept_callback(self.accept)

    def __set_change_page_callback(self) -> None:
        """
        Sets change page callbacks for each UI component that might issue an change page command.
        """
        self.menu_ui.set_change_page_callback(self.change_page)

    def show_win(self, 
            page: int=Constants.UIPages.MENU, 
            accessible_pages: list[int]=[
                Constants.UIPages.CHANGE_USERNAME, 
                Constants.UIPages.CHANGE_PASSWORD, 
                Constants.UIPages.ALL_USERS,
                Constants.UIPages.SIGNUP,
            ]
        ) -> None:
        """Shows the window and sets the initial page.

        Args:
            page (int, optional): Initial page index. Defaults to Constants.UIPages.MENU.

        Returns:
            bool: accept or reject.
        """
        self.change_page(page=page)
        self.menu_ui.set_accessible_pages(accessible_pages)
        return self.exec()

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
            if time.time() - self.move_refresh_time > Constants.RefreshRates.WINDOW_MOVE:
                self.move_refresh_time = time.time()
                self.move(self.pos() + QPoint(event.scenePosition().x(), event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        """Finalizes the dragging operation by clearing the offset."""
        self.offset = None
        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event):
        """Connect enter key press event into appropriate pushButton click.
        """
        if event.key() == 16777220:  # Enter key
            if self.ui_components['main_stackedWidget'].currentIndex() == Constants.UIPages.LOGIN:
                self.ui_components['login_btn'].click()
            if self.ui_components['main_stackedWidget'].currentIndex() == Constants.UIPages.CHANGE_USERNAME:
                self.ui_components['change_username_btn'].click()
            if self.ui_components['main_stackedWidget'].currentIndex() == Constants.UIPages.CHANGE_PASSWORD:
                self.ui_components['change_password_btn'].click()
            if self.ui_components['main_stackedWidget'].currentIndex() == Constants.UIPages.SIGNUP:
                self.ui_components['signup_btn'].click()

    def set_change_page_external_callback(self, func: Callable[[int], None]) -> None:
        """Sets a callback function that is called when changing pages within the dialog,
        allowing external actions to be triggered on page changes.

        Args:
            func (Callable[[int], None]): Callback function.
        """
        self.change_page_external_callback = func

    def call_change_page_external_callback(self, page: int):
        """Calls the change page callback function, if set."""
        if self.change_page_external_callback:
            return self.change_page_external_callback(page)

    def change_page(self, page: int) -> None:
        """Changes the current page of the main stacked widget to the specified page index,
        and triggers any associated page change actions.

        Args:
            page (int): Specified page index.
        """
        self.ui_components['main_stackedWidget'].setCurrentIndex(page)
        if page == Constants.UIPages.MENU or page == Constants.UIPages.LOGIN:
            self.ui_components['menu_btn'].setVisible(False)
        else:
            self.ui_components['menu_btn'].setVisible(True)
        self.call_change_page_external_callback(page)

    def is_logined(self) -> bool:
        """Check whether any user loged-in or not.

        Returns:
            bool: True if any user loged-in.
        """
        return self.logined_user is not None

    def get_logined_user(self) -> dict:
        """
        Retrieves the currently logged-in user's info.

        Returns:
            dict: The information of the currently logged-in user.
        """
        return self.logined_user

class pagesUI:
    """
    Base class for individual pages within a user profile dialog in a Qt application.
    This class provides common functionalities like setting messages, clearing fields,
    and handling UI callbacks across different pages.
    """

    def __init__(self, ui: Ui_userProfile) -> None:
        """
        Initializes the pagesUI with a reference to the overall user interface.

        Args:
            ui: The user interface this page is part of, typically passed from a parent QDialog.
        """
        self.ui = ui
        self.ui_components: dict[str, QWidget] = {}

        # Setup the UI components specific to this page
        self.define_ui_components()
        self.connect_ui_components()

        # Optional callbacks for page-specific actions
        self.accept_callback = None

    def define_ui_components(self) -> None:
        """Defines the UI components that are part of this page. To be implemented by subclasses."""
        pass

    def connect_ui_components(self) -> None:
        """Connects UI components like buttons and inputs to their respective functions. To be implemented by subclasses."""
        pass

    def clear_fields(self) -> None:
        """Clears all the input fields on the page. To be implemented by subclasses where applicable."""
        pass

    def get_fields(self) -> dict:
        """Retrieves the data from the input fields. To be implemented by subclasses to return data in a dictionary format."""
        pass

    def set_accept_callback(self, func: Callable[[], None]) -> None:
        """
        Sets a callback function that is called when an accept-related event is triggered.

        Args:
            func (Callable): A callback function to be executed on accept events.
        """
        self.accept_callback = func

    def call_accept_callback(self):
        """
        Calls the accept callback function if it has been set, allowing for custom actions
        when page-specific operations (like saving data) are successfully completed.
        """
        if self.accept_callback:
            return self.accept_callback()

    def set_message(self, message: str, level: int = 0) -> None:
        """
        Displays a message on the page with specific styling based on the message's severity level.

        Args:
            message (str): The message to display.
            level (int): The severity level of the message (info, warning, or error).
        """
        styles = {
            Constants.MessagesLevels.INFO: 'color:rgb(84, 156, 86);',
            Constants.MessagesLevels.WARNING: 'color:rgb(255, 255, 94);',
            Constants.MessagesLevels.ERROR: 'color:rgb(255, 99, 94);'
        }
        style = styles.get(level, 'color:rgb(84, 156, 86);')  # Default to info if level is unknown
        self.ui_components['message_label'].setStyleSheet(style)
        self.ui_components['message_label'].setText(message)

        # Clear the message after a set time
        if message:
            threading.Timer(Constants.RefreshRates.MESSAGES_TIME, self.set_message, args=('',)).start()

    def highlight_field(self, field: str, level: int = 0):
        """
        Highlights an input field to indicate an issue, using colors and styles based on the message level.

        Args:
            field (str): The name of the field to highlight.
            level (int): The severity level for the highlighting.
        """
        # Define styles based on severity levels
        styles = {
            Constants.MessagesLevels.INFO: 'color:rgb(84, 156, 86); border-bottom: 2px solid rgb(84, 156, 86);',
            Constants.MessagesLevels.WARNING: 'color:rgb(255, 255, 94); border-bottom: 2px solid rgb(255, 255, 94);',
            Constants.MessagesLevels.ERROR: 'color:rgb(255, 99, 94); border-bottom: 2px solid rgb(255, 99, 94);'
        }
        style = styles.get(level, '')
        self.ui_components[field].setStyleSheet(style)

        # Reset the style after a delay
        if level >= 0:
            threading.Timer(Constants.RefreshRates.MESSAGES_TIME, self.highlight_field, args=(field, -1)).start()
        else:
            self.ui_components[field].setStyleSheet('')

class menuUI(pagesUI):
    def __init__(self, ui) -> None:
        """
        Initialize the menuUI with a reference to the main user interface.

        Args:
            ui: The main user interface object which this page belongs to.
        """
        super(menuUI, self).__init__(ui)

        # Optional callbacks for page-specific actions
        self.change_page_callback = None
        self.logout_api_callback = None

    def define_ui_components(self) -> None:
        """
        Defines and maps the UI components necessary for the login functionality.
        """
        self.ui_components: dict[str, Union[QPushButton, QFrame]] = {
            #----------PushButtons------------
            'change_username_btn': self.ui.show_change_username_btn,
            'change_password_btn': self.ui.show_change_password_btn,
            'all_users_btn': self.ui.show_all_users_btn,
            'signup_btn': self.ui.show_signup_btn,
            'logout_btn': self.ui.show_logout_btn,

            #----------Lines------------
            'change_username_line': self.ui.change_username_line,
            'change_password_line': self.ui.change_password_line,
            'all_users_line': self.ui.all_users_line,
            'signup_line': self.ui.signup_line,
        }

        self.button_to_page_mapper: dict[QPushButton, int] = {
            self.ui_components['change_username_btn']: Constants.UIPages.CHANGE_USERNAME,
            self.ui_components['change_password_btn']: Constants.UIPages.CHANGE_PASSWORD,
            self.ui_components['all_users_btn']: Constants.UIPages.ALL_USERS,
            self.ui_components['signup_btn']: Constants.UIPages.SIGNUP,
        }

        self.button_to_line_mapper: dict[QPushButton, QFrame] = {
            self.ui_components['change_username_btn']: self.ui_components['change_username_line'],
            self.ui_components['change_password_btn']: self.ui_components['change_password_line'],
            self.ui_components['all_users_btn']: self.ui_components['all_users_line'],
            self.ui_components['signup_btn']: self.ui_components['signup_line'],
        }

    def connect_ui_components(self) -> None:
        """
        Connects UI components like buttons to their respective handling functions.
        """
        for btn, page in self.button_to_page_mapper.items():
            btn.clicked.connect(
                self.call_change_page_callback(page)
            )

        self.ui_components['logout_btn'].clicked.connect(
            self.logout
        )

    def set_change_page_callback(self, func: Callable[[int], None]) -> None:
        """
        Sets a callback function that change current page to given index.

        Args:
            func (Callable): A callback function to be executed on change page events.
        """
        self.change_page_callback = func

    def call_change_page_callback(self, page: int):
        """
        Calls the change page callback function if it has been set.

        Args:
            page (int): Specified page index.
        """
        def func():
            if self.change_page_callback:
                return self.change_page_callback(page)
        
        return func

    def set_logout_callback(self, callback: Callable[[None], bool]) -> None:
        """
        Sets the callback function that will be called to perform the actual logout operation.

        Args:
            callback (Callable[[None], bool]): The function to call with the user's logout.
        """
        self.logout_api_callback = callback

    def call_logout_callback(self,):
        """
        Calls the logout callback with the user's information.

        Returns:
            bool: The result of the logout operation.
        """
        if self.logout_api_callback:
            return self.logout_api_callback()

    def logout(self) -> bool:
        """
        Attempts to log the user out.

        Returns:
            bool: True if logout is successful, otherwise False.
        """
        cmb = messageBox(
            Messages.Messages.CONFIRM_LOGOUT_USER_TITLE,
            Messages.Messages.CONFIRM_LOGOUT_USER_MESSAGE,
            buttons=['yes', 'cancel'],
            icon_type='question',
        )
        ret = cmb.render()
        if ret == 'yes':
            res = self.call_logout_callback()
            if res:
                self.call_accept_callback()
                return True
        return False
    
    def set_accessible_pages(self, accessible_pages: list[int]):
        """This is a function to visible or unvisible pages buttons in menu page

        Args:
            accessible_pages (list[int]): List of accessible page
        """
        for btn in self.button_to_page_mapper:
            if self.button_to_page_mapper[btn] not in accessible_pages:
                btn.setVisible(False)
                self.button_to_line_mapper[btn].setVisible(False)
            else:
                btn.setVisible(True)
                self.button_to_line_mapper[btn].setVisible(True)

class loginUI(pagesUI):
    """
    A user interface class dedicated to the login functionality. This class handles
    user authentication inputs and interactions within a larger user profile management system.
    """

    def __init__(self, ui) -> None:
        """
        Initialize the loginUI with a reference to the main user interface.

        Args:
            ui: The main user interface object which this page belongs to.
        """
        super(loginUI, self).__init__(ui)
        self.login_api_callback = None  # API callback for the login process

    def define_ui_components(self) -> None:
        """
        Defines and maps the UI components necessary for the login functionality.
        """
        self.ui_components: dict[str, Union[QLineEdit, QPushButton, QLabel]] = {
            #------------LineEdits------------
            'username_lineEdit': self.ui.login_username_lineEdit,
            'password_lineEdit': self.ui.login_password_lineEdit,

            #----------PushButtons------------
            'password_eye_btn': self.ui.login_eye_btn,
            'login_btn': self.ui.login_btn,

            #---------------Label-------------
            'message_label': self.ui.login_message_label
        }

    def connect_ui_components(self) -> None:
        """
        Connects UI components like buttons to their respective handling functions.
        """
        # Set up the password visibility toggle handler
        self.password_eye_handler = eyeButtonHandler(
            self.ui_components['password_eye_btn'],
            self.ui_components['password_lineEdit']
        )
        # Connect the login button to the login method
        self.ui_components['login_btn'].clicked.connect(self.login)

    def clear_fields(self) -> None:
        """
        Clears all input fields on the login page to reset the form.
        """
        self.ui_components['username_lineEdit'].clear()
        self.ui_components['password_lineEdit'].clear()

    def get_fields(self) -> dict:
        """
        Retrieves and validates the input from the login fields.

        Returns:
            dict: A dictionary containing the user's login credentials if valid, otherwise returns None.
        """
        flag = True
        username = self.ui_components['username_lineEdit'].text()
        password = self.ui_components['password_lineEdit'].text()

        # Validate inputs and highlight fields if necessary
        if not username:
            self.highlight_field('username_lineEdit', Constants.MessagesLevels.ERROR)
            flag = False
        if not password:
            self.highlight_field('password_lineEdit', Constants.MessagesLevels.ERROR)
            flag = False

        if not flag:
            self.set_message(Messages.Messages.EMPTY_FIELD, Constants.MessagesLevels.ERROR)
            return

        return {
            Constants.Keys.USERNAME_KEY: username,
            Constants.Keys.PASSWORD_KEY: password
        }

    def set_login_callback(self, callback: Callable[[dict], bool]) -> None:
        """
        Sets the callback function that will be called to perform the actual login operation.

        Args:
            callback (Callable[[dict], bool]): The function to call with the user's credentials.
        """
        self.login_api_callback = callback

    def call_login_callback(self, user_info: dict):
        """
        Calls the login callback with the user's information.

        Args:
            user_info (dict): The user's login credentials.

        Returns:
            bool: The result of the login operation.
        """
        if self.login_api_callback:
            return self.login_api_callback(user_info)

    def login(self) -> bool:
        """
        Retrieves user credentials, validates them, and attempts to log the user in.

        Returns:
            bool: True if login is successful, otherwise False.
        """
        user_info = self.get_fields()
        if user_info:
            res = self.call_login_callback(user_info)
            if res:
                self.clear_fields()
                self.call_accept_callback()
                return True
        return False

class changePasswordUI(pagesUI):
    """
    A class to handle user interface for password change operations within a user profile management system.
    It provides fields for entering the current password, new password, and confirmation of the new password.
    """

    def __init__(self, ui: Ui_userProfile):
        """
        Initializes the changePasswordUI class with a user interface setup.
        
        Args:
            ui (Ui_userProfile): The main user interface context this class is part of.
        """
        super(changePasswordUI, self).__init__(ui)
        self.change_password_api_callback = None  # API callback for executing the password change.


    def define_ui_components(self):
        """
        Defines and maps the UI components necessary for the change password functionality.
        """
        self.ui_components: dict[str, Union[QLineEdit, QPushButton, QLabel]] = {
            #------------LineEdits------------
            'current_password_lineEdit': self.ui.change_current_password_lineEdit,
            'new_password_lineEdit': self.ui.change_new_password_lineEdit,
            'confirm_password_lineEdit': self.ui.change_confirm_password_lineEdit,

            #-----------PushButtons-----------
            'current_password_eye_btn': self.ui.change_current_password_eye_btn,
            'new_password_eye_btn': self.ui.change_new_password_eye_btn,
            'confirm_password_eye_btn': self.ui.change_confirm_password_eye_btn,
            'change_password_btn': self.ui.change_password_btn,
            
            #---------------Label-------------
            'message_label': self.ui.change_password_message_label
        }

    def connect_ui_components(self) -> None:
        """
        Connects the UI components such as buttons and password fields to their respective event handlers.
        This method initializes the visibility toggle handlers for the password fields and connects
        the change password button to its functionality.
        """
        self.current_password_eye_handler = eyeButtonHandler(
            self.ui_components['current_password_eye_btn'],
            self.ui_components['current_password_lineEdit']
        )

        self.new_password_eye_handler = eyeButtonHandler(
            self.ui_components['new_password_eye_btn'],
            self.ui_components['new_password_lineEdit']
        )

        self.confirm_password_eye_handler = eyeButtonHandler(
            self.ui_components['confirm_password_eye_btn'],
            self.ui_components['confirm_password_lineEdit']
        )

        self.ui_components['change_password_btn'].clicked.connect(self.change_password)

    def clear_fields(self) -> None:
        """
        Clears all the input fields related to the password change form.
        """
        self.ui_components['current_password_lineEdit'].clear()
        self.ui_components['new_password_lineEdit'].clear()
        self.ui_components['confirm_password_lineEdit'].clear()

    def get_fields(self) -> dict:
        """
        Retrieves and validates the data from the password fields.

        Returns:
            dict: A dictionary containing the password data if all fields are valid; None if any field is invalid.
        """
        flag = True
        current_password = self.ui_components['current_password_lineEdit'].text()
        if not current_password:
            self.highlight_field(field='current_password_lineEdit', level=Constants.MessagesLevels.ERROR)
            flag = False

        new_password = self.ui_components['new_password_lineEdit'].text()
        if not new_password:
            self.highlight_field(field='new_password_lineEdit', level=Constants.MessagesLevels.ERROR)
            flag = False

        confirm_password = self.ui_components['confirm_password_lineEdit'].text()
        if not confirm_password:
            self.highlight_field(field='confirm_password_lineEdit', level=Constants.MessagesLevels.ERROR)
            flag = False

        if not flag:
            self.set_message(message=Messages.Messages.EMPTY_FIELD, level=Constants.MessagesLevels.ERROR)
            return 

        return {
            Constants.Keys.CURRENT_PASSWORD_KEY: current_password, 
            Constants.Keys.NEW_PASSWORD_KEY: new_password,
            Constants.Keys.CONFIRM_PASSWORD_KEY: confirm_password
        }

    def set_change_password_callback(self, callback: Callable[[dict], bool]) -> None:
        """
        Sets the callback function that will be called to process the password change.

        Args:
            callback (Callable[[dict], bool]): The function that processes the password change.
        """
        self.change_password_api_callback = callback

    def call_change_password_callback(self, password_info: dict):
        """
        Invokes the password change callback if set, passing the user's password information.

        Args:
            password_info (dict): The dictionary containing the password information.

        Returns:
            bool: The result of the password change operation.
        """
        if self.change_password_api_callback:
            return self.change_password_api_callback(password_info)

    def change_password(self) -> bool:
        """
        Attempts to change the user's password by validating and submitting the password information.

        Returns:
            bool: True if the password change is successful, otherwise False.
        """
        password_info = self.get_fields()
        if password_info:
            res = self.call_change_password_callback(password_info)
            if res:
                self.clear_fields()
                self.call_accept_callback()
                return True
        else:
            return False

class changeUsernameUI(pagesUI):
    """
    Handles the user interface for changing usernames within a user profile management system. This class
    provides the necessary UI components and functionality to manage username updates.
    """

    def __init__(self, ui: Ui_userProfile):
        """
        Initialize the changeUsernameUI with a reference to the user interface.

        Args:
            ui (Ui_userProfile): The user interface that this class is part of.
        """
        super(changeUsernameUI, self).__init__(ui)
        self.change_username_api_callback = None  # Callback for handling the username change API.

    def define_ui_components(self) -> None:
        """
        Defines and maps the UI components necessary for the username change functionality.
        """
        self.ui_components: dict[str, Union[QLineEdit, QPushButton, QLabel]] = {
            #------------LineEdits------------
            'current_username_lineEdit': self.ui.change_current_username_lineEdit,
            'new_username_lineEdit': self.ui.change_new_username_lineEdit,

            #------------PushButtons------------
            'change_username_btn': self.ui.change_username_btn,

            #---------------Label-------------
            'message_label': self.ui.change_username_message_label
        }

    def connect_ui_components(self) -> None:
        """
        Connects the UI components such as the change username button to their respective handling functions.
        """
        self.ui_components['change_username_btn'].clicked.connect(self.change_username)

    def clear_fields(self) -> None:
        """
        Clears all the input fields on the username change page.
        """
        self.ui_components['current_username_lineEdit'].clear()
        self.ui_components['new_username_lineEdit'].clear()

    def get_fields(self) -> dict:
        """
        Retrieves and validates the new username from the input field.

        Returns:
            dict: A dictionary containing the new username if valid; None if validation fails.
        """
        flag = True
        new_username = self.ui_components['new_username_lineEdit'].text()
        if not new_username:
            self.highlight_field(field='new_username_lineEdit', level=Constants.MessagesLevels.ERROR)
            flag = False

        if not flag:
            self.set_message(message=Messages.Messages.EMPTY_FIELD, level=Constants.MessagesLevels.ERROR)
            return 

        return {
            Constants.Keys.NEW_USERNAME_KEY: new_username
        }
    
    def set_current_username(self, username: str) -> None:
        """
        Sets the current username in the current username input field.

        Args:
            username (str): The current username to display.
        """
        self.ui_components['current_username_lineEdit'].setText(username)

    def set_change_username_callback(self, callback: Callable[[dict], bool]) -> None:
        """
        Sets the callback function that will be called to process the username change.

        Args:
            callback (Callable[[dict], bool]): The function to call with the username information.
        """
        self.change_username_api_callback = callback

    def call_change_username_callback(self, username_info: dict):
        """
        Invokes the username change callback if set, passing the user's new username information.

        Args:
            username_info (dict): The dictionary containing the new username details.

        Returns:
            bool: The result of the username change operation.
        """
        if self.change_username_api_callback:
            return self.change_username_api_callback(username_info)

    def change_username(self) -> None:
        """
        Processes the username change by validating input and calling the username change API.

        Returns:
            bool: True if username change is successful, otherwise False.
        """
        username_info = self.get_fields()
        if username_info:
            res = self.call_change_username_callback(username_info)
            if res:
                self.clear_fields()
                self.call_accept_callback()
                return True
        return False

class allUsersUI(pagesUI):
    """
    Provides a user interface for managing a table of users including actions like edit and delete.
    This class extends pagesUI to integrate seamlessly with the larger user profile management system.
    """

    def __init__(self, ui: Ui_userProfile) -> None:
        """
        Initializes the allUsersUI with necessary configurations and setups the UI components.

        Args:
            ui (Ui_userProfile): The user interface that this class is part of.
        """
        super(allUsersUI, self).__init__(ui)

        self.delete_user_api_callback = None  # API callback for deleting a user.
        self.edit_user_api_callback = None    # API callback for editing a user.

        self.table_headers = [
            'edit',
            'delete',
            Constants.Keys.USERNAME_KEY,
            Constants.Keys.PASSWORD_KEY,
            Constants.Keys.ROLE_KEY,
        ]

        self.table_columns_width = [
            6,
            6,
            120,
            120,
            120,
        ]

        self.setup_table()  # Initial setup of the user table.

    def define_ui_components(self) -> None:
        """
        Defines the main UI components used in the user table interface.
        """
        self.ui_components: dict[str, Union[QTableWidget, QLabel]] = {
            #------------Tables------------
            'all_users_table': self.ui.all_users_table,  # The table displaying all users.

            #---------------Labels-------------
            'message_label': self.ui.all_users_message_label,  # Label for displaying messages.
        }

    def connect_ui_components(self) -> None:
        """
        Connects the UI components.
        """
        pass

    def clear_fields(self) -> None:
        """
        Clears the user table completely.
        """
        self.ui_components['all_users_table'].clear()

    def get_fields(self) -> dict:
        """
        This method would typically collect data from fields, but since this UI deals with a table,
        it does not need to collect fields in the typical sense.
        """
        pass

    def set_delete_user_callback(self, callback: Callable[[dict], bool]) -> None:
        """
        Sets the callback function for deleting a user.

        Args:
            callback (Callable[[dict], bool]): The function to call with the user's information for deletion.
        """
        self.delete_user_api_callback = callback

    def call_delete_user_callback(self, user_info: dict):
        """
        Calls the delete user API callback function if it has been set.

        Args:
            user_info (dict): A dictionary containing the details of the user to be deleted.

        Returns:
            The result of the delete operation from the callback function, if any, otherwise `None`.
        """
        if self.delete_user_api_callback:
            return self.delete_user_api_callback(user_info)
        
    def set_edit_user_callback(self, callback: Callable[[dict, dict], bool]) -> None:
        """
        Sets the callback function for editing a user.

        Args:
            callback (Callable[[dict, dict], bool]): The function to call with the original and edited user information.
        """
        self.edit_user_api_callback = callback

    def call_edit_user_callback(self, user_info: dict, edited_user_info: dict):
        """
        Calls the edit user API callback function if it has been set.

        Args:
            user_info (dict): A dictionary containing the details of the user to be edited.

        Returns:
            The result of the edit operation from the callback function, if any, otherwise `None`.
        """
        if self.edit_user_api_callback:
            return self.edit_user_api_callback(user_info, edited_user_info)

    def setup_table(self) -> None:
        """
        Sets up the initial configuration of the user table including column headers and widths.
        """
        self.clear_fields()
        self.ui_components['all_users_table'].setColumnCount(len(self.table_headers))
        self.ui_components['all_users_table'].setRowCount(0)
        self.ui_components['all_users_table'].setHorizontalHeaderLabels(self.table_headers)
        self.ui_components['all_users_table'].resizeColumnsToContents()
        for i in range(len(self.table_headers)):
            self.ui_components['all_users_table'].setColumnWidth(i, self.table_columns_width[i])

    def append_table_row(self, user_info: dict, edit: bool=True, delete: bool=True):
        """
        Appends a row to the user table with the specified user information and control buttons.

        Args:
            user_info (dict): Dictionary containing user details like username and role.
            edit (bool): If true, an edit button is enabled for this row.
            delete (bool): If true, a delete button is enabled for this row.
        """
        row_position = self.ui_components['all_users_table'].rowCount()
        self.ui_components['all_users_table'].insertRow(row_position)

        for i, header in enumerate(self.table_headers):
            if header=='edit':
                edit_btn = editButton()
                self.ui_components['all_users_table'].setCellWidget(row_position, 0, edit_btn)
                edit_btn.clicked.connect(lambda: self.edit_user(edit_btn.pos(), user_info))
                edit_btn.setEnabled(edit)

            elif header=='delete':
                delete_btn = deleteButton()
                self.ui_components['all_users_table'].setCellWidget(row_position, 1, delete_btn)
                delete_btn.clicked.connect(lambda: self.delete_user(delete_btn.pos(), user_info))
                delete_btn.setEnabled(delete)

            elif header==Constants.Keys.PASSWORD_KEY:
                item = QTableWidgetItem(Constants.ReservedPassword.RESERVED_PASSWORD)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui_components['all_users_table'].setItem(row_position, i, item)

            else:
                item = QTableWidgetItem(str(user_info.get(header, '')))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui_components['all_users_table'].setItem(row_position, i, item)

    def delete_table_row(self, pos):
        """
        Deletes a row from the user table at the specified position.

        This method directly manipulates the table widget by removing a row based on the position provided, which is typically
        triggered by a delete operation from the user interface.

        Args:
            pos (QPoint): The position in the table, typically provided by the position of a delete button.
        """
        row = self.ui_components['all_users_table'].indexAt(pos).row()
        self.ui_components['all_users_table'].removeRow(row)

    def edit_table_row(self, pos, user_info):
        """
        Updates a table row with new user information at the specified position.

        This method is called typically after a user has edited their details through a dialog. It updates the respective row
        in the table to reflect these changes. Special handling is included for password fields to maintain security by not
        displaying actual passwords.

        Args:
            pos (QPoint): The position in the table, typically provided by the position of an edit button.
            user_info (dict): A dictionary containing updated user information.
        """
        row = self.ui_components['all_users_table'].indexAt(pos).row()
        for i, header in enumerate(self.table_headers):
            if header==Constants.Keys.PASSWORD_KEY:
                item = QTableWidgetItem(Constants.ReservedPassword.RESERVED_PASSWORD)
                item.setTextAlignment(Qt.AlignCenter)
                self.ui_components['all_users_table'].setItem(row, i, item)
            else:
                item = QTableWidgetItem(str(user_info.get(header, '')))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui_components['all_users_table'].setItem(row, i, item)

    def delete_user(self, pos, user_info):
        """
        Triggers the delete operation for a specified user.

        Args:
            pos (QPoint): Position in the table, used to determine the row to delete.
            user_info (dict): Information of the user to be deleted.

        Returns:
            bool: True if user delete is successful, otherwise False.
        """
        cmb = messageBox(
            Messages.Messages.CONFIRM_DELETE_USER_TITLE,
            Messages.Messages.CONFIRM_DELETE_USER_MESSAGE,
            buttons=['yes', 'cancel'],
            icon_type='question',
        )
        ret = cmb.render()
        if ret == 'yes':
            res = self.call_delete_user_callback(user_info)
            if res:
                self.delete_table_row(pos)
                return True
        return False

    def edit_user(self, pos, user_info):
        """
        Opens the edit dialog for a specified user and applies changes if confirmed.

        Args:
            pos (QPoint): Position in the table, used to determine the row to edit.
            user_info (dict): Information of the user being edited.
        
        Returns:
            bool: True if user edit is successful, otherwise False.
        """
        edit_user_dialog = editUser_UI()
        edited_user_info = edit_user_dialog.show_win(user_info)
        if edited_user_info:
            res = self.call_edit_user_callback(user_info, edited_user_info)
            if res:
                self.edit_table_row(pos, edited_user_info)
                return True
        return False

class signupUI(pagesUI):
    """
    Provides a user interface for signing up new users, handling user input and interactions 
    necessary for creating user accounts.
    """

    def __init__(self, ui: Ui_userProfile) -> None:
        """
        Initializes the signupUI with necessary setups for user interface components.

        Args:
            ui (Ui_userProfile): The user interface that this class is part of.
        """
        super(signupUI, self).__init__(ui)

        self.signup_api_callback = None  # API callback for handling user registration.
        self.set_role_comboBox_items()  # Populate the roles dropdown at initialization.

    def define_ui_components(self) -> None:
        """
        Defines and maps UI components such as input fields, buttons, and labels required for the signup process.
        """
        self.ui_components: dict[str, Union[QLineEdit, QPushButton, QComboBox, QLabel]] = {
            #------------LineEdits------------
            'username_lineEdit': self.ui.signup_username_lineEdit,
            'password_lineEdit': self.ui.signup_password_lineEdit,
            'confirm_password_lineEdit': self.ui.signup_confirm_password_lineEdit,

            #-----------PushButtons-----------
            'password_eye_btn': self.ui.signup_password_eye_btn,
            'confirm_password_eye_btn': self.ui.signup_confirm_password_eye_btn,
            'signup_btn': self.ui.signup_btn,

            #-----------ComboBoxes-----------
            'role_comboBox': self.ui.signup_role_comboBox,
            
            #---------------Label-------------
            'message_label': self.ui.signup_message_label
        }

    def connect_ui_components(self) -> None:
        """
        Connects UI components to their respective functionalities, like setting up eye buttons for toggling
        password visibility and connecting the signup button to its action.
        """
        self.password_eye_handler = eyeButtonHandler(
            self.ui_components['password_eye_btn'],
            self.ui_components['password_lineEdit']
        )

        self.confirm_password_eye_handler = eyeButtonHandler(
            self.ui_components['confirm_password_eye_btn'],
            self.ui_components['confirm_password_lineEdit']
        )

        self.ui_components['signup_btn'].clicked.connect(self.signup)

    def clear_fields(self) -> None:
        """
        Clears all input fields on the signup form.
        """
        self.ui_components['username_lineEdit'].clear()
        self.ui_components['password_lineEdit'].clear()
        self.ui_components['confirm_password_lineEdit'].clear()

    def get_fields(self) -> dict:
        """
        Retrieves and validates the input from the signup form fields.

        Returns:
            dict: A dictionary containing the user's input data if all fields are valid; otherwise, None.
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
    
    def set_role_comboBox_items(self,) -> None:
        """
        Populates the role ComboBox with roles available from the Constants module.
        """
        items = [v for k, v in vars(Constants.Roles).items() if not(k.startswith('__'))]
        self.ui_components['role_comboBox'].clear()
        self.ui_components['role_comboBox'].addItems(items)
    
    def set_singup_callback(self, callback: Callable[[dict], bool]) -> None:
        """
        Sets the callback function that will be called to process the signup operation.

        Args:
            callback (Callable[[dict], bool]): The function to call with the user's signup data.
        """
        self.singup_api_callback = callback

    def call_signup_callback(self, user_info: dict):
        """
        Invokes the signup callback if set, passing the user's information for processing.

        Args:
            user_info (dict): A dictionary containing the new user's information.

        Returns:
            bool: The result of the signup operation.
        """
        if self.singup_api_callback:
            return self.singup_api_callback(user_info)

    def signup(self) -> None:
        """
        Processes the signup operation by validating input and calling the signup API.

        Returns:
            bool: True if signup is successful, otherwise False.
        """
        user_info = self.get_fields()
        if user_info:
            res = self.call_signup_callback(user_info)
            if res:
                self.clear_fields()
                self.call_accept_callback()
                return True
        return False
from PySide6.QtWidgets import QPushButton, QLineEdit
from PySide6.QtGui import QIcon

from LoginConstants.IconsPath import IconsPath

class eyeButtonHandler:
    """
    Handles the functionality of an eye button associated with a password field,
    allowing the user to toggle visibility of the password.

    Attributes:
        eye_btn (QPushButton): The button used to toggle password visibility.
        password_input (QLineEdit): The input field whose visibility is controlled.
    """

    def __init__(self, eye_btn: QPushButton, password_input: QLineEdit) -> None:
        """
        Initializes the eyeButtonHandler with a button and a password field.

        Args:
            eye_btn (QPushButton): The toggle button for showing/hiding the password.
            password_input (QLineEdit): The password field associated with this handler.
        """
        self.eye_btn = eye_btn  # The button that will toggle the password visibility
        self.password_input = password_input  # The password input field

        # Set initial state of password field to hidden (password dots)
        self.password_input.setEchoMode(QLineEdit.Password)
        # Set initial icon for the eye button to show an 'eye open' icon indicating password is hidden
        self.set_eye_icon(IconsPath.EYE_ON)
        # Flag to track whether the password is currently shown or hidden
        self.show_password_flag = False

        # Connect the button's clicked signal to the method that changes password visibility
        self.eye_btn.clicked.connect(self.change_eye_status)

    def set_eye_icon(self, icon_path: str):
        """
        Sets the icon for the eye button.

        Args:
            icon_path (str): The path to the icon to be displayed on the eye button.
        """
        icon = QIcon(icon_path)  # Load the icon from the specified path
        self.eye_btn.setIcon(icon)  # Set the loaded icon on the button

    def change_eye_status(self):
        """
        Toggles the password visibility state and updates the icon accordingly.
        """
        # Toggle the flag to reflect the new visibility state
        self.show_password_flag = not self.show_password_flag

        if self.show_password_flag:
            # If toggled to show, set the echo mode to normal (revealing the password)
            self.password_input.setEchoMode(QLineEdit.Normal)
            # Change the icon to 'eye closed' indicating that the password is visible
            self.set_eye_icon(IconsPath.EYE_OFF)
        else:
            # If toggled to hide, reset the echo mode to password (hiding the password)
            self.password_input.setEchoMode(QLineEdit.Password)
            # Change the icon back to 'eye open' indicating that the password is hidden
            self.set_eye_icon(IconsPath.EYE_ON)

from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from LoginConstants.IconsPath import IconsPath

# Stylesheets for various QMessageBox components and QPushButton appearances
CONFIRMBOX_STYLESHEET = """
    QMessageBox{ 
        background-image: url('login_qt/uiFiles/resources/Icons/logout2.png'); /* Set your image path */
        font: auto "Roboto";
        font-size: 16px;
        border-radius: 10px; /* Add this line */
        background-repeat: no-repeat;
        background-position: center;
    }

    QMessageBox QLabel#qt_msgbox_label {
        min-width: 350px;
    }
"""

# Different button styles for the QMessageBox
OK_BUTTUN_STYLE= """
    QPushButton
    {{
        background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));
        color: rgba(255, 255, 255, 210);
        border-radius: 20px;
        min-width: 100;
        max-width: 100;
        min-height: 40;
        max-height: 40;
        font-size: 14px;
        font-weight: bold;
        icon: url({0})
    }}

    QPushButton:hover
    {{
        background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));
    }}

    QPushButton:pressed
    {{
        padding-left: 5px;
        padding-top: 5px;
    }}
""".format(IconsPath.TICK)

YES_BUTTUN_STYLE= """
    QPushButton
    {{
        background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));
        color: rgba(255, 255, 255, 210);
        border-radius: 20px;
        min-width: 100;
        max-width: 100;
        min-height: 40;
        max-height: 40;
        font-size: 14px;
        font-weight: bold;
        icon: url({0})
    }}

    QPushButton:hover
    {{
        background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));
    }}

    QPushButton:pressed
    {{
        padding-left: 5px;
        padding-top: 5px;
    }}
""".format(IconsPath.TICK)

SAVE_BUTTUN_STYLE= """
    QPushButton
    {{
        background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(46, 76, 153, 255), stop:1 rgba(76, 126, 255, 255));
        color: rgba(255, 255, 255, 210);
        border-radius: 20px;
        min-width: 100;
        max-width: 100;
        min-height: 40;
        max-height: 40;
        font-size: 14px;
        font-weight: bold;
        icon: url({0})
    }}

    QPushButton:hover
    {{
        background-color: qlineargradient(spread:pad, x1:0.635, y1:1, x2:0.44, y2:0, stop:0 rgba(77, 98, 153, 255), stop:1 rgba(114, 152, 252, 255));
    }}

    QPushButton:pressed
    {{
        padding-left: 5px;
        padding-top: 5px;
    }}
""".format(IconsPath.SAVE)

CANCEL_BUTTUN_STYLE= """
    QPushButton
    {{
        border: 2px solid  rgba(46, 76, 153, 255);
        color:  rgba(46, 76, 153, 255);
        border-radius: 18px;
        min-width: 100;
        max-width: 100;
        min-height: 36;
        max-height: 36;
        font-size: 14px;
        font-weight: bold;
        icon: url({0});
    }}

    QPushButton:hover
    {{
        border: 2px solid rgba(76, 126, 255, 255);
        color:  rgba(76, 126, 255, 255);
        icon: url({1});
    }}

    QPushButton:pressed
    {{
        padding-left: 5px;
        padding-top: 5px;
    }}
""".format(IconsPath.CANCEL, IconsPath.CANCEL_HOVER)

NO_BUTTUN_STYLE= """
    QPushButton
    {{
        border: 2px solid  rgba(46, 76, 153, 255);
        color:  rgba(46, 76, 153, 255);
        border-radius: 18px;
        min-width: 100;
        max-width: 100;
        min-height: 36;
        max-height: 36;
        font-size: 14px;
        font-weight: bold;
        icon: url({0});
    }}

    QPushButton:hover
    {{
        border: 2px solid rgba(76, 126, 255, 255);
        color:  rgba(76, 126, 255, 255);
        icon: url({1});
    }}

    QPushButton:pressed
    {{
        padding-left: 5px;
        padding-top: 5px;
    }}
""".format(IconsPath.CANCEL, IconsPath.CANCEL_HOVER)

IGNORE_BUTTUN_STYLE= """
    QPushButton
    {
        border: 2px solid  rgba(46, 76, 153, 255);
        color:  rgba(46, 76, 153, 255);
        border-radius: 18px;
        min-width: 100;
        max-width: 100;
        min-height: 36;
        max-height: 36;
        font-size: 14px;
        font-weight: bold;
    }

    QPushButton:hover
    {
        border: 2px solid rgba(76, 126, 255, 255);
        color:  rgba(76, 126, 255, 255);
    }

    QPushButton:pressed
    {
        padding-left: 5px;
        padding-top: 5px;
    }
"""


class messageBox:
    """
    A customizable message box class that uses QMessageBox from PySide6 to display messages
    with specific icons, text, and a selection of buttons with custom styles.
    """

    def __init__(self, title: str, text: str, buttons: list, icon_type: str, parent=None):
        """
        Initializes the message box with the specified parameters.

        Args:
            title (str): The title of the message box.
            text (str): The main text or content of the message box.
            buttons (list): A list of strings representing the buttons to include.
            icon_type (str): A string specifying the type of icon to display (e.g., 'info', 'warning').
            parent (optional): The parent widget, default is None.
        """

        # Maps the button names to QMessageBox standard buttons
        self.STANDARD_BUTTONS = {
            'yes': QMessageBox.Yes,
            'no': QMessageBox.No,
            'cancel': QMessageBox.Cancel,
            'save': QMessageBox.Save,
            'ok': QMessageBox.Ok,
            'ignore': QMessageBox.Ignore,
        }

        # Maps the button names to their respective styles
        self.STANDARD_BUTTONS_STYLES = {
            'yes': YES_BUTTUN_STYLE,
            'no': NO_BUTTUN_STYLE,
            'cancel': CANCEL_BUTTUN_STYLE,
            'save': SAVE_BUTTUN_STYLE,
            'ignore': IGNORE_BUTTUN_STYLE,
            'ok': OK_BUTTUN_STYLE
        }

        self.buttons = buttons  # List of button names to be included

        self.msg = QMessageBox(parent=parent)  # Create a new QMessageBox
        self.msg.setWindowFlags(Qt.FramelessWindowHint)  # Frameless window for custom styling
        self.msg.setStyleSheet(CONFIRMBOX_STYLESHEET)  # Apply the custom stylesheet
        self.msg.setMinimumSize(250, 100)  # Set a minimum size for the QMessageBox

        # Determine the icon based on the type and set it
        icon_path = getattr(IconsPath, icon_type.upper(), IconsPath.INFO)
        self.icon = QPixmap(icon_path)
        self.msg.setIconPixmap(self.icon)

        # Set the formatted title and text for the message box using HTML
        html_text = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
        .title {{ color: rgb(80, 80, 80); font-size: 22px; font-weight: bold; }}
        .text {{ color: rgb(20,20, 20); font-size: 16px; }}
        </style>
        </head>
        <body>
        <p class="title">{title}</p>
        <p class="text">{text}</p>
        </body>
        </html>
        """
        self.msg.setTextFormat(Qt.RichText)  # Set the text format of the message box to RichText for HTML support
        self.msg.setText(html_text)

        # Configure the buttons for the message box
        selected_buttons_obj = QMessageBox.NoButton
        for btn_name in buttons:
            btn = self.STANDARD_BUTTONS[btn_name]
            selected_buttons_obj |= btn  # Combine buttons using bitwise OR
        self.msg.setStandardButtons(selected_buttons_obj)  # Set the buttons to display

        # Apply styles to the individual buttons
        for btn_name in buttons:
            style = self.STANDARD_BUTTONS_STYLES[btn_name]
            btn = self.msg.button(self.STANDARD_BUTTONS[btn_name])
            btn.setStyleSheet(style)

    def render(self) -> str:
        """
        Shows the message box and returns the name of the button pressed by the user.

        Returns:
            str: The name of the button pressed.
        """
        retval = self.msg.exec()  # Execute the message box and get the return value
        for btn_name in self.buttons:
            if self.STANDARD_BUTTONS[btn_name] == retval:
                return btn_name  # Return the name of the button pressed
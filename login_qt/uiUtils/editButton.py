from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from Constants.IconsPath import IconsPath

class editButton(QPushButton):
    """
    A specialized QPushButton for edit actions, featuring dynamic icon changes for
    different states to enhance the user interface experience.

    Attributes:
        TABEL_BUTTON_STYLE (str): Styling for the edit button, setting transparency and icon properties.
    """

    TABEL_BUTTON_STYLE = """
    QPushButton
        { 
            background-color: rgba(255,255,255,0);
            border: 0px solid gray;
            min-height:0px; 
            min-width:0px; 
            width:auto;
            qproperty-iconSize: 24px;
        } 
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the edit button with specified properties and setups up its visual representation
        and behavior, including normal, hover, and disabled states.

        Args:
            *args: Variable length argument list for QPushButton.
            **kwargs: Arbitrary keyword arguments for QPushButton.
        """
        super(editButton, self).__init__(*args, **kwargs)

        # Set the button size policy to fixed to maintain a consistent button size across different states.
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setSizePolicy(sizePolicy)

        # Initialize icons for different button states.
        self._icon_normal = QIcon()
        self._icon_normal.addFile(IconsPath.EDIT, mode=QIcon.Normal, state=QIcon.On)
        self._icon_normal.addFile(IconsPath.EDIT_DISABLED, mode=QIcon.Disabled, state=QIcon.Off)

        self._icon_over = QIcon(IconsPath.EDIT_HOVER)  # Icon to be used when the mouse hovers over the button.

        # Apply custom styles, set the initial icon, and adjust the cursor for better user interaction.
        self.setStyleSheet(self.TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event):
        """
        Handles the mouse entering the button's area, switching to the hover icon if the button is enabled.

        Args:
            event: Event object containing details about the mouse event.
        """
        if self.isEnabled():
            self.setIcon(self._icon_over)

    def leaveEvent(self, event):
        """
        Handles the mouse leaving the button's area, reverting the icon back to normal if the button is enabled.

        Args:
            event: Event object containing details about the mouse event.
        """
        if self.isEnabled():
            self.setIcon(self._icon_normal)

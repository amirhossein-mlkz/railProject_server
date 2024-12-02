from PySide6.QtWidgets import QPushButton, QSizePolicy
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from LoginConstants.IconsPath import IconsPath

class deleteButton(QPushButton):
    """
    Custom QPushButton tailored for deletion actions within the application, featuring icon swapping 
    on hover to enhance user experience and provide visual feedback.

    Attributes:
        TABEL_BUTTON_STYLE (str): Styling for the delete button, setting transparency and icon properties.
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
        Constructs the delete button with initial setup for iconography and UI responsiveness.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super(deleteButton, self).__init__(*args, **kwargs)

        # Set the button size policy to fixed to maintain constant button dimensions.
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setSizePolicy(sizePolicy)

        # Prepare icons for different button states.
        self._icon_normal = QIcon()
        self._icon_normal.addFile(IconsPath.DELETE, mode=QIcon.Normal, state=QIcon.On)
        self._icon_normal.addFile(IconsPath.DELETE_DISABLED, mode=QIcon.Disabled, state=QIcon.Off)

        self._icon_over = QIcon(IconsPath.DELETE_HOVER)  # Hover icon for the button.

        # Apply custom styles and set the default icon.
        self.setStyleSheet(self.TABEL_BUTTON_STYLE)
        self.setIcon(self._icon_normal)
        self.setCursor(Qt.PointingHandCursor)  # Set cursor to pointing hand.

    def enterEvent(self, event):
        """
        Handles mouse entering the button's area. Changes icon to hover state if enabled.

        Args:
            event: The event object containing event details.
        """
        if self.isEnabled():
            self.setIcon(self._icon_over)

    def leaveEvent(self, event):
        """
        Handles mouse leaving the button's area. Reverts icon to normal state if enabled.

        Args:
            event: The event object containing event details.
        """
        if self.isEnabled():
            self.setIcon(self._icon_normal)

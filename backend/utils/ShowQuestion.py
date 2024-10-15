



from PySide6.QtWidgets import QMessageBox
from backend.utils import texts
from PySide6.QtGui import QFont,QIcon






def show_question( title, message, question=True):
    # Create the custom QMessageBox
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)

    # Set the font size to 20 for the message box
    font = QFont()
    font.setPointSize(10)
    msg_box.setFont(font)

    if question:
        # Add custom buttons for "بلی" and "خیر"
        yes_button = msg_box.addButton("Yes", QMessageBox.YesRole)
        yes_button.setFont(font)

        no_button = msg_box.addButton("No", QMessageBox.NoRole)
        no_button.setFont(font)


        # Set default button (optional)
        msg_box.setDefaultButton(no_button)

        # Execute and check which button was clicked
        msg_box.exec_()

        if msg_box.clickedButton() == yes_button:
            return True
        if msg_box.clickedButton() == no_button:
            return False
    else:
        # Add the "تایید" button for simple confirmations
        ok_button = msg_box.addButton("Confirm", QMessageBox.AcceptRole)

        # Execute and check if Ok (or تایید) was clicked
        msg_box.exec_()

        if msg_box.clickedButton() == ok_button:
            return True


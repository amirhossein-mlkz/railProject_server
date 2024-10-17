from PySide6.QtWidgets import QPushButton, QLabel, QComboBox, QGridLayout, QDialogButtonBox, QVBoxLayout,QHBoxLayout, QWidget, QDialog
from PySide6 import QtCore
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt, QPoint

from persiantools.jdatetime import JalaliDateTime





stylesheet = """


QDialog {
 background-color: rgba(77, 158, 255, 0.2); /* Light blue with 20% opacity */
    background-color: #2E2A3D; /* Dark background */
    border: 2px solid #4D9EFF; /* Blue border */
    border-radius: 10px;
}

QComboBox {
    background-color: #3A3F44; /* Dark background */
    color: white; /* White text */
    border: 1px solid #4D9EFF; /* Blue border */
    border-radius: 8px; /* Smoother rounded corners */
    padding: 5px 10px; /* Spacing for text */
    font-size: 14px; /* Adjust font size for readability */
}

QComboBox:hover {
    background-color: #444A52; /* Slightly lighter background on hover */
    border: 1px solid #3A7CCC; /* Lighter blue border on hover */
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px; /* Adjust width of drop-down arrow button */
    border-left: 1px solid #4D9EFF; /* Left border separating drop-down */
    background-color: #3A3F44; /* Match background with the combobox */
    border-top-right-radius: 8px; /* Keep the same border radius */
    border-bottom-right-radius: 8px; /* Keep the same border radius */
}

QComboBox::down-arrow {
    image:  url(:/icons/icons/prev_gray.png); /* Optional hover state for the icon */
    width: 16px;
    height: 16px;
}

QComboBox QAbstractItemView {
    background-color: #2E2A3D; /* Dark background for dropdown */
    color: white; /* White text */
    border: 1px solid #4D9EFF; /* Blue border for dropdown */
    selection-background-color: #4D9EFF; /* Blue background for selected item */
    selection-color: white; /* White text for selected item */
    border-radius: 8px;
    padding: 5px;
}

QComboBox::down-arrow:hover {
    image:  url(:/icons/icons/prev_gray.png); /* Optional hover state for the icon */
    width: 20px;
    height: 20px;

}

QComboBox QAbstractItemView::item {
    padding: 6px 10px; /* Adjust padding for list items */
    font-size: 14px; /* Font size */
}

QComboBox QAbstractItemView::item:selected {
    background-color: #4D9EFF; /* Blue background when an item is selected */
    color: white;
}

QComboBox::drop-down:hover {
    background-color: #3A7CCC; /* Lighter blue background for drop-down hover */
}


QPushButton {
    background-color: #3A3F44; /* Dark gray for buttons */
    color: white; /* White text */
    border: 2px solid #4D9EFF; /* Blue border */
    border-radius: 5px;
    padding: 5px 10px;
}

QPushButton:hover {
    background-color: #4D9EFF; /* Blue background on hover */
    color: white;
}

QPushButton:pressed {
    background-color: #3A7CCC; /* Darker blue when pressed */
}

QPushButton#okButton {
    background-color: #3A7CCC; /* Darker blue for OK button */
}

QPushButton#cancelButton {
    background-color: #444444; /* Dark gray for Cancel button */
    border: 2px solid #777777; /* Lighter gray border */
}

QLabel {
    color: white; /* White text color for labels */
    font-size: 14px;
}

/* Calendar Day Buttons */
QPushButton#dayButton {
    background-color: #3A3F44; /* Dark gray background for unselected day buttons */
    color: white;
    border: 1px solid #4D9EFF; /* Blue border for unselected buttons */
    border-radius: 5px;
    padding: 10px;
}

QPushButton#dayButton:hover {
    background-color: #4D9EFF; /* Blue background on hover */
}

QPushButton#dayButton:selected {
    background-color: #4D9EFF; /* Blue background for selected day */
    color: white;
}

QPushButton#todayButton {
    background-color: #4D9EFF; /* Blue for "Today" button */
    color: white;
    border-radius: 5px;
    padding: 8px 12px;
}

QPushButton#todayButton:hover {
    background-color: #3A7CCC; /* Slightly darker blue on hover */
}

QPushButton#todayButton:pressed {
    background-color: #3A3F44; /* Dark gray when pressed */
}


"""










class JalaliCalendarDialog(QDialog):
    def __init__(self, input_field=None, date=None):
        super().__init__()

        self.setWindowTitle("Jalali Calendar Dialog")
        self.setStyleSheet(stylesheet)
        self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint))
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.selected_button = None
        self.selected_day = None
        self.input_field = input_field
        self.days_buttons:dict[str,QPushButton] = {}

        self.today_date = JalaliDateTime.now()

        if date is None:
            date = JalaliDateTime.now()

        self.date = date

        # Set up the layout
        layout = QVBoxLayout()

        self.yearCombo = QComboBox()
        self.monthCombo = QComboBox()

        current_jalali_year = self.today_date.year
        for year in range(current_jalali_year - 50, current_jalali_year + 50):
            self.yearCombo.addItem(str(year))

        jalali_months = [
            "فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
            "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"
        ]
        for month in jalali_months:
            self.monthCombo.addItem(month)

        self.yearCombo.setCurrentText(str(current_jalali_year))
        self.monthCombo.setCurrentIndex(self.today_date.month - 1)

        self.yearCombo.currentTextChanged.connect(self.updateCalendar)
        self.monthCombo.currentIndexChanged.connect(self.updateCalendar)

        self.calendarGrid = QGridLayout()
        self.updateCalendar()

        layout.addWidget(self.yearCombo)
        layout.addWidget(self.monthCombo)

        calendar_widget = QWidget()
        calendar_widget.setLayout(self.calendarGrid)
        layout.addWidget(calendar_widget)

        # Add Today button
        todayButton = QPushButton("امروز")
        # todayButton.setStyleSheet(TODAY_BUTTON_STYLE)
        todayButton.clicked.connect(self.select_today)
        layout.addWidget(todayButton)

        # Add OK and Cancel buttons
        buttonBox = QDialogButtonBox()
        ok_button = QPushButton("تایید")
        ok_button.setObjectName("okButton")
        ok_button.clicked.connect(self.accept_date)
        cancel_button = QPushButton("لغو")
        cancel_button.setObjectName("cancelButton")
        cancel_button.clicked.connect(self.reject)

        buttonBox.addButton(ok_button, QDialogButtonBox.AcceptRole)
        buttonBox.addButton(cancel_button, QDialogButtonBox.RejectRole)
        

        button_layout = QHBoxLayout()
        button_layout.addWidget(buttonBox)
        button_layout.setAlignment(QtCore.Qt.AlignHCenter)

        layout.addWidget(buttonBox)
        layout.setAlignment(QtCore.Qt.AlignHCenter)

        self.setLayout(layout)

        self.set_date(self.date, accept=True)







    def updateCalendar(self):
        while self.calendarGrid.count():
            item = self.calendarGrid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        year = int(self.yearCombo.currentText())
        month = self.monthCombo.currentIndex() + 1

        first_day_of_month = JalaliDateTime(year, month, 1)
        first_day_of_week = first_day_of_month.weekday()

        days_in_month = self.days_in_jalali_month(year, month)

        self.days_buttons = {}

        day = 1
        for week in range(6):
            for weekday in range(7):
                if week == 0 and weekday < first_day_of_week:
                    label = QLabel("")
                    self.calendarGrid.addWidget(label, week, weekday)
                elif day > days_in_month:
                    label = QLabel("")
                    self.calendarGrid.addWidget(label, week, weekday)
                else:
                    button = QPushButton(str(day))
                    # button.setStyleSheet(DAY_BUTTON_STYLE)
                    button.clicked.connect(self.select_day)
                    self.calendarGrid.addWidget(button, week, weekday)
                    self.days_buttons[day] = button
                    day += 1

    def select_day(self):
        # for btn in self.days_buttons.values():
            # btn.setStyleSheet(DAY_BUTTON_STYLE)
        
        self.selected_button = self.sender()
        # self.selected_button.setStyleSheet(DAY_BUTTON_SELECTED_STYLE)
        self.selected_day = int(self.selected_button.text())

    def set_date(self, date:JalaliDateTime, accept=False):
        self.yearCombo.setCurrentText(str(date.year))
        self.monthCombo.setCurrentIndex(date.month - 1)
        self.selected_day = date.day
        self.updateCalendar()
        # Simulate day selection for today's date
        self.days_buttons[self.selected_day].click()
        if accept:
            self.accept_date()

    def select_today(self):
        self.set_date(JalaliDateTime.now())


    def days_in_jalali_month(self, year, month):
        if month <= 6:
            return 31
        elif month <= 11:
            return 30
        else:
            return 30 if JalaliDateTime.is_leap(year) else 29

    def accept_date(self):
        year = int(self.yearCombo.currentText())
        month = self.monthCombo.currentIndex() + 1
        day = self.selected_day
        if day:
            self.date = JalaliDateTime(year, month, day)
            self.__set_date_into_field()
        self.accept()

    def __set_date_into_field(self):
        str_date = self.date.strftime("%Y/%m/%d")
        if self.input_field:
            self.input_field.setText(str_date)

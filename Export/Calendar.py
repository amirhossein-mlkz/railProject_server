from PySide6.QtWidgets import QPushButton, QLabel, QComboBox, QGridLayout, QDialogButtonBox, QVBoxLayout,QHBoxLayout, QWidget, QDialog
from PySide6 import QtCore
from PySide6.QtGui import QColor

from persiantools.jdatetime import JalaliDateTime

TODAY_BUTTON_STYLE="""
    QPushButton {
        background-color: transparent;
        border:none;
        color:rgba(0, 122, 255, 255);
        font-weight:bold;
        padding:10px;
    }
    QPushButton:hover {
        color:rgba(0, 40, 255, 255)
    }
"""

# Button styles
DAY_BUTTON_STYLE = """
    QPushButton {
        background-color: transparent;
        border: 1px solid transparent;
        border-radius: 20px;
        min-width: 40px;
        min-height: 40px;
    }
    QPushButton:hover {
        background-color: rgba(0, 122, 255, 30);
    }
"""

DAY_BUTTON_SELECTED_STYLE = """
    QPushButton {
        background-color: rgba(0, 122, 255, 255);
        color: white;
        border-radius: 20px;
        border: none;
        min-width: 40px;
        min-height: 40px;
    }
"""

MAIN_STYLE = """
    QComboBox {
        border: 2px solid #e0e0e0;
        border-radius: 17px;
        padding: 8px;
        font-size: 14px;
    }

    QComboBox::drop-down {
    border: none;
    background-color: transparent;
}

    QPushButton#okButton {
        background-color: #007AFF;
        color: white;
        border-radius: 18px;
        border: 2px solid #007AFF;
        font-size: 14px;
        min-height:36px;
        max-height:36px;
        min-width:85px;

    }

    QPushButton#okButton:hover {
        background-color: #0051a8;

    }

    QPushButton#cancelButton {
        color: #007AFF;
        background-color: transparent;
        border: 2px solid #007AFF;
        border-radius: 18px;
        font-size: 14px;
        min-height:36px;
        max-height:36px;
        min-width:85px;

    }

    QPushButton#cancelButton:hover {
        color: #0051a8;
        border: 2px solid #0051a8;
        
    }
"""

class JalaliCalendarDialog(QDialog):
    def __init__(self, input_field=None, date=None):
        super().__init__()

        self.setWindowTitle("Jalali Calendar Dialog")
        self.setStyleSheet(MAIN_STYLE)

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
        todayButton.setStyleSheet(TODAY_BUTTON_STYLE)
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
                    button.setStyleSheet(DAY_BUTTON_STYLE)
                    button.clicked.connect(self.select_day)
                    self.calendarGrid.addWidget(button, week, weekday)
                    self.days_buttons[day] = button
                    day += 1

    def select_day(self):
        for btn in self.days_buttons.values():
            btn.setStyleSheet(DAY_BUTTON_STYLE)
        
        self.selected_button = self.sender()
        self.selected_button.setStyleSheet(DAY_BUTTON_SELECTED_STYLE)
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

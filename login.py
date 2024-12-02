import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6 import QtCore as sQtCore
from login_qt.LoginConstants.Constants import UIPages
from login_qt.userProfile_UI import userProfile_UI
from login_qt.LoginDatabase.usersDatabase import usersDB

from login_qt.userProfile_API import userProfile_API

from PySide6.QtWidgets import QDialog 

class LoginPage():
        
        def __init__(self):
              

            self.main_ui = userProfile_UI()  # Creates an instance of the main user profile interface.
            self.database = usersDB()  # Initializes the database handler for user data operations.
            
        # Initializes the API handler that connects the UI with database operations.
        # API = userProfile_API(main_ui,
        #     load_user_func=database.load,
        #     update_user_func=database.update,
        #     load_all_users_func=database.load_all,
        #     add_user_func=database.save,
        #     delete_user_func=database.remove,
        # )


            self.login_API = userProfile_API(self.main_ui,
                load_user_func=self.database.load,
                update_user_func=self.database.update,
                load_all_users_func=self.database.load_all,
                add_user_func=self.database.save,
                delete_user_func=self.database.remove,
            )



        def show_page(self,page_name=UIPages.LOGIN,accessibility=[]):
             

            status_login = self.main_ui.show_win(page_name,accessibility)
            
            return status_login
        
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_page = LoginPage()
    sys.exit(app.exec())

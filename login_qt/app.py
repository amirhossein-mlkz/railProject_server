import sys
import os

# Adds the 'uiFiles/resources' directory to the system path for accessing custom UI resources.
sys.path.append(os.path.join('uiFiles', 'resources'))

from PySide6.QtWidgets import QApplication
from userProfile_UI import userProfile_UI
from userProfile_API import userProfile_API
from Constants.Constants import UIPages
from Database.usersDatabase import usersDB

# Compiles the Qt resource file into a Python module, enabling access to resource files like images.
os.system('pyside6-rcc {} -o {}'.format(os.path.join('uiFiles', 'resources', 'resource.qrc'), os.path.join('uiFiles', 'resources', 'resource_rc.py')))

# Converts UI files created with Qt Designer to Python code, generating modules for each UI.
os.system('pyside6-uic {} -o {}'.format(os.path.join('uiFiles', 'userProfile.ui'), os.path.join('uiFiles', 'userProfile.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('uiFiles', 'editUser.ui'), os.path.join('uiFiles', 'editUser.py')))

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Initializes the QApplication, which is necessary for all Qt applications.
    
    main_ui = userProfile_UI()  # Creates an instance of the main user profile interface.
    database = usersDB()  # Initializes the database handler for user data operations.
    
    # Initializes the API handler that connects the UI with database operations.
    API = userProfile_API(main_ui,
        load_user_func=database.load,
        update_user_func=database.update,
        load_all_users_func=database.load_all,
        add_user_func=database.save,
        delete_user_func=database.remove,
    )

    # Various calls to display different pages of the user profile system, and prints the return value.

    # ret = main_ui.show_win(UIPages.LOGIN)
    # print(ret)

    ret = main_ui.show_win(UIPages.MENU, [1,2,3,4,5])
    print(ret)

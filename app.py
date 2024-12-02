import os,sys




ADMIN_ACCESS = False
BUILD_UI = False

if BUILD_UI:
    os.system('CMD /C pyside6-rcc assets.qrc -o assets.py')#PySide
    os.system('pyside6-rcc {} -o {}'.format(os.path.join(r'login_qt\uiFiles\resources', 'resource.qrc'), os.path.join(r'', 'resource_rc.py')))
    os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'calendar.ui'), os.path.join('UIFiles', 'calendar.py')))
    os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'main_UI.ui'), os.path.join('UIFiles', 'main_UI.py')))
    os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'stationDownloadUI.ui'), os.path.join('UIFiles', 'stationDownload_UI.py')))



# Specify the path to the directory you want to add
login_directory = "login_qt"
export_directory = "Export"
# Add the directory to sys.path

if export_directory not in sys.path:
    sys.path.append(export_directory)
if login_directory not in sys.path:
    sys.path.append(login_directory)
    from Export import assets_rc

from PySide6.QtWidgets import QApplication as sQApplication
from PySide6.QtWidgets import QStyleFactory
from main_ui import UI_main_window_org
from backend import adminPrivilage
import ctypes
from backend.utils.Trial import TrialManager
from main_api import API

ADMIN_ACCESS = False

def main_func():
    trial_manager = TrialManager(trial_days=30)
    trial_manager.reset_trial()
    if trial_manager.check_trial():
        print("The software is running in trial mode.")
    else:
        print("Trial has expired. Please purchase the software.")
        return
    

    if ADMIN_ACCESS:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Not admin. Requesting access...")
            if adminPrivilage.run_as_admin():
                # Don't exit, just let the program continue to the next steps
                print("Now running as admin! Continuing execution...")
            else:
                print("Failed to obtain admin privileges. Exiting.")
                return
        else:
            print("Running as administrator!")



    app = sQApplication()
    app.setStyle(QStyleFactory.create("windows"))  # Enforces a consistent style


    win = UI_main_window_org()
    api = API(win)
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":

    main_func()
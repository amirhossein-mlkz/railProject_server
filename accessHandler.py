# class userRoles

from main_ui import UI_main_window_org
from login_qt.Constants import Constants as userConstants
from uiUtils.guiBackend import GUIBackend


class accessHandler:

    def __init__(self, main_ui:UI_main_window_org):
        self.main_ui = main_ui


    def set_role(self, role:str):
        if role is None:
            self.main_ui.ui.btn_side_playback.hide()
            self.main_ui.ui.btn_side_settings.hide()
            self.main_ui.ui.btn_side_download.hide()
            GUIBackend.set_stack_widget_page(self.main_ui.ui.pages_stackwidget,
                                             self.main_ui.ui.empty_page)
            

        elif role.lower() == 'user':
            self.main_ui.ui.btn_side_playback.show()
            self.main_ui.ui.btn_side_settings.hide()
            self.main_ui.ui.btn_side_download.hide()
            GUIBackend.set_stack_widget_page(self.main_ui.ui.pages_stackwidget,
                                             self.main_ui.ui.page_playback)
        
        elif role.lower() == 'admin':
            self.main_ui.ui.btn_side_playback.show()
            self.main_ui.ui.btn_side_settings.show()
            self.main_ui.ui.btn_side_download.show()
            GUIBackend.set_stack_widget_page(self.main_ui.ui.pages_stackwidget,
                                             self.main_ui.ui.page_playback)

                                             

    # def show_user_managment_page(self,role):
    #     if role == 'Admin':
    #         accessibity = [userConstants.UIPages.CHANGE_PASSWORD,
    #                        userConstants.UIPages.CHANGE_USERNAME,
    #                        userConstants.UIPages.ALL_USERS,
    #                        userConstants.UIPages.SIGNUP,
    #                        userConstants.UIPages.LOGIN]
    #     else:
    #         accessibity = [userConstants.UIPages.CHANGE_PASSWORD,
    #                        userConstants.UIPages.CHANGE_USERNAME,
    #                        userConstants.UIPages.LOGIN]

    #     if self.main_ui.login_obj.login_API.get_logined_user() is not None:
    #         ret= self.main_ui.login_obj.show_page(accessibity)
            

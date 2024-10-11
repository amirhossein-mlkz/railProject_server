from UIFiles.main_UI import Ui_MainWindow
from uiUtils.guiBackend import GUIBackend
from uiUtils import GUIComponents

class settingPageUI:

    def __init__(self, ui:Ui_MainWindow):
        self.ui = ui

        self.new_system_station_fields:dict[str, tuple] = {
            'name': (self.ui.name_input, True),
            'city': (self.ui.city_input, True),
            'ip'  : (self.ui.ip_input  , True),
            'username': (self.ui.username_input, False),
            'password': (self.ui.password_input, False),
        }

        self.modify_system_station_fields = {
            'name': (self.ui.name_input_modify, True),
            'city': (self.ui.city_input_modify, True),
            'ip'  : (self.ui.ip_input_modify  , True),
            'username': (self.ui.username_input_modify, False),
            'password': (self.ui.password_input_modify, False),
        }

    def get_add_ip(self):
        return GUIBackend.get_input_text(self.ui.ip_input)
    
    def get_add_system_station(self):
        input_fields = {}
        for field_name,(field, require) in self.new_system_station_fields.items():
            value = GUIBackend.get_input(field)
            if require==True and value=='':
                return None
        
            input_fields[field_name] = value
        return input_fields
    

    def clear_add_system_station(self,):
        for field_name,(field, require) in self.new_system_station_fields.items():
            GUIBackend.set_input(field, '')


    def set_modify_system_station_fields(self,datas:dict):
        for name ,value in datas.items():
            if name in self.modify_system_station_fields:
                field, require = self.modify_system_station_fields[name]
                GUIBackend.set_input(field, value)

    def get_modify_system_station_fields(self):
        input_fields = {}
        for field_name,(field, require) in self.modify_system_station_fields.items():
            value = GUIBackend.get_input(field)
            if require==True and value=='':
                return None
        
            input_fields[field_name] = value
        return input_fields

    def clear_modify_system_station_fields(self,):
        for name ,(field,_) in self.modify_system_station_fields.items():
            GUIBackend.set_input(field,"")
            
    
    def show_modify_system_station_form(self, state):
        self.ui.modify_station_message.hide()
        if state:
            self.ui.modify_form_frame.show()
            self.ui.system_stations_table.hide()
        else:
            self.ui.modify_form_frame.hide()
            self.ui.system_stations_table.show()

    def set_system_stations_table(self, datas:list[dict], event_func):
        headers = ['edit', 'delete', 'name', 'city', 'ip', 'username', 'password']
        GUIBackend.set_table_dim(self.ui.system_stations_table, len(datas), len(headers))
        GUIBackend.set_table_cheaders(self.ui.system_stations_table, headers)


        for row_idx, row_info in enumerate(datas):
            for cell_name, cell_value in row_info.items():
                if cell_name in headers:
                    col_idx = headers.index(cell_name)
                    GUIBackend.set_table_cell_value(table=self.ui.system_stations_table,
                                                    index=(row_idx, col_idx),
                                                    value=cell_value
                                                    )
        


            del_btn = GUIComponents.deleteButton()
            GUIBackend.button_connector_argument_pass(del_btn, event_func, args=('delete', row_info['id']))

            edit_btn = GUIComponents.editButton()
            GUIBackend.button_connector_argument_pass(edit_btn, event_func, args=('edit', row_info['id']))

            GUIBackend.set_table_cell_widget(table=self.ui.system_stations_table,
                                             index=(row_idx, headers.index('delete')),
                                             widget=del_btn
                                             )
            
            GUIBackend.set_table_cell_widget(table=self.ui.system_stations_table,
                                             index=(row_idx, headers.index('edit')),
                                             widget=edit_btn
                                            )
    def show_confirmbox(self, title:str, text:str, buttons:list[str]):
        confirmbox = GUIComponents.confirmMessageBox(title, text, buttons)
        return confirmbox.render()
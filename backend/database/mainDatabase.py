import sqlite3
from backend.database.databaseManager import DataBaseManager



class mainDatabase():
    
    def __init__(self, database_manager:DataBaseManager):
        self.database_manager = database_manager

    
    def load_all_system_stations(self,)->list[dict]:
        results = self.database_manager.fetch_table_as_dict('system_config')
        return results
    
    def load_system_station_by_id(self, id)->list[dict]:
        results = self.database_manager.fetch_rows_by_col_name('system_config', 'id', id)
        if len(results) == 0:
            return None
        return results[0]
    
    def load_system_station_by_name(self, name)->list[dict]:
        results = self.database_manager.fetch_rows_by_col_name('system_config', 'name', name)
        if len(results) == 0:
            return None
        return results[0]
    
    def remove_system_station_by_id(self, id):
        ret = self.database_manager.remove_row_by_col_name(table_name='system_config',col_name='id',name_value=id)
        return ret
    
    def update_system_station_by_id(self, data:dict, id):
        ret = self.database_manager.update_row_by_col_name('system_config', 'id', id, data)
        return ret

    def save_system_station(self, data:dict):
        ret = self.database_manager.add_value('system_config',**data)
        return ret
    
    

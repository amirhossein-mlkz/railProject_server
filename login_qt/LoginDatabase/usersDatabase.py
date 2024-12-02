from Logindorsa_database.dorsa_Database import dataBase
from LoginConstants.Constants import Keys

class usersDB:
    """
    A class to manage the users' data in the database.
    Handles operations like creating the users table, checking if a user exists, saving, updating,
    loading, and removing user records.
    """

    TABLE_NAME = 'users'  # Name of the database table for users.
    TABLE_COLS = [
                   {'col_name': Keys.USERNAME_KEY, 'col_type': 'TEXT', 'length': 200},  # Username column configuration.
                   {'col_name': Keys.PASSWORD_KEY, 'col_type': 'TEXT', 'length': 200},  # Password column configuration.
                   {'col_name': Keys.ROLE_KEY, 'col_type': 'TEXT', 'length': 50},       # Role column configuration.
                 ]
    
    PRIMERY_KEY_COL_NAME = Keys.USERNAME_KEY  # Primary key column name for the users table.
    
    def __init__(self) -> None:
        """
        Initializes the usersDB instance, sets up database connection and creates the table if it doesn't exist.
        """
        # SQLite doesn't need credentials, just the database file path
        self.db_manager = dataBase(
            db_file= Keys.DATABASE_PATH  # Provide the path to the SQLite database file
        )
        self.__create_table__()

    def __create_table__(self) -> None:
        """
        Private method to create the users table with specified columns if it does not already exist.
        """
        if not self.db_manager.table_exists(self.TABLE_NAME):
            self.db_manager.create_table(self.TABLE_NAME)
            for col in self.TABLE_COLS:
                self.db_manager.add_column(self.TABLE_NAME, **col)

    def is_exist(self, username: str) -> bool:
        """
        Checks if a user exists in the database by username.

        Args:
            username (str): Username of the user to check.

        Returns:
            bool: True if user exists, False otherwise.
        """
        founded_records = self.db_manager.search(self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, username)
        return len(founded_records) > 0

    def save(self, data: dict):
        """
        Saves a new user record to the database.

        Args:
            data (dict): Dictionary containing the user data to save.
        """
        self.db_manager.add_record_dict(self.TABLE_NAME, data)

    def update(self, data: dict):
        """
        Updates an existing user record in the database.

        Args:
            data (dict): Dictionary containing the updated user data.
        """
        self.db_manager.update_record_dict(self.TABLE_NAME, data, id_name='id', id_value=data['id'])

    def load(self, username: str) -> list[dict]:
        """
        Loads a user record from the database by username.

        Args:
            username (str): Username of the user to load.

        Returns:
            list[dict]: List of dictionaries representing the user's data.
        """
        return self.db_manager.search(self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, username)

    def load_all(self) -> list[dict]:
        """
        Loads all user records from the database.

        Returns:
            list[dict]: List of dictionaries representing all users' data.
        """
        return self.db_manager.get_all_content(self.TABLE_NAME)
    
    def remove(self, id: str):
        """
        Removes a user record from the database by primary key.

        Args:
            id (str): The primary key value of the user to be removed.
        """
        self.db_manager.remove_record(self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)

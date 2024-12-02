


CONNECTION_ERROR = "Connection error"
SUCCESSFULL = "True"
DEFAULT_SCHEMA = False

NULL = "NULL"
NOT_NULL = "NOT NULL"
AUTO_INCREMENT = "AUTO_INCREMENT"
INT = "INT"
BIGINT = "BIGINT"
VARCHAR = "VARCHAR"
FLOAT = "FLOAT"
DEFAULT = "DEFAULT "
BOOLEAN = "BOOLEAN"


NOTHING = 0  # Print nothing
INFO = 1  # Only print errors
WARNING = 2  # Print All messages


Error_auto_increment = "AUTO INCREMENT Only can set on INT type"
import sqlite3

class dataBase:
    """This class is used to create a connection and perform functions such as: add, delete, create, etc."""

    def __init__(self, db_file, log_level=1, func=None):
        self.db_file = db_file  # SQLite database file path
        self.log_level = log_level
        self.func = func
        self.connection = None
        self.cursor = None
        self.check_connection()

    def set_log_level(self, num):
        """Sets the log level."""
        self.log_level = num

    def connect(self):
        """Establishes a connection to the SQLite database using the provided file."""
        connection = sqlite3.connect(self.db_file)
        cursor = connection.cursor()
        self.connection, self.cursor = connection, cursor
        return cursor, connection

    def check_connection(self):
        """Checks if the connection to the database can be established."""
        try:
            self.connect()
            return True
        except sqlite3.Error as e:
            self.show_message(("Error while connecting to SQLite", e))
            return False

    def execute_query(self, query):
        """Executes a given query on the database."""
        try:
            if self.check_connection():
                self.cursor.execute(query)
                return self.cursor
            else:
                self.show_message("Error in SQL Connection")
                return False
        except sqlite3.Error as e:
            self.show_message(("Error while executing query", e))
            return False



    def create_table(self, table_name):
        """
        Creates a new table with the specified name, if it doesn't already exist.

        Args:
            table_name (str): The name of the table to create.

        Returns:
            bool: True if the table was created or already exists, False otherwise.

        Raises:
            None.

        Example:
            To create a table named 'users', you can call the function like this:
                create_table('users')

            This will create the 'users' table with a primary key column named 'id' if it doesn't already exist.
            If the table already exists, the function will return True without creating it.
        """
        try:
            if self.check_connection():
                query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT);"
                self.execute_query(query=query)
                return True
            else:
                self.show_message("Error in SQL Connection")
                return False
        except sqlite3.Error as e:
            self.show_message(("Error creating table", e))
            return False






    def add_record_dict(self, table_name, data: dict):
        """Adds a new record to the specified table using a dictionary."""
        cols = ', '.join(data.keys())
        placeholders = ', '.join('?' * len(data))
        query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
        values = tuple(data.values())

        try:
            if self.check_connection():
                self.cursor.execute(query, values)
                self.connection.commit()
                return True
            else:
                self.show_message("Error in SQL Connection")
                return False
        except sqlite3.Error as e:
            self.show_message(("Error while adding record", e))
            return False

    def update_record(self, table_name, col_name, value, id_name, id_value):
        """Updates a row in the specified table."""
        try:
            query = f"UPDATE {table_name} SET {col_name} = ? WHERE {id_name} = ?"
            if self.check_connection():
                self.cursor.execute(query, (value, id_value))
                self.connection.commit()
                return True
            else:
                self.show_message("Error in SQL Connection")
                return False
        except sqlite3.Error as e:
            self.show_message(("Error while updating record", e))
            return False

    def update_record_dict(self, table_name, data, id_name, id_value):
        """Updates a row in the specified table using a dictionary."""
        set_clause = ', '.join([f"{col} = ?" for col in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {id_name} = ?"
        values = tuple(data.values()) + (id_value,)

        try:
            if self.check_connection():
                self.cursor.execute(query, values)
                self.connection.commit()
                return True
            else:
                self.show_message("Error in SQL Connection")
                return False
        except sqlite3.Error as e:
            self.show_message(("Error while updating record", e))
            return False

    def remove_record(self, table_name, col_name, value):
        """Removes a record from the specified table."""
        query = f"DELETE FROM {table_name} WHERE {col_name} = ?"

        try:
            if self.check_connection():
                self.cursor.execute(query, (value,))
                self.connection.commit()
                return True
            else:
                self.show_message("Error in SQL Connection")
                return False
        except sqlite3.Error as e:
            self.show_message(("Error while removing record", e))
            return False
        
        
    def search(self, table_name, col_name, value):
        """
        Searches the specified SQLite table for records matching the given column name and value.

        Args:
            table_name (str): The name of the table to search.
            col_name (str): The name of the column to match against.
            value (Any): The value to search for. It will be converted to a string for comparison.

        Returns:
            list: A list of dictionaries representing the matching records. Each dictionary contains
                the field names as keys and corresponding field values as values.
        """

        try:
            value = str(value)
            int_type = False
            if value.isnumeric():
                int_type = True

            if self.check_connection():
                # Construct SQL query based on value type
                if int_type:
                    sql_select_query = f"SELECT * FROM {table_name} WHERE {col_name} = {value};"
                else:
                    sql_select_query = f"SELECT * FROM {table_name} WHERE {col_name} = '{value}';"

                # Execute the query
                cursor = self.execute_query(sql_select_query)
                records = cursor.fetchall()

                # Get column names (field names)
                field_names = [col[0] for col in cursor.description]

                # Process the records into a list of dictionaries
                res = []
                for record in records:
                    record_dict = {field_names[i]: record[i] for i in range(len(field_names))}
                    res.append(record_dict)

                cursor.close()
                return res
            else:
                self.show_message("Error in SQL Connection")
                return []

        except sqlite3.Error as e:
            self.show_message(("Error in search", e))
            return []
        

    def delete_table(self, table_name):
        """Deletes the specified table."""
        query = f"DROP TABLE IF EXISTS {table_name}"

        try:
            if self.check_connection():
                self.cursor.execute(query)
                return True
            else:
                self.show_message("Error in SQL Connection")
                return False
        except sqlite3.Error as e:
            self.show_message(("Error while deleting table", e))
            return False

    def show_message(self, message, level=1):
        """Displays messages based on log level."""
        if self.log_level >= level:
            print(message)



    def table_exists(self, table_name):
        """Check if a table exists in the SQLite database."""
        try:
            if self.check_connection():
                query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"
                cursor = self.execute_query(query)
                record = cursor.fetchall()
                if len(record):
                    return True
                return False
            else:
                self.show_message('Error in SQL Connection')
                return False
        except sqlite3.Error as e:
            self.show_message(("Error checking table existence", e))
            return False
        


    def add_column(
        self,
        table_name,
        col_name,
        col_type,
        length=255,
        nullable=True,
        default="",
        unique=False,
    ):
        """
        Adds a new column to the specified table in SQLite.

        Args:
            table_name (str): The name of the table to add the column to.
            col_name (str): The name of the column to add.
            col_type (str): The data type of the column.
            length (int): Optional. The length of the column if the data type is VARCHAR. Default is 255.
            nullable (bool): Optional. Whether the column allows NULL values. Default is True.
            default (Any): Optional. The default value for the column. Default is an empty string.
            unique (bool): Optional. Whether the column has a UNIQUE constraint. Default is False.

        Returns:
            bool: True if the column was successfully added, False otherwise.
        """

        # In SQLite, there is no auto-increment for non-primary key columns
        self.create_table(table_name=table_name)

        # Handle VARCHAR type with length
        if col_type.upper() == "VARCHAR":
            col_type = f"VARCHAR({length})"

        # Handle default value
        default_clause = f"DEFAULT '{default}'" if default else ""

        # Handle NULL/NOT NULL constraint
        null_clause = "NOT NULL" if not nullable else ""

        # Construct the SQL query to add the column
        try:
            if self.check_connection():
                query = f"ALTER TABLE {table_name} ADD COLUMN {col_name} {col_type} {null_clause} {default_clause}"
                self.execute_query(query=query)

                # Add UNIQUE constraint if specified
                if unique:
                    query_unique = f"CREATE UNIQUE INDEX idx_{table_name}_{col_name} ON {table_name} ({col_name})"
                    self.execute_query(query=query_unique)

                return True
            else:
                self.show_message("Error in SQL Connection")
                return False

        except sqlite3.Error as e:
            self.show_message(("Error adding column", e))
            return False


    def get_all_content(
        self,
        table_name,
        limit=False,
        limit_size=20,
        offset=0,
        reverse_order=False,
        column_order="id",
    ):
        """
        Retrieves all content from the specified SQLite table.

        Args:
            table_name (str): The name of the table from which to retrieve the content.
            limit (bool): Optional. If True, limits the number of records returned by limit_size.
                Default is False.
            limit_size (int): Optional. The maximum number of records to retrieve if limit is True.
                Default is 20.
            offset (int): Optional. The number of records to skip before retrieving the content.
                Default is 0.
            reverse_order (bool): Optional. If True, retrieves the content in reverse order.
                Default is False.
            column_order (str): Optional. The name of the column used for sorting the content.
                Default is 'id'.

        Returns:
            list: A list of dictionaries representing the content. Each dictionary contains
                the field names as keys and corresponding field values as values.
        """

        sort_order = "DESC" if reverse_order else "ASC"
        try:
            if self.check_connection():
                # Construct the query
                if not limit:
                    sql_select_query = f"SELECT * FROM {table_name} ORDER BY {column_order} {sort_order}"
                else:
                    sql_select_query = f"SELECT * FROM {table_name} ORDER BY {column_order} {sort_order} LIMIT {limit_size} OFFSET {offset}"

                # Execute the query
                cursor = self.execute_query(sql_select_query)
                records = cursor.fetchall()

                # Get column names (field names)
                field_names = [col[0] for col in cursor.description]

                # Process the records into a list of dictionaries
                res = []
                for record in records:
                    record_dict = {field_names[i]: record[i] for i in range(len(field_names))}
                    res.append(record_dict)

                cursor.close()
                return res
            else:
                self.show_message("Error in SQL Connection")
                return []
        except sqlite3.Error as e:
            self.show_message(("Error retrieving content", e))
            return []

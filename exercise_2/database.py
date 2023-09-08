from typing import List
import sqlite3


class Connection:
    """
        Manages the database connection
    """

    def __init__(self, database_name:str) -> None:
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.connection.row_factory = sqlite3.Row
    
    def query(self, sql:str) -> List:
        """
            Executes a query for the provided sql
        Args:
            sql (str): an sql query

        Returns:
            List: List of Rows
        """

        cursor = self.connection.execute(sql)
        records = cursor.fetchall()
        cursor.close()
        return records

    def insert(self, table_name:str, fields: dict) -> None:
        """
            Insert records on a given table
        Args:
            table_name (str): table to insert on
            fields (dict): fields (key: value) to be inserted
        """

        field_names = ", ".join(fields.keys())
        field_values = ", ".join([f'"{v}"' for v in fields.values()])
        columns = f'insert into {table_name} ({field_names})'
        values = f'values ({field_values})'
        sql = f'{columns} {values};'
        cursor = self.connection.execute(sql.strip())
        self.connection.commit()

    def table_exists(self, table_name:str ) -> bool:
        """
            Checks if given table exists on the database.
        Args:
            table_name (str): table name to be checked

        Returns:
            bool: _description_
        """
        sql = f'''SELECT EXISTS (
                SELECT 
                    name
                FROM 
                    sqlite_schema 
                WHERE 
                    type='table' AND 
                    name='{table_name}'
                );
        '''
        cursor = self.connection.execute(sql)
        rows = cursor.fetchall()
        
        return rows[0][0] > 0

    def close(self):
        """
            Closes the connection
        """
        self.connection.close()

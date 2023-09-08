# Classes used to manage database actions

import abc
import enum
from typing import List

class ColumnType(enum.Enum):
    """
        Represents a column type to be
        used on the models
    """
    string = 'string'
    boolean = 'boolean'
    date = 'string'
    

class Column:
    """
        Represents a column from a model
    """

    def __init__(
            self,
            name: str,
            type:ColumnType,
            required:bool=False
        ) -> None:

        self.name = name
        self.type = type
        self.required = required
    
    def to_dict(self):
        """
            Converts the column to a dict, following
            JSONSchema rules for properties
        Returns:
            _type_: _description_
        """
        return {
            self.name: {'type': self.type.value}
        }


class SqlAdapter(abc.ABC):
    """
        Abastract class to implement different databases adaptations
    """
    
    def __init__(self) -> None:
        super().__init__()
    
    @abc.abstractmethod
    def get_ddl(self, table_name:str, schema:dict) -> str:
        """
            Generates a ddl commands to create the table for a given database type.
        Args:
            table_name (str): name of the table to be created
            schema (dict): a JSONSchema representation of the table

        Returns:
            str: DDL command to create table
        """
        pass


class SqliteAdapter(SqlAdapter):
    """
        Adapter for SQlite database
    """

    # type convertion table
    type_table = {
        'string': 'text',
        'date': 'text',
        'boolean': 'integer',
    }

    def get_ddl(self, table_name:str, schema:dict) -> str:
        """
            Generate DDL for Sqlite
        Args:
            table_name (str): name of the table to be created
            schema (dict): a JSONSchema representation of the table

        Raises:
            Exception: Exception if type is not implemented

        Returns:
            str: _description_
        """
        columns = []
        for column_name, attributes in schema.get('properties', {}).items():
            type_name = self.type_table.get(attributes.get('type'))
            if not type_name:
                raise Exception(
                    f'Error on column "{column_name}".'
                    'Data type convertion not implemented for: {type_name}'
                )

            column = f'{column_name} {type_name}'
            columns.append(column)

        columns_list = ', '.join(columns)

        sql = f'create table {table_name} ({columns_list})'

        return sql


class Model():
    """
        Represents a model/table
    """

    def __init__(self, table_name, columns:List[Column]) -> None:
        self.table_name = table_name
        self.columns = columns
    
    def get_json_schema(self) -> dict:
        """
            Generates a dict containing a JSONSchema 
            representing the model.
        Returns:
            str: _description_
        """
        properties = {}
        required = []
        for column in self.columns:
            properties.update(column.to_dict())
            if column.required:
                required.append(column.name)
        
        return {
            'type': 'object',
            'properties': properties,
            'required': required
        }
    
    def get_ddl(self, adapter:SqlAdapter) -> str:
        """
            Generates DDL to create the table
            with the given adapter
        Args:
            adapter (SqlAdapter): any implementation of SqlAdapter

        Returns:
            str: a DDL command to create the table
        """
        return adapter.get_ddl(
            self.table_name,
            self.get_json_schema()
        )
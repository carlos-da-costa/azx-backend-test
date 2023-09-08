from typing import List
from database import Connection
from schemas import task


class TaskController:
    """
        Controls the task list repository
    """
    schema = task

    def __init__(self, connection: Connection) -> None:
        self.connection = connection


    def add(self, task_dict: dict):
        """
            Add a task o the database
        Args:
            task_dict (dict): a dictionary containing task data
        """
        self.connection.insert(
            table_name=self.schema.table_name,
            fields=task_dict
        )
    
    def all(self) -> List[dict]:
        """
            List all tasks on the database.
        Returns:
            _type_: a list of dicts containing task data
        """
        rows = self.connection.query(
            f'select * from {self.schema.table_name}'
        )
        return [dict(row) for row in rows]

from flask import g, current_app
from database import Connection
from config import DATABASE_NAME
from controllers import TaskController

class TaskManager:
    """
        Helper class to manage connection and model controller.
    """

    def __init__(self) -> None:
        with current_app.app_context():
            self.connection = Connection(DATABASE_NAME)
            self.controller = TaskController(self.connection)
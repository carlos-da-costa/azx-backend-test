from asyncio import Task
from re import A
from flask import Flask, request, jsonify, g
from flask_expects_json import expects_json

from database import Connection
from managers import TaskManager
from dal import SqliteAdapter
from schemas import task
import config


def init_db():
    """
        Initializes the database by creating tables it they do not exist.
    """
    connection = Connection(config.DATABASE_NAME)
    models = [task]
    for model in models:
        if not connection.table_exists(model.table_name):
            connection.query(model.get_ddl(SqliteAdapter()))
            connection.connection.commit()


def create_app():
    app = Flask(__name__)
    init_db()
    return app


app = create_app()


@app.route('/add_task', methods=['POST'])
@expects_json(task.get_json_schema())
def add_task():
    try:
        manager = TaskManager()
        data = request.get_json()

        # Add the task to the tasks list
        manager.controller.add(data)

        return jsonify({"message": "Task added successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/list_tasks', methods=['GET'])
def list_tasks():
    manager = TaskManager()
    return jsonify({"tasks": manager.controller.all()}), 200




if __name__ == '__main__':
    app.run(debug=True)


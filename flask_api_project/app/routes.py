from flask import Blueprint, jsonify, request
from app.models import Task

api = Blueprint('api', __name__)

tasks = []

# Endpoint to get all tasks
@api.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Endpoint to create a new task
@api.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(data['id'], data['title'], data['description'], data['completed'])
    tasks.append(new_task.to_dict())
    return jsonify(new_task.to_dict()), 201

# Endpoint to get a task by ID
@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({'message': 'Task not found'}), 404

# Endpoint to update a task
@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    data = request.json
    task.update(data)
    return jsonify(task), 200

# Endpoint to delete a task
@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

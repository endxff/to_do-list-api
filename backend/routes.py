# Implement the CRUD API endpoints.
from flask import Blueprint, request, jsonify
from models import Task, db

app = Blueprint("routes", __name__)


# Helper function to format task
def format_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "done": task.done,
    }


# Helper function to handle errors
def handle_error(message, status_code):
    response = jsonify({"error": message})
    response.status_code = status_code
    return response


# Create task
@app.route("/create_task", methods=["POST"])
def create_task():
    # Get data from the request
    data = request.json  # or request.form for HTML form data

    # Validate input
    title = data.get("title")
    description = data.get("description", "")  # Default to empty string
    if not title:
        return handle_error("Title is required", 400)

    # Create new task
    new_task = Task(title=title, description=description)
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return handle_error("An error occurred while creating the task", 500)

    # Return success response
    return (
        jsonify(
            {"message": "Task created successfully", "task": format_task(new_task)}
        ),
        201,
    )


# Get task
@app.route("/task/get", methods=["GET"])
def get_task():
    # Get all db tasks ordered by id
    tasks = db.session.execute(db.select(Task).order_by(Task.id)).scalars().all()

    # Iterate through tasks
    tasks_list = [format_task(task) for task in tasks]

    # Return json with all tasks
    return jsonify(tasks_list), 200


# Edit task
@app.route("/task/edit/<int:id>", methods=["PUT"])
def edit_task(id):
    # Get Task ID
    task = db.get_or_404(Task, id)

    # Proceed to updating task
    data = request.json  # Gather data for update

    # Validate input
    title = data.get("title")
    description = data.get("description", "")  # Default to empty string

    if not title:
        return handle_error("Title is required", 400)

    task.title = title
    task.description = description

    # Update task
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return handle_error("An error occurred while updating the task", 500)

    # Return success response
    return (
        jsonify({"message": "Task updated successfully", "task": format_task(task)}),
        200,
    )


# Delete task
@app.route("/task/delete/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = db.get_or_404(Task, id)  # Get selected task ID

    # Proceed to deleting
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return handle_error("An error occurred while deleting the task", 500)

    # Return success message
    return jsonify({"message": "Task deleted successfully"}), 200


# Delete all tasks
@app.route("/task/delete/all", methods=["DELETE"])
def delete_all_tasks():
    try:
        db.session.execute(db.delete(Task))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return handle_error("An error occurred while deleting all tasks", 500)

    # Return success message
    return jsonify({"message": "All tasks deleted"}), 200

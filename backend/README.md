# README.md

This project is a simple Todo List API built using Flask and SQLAlchemy. It provides a RESTful API for creating, reading, updating, and deleting tasks.

## Features

- Create a new task
- Retrieve all tasks
- Update an existing task
- Delete a specific task
- Delete all tasks

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/todo-list-api.git
   cd todo-list-api
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```sh
   flask db upgrade
   ```

## Configuration

The application uses a configuration file `config.py` to store database configurations. By default, it uses SQLite as the database.

## Running the Application

1. Start the Flask development server:

   ```sh
   flask run
   ```

2. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

- **Create a new task**

  - URL: `/create_task`
  - Method: `POST`
  - Request Body: `{ "title": "Task Title", "description": "Task Description" }`
  - Response: `{ "message": "Task created successfully", "task": { ... } }`

- **Retrieve all tasks**

  - URL: `/task/get`
  - Method: `GET`
  - Response: `[ { "id": 1, "title": "Task Title", "description": "Task Description", "done": false }, ... ]`

- **Update an existing task**

  - URL: `/task/edit/<int:id>`
  - Method: `PUT`
  - Request Body: `{ "title": "Updated Title", "description": "Updated Description" }`
  - Response: `{ "message": "Task updated successfully", "task": { ... } }`

- **Delete a specific task**

  - URL: `/task/delete/<int:id>`
  - Method: `DELETE`
  - Response: `{ "message": "Task deleted successfully" }`

- **Delete all tasks**
  - URL: `/task/delete/all`
  - Method: `DELETE`
  - Response: `{ "message": "All tasks deleted" }`

## License

This project is licensed under the MIT License.

## CLI Based To-Do Application
This is a simple command-line based To-Do application built in Python. It allows users to add, view, and delete tasks from their to-do list. The tasks are stored in a JSON file for persistence.
### Features
- Add new tasks with a description and timestamp.
- View all tasks in the to-do list.
- Delete tasks by their index.
- Tasks are stored in a JSON file for easy access and modification.
### Requirements
- Python 3.x
- No external libraries are required; only standard Python libraries are used.
### Usage
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Run the application using the command:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to add, view, or delete tasks.
### File Structure
- `main.py`: The main script to run the To-Do application.
- `todo/Todo.py`: Contains the `TodoApp` class which manages the to-do list functionalities.
- `todo/tasks.json`: The JSON file where tasks are stored.
- `app.log`: Log file for recording application events and errors.
- `readme.md`: This readme file with instructions and information about the application.

### Logging
The application uses Python's built-in logging module to log important events and errors to `app.log`. This helps in debugging and keeping track of application usage. 
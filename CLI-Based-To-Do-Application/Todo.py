import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, file_path):
        self.file_path = os.path.join(os.path.dirname(__file__), file_path)
        self._ensure_file()
    def _ensure_file(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f, indent=4)
        if not os.path.exists(os.path.join(os.path.dirname(__file__), "ids.txt")):
            with open(os.path.join(os.path.dirname(__file__), "ids.txt"), 'w') as file:
                file.write('0')

    def load(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_new_id(self):
        with open(os.path.join(os.path.dirname(__file__), "ids.txt"), 'r') as file:
            ids = file.read().strip()
            last_id = int(ids) if ids else 0
        id = last_id + 1
        with open(os.path.join(os.path.dirname(__file__), "ids.txt"), 'w') as file:
            file.write(f"{id}")
        return id

    def _save_all(self, tasks):
        with open(self.file_path, "w") as f:
            json.dump(tasks, f, indent=4)

    def save(self, task):
        tasks = self.load()
        id = self.save_new_id()
        new_task = {
            "id": id,
            "task": task,
            "created_time": datetime.now().isoformat(),
            "updated_time": None,
            "status": "Pending"
        }
        tasks.append(new_task)
        self._save_all(tasks)

    def list_todos(self, status=None):
        tasks = self.load()
        if len(tasks) == 0:
            print("No tasks found.")
            return
        for task in tasks:
            if status and task["status"].lower() != status.lower():
                continue
            print(f'{task["id"]}. {task["task"]} [{task["status"]}]')
            

    def delete(self, task_id):
        tasks = self.load()
        tasks = [t for t in tasks if t["id"] != task_id]
        self._save_all(tasks)

    def update_task(self, task_id, new_task):
        tasks = self.load()
        for task in tasks:
            if task["id"] == task_id:
                task["task"] = new_task
                task["updated_time"] = datetime.now().isoformat()
        self._save_all(tasks)

    def complete_task(self, task_id):
        tasks = self.load()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "Completed"
                task["updated_time"] = datetime.now().isoformat()
        self._save_all(tasks)
    def set_pending(self, task_id):
        tasks = self.load()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "Pending"
                task["updated_time"] = datetime.now().isoformat()
        self._save_all(tasks)
    def clear(self):
        self._save_all([])

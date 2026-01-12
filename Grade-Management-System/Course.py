import os
import json
from utils import print_and_log, generate_id
from datetime import datetime

class Course:
    def __init__(self, file_name):
        self.file_name = os.path.join(os.path.dirname(__file__), file_name)
        self.ensure_file()

    def correct(self):
        return self.file_name.endswith(".json")

    def ensure_file(self):
        if self.correct():
            try:
                if not os.path.exists(self.file_name):
                    with open(self.file_name, "w") as f:
                        json.dump([], f, indent=4)
                    print_and_log("INFO", "Course json file created and initiated", 1)
            except Exception as e:
                print_and_log("ERROR", f"Error happened {e}", 1)

    def load_courses(self):
        try:
            with open(self.file_name, "r") as f:
                courses = json.load(f)
            if courses is None:
                return []
            return courses
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_all(self, courses):
        with open(self.file_name, "w") as f:
            json.dump(courses, f, indent=4)

    def save(self, name):
        if not name.strip():
            print_and_log("warning", "Course name cannot be empty", 1)
            return {"status": "failed", "message": "name cannot be empty"}
        
        id = generate_id("courses_id")
        if id is None:
             return {"status": "failed", "message": "Failed to generate ID"}

        course = {
            "id": id,
            "name": name,
            "created_at": datetime.now().isoformat()
        }
        courses = self.load_courses()
        courses.append(course)
        self.save_all(courses)
        return {"status": "success", "message": "Course created successfully", "data": course}

    def get_all_courses(self):
        return self.load_courses()

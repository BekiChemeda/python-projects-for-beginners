import os
import json
import logging
from utils import print_and_log, generate_id
from datetime import datetime

class Student:
    def __init__(self, file_name):
        self.file_name = os.path.join(os.path.dirname(__file__), file_name)
        self.correct()
        self.ensure_file()
    def correct(self):
        return self.file_name.endswith(".json")
    def ensure_file(self):
        if self.correct():
            try:
                if not os.path.exists(self.file_name):
                    with open(self.file_name, "w") as f:
                        json.dump([], f, indent=4)
                    print_and_log("INFO","Student json file created and initiated",1 )
            except Exception as e:
                print_and_log("ERROR", f"Error happened {e}", 1)
    

    def load_students(self):
        try:
            with open(self.file_name, "r") as f:
                students = json.load(f)
            if students is None:
                return []
            return students
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_all(self, students):
        with open(self.file_name, "w") as f:
            json.dump(students, f, indent=4)

    def save(self, name):
        if not name.strip():
            print_and_log("warning", "Name cannot be empty", 1)
            return {"status": "failed",
                    "message": "name cannot be empty"}
        id = generate_id("students_id")
        if id is None:
             return {"status": "failed", "message": "Failed to generate ID"}

        student = {
            "id": id,
            "name": name,
            "created_at": datetime.now().isoformat()
        }
        students = self.load_students()
        students.append(student)
        self.save_all(students)
        

Student = Student("students.json")
Student.save("Beknan")
import os
import json
from utils import print_and_log, generate_id
from datetime import datetime

class Grade:
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
                    print_and_log("INFO", "Grade json file created and initiated", 1)
            except Exception as e:
                print_and_log("ERROR", f"Error happened {e}", 1)

    def load_grades(self):
        try:
            with open(self.file_name, "r") as f:
                grades = json.load(f)
            if grades is None:
                return []
            return grades
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_all(self, grades):
        with open(self.file_name, "w") as f:
            json.dump(grades, f, indent=4)

    def save(self, student_id, course_id, grade_value):
        try:
            grade_value = float(grade_value)
        except ValueError:
            return {"status": "failed", "message": "Grade must be a number"}

        if not (0 <= grade_value <= 100):
             return {"status": "failed", "message": "Grade must be between 0 and 100"}

        id = generate_id("grades_id")
        if id is None:
             return {"status": "failed", "message": "Failed to generate ID"}

        grade_entry = {
            "id": id,
            "student_id": int(student_id),
            "course_id": int(course_id),
            "grade": grade_value,
            "created_at": datetime.now().isoformat()
        }
        grades = self.load_grades()
        # Optional: Check if grade already exists for this student and course and update it?
        # For now, let's just append new grade record (history).
        # Or maybe replace. Usually current grade is what matters.
        # Let's check if exists and update, or just append. 
        # Appending allows history. If I want current, I filter by latest.
        # Let's simple append.
        
        grades.append(grade_entry)
        self.save_all(grades)
        return {"status": "success", "message": "Grade assigned successfully", "data": grade_entry}

    def get_student_grades(self, student_id):
        grades = self.load_grades()
        return [g for g in grades if g["student_id"] == int(student_id)]

    def get_course_grades(self, course_id):
        grades = self.load_grades()
        return [g for g in grades if g["course_id"] == int(course_id)]

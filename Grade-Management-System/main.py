import os
from Student import Student
from Course import Course
from Grade import Grade
from utils import print_and_log

student_manager = Student("students.json")
course_manager = Course("courses.json")
grade_manager = Grade("grades.json")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_student():
    name = input("Enter Student Name: ")
    result = student_manager.save(name)
    print(result["message"])

def add_course():
    name = input("Enter Course Name: ")
    result = course_manager.save(name)
    print(result["message"])

def assign_grade():
    # List Students to pick from
    students = student_manager.get_all_students()
    if not students:
        print("No students found. Add a student first.")
        return

    print("\n--- Select Student ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']}")
    
    try:
        s_id = int(input("Enter Student ID: "))
        # Validate existence
        if not any(s['id'] == s_id for s in students):
            print("Invalid Student ID.")
            return
    except ValueError:
        print("Invalid input.")
        return

    # List Courses
    courses = course_manager.get_all_courses()
    if not courses:
        print("No courses found. Add a course first.")
        return

    print("\n--- Select Course ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")
    
    try:
        c_id = int(input("Enter Course ID: "))
        # Validate existence
        if not any(c['id'] == c_id for c in courses):
            print("Invalid Course ID.")
            return
    except ValueError:
        print("Invalid input.")
        return

    try:
        grade_val = float(input("Enter Grade (0-100): "))
    except ValueError:
        print("Invalid grade.")
        return

    result = grade_manager.save(s_id, c_id, grade_val)
    print(result["message"])

def view_students():
    students = student_manager.get_all_students()
    print("\n--- All Students ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Created: {s['created_at']}")

def view_courses():
    courses = course_manager.get_all_courses()
    print("\n--- All Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def view_student_report():
    students = student_manager.get_all_students()
    courses = {c['id']: c['name'] for c in course_manager.get_all_courses()}
    
    if not students:
        print("No students found.")
        return

    for s in students:
        print(f"\nReport for {s['name']} (ID: {s['id']})")
        s_grades = grade_manager.get_student_grades(s['id'])
        if not s_grades:
            print("  No grades recorded.")
            continue
        
        for g in s_grades:
            c_name = courses.get(g['course_id'], f"Unknown Course {g['course_id']}")
            print(f"  Course: {c_name} | Grade: {g['grade']}")

def main():
    while True:
        print("\n=== Grade Management System ===")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Assign Grade")
        print("4. View Students")
        print("5. View Courses")
        print("6. View Student Grades Report")
        print("7. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            assign_grade()
        elif choice == '4':
            view_students()
        elif choice == '5':
            view_courses()
        elif choice == '6':
            view_student_report()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

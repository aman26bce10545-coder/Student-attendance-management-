import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "attendance.json"


def load_data():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_data(records):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=4)


def find_student(records, roll_no):
    roll_no = str(roll_no).strip().lower()
    for student in records:
        if str(student.get("roll_no", "")).strip().lower() == roll_no:
            return student
    return None


def calculate_summary(student):
    attendance = student.get("attendance", [])
    total = len(attendance)
    present = sum(1 for entry in attendance if entry.get("status") == "P")
    absent = total - present
    percentage = present / total * 100 if total else 0.0
    return total, present, absent, round(percentage, 2)


def add_student(records):
    roll_no = input("Enter roll number: ").strip()
    if not roll_no:
        print("Roll number cannot be empty.")
        return
    if find_student(records, roll_no):
        print("A student with this roll number already exists.")
        return
    name = input("Enter student name: ").strip()
    course = input("Enter course/class: ").strip()
    if not name or not course:
        print("Name and course cannot be empty.")
        return
    records.append({"roll_no": roll_no, "name": name, "course": course, "attendance": []})
    save_data(records)
    print("Student added successfully.")


def mark_attendance(records):
    if not records:
        print("No students found. Add students first.")
        return
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD.")
        return
    print("\nEnter P for Present and A for Absent.")
    for student in records:
        while True:
            status = input(f"{student['roll_no']} - {student['name']}: ").strip().upper()
            if status in ("P", "A"):
                break
            print("Please enter only P or A.")
        student["attendance"] = [e for e in student["attendance"] if e["date"] != date]
        student["attendance"].append({"date": date, "status": status})
    save_data(records)
    print(f"Attendance saved for {date}.")


def view_students(records):
    if not records:
        print("No students found.")
        return
    print("\n" + "-" * 78)
    print(f"{'Roll No.':<12}{'Name':<24}{'Course':<20}{'Attendance':>12}")
    print("-" * 78)
    for student in records:
        _, _, _, percentage = calculate_summary(student)
        print(f"{student['roll_no']:<12}{student['name'][:23]:<24}{student['course'][:19]:<20}{percentage:>10.2f}%")
    print("-" * 78)


def search_student(records):
    student = find_student(records, input("Enter roll number to search: ").strip())
    if not student:
        print("Student not found.")
        return
    total, present, absent, percentage = calculate_summary(student)
    print("\nStudent Details")
    print("-" * 40)
    print(f"Roll Number : {student['roll_no']}")
    print(f"Name        : {student['name']}")
    print(f"Course      : {student['course']}")
    print(f"Total Classes: {total}")
    print(f"Present     : {present}")
    print(f"Absent      : {absent}")
    print(f"Attendance  : {percentage:.2f}%")
    if student["attendance"]:
        print("\nAttendance History")
        for entry in sorted(student["attendance"], key=lambda x: x["date"]):
            print(f"{entry['date']} - {entry['status']}")


def update_student(records):
    student = find_student(records, input("Enter roll number to update: ").strip())
    if not student:
        print("Student not found.")
        return
    name = input(f"New name (press Enter to keep '{student['name']}'): ").strip()
    course = input(f"New course/class (press Enter to keep '{student['course']}'): ").strip()
    if name:
        student["name"] = name
    if course:
        student["course"] = course
    save_data(records)
    print("Student details updated successfully.")


def delete_student(records):
    student = find_student(records, input("Enter roll number to delete: ").strip())
    if not student:
        print("Student not found.")
        return
    print(f"Student: {student['name']} ({student['roll_no']})")
    if input("Are you sure? (y/n): ").strip().lower() == "y":
        records.remove(student)
        save_data(records)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


def attendance_report(records):
    if not records:
        print("No students found.")
        return
    summaries = [calculate_summary(s) for s in records]
    average = sum(s[3] for s in summaries) / len(records)
    low = [(s, calculate_summary(s)[3]) for s in records if calculate_summary(s)[3] < 75]
    print("\nAttendance Report")
    print("-" * 45)
    print(f"Total Students        : {len(records)}")
    print(f"Average Attendance    : {average:.2f}%")
    print(f"Students Below 75%    : {len(low)}")
    if low:
        print("\nStudents Below 75%")
        for student, pct in low:
            print(f"- {student['roll_no']} | {student['name']} | {pct:.2f}%")
    print("\nIndividual Attendance")
    for student in records:
        print(f"{student['roll_no']} - {student['name']}: {calculate_summary(student)[3]:.2f}%")


def main():
    records = load_data()
    while True:
        print("\n" + "=" * 60)
        print("        STUDENT ATTENDANCE MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. Add Student\n2. Mark Attendance\n3. View All Students\n4. Search Student")
        print("5. Update Student\n6. Delete Student\n7. Attendance Report\n8. Exit")
        print("=" * 60)
        choice = input("Enter your choice: ").strip()
        actions = {"1": add_student, "2": mark_attendance, "3": view_students,
                   "4": search_student, "5": update_student, "6": delete_student,
                   "7": attendance_report}
        if choice in actions:
            actions[choice](records)
        elif choice == "8":
            print("Thank you for using the Student Attendance Management System.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()

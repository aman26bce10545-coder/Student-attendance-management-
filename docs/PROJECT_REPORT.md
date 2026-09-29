# Student Attendance Management System

## 1. Abstract

The Student Attendance Management System is a small Python application made to handle a common classroom task: keeping track of who attended class. Instead of maintaining separate notes and calculating percentages manually, the program keeps student details and date-wise attendance in one JSON file.

The application allows a user to add students, mark attendance, view records, search by roll number, update or delete students, and generate a simple attendance report. It is a console application and uses only Python's standard library, which keeps it easy to run and suitable for a first-year project.

## 2. Introduction

Attendance is simple when there are only a few records, but it becomes repetitive when there are many students and class dates. A small program can handle the calculations and keep the records organized.

This project uses basic Python concepts such as functions, lists, dictionaries, loops, conditions, file handling, JSON, exception handling, and unit testing.

## 3. Problem Statement

Manual attendance records can make it difficult to find a student's history, calculate percentages, or identify students with low attendance. The aim of this project is to provide one simple system for these tasks.

## 4. Objectives

1. Maintain student records.
2. Record attendance date-wise.
3. Calculate attendance percentages automatically.
4. Provide search, update, and delete operations.
5. Generate a class attendance report.
6. Identify students below 75%.
7. Practice Python file handling and JSON.
8. Test important functions.

## 5. Scope

The application is intended for a small classroom, batch, or college section. It covers student registration, daily attendance, calculations, record management, and basic reporting.

It is a local, single-user console application. Login systems, online access, cloud storage, and biometric attendance are outside the current scope.

## 6. Target Users

The project can be used by a teacher handling a small batch, a class representative, or a student learning Python and wanting a practical example.

## 7. Technologies Used

- Python 3
- JSON
- `pathlib`
- `datetime`
- `unittest`
- Python standard library only

## 8. Project Structure

```text
Student Attendance Management System/
├── student_attendance_management.py
├── README.md
├── statement.md
├── RUN_PROJECT.txt
├── requirements.txt
├── .gitignore
├── data/
│   └── attendance.json
├── docs/
│   ├── PROJECT_REPORT.md
│   └── ALGORITHM_AND_FLOW.md
└── tests/
    ├── __init__.py
    └── test_attendance.py
```

## 9. Student Record Design

Each student is stored as a dictionary containing `roll_no`, `name`, `course`, and an `attendance` list.

```text
{
    "roll_no": "101",
    "name": "Aarav",
    "course": "BCA",
    "attendance": [
        {"date": "2026-09-01", "status": "P"},
        {"date": "2026-09-02", "status": "A"}
    ]
}
```

## 10. Adding Students

The program asks for roll number, name, and course/class. Empty values are rejected and duplicate roll numbers are not allowed. A valid record is saved to the JSON file.

## 11. Marking Attendance

The user enters a date in `YYYY-MM-DD` format or presses Enter to use today's date. For each student, the program accepts `P` for Present or `A` for Absent.

If attendance for the same student and date is entered again, the previous entry for that date is replaced. This avoids duplicate class records.

## 12. Attendance Calculation

The formula used is:

```text
Attendance Percentage =
(Present Classes / Total Recorded Classes) × 100
```

For example, 8 present classes out of 10 gives 80%.

If no attendance is recorded, the percentage is 0%.

## 13. Viewing and Searching

The View All Students option shows roll number, name, course, and attendance percentage.

Search uses the roll number and displays the student's total classes, present count, absent count, percentage, and attendance history.

## 14. Updating and Deleting

The update option changes the student's name or course while keeping attendance history. The delete option asks for confirmation before removing the entire student record.

## 15. Attendance Report

The report shows total students, average attendance, the number of students below 75%, the names of those students, and individual percentages.

The 75% value is only a reporting threshold chosen for this project; it is not presented as an institution-specific rule.

## 16. JSON Storage

Records are stored in `data/attendance.json`. The program loads this file when it starts and saves changes after student or attendance operations.

If the file does not exist, the program starts with an empty list.

## 17. Input Validation and Error Handling

The application checks for empty roll numbers, duplicate roll numbers, empty names and courses, invalid dates, invalid attendance values, and invalid menu choices.

JSON loading catches invalid JSON or file errors so that a bad or missing file does not immediately terminate the program.

## 18. Functional Requirements

- Add student
- Mark attendance
- View students
- Search by roll number
- Update student details
- Delete student
- Calculate attendance percentage
- Generate attendance report
- Save records permanently

## 19. Non-Functional Requirements

### Usability
Prompts and numbered menu choices are kept straightforward.

### Reliability
Input is validated and changes are saved to the data file.

### Maintainability
The application is split into functions with clear responsibilities.

### Portability
Only the Python standard library is required.

### Performance
The list-based approach is adequate for a small classroom dataset.

## 20. Data Structures

The main collection is a list. Each student is a dictionary, and each attendance entry is another dictionary. JSON is used to serialize the complete structure.

## 21. Algorithms

### Sequential Search
`find_student()` checks student records one by one until a matching roll number is found.

### Attendance Calculation
The program counts total attendance entries and entries marked `P`, then calculates the percentage.

### Duplicate Date Handling
Before adding attendance for a date, any existing entry for that date is removed and the new status is stored.

## 22. Program Flow

```text
START
  |
Load JSON
  |
Main Menu
  |
Select operation
  |
Validate input
  |
Perform operation
  |
Save changes
  |
Main Menu
  |
Exit
  |
END
```

## 23. Testing

The project contains `tests/test_attendance.py` and uses Python's built-in `unittest` framework.

The tests cover:

1. Correct attendance calculation.
2. Case-insensitive student search.
3. Empty attendance calculation.
4. Adding a student.
5. Rejecting a duplicate student.

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## 24. Advantages

- Simple to use
- No external packages
- Automatic calculations
- Date-wise attendance history
- Persistent storage
- Search, update, and delete functions
- Low-attendance report
- Automated tests

## 25. Limitations

The application is console based and intended for local use. JSON is suitable for this small project but a larger system would normally use a database. There is also no login system, multi-user access, QR scanning, or biometric attendance.

## 26. Future Scope

Possible improvements include a Tkinter GUI, SQLite database, teacher login, subject-wise attendance, CSV/PDF export, charts, configurable thresholds, backups, and QR-code attendance.

## 27. Learning Outcomes

The project gives practice with Python functions, lists, dictionaries, loops, conditions, file handling, JSON, exception handling, date validation, modular design, and unit testing. It also demonstrates how a familiar real-world problem can be converted into a small working application.

## 28. Conclusion

The Student Attendance Management System provides a straightforward way to maintain classroom attendance. It handles the main tasks needed in a small class: adding students, recording attendance, finding records, calculating percentages, and preparing a simple report.

The project is intentionally not presented as a large commercial system. Its main purpose is to demonstrate practical Python programming in a form that is understandable, testable, and useful.

## 29. How to Run

Run the application:

```bash
python student_attendance_management.py
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

No additional packages are required.

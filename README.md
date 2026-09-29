# Student Attendance Management System

This is a small Python project for keeping track of student attendance. I kept the design deliberately simple so that the program is easy to run, understand, and demonstrate in a first-year project.

The program can add students, mark daily attendance, search and update records, calculate attendance percentages, and produce a report showing students below 75%.

## Features

- Add student
- Mark Present/Absent attendance by date
- View all students
- Search by roll number
- Update student details
- Delete a student with confirmation
- Calculate attendance percentage
- Show class average
- Find students below 75%
- Save records in JSON
- Automated unit tests

## Technology

Python 3 and the Python standard library only. JSON is used for storage and `unittest` is used for testing.

## Structure

```text
Student Attendance Management System/
├── student_attendance_management.py
├── README.md
├── statement.md
├── RUN_PROJECT.txt
├── requirements.txt
├── .gitignore
├── data/attendance.json
├── docs/ALGORITHM_AND_FLOW.md
├── docs/PROJECT_REPORT.md
└── tests/
    ├── __init__.py
    └── test_attendance.py
```

## Run

```bash
python student_attendance_management.py
```

## Test

```bash
python -m unittest discover -s tests -v
```

No external packages are required.

## Data

Attendance is stored in `data/attendance.json`. If the file is missing, the program starts with an empty list and creates the file when data is first saved.

## Note

The 75% value is used as a reporting threshold in this project. It is not intended to represent a specific college's official attendance policy.

## Student Attendance Management System

A small project implemented in Python for managing student's attendance. The design is kept simple for easier run, understanding, and demonstration as it is a first-year project.

The application allows you to add students, mark attendance (present/absent) for a particular day, view students, search for a student by roll number, update and delete students, calculate attendance percentage, view class average, view students below 75%, save in JSON, and automated unit tests.

## Features

• Add student
• Mark Present/Absent attendance by date
• View all students
• Search by roll number
• Update student
• Delete a student (with confirmation)
• Calculate attendance percentage
• View class average
• View students below 75%
• Save records in JSON
• Automated unit tests
Tech

Python 3 and the Python standard library only. JSON is used for saving, and unittest is used for testing.

## Structure

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

## How to Run

python student_attendance_management.py

## How to Test

python -m unittest discover -s tests -v

No external libraries are used.

## Data

The data is stored in data/attendance,json. In case of a missing file, the application will start with an empty list and save the data on the first run.

## Note

The value 75% is set as the lower threshold for attendance percentage in this application, but it does not imply that it is the actual attendance policy of any particular college.

## Author

Name :- AMAN RAJ GUPTA
Registration Number :- 26BCE10545

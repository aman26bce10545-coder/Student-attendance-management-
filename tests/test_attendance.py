import unittest
from unittest.mock import patch
import student_attendance_management as app


class AttendanceTests(unittest.TestCase):
    def test_calculate_summary(self):
        student = {"attendance": [
            {"date": "2026-09-01", "status": "P"},
            {"date": "2026-09-02", "status": "P"},
            {"date": "2026-09-03", "status": "A"},
            {"date": "2026-09-04", "status": "P"}]}
        self.assertEqual(app.calculate_summary(student), (4, 3, 1, 75.0))

    def test_find_student_case_insensitive(self):
        records = [{"roll_no": "A101", "name": "Aarav", "course": "BCA", "attendance": []}]
        self.assertIsNotNone(app.find_student(records, "a101"))
        self.assertIsNone(app.find_student(records, "B101"))

    def test_empty_attendance(self):
        self.assertEqual(app.calculate_summary({"attendance": []}), (0, 0, 0, 0.0))

    def test_add_student(self):
        records = []
        with patch("builtins.input", side_effect=["101", "Aarav", "BCA"]):
            with patch.object(app, "save_data"):
                app.add_student(records)
        self.assertEqual(records[0]["roll_no"], "101")

    def test_duplicate_student(self):
        records = [{"roll_no": "101", "name": "Aarav", "course": "BCA", "attendance": []}]
        with patch("builtins.input", return_value="101"):
            app.add_student(records)
        self.assertEqual(len(records), 1)


if __name__ == "__main__":
    unittest.main()

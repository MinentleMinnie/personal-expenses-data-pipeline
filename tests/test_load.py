import sqlite3
import tempfile
import unittest
from pathlib import Path

from src.load import load_expenses


class TestLoadExpenses(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_expenses.db"

        self.records = [
            {
                "expense_id": 1,
                "date": "2026-10-01",
                "category": "Groceries",
                "amount": 450.0,
            },
            {
                "expense_id": 2,
                "date": "2026-10-02",
                "category": "Transport",
                "amount": 35.0,
            },
        ]

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_expenses_are_inserted(self):
        inserted = load_expenses(self.records, self.db_path)

        self.assertEqual(inserted, 2)

        with sqlite3.connect(self.db_path) as connection:
            result = connection.execute(
                "SELECT COUNT(*) FROM expenses"
            ).fetchone()[0]

        self.assertEqual(result, 2)

    def test_running_loader_twice_does_not_duplicate_records(self):
        first_insert = load_expenses(self.records, self.db_path)
        second_insert = load_expenses(self.records, self.db_path)

        self.assertEqual(first_insert, 2)
        self.assertEqual(second_insert, 0)

        with sqlite3.connect(self.db_path) as connection:
            result = connection.execute(
                "SELECT COUNT(*) FROM expenses"
            ).fetchone()[0]

        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()

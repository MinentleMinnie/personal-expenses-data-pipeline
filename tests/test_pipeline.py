import sqlite3
import tempfile
import unittest
from pathlib import Path

from src.transform import transform_data
from src.load import load_expenses


class TestExpensePipeline(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_dir.name) / "test_expenses.db"

        self.raw_records = [
            {
                "date": "2026-10-01",
                "category": "Groceries",
                "amount": "450"
            },
            {
                "date": "2026-10-02",
                "category": "transport",
                "amount": "35"
            },
            {
                "date": "invalid-date",
                "category": "Entertainment",
                "amount": "100"
            }
        ]

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_pipeline_cleans_and_loads_valid_records(self):
        clean_records, rejected_records = transform_data(self.raw_records)

        self.assertEqual(len(clean_records), 2)
        self.assertEqual(len(rejected_records), 1)

        inserted_count = load_expenses(clean_records, self.db_path)

        self.assertEqual(inserted_count, 2)

        with sqlite3.connect(self.db_path) as connection:
            rows = connection.execute(
                "SELECT category, amount FROM expenses ORDER BY expense_id"
            ).fetchall()

        self.assertEqual(
            rows,
            [("Groceries", 450.0), ("Transport", 35.0)]
        )

    def test_pipeline_does_not_duplicate_records(self):
        clean_records, _ = transform_data(self.raw_records)

        first_insert = load_expenses(clean_records, self.db_path)
        second_insert = load_expenses(clean_records, self.db_path)

        self.assertEqual(first_insert, 2)
        self.assertEqual(second_insert, 0)


if __name__ == "__main__":
    unittest.main()
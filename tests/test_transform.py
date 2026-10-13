import unittest

from src.transform import transform_data


class TestTransformData(unittest.TestCase):

    def test_valid_record_is_accepted(self):
        records = [{
            "expense_id": "1",
            "date": "2026-10-01",
            "category": "Groceries",
            "amount": "450"
        }]

        clean, rejected = transform_data(records)

        self.assertEqual(len(clean), 1)
        self.assertEqual(len(rejected), 0)

    def test_category_is_standardised(self):
        records = [{
            "expense_id": "1",
            "date": "2026-10-01",
            "category": "groceries",
            "amount": "450"
        }]

        clean, rejected = transform_data(records)

        self.assertEqual(clean[0]["category"], "Groceries")

    def test_invalid_date_is_rejected(self):
        records = [{
            "expense_id": "1",
            "date": "not-a-date",
            "category": "Groceries",
            "amount": "450"
        }]

        clean, rejected = transform_data(records)

        self.assertEqual(len(clean), 0)
        self.assertEqual(len(rejected), 1)

    def test_invalid_amount_is_rejected(self):
        records = [{
            "expense_id": "1",
            "date": "2026-10-01",
            "category": "Groceries",
            "amount": "invalid"
        }]

        clean, rejected = transform_data(records)

        self.assertEqual(len(clean), 0)
        self.assertEqual(len(rejected), 1)

    def test_blank_category_is_rejected(self):
        records = [{
            "expense_id": "1",
            "date": "2026-10-01",
            "category": "",
            "amount": "450"
        }]

        clean, rejected = transform_data(records)

        self.assertEqual(len(clean), 0)
        self.assertEqual(len(rejected), 1)


if __name__ == "__main__":
    unittest.main()

import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "expenses.csv"


def extract_data():
    with open(CSV_PATH, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    expenses = extract_data()

    print(f"Records extracted: {len(expenses)}")

    for expense in expenses:
        print(expense)

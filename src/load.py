import sqlite3
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "database" / "expenses.db"
SCHEMA_PATH = PROJECT_ROOT / "database" / "schema.sql"


def initialize_database(db_path=DATABASE_PATH):
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    schema = SCHEMA_PATH.read_text(encoding="utf-8")

    with sqlite3.connect(db_path) as connection:
        connection.executescript(schema)


def load_expenses(records, db_path=DATABASE_PATH):
    initialize_database(db_path)

    inserted_count = 0

    with sqlite3.connect(db_path) as connection:
        for record in records:
            cursor = connection.execute(
                """
                INSERT OR IGNORE INTO expenses
                    (expense_id, date, category, amount)
                VALUES (?, ?, ?, ?)
                """,
                (
                    record["expense_id"],
                    record["date"],
                    record["category"],
                    record["amount"],
                ),
            )

            inserted_count += cursor.rowcount

    return inserted_count


if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    raw_records = extract_data()
    clean_records, rejected_records = transform_data(raw_records)

    inserted = load_expenses(clean_records)

    print(f"Records extracted: {len(raw_records)}")
    print(f"Records accepted: {len(clean_records)}")
    print(f"Records rejected: {len(rejected_records)}")
    print(f"New records loaded: {inserted}")
    print(f"Database location: {DATABASE_PATH}")

import sqlite3
from load import DATABASE_PATH


def get_total_expenses(db_path=DATABASE_PATH):
    with sqlite3.connect(db_path) as connection:
        result = connection.execute(
            "SELECT SUM(amount) FROM expenses"
        ).fetchone()

    return result[0] or 0


def get_expenses_by_category(db_path=DATABASE_PATH):
    with sqlite3.connect(db_path) as connection:
        results = connection.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            GROUP BY category
            ORDER BY total DESC
            """
        ).fetchall()

    return results


def get_expense_count(db_path=DATABASE_PATH):
    with sqlite3.connect(db_path) as connection:
        result = connection.execute(
            "SELECT COUNT(*) FROM expenses"
        ).fetchone()

    return result[0]


def get_average_expense(db_path=DATABASE_PATH):
    with sqlite3.connect(db_path) as connection:
        result = connection.execute(
            "SELECT AVG(amount) FROM expenses"
        ).fetchone()

    return result[0] or 0


def main():
    total = get_total_expenses()
    categories = get_expenses_by_category()
    count = get_expense_count()
    average = get_average_expense()

    print("EXPENSE ANALYSIS")
    print("================")
    print(f"Total expenses: R{total:.2f}")
    print(f"Number of records: {count}")
    print(f"Average expense: R{average:.2f}")

    print("\nSpending by category:")

    for category, amount in categories:
        print(f"{category}: R{amount:.2f}")


if __name__ == "__main__":
    main()

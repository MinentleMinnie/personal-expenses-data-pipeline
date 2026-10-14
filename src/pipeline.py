import logging

from extract import extract_data
from transform import transform_data
from load import load_expenses
from analyze import (
    get_total_expenses,
    get_expenses_by_category,
    get_expense_count,
    get_average_expense,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def run_pipeline():
    logging.info("Starting expense data pipeline")

    # Step 1: Extract
    raw_records = extract_data()
    logging.info("Records extracted: %s", len(raw_records))

    # Step 2: Transform
    clean_records, rejected_records = transform_data(raw_records)

    logging.info("Records accepted: %s", len(clean_records))
    logging.info("Records rejected: %s", len(rejected_records))

    # Step 3: Load
    inserted_count = load_expenses(clean_records)
    logging.info("New records loaded: %s", inserted_count)

    # Step 4: Analyse
    print("\nEXPENSE ANALYSIS")
    print("================")

    print(f"Total expenses: R{get_total_expenses():.2f}")
    print(f"Number of records: {get_expense_count()}")
    print(f"Average expense: R{get_average_expense():.2f}")

    print("\nSpending by category:")

    for category, amount in get_expenses_by_category():
        print(f"{category}: R{amount:.2f}")

    # Step 5: Finish
    logging.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
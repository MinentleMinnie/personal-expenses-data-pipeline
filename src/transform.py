from datetime import datetime
import math


def transform_data(records):
    clean_records = []
    rejected_records = []

    for expense_id, record in enumerate(records, start=1):
        try:
            date_value = record["date"].strip()
            category_value = record["category"].strip()
            amount = float(record["amount"])

            datetime.strptime(date_value, "%Y-%m-%d")

            if not category_value:
                raise ValueError("Category cannot be blank")

            if not math.isfinite(amount) or amount <= 0:
                raise ValueError("Amount must be a positive number")

            clean_records.append({
                "expense_id": expense_id,
                "date": date_value,
                "category": category_value.title(),
                "amount": amount
            })

        except (KeyError, TypeError, ValueError):
            rejected_records.append(record)

    return clean_records, rejected_records


if __name__ == "__main__":
    from extract import extract_data

    raw_records = extract_data()
    clean_records, rejected_records = transform_data(raw_records)

    print(f"Records extracted: {len(raw_records)}")
    print(f"Records accepted: {len(clean_records)}")
    print(f"Records rejected: {len(rejected_records)}")

    for record in clean_records:
        print(record)

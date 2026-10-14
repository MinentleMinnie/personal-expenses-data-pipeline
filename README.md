# Personal Expenses Data Pipeline

## Project Overview

This project is a beginner-friendly data engineering project
that processes personal expense records.

The pipeline reads expense data from a CSV file, validates and
cleans the records, stores valid records in an SQLite database,
and generates spending analysis.

It also produces a data quality report showing how many records
were extracted, accepted, and rejected.

## Project Objectives

- Extract data from a CSV file.
- Validate and clean expense records using Python.
- Reject records containing invalid data.
- Store valid records in an SQLite database.
- Analyse spending using SQL queries.
- Generate a data quality report.
- Test the application using Python's unittest framework.

## Technologies Used

- Python
- CSV
- SQLite
- SQL
- Git and GitHub
- Python unittest

## Project Structure

```text
personal-expenses-data-pipeline/
├── data/
│   └── expenses.csv
├── database/
│   ├── expenses.db
│   └── schema.sql
├── reports/
│   └── data_quality_report.txt
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── analyze.py
│   └── pipeline.py
├── tests/
│   ├── test_transform.py
│   ├── test_load.py
│   └── test_pipeline.py
└── README.md
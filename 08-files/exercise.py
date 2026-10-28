# Exercise 8: spending report
#
# transactions.csv (in this folder) is a month of bank transactions with the
# columns date, description, category and amount.
#
# Replace each `pass` with your code. Test with:  python3 -m unittest -v
# Open files with encoding="utf-8", and CSV files with newline="" too.

import csv
import json
from pathlib import Path


def load_transactions(path):
    """Read the CSV file and return a list of dictionaries, with "amount" as a float."""
    pass


def total_by_category(transactions):
    """Return a dictionary of category -> total amount, each rounded to 2 decimal places."""
    pass


def write_summary(totals, path):
    """Write a CSV file with the header category,total and one row per category,
    biggest total first, with totals shown to 2 decimal places."""
    pass


def save_json(data, path):
    """Save data (a dictionary or list) to a JSON file, with indent=2."""
    pass


def load_json(path):
    """Load a JSON file and return its contents."""
    pass


if __name__ == "__main__":
    here = Path(__file__).parent
    transactions = load_transactions(here / "transactions.csv")
    totals = total_by_category(transactions)
    (here / "output").mkdir(exist_ok=True)
    write_summary(totals, here / "output" / "summary.csv")
    save_json(totals, here / "output" / "totals.json")
    print("Wrote output/summary.csv and output/totals.json")

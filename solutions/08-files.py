# Solution to exercise 8: spending report

import csv
import json
from pathlib import Path


def load_transactions(path):
    """Read the CSV file and return a list of dictionaries, with "amount" as a float."""
    transactions = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["amount"] = float(row["amount"])
            transactions.append(row)
    return transactions


def total_by_category(transactions):
    """Return a dictionary of category -> total amount, each rounded to 2 decimal places."""
    totals = {}
    for t in transactions:
        totals[t["category"]] = totals.get(t["category"], 0) + t["amount"]
    for category in totals:
        totals[category] = round(totals[category], 2)
    return totals


def write_summary(totals, path):
    """Write a CSV file with the header category,total and one row per category,
    biggest total first, with totals shown to 2 decimal places."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "total"])
        for category in sorted(totals, key=totals.get, reverse=True):
            writer.writerow([category, f"{totals[category]:.2f}"])


def save_json(data, path):
    """Save data (a dictionary or list) to a JSON file, with indent=2."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(path):
    """Load a JSON file and return its contents."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    here = Path(__file__).parent
    transactions = load_transactions(here / "transactions.csv")
    totals = total_by_category(transactions)
    (here / "output").mkdir(exist_ok=True)
    write_summary(totals, here / "output" / "summary.csv")
    save_json(totals, here / "output" / "totals.json")
    print("Wrote output/summary.csv and output/totals.json")

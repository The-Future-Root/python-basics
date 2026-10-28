# Solution to exercise 9: careful input handling

import json


def parse_amount(text):
    """Turn text like "12.50", " $1,234.99 " or "$5" into a float."""
    cleaned = text.strip()
    if cleaned.startswith("$"):
        cleaned = cleaned[1:]
    cleaned = cleaned.replace(",", "")
    try:
        amount = float(cleaned)
    except ValueError:
        raise ValueError(f"Not a valid amount: {text!r}")
    if amount <= 0:
        raise ValueError("Amount must be more than zero")
    return amount


def safe_divide(a, b):
    """Return a / b, or None if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def read_setting(path, key, default):
    """Return data[key] from the JSON file at path, or default if anything is missing."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data[key]
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return default


def ask_for_quantity():
    """Ask "Quantity: " until the user types a whole number of at least 1, then return it."""
    while True:
        try:
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Please enter a whole number of at least 1")
            continue
        if quantity >= 1:
            return quantity
        print("Please enter a whole number of at least 1")


if __name__ == "__main__":
    print(parse_amount(" $1,234.99 "))
    print(safe_divide(10, 0))
    print("You ordered", ask_for_quantity())

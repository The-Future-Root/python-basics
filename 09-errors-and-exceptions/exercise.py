# Exercise 9: careful input handling
#
# Replace each `pass` with your code. Test with:  python3 -m unittest -v

import json


def parse_amount(text):
    """Turn text like "12.50", " $1,234.99 " or "$5" into a float.

    Raise ValueError("Not a valid amount: '<text>'") if it isn't a number,
    and ValueError("Amount must be more than zero") if it's zero or negative.
    """
    pass


def safe_divide(a, b):
    """Return a / b, or None if b is zero. Use try/except, not an if."""
    pass


def read_setting(path, key, default):
    """Return data[key] from the JSON file at path, or default if the file is
    missing, isn't valid JSON, or doesn't have that key."""
    pass


def ask_for_quantity():
    """Ask "Quantity: " until the user types a whole number of at least 1, then return it.
    After invalid input, print "Please enter a whole number of at least 1"."""
    pass


if __name__ == "__main__":
    print(parse_amount(" $1,234.99 "))
    print(safe_divide(10, 0))
    print("You ordered", ask_for_quantity())

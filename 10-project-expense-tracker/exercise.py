# Project 10: expense tracker
#
# Build it in the steps described in README.md, running the tests after each step:
#     python3 -m unittest -v
# Replace each `pass` with your code.

import json

HELP = """Commands:
  add <amount> <category> <description>   record an expense
  list                                    show every expense
  total                                   show the total spent
  summary                                 show the total for each category
  delete <number>                         remove an expense
  help                                    show this list
  quit                                    save and exit"""


# Step 1: amounts and expenses

def parse_amount(text):
    """Turn text like "12.50", " $1,234.99 " or "$5" into a float (see lesson 9)."""
    pass


def make_expense(amount_text, category, description):
    """Return a dictionary with "amount" (a float), "category" (lowercase) and "description"."""
    pass


# Step 2: reporting

def total(expenses):
    """Return the sum of all the amounts, rounded to 2 decimal places."""
    pass


def summary(expenses):
    """Return a dictionary of category -> total, each rounded to 2 decimal places."""
    pass


def format_expense(number, expense):
    """Return one line like "1. $12.50 food: Lunch with Sam"."""
    pass


# Step 3: deleting

def delete_expense(expenses, number_text):
    """Remove expense number `number_text` (counting from 1) and return it, or return None."""
    pass


# Step 4: saving and loading

def load_expenses(path):
    """Return the list saved at path, or an empty list if the file doesn't exist."""
    pass


def save_expenses(expenses, path):
    """Save the list of expenses to path as JSON, with indent=2."""
    pass


# Step 5: the command loop

def main(path="expenses.json"):
    """Load the expenses, then read commands until "quit" (see the table in README.md)."""
    pass


if __name__ == "__main__":
    main()

# Solution to project 10: expense tracker

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


def make_expense(amount_text, category, description):
    """Return a dictionary with "amount" (a float), "category" (lowercase) and "description"."""
    return {
        "amount": parse_amount(amount_text),
        "category": category.strip().lower(),
        "description": description.strip(),
    }


# Step 2: reporting

def total(expenses):
    """Return the sum of all the amounts, rounded to 2 decimal places."""
    amount = 0
    for e in expenses:
        amount += e["amount"]
    return round(amount, 2)


def summary(expenses):
    """Return a dictionary of category -> total, each rounded to 2 decimal places."""
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for category in totals:
        totals[category] = round(totals[category], 2)
    return totals


def format_expense(number, expense):
    """Return one line like "1. $12.50 food: Lunch with Sam"."""
    return f"{number}. ${expense['amount']:.2f} {expense['category']}: {expense['description']}"


# Step 3: deleting

def delete_expense(expenses, number_text):
    """Remove expense number `number_text` (counting from 1) and return it, or return None."""
    try:
        number = int(number_text)
    except ValueError:
        return None
    if 1 <= number <= len(expenses):
        return expenses.pop(number - 1)
    return None


# Step 4: saving and loading

def load_expenses(path):
    """Return the list saved at path, or an empty list if the file doesn't exist."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses, path):
    """Save the list of expenses to path as JSON, with indent=2."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)


# Step 5: the command loop

def main(path="expenses.json"):
    expenses = load_expenses(path)
    print("Expense tracker. Type help to see the commands.")
    while True:
        line = input("> ").strip()
        if not line:
            continue
        parts = line.split(maxsplit=3)
        command = parts[0].lower()

        if command == "add":
            if len(parts) < 4:
                print("Usage: add <amount> <category> <description>")
                continue
            try:
                expense = make_expense(parts[1], parts[2], parts[3])
            except ValueError as error:
                print(error)
                continue
            expenses.append(expense)
            print(f"Added: ${expense['amount']:.2f} {expense['category']} ({expense['description']})")

        elif command == "list":
            if not expenses:
                print("No expenses yet")
            for number, expense in enumerate(expenses, start=1):
                print(format_expense(number, expense))

        elif command == "total":
            print(f"Total: ${total(expenses):.2f}")

        elif command == "summary":
            totals = summary(expenses)
            if not totals:
                print("No expenses yet")
            for category in sorted(totals, key=totals.get, reverse=True):
                print(f"{category}: ${totals[category]:.2f}")

        elif command == "delete":
            number_text = parts[1] if len(parts) > 1 else ""
            removed = delete_expense(expenses, number_text)
            if removed is None:
                print(f"No expense number {number_text}")
            else:
                print(f"Deleted: {removed['description']}")

        elif command == "help":
            print(HELP)

        elif command == "quit":
            save_expenses(expenses, path)
            word = "expense" if len(expenses) == 1 else "expenses"
            print(f"Saved {len(expenses)} {word}. Goodbye.")
            break

        else:
            print("Unknown command. Type help to see the commands.")


if __name__ == "__main__":
    main()

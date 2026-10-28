# Solution to exercise 6: bill toolkit


def calculate_tip(bill, percent=15):
    """Return the tip for a bill, rounded to 2 decimal places."""
    return round(bill * percent / 100, 2)


def split_bill(total, people):
    """Return each person's share, rounded to 2 decimal places, or None if people is less than 1."""
    if people < 1:
        return None
    return round(total / people, 2)


def format_money(amount):
    """Return the amount as text like "$1,234.50"."""
    return f"${amount:,.2f}"


def bill_summary(bill, percent, people):
    """Return three lines of text: the tip, the total and each person's share."""
    tip = calculate_tip(bill, percent)
    total = bill + tip
    each = split_bill(total, people)
    return ("Tip: " + format_money(tip) + "\n"
            + "Total: " + format_money(total) + "\n"
            + "Each person pays: " + format_money(each))


if __name__ == "__main__":
    print(bill_summary(84.40, 15, 4))

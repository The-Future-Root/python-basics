# Exercise 6: bill toolkit
#
# Fill in the four functions. None of them should use input() or print():
# they take values as parameters and return a value.
# Replace each `pass` with your code. Test with:  python3 -m unittest -v


def calculate_tip(bill, percent=15):
    """Return the tip for a bill, rounded to 2 decimal places."""
    pass


def split_bill(total, people):
    """Return each person's share, rounded to 2 decimal places, or None if people is less than 1."""
    pass


def format_money(amount):
    """Return the amount as text like "$1,234.50"."""
    pass


def bill_summary(bill, percent, people):
    """Return three lines of text: the tip, the total and each person's share.

    Use calculate_tip, split_bill and format_money to build it.
    """
    pass


# This only runs when you run the file directly (python3 exercise.py),
# not when the tests import it.
if __name__ == "__main__":
    print(bill_summary(84.40, 15, 4))

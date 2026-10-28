import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

from exercise import (delete_expense, format_expense, load_expenses, make_expense, parse_amount,
                      save_expenses, summary, total)

PROGRAM = pathlib.Path(__file__).with_name("exercise.py")


def sample():
    return [
        {"amount": 12.5, "category": "food", "description": "Lunch with Sam"},
        {"amount": 2.0, "category": "transport", "description": "Bus to work"},
        {"amount": 4.8, "category": "food", "description": "Coffee"},
    ]


class TestStep1AmountsAndExpenses(unittest.TestCase):
    def test_parse_amount(self):
        self.assertEqual(parse_amount(" $1,234.99 "), 1234.99)
        with self.assertRaises(ValueError):
            parse_amount("lots")
        with self.assertRaises(ValueError):
            parse_amount("0")

    def test_make_expense(self):
        self.assertEqual(make_expense("12.50", " Food ", " Lunch with Sam "),
                         {"amount": 12.5, "category": "food", "description": "Lunch with Sam"})

    def test_make_expense_bad_amount(self):
        with self.assertRaises(ValueError):
            make_expense("abc", "food", "Lunch")


class TestStep2Reporting(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(sample()), 19.3)
        self.assertEqual(total([]), 0)

    def test_summary(self):
        self.assertEqual(summary(sample()), {"food": 17.3, "transport": 2.0})
        self.assertEqual(summary([]), {})

    def test_format_expense(self):
        self.assertEqual(format_expense(1, sample()[0]), "1. $12.50 food: Lunch with Sam")
        self.assertEqual(format_expense(2, sample()[1]), "2. $2.00 transport: Bus to work")


class TestStep3Deleting(unittest.TestCase):
    def test_delete_by_number_from_1(self):
        expenses = sample()
        removed = delete_expense(expenses, "2")
        self.assertEqual(removed["description"], "Bus to work", "Numbers start at 1: delete 2 removes the second")
        self.assertEqual(len(expenses), 2)

    def test_delete_invalid(self):
        expenses = sample()
        for text in ("0", "4", "-1", "two", ""):
            self.assertIsNone(delete_expense(expenses, text), f"delete {text!r} should return None")
        self.assertEqual(len(expenses), 3, "Invalid numbers shouldn't remove anything")


class TestStep4SavingAndLoading(unittest.TestCase):
    def test_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "expenses.json"
            save_expenses(sample(), path)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), sample())
            self.assertEqual(load_expenses(path), sample())

    def test_missing_file_is_empty(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_expenses(pathlib.Path(folder) / "nothing.json"), [])


class TestStep5WholeProgram(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.folder.cleanup()

    def run_program(self, *commands):
        result = subprocess.run([sys.executable, str(PROGRAM)], input="\n".join(commands) + "\n",
                                capture_output=True, text=True, timeout=10, cwd=self.folder.name)
        return result.stdout + result.stderr

    def test_session_from_readme(self):
        output = self.run_program("add 12.50 food Lunch with Sam", "add 2.00 transport Bus to work",
                                  "add 4.80 food Coffee", "list", "total", "summary", "delete 2",
                                  "add lots food Dinner", "quit")
        for line in ("Expense tracker. Type help to see the commands.",
                     "Added: $12.50 food (Lunch with Sam)",
                     "1. $12.50 food: Lunch with Sam", "2. $2.00 transport: Bus to work", "3. $4.80 food: Coffee",
                     "Total: $19.30", "food: $17.30", "transport: $2.00",
                     "Deleted: Bus to work", "Not a valid amount: 'lots'", "Saved 2 expenses. Goodbye."):
            self.assertIn(line, output, f"Expected to see: {line}")
        self.assertLess(output.index("food: $17.30"), output.index("transport: $2.00"),
                        "summary should list the biggest category first")

    def test_remembers_between_runs(self):
        self.run_program("add 3.20 coffee Flat white", "quit")
        output = self.run_program("list", "quit")
        self.assertIn("1. $3.20 coffee: Flat white", output, "Expenses should be loaded from expenses.json")
        self.assertIn("Saved 1 expense. Goodbye.", output, "Use 'expense', not 'expenses', for one")

    def test_handles_mistakes(self):
        output = self.run_program("add 12.50", "dance", "delete 7", "", "LIST", "quit")
        self.assertIn("Usage: add <amount> <category> <description>", output)
        self.assertIn("Unknown command. Type help to see the commands.", output)
        self.assertIn("No expense number 7", output)
        self.assertIn("No expenses yet", output, "Commands should be case-insensitive: LIST works like list")

    def test_help(self):
        output = self.run_program("help", "quit")
        for command in ("add", "list", "total", "summary", "delete", "quit"):
            self.assertIn(command, output)


if __name__ == "__main__":
    unittest.main()

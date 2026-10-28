import pathlib
import subprocess
import sys
import unittest

PROGRAM = pathlib.Path(__file__).with_name("exercise.py")


def run(*answers):
    """Run exercise.py as a user would, typing each answer and pressing Enter."""
    result = subprocess.run([sys.executable, str(PROGRAM)], input="\n".join(answers) + "\n",
                            capture_output=True, text=True, timeout=10)
    return result.stdout + result.stderr


def expected(bill, tip_percent, people):
    tip = bill * tip_percent / 100
    total = bill + tip
    return [f"Bill: ${bill:.2f}", f"Tip ({tip_percent}%): ${tip:.2f}",
            f"Total: ${total:.2f}", f"Each person pays: ${total / people:.2f}"]


class TestSplitTheBill(unittest.TestCase):
    def check(self, bill, tip, people):
        output = run(str(bill), str(tip), str(people))
        for line in expected(bill, tip, people):
            self.assertIn(line, output, f"With {bill}, {tip}% and {people} people, expected the line: {line}")

    def test_asks_three_questions(self):
        output = run("84.40", "15", "4")
        for prompt in ("Bill amount: ", "Tip percent: ", "Number of people: "):
            self.assertIn(prompt, output, f"Expected the prompt {prompt!r}")

    def test_example_from_readme(self):
        self.check(84.40, 15, 4)

    def test_no_tip_one_person(self):
        self.check(20.0, 0, 1)

    def test_bigger_group(self):
        self.check(312.5, 20, 6)

    def test_two_decimal_places(self):
        output = run("10", "10", "3")
        self.assertIn("Bill: $10.00", output, "Show the bill with 2 decimal places: $10.00")
        self.assertIn("Each person pays: $3.67", output, "Round to 2 decimal places with :.2f")


if __name__ == "__main__":
    unittest.main()

import pathlib
import subprocess
import sys
import unittest

PROGRAM = pathlib.Path(__file__).with_name("exercise.py")


def run(*answers):
    result = subprocess.run([sys.executable, str(PROGRAM)], input="\n".join(answers) + "\n",
                            capture_output=True, text=True, timeout=10)
    return result.stdout + result.stderr


class TestSavingsGoal(unittest.TestCase):
    def test_asks_both_questions(self):
        output = run("100", "100")
        self.assertIn("Monthly saving: ", output)
        self.assertIn("Savings goal: ", output)

    def test_example_from_readme(self):
        output = run("250", "900")
        for line in ("Month 1: $250.00", "Month 2: $500.00", "Month 3: $750.00", "Month 4: $1,000.00",
                     "Goal reached in 4 months"):
            self.assertIn(line, output, f"Expected the line: {line}")
        self.assertNotIn("Month 5", output, "Stop as soon as the balance reaches the goal")

    def test_exactly_on_the_goal(self):
        output = run("300", "900")
        self.assertIn("Month 3: $900.00", output)
        self.assertIn("Goal reached in 3 months", output)
        self.assertNotIn("Month 4", output, "Reaching the goal exactly counts as reached")

    def test_one_month(self):
        output = run("500", "200")
        self.assertIn("Month 1: $500.00", output)
        self.assertIn("Goal reached in 1 month", output)
        self.assertNotIn("1 months", output, "Use 'month', not 'months', for one month")

    def test_decimals_and_thousands(self):
        output = run("1234.5", "2500")
        self.assertIn("Month 2: $2,469.00", output)
        self.assertIn("Month 3: $3,703.50", output)

    def test_zero_saving_stops(self):
        output = run("0", "500")
        self.assertIn("Monthly saving must be more than zero", output)
        self.assertNotIn("Month 1", output)


if __name__ == "__main__":
    unittest.main()

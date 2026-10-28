import pathlib
import subprocess
import sys
import unittest

PROGRAM = pathlib.Path(__file__).with_name("exercise.py")


def run(*answers):
    result = subprocess.run([sys.executable, str(PROGRAM)], input="\n".join(answers) + "\n",
                            capture_output=True, text=True, timeout=10)
    return result.stdout + result.stderr


class TestShipping(unittest.TestCase):
    def check(self, total, country, shipping_line, pay):
        output = run(total, country)
        self.assertIn(shipping_line, output, f"Order {total} to {country!r}: expected {shipping_line!r}")
        self.assertIn(f"Total to pay: ${pay}", output, f"Order {total} to {country!r}: expected Total to pay: ${pay}")

    def test_asks_both_questions(self):
        output = run("10", "US")
        self.assertIn("Order total: ", output)
        self.assertIn("Country: ", output)

    def test_us_small_order(self):
        self.check("42.50", "US", "Shipping: $4.99", "47.49")

    def test_us_free_at_exactly_50(self):
        self.check("50", "US", "Shipping: FREE", "50.00")

    def test_country_any_case_and_spaces(self):
        self.check("75", "  us ", "Shipping: FREE", "75.00")

    def test_international_small_order(self):
        self.check("60", "France", "Shipping: $19.99", "79.99")

    def test_international_large_order(self):
        self.check("100", "Japan", "Shipping: $9.99", "109.99")

    def test_invalid_total(self):
        for total in ("0", "-5"):
            output = run(total, "US")
            self.assertIn("Order total must be more than zero", output)
            self.assertNotIn("Shipping", output, "For an invalid total, print only the error message")


if __name__ == "__main__":
    unittest.main()

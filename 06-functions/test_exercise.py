import ast
import pathlib
import unittest

from exercise import bill_summary, calculate_tip, format_money, split_bill

SOURCE = pathlib.Path(__file__).with_name("exercise.py").read_text()


def functions_called_inside(function_name):
    for node in ast.walk(ast.parse(SOURCE)):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            return {n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    return set()


def uses(function_name, builtin):
    return builtin in functions_called_inside(function_name)


class TestCalculateTip(unittest.TestCase):
    def test_default_is_15_percent(self):
        self.assertEqual(calculate_tip(100), 15.0)

    def test_other_percent(self):
        self.assertEqual(calculate_tip(84.40, 15), 12.66)
        self.assertEqual(calculate_tip(50, 20), 10.0)

    def test_rounded_to_2_places(self):
        self.assertEqual(calculate_tip(33.33, 10), 3.33)


class TestSplitBill(unittest.TestCase):
    def test_even_split(self):
        self.assertEqual(split_bill(100, 4), 25.0)

    def test_rounded_to_2_places(self):
        self.assertEqual(split_bill(10, 3), 3.33)

    def test_less_than_one_person(self):
        self.assertIsNone(split_bill(50, 0), "Return None when people is less than 1")
        self.assertIsNone(split_bill(50, -2))


class TestFormatMoney(unittest.TestCase):
    def test_two_decimals(self):
        self.assertEqual(format_money(3.4), "$3.40")

    def test_thousands(self):
        self.assertEqual(format_money(1234.5), "$1,234.50")

    def test_returns_text(self):
        self.assertIsInstance(format_money(5), str, "Return the text, don't print it")


class TestBillSummary(unittest.TestCase):
    def test_example(self):
        self.assertEqual(bill_summary(84.40, 15, 4), "Tip: $12.66\nTotal: $97.06\nEach person pays: $24.27")

    def test_another_bill(self):
        self.assertEqual(bill_summary(1000, 10, 3), "Tip: $100.00\nTotal: $1,100.00\nEach person pays: $366.67")

    def test_uses_the_other_functions(self):
        called = functions_called_inside("bill_summary")
        for helper in ("calculate_tip", "split_bill", "format_money"):
            self.assertIn(helper, called, f"bill_summary should call {helper}() instead of repeating its code")


class TestNoInputOrPrint(unittest.TestCase):
    def test_functions_return_instead_of_printing(self):
        for name in ("calculate_tip", "split_bill", "format_money", "bill_summary"):
            self.assertFalse(uses(name, "print") or uses(name, "input"),
                             f"{name} should return its result, not use print() or input()")


if __name__ == "__main__":
    unittest.main()

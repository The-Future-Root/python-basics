import ast
import contextlib
import io
import pathlib
import unittest

with contextlib.redirect_stdout(io.StringIO()):
    import exercise

SOURCE = pathlib.Path(__file__).with_name("exercise.py").read_text()


def names_used_in(variable):
    """The variable names used on the right-hand side of `variable = ...` in exercise.py."""
    for node in ast.walk(ast.parse(SOURCE)):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == variable for t in node.targets):
            return {n.id for n in ast.walk(node.value) if isinstance(n, ast.Name)}
    return set()


class TestReceipt(unittest.TestCase):
    def test_product_details(self):
        self.assertEqual(exercise.product_name, "Blueberry muffin")
        self.assertEqual(exercise.unit_price, 2.75)
        self.assertEqual(exercise.quantity, 4)

    def test_subtotal(self):
        self.assertAlmostEqual(exercise.subtotal, 11.0)

    def test_subtotal_is_calculated(self):
        self.assertEqual(names_used_in("subtotal"), {"unit_price", "quantity"},
                         "Calculate subtotal from unit_price and quantity, don't type the number in")

    def test_discount(self):
        self.assertEqual(exercise.discount_percent, 10)
        self.assertAlmostEqual(exercise.discount, 1.1)
        self.assertEqual(names_used_in("discount"), {"subtotal", "discount_percent"},
                         "Calculate discount from subtotal and discount_percent")

    def test_total(self):
        self.assertAlmostEqual(exercise.total, 9.9)
        self.assertEqual(names_used_in("total"), {"subtotal", "discount"},
                         "Calculate total from subtotal and discount")


if __name__ == "__main__":
    unittest.main()

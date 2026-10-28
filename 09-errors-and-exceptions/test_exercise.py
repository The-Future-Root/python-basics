import ast
import io
import json
import pathlib
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest import mock

from exercise import ask_for_quantity, parse_amount, read_setting, safe_divide

SOURCE = pathlib.Path(__file__).with_name("exercise.py").read_text()


def function_node(name):
    for node in ast.walk(ast.parse(SOURCE)):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node


class TestParseAmount(unittest.TestCase):
    def test_plain_number(self):
        self.assertEqual(parse_amount("12.50"), 12.5)

    def test_dollar_sign_commas_and_spaces(self):
        self.assertEqual(parse_amount(" $1,234.99 "), 1234.99)
        self.assertEqual(parse_amount("$5"), 5.0)

    def test_not_a_number(self):
        with self.assertRaises(ValueError) as caught:
            parse_amount("twelve")
        self.assertEqual(str(caught.exception), "Not a valid amount: 'twelve'")

    def test_empty_text(self):
        with self.assertRaises(ValueError) as caught:
            parse_amount("   ")
        self.assertEqual(str(caught.exception), "Not a valid amount: '   '")

    def test_zero_and_negative(self):
        for text in ("0", "-5", "$0.00"):
            with self.assertRaises(ValueError) as caught:
                parse_amount(text)
            self.assertEqual(str(caught.exception), "Amount must be more than zero")


class TestSafeDivide(unittest.TestCase):
    def test_divides(self):
        self.assertEqual(safe_divide(10, 4), 2.5)

    def test_zero(self):
        self.assertIsNone(safe_divide(10, 0))

    def test_uses_try_except(self):
        node = function_node("safe_divide")
        self.assertTrue(any(isinstance(n, ast.Try) for n in ast.walk(node)),
                        "Use try/except ZeroDivisionError in safe_divide")


class TestReadSetting(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.folder.name)

    def tearDown(self):
        self.folder.cleanup()

    def test_reads_key(self):
        path = self.dir / "settings.json"
        path.write_text(json.dumps({"tables": 12, "wifi": True}), encoding="utf-8")
        self.assertEqual(read_setting(path, "tables", 0), 12)

    def test_missing_key(self):
        path = self.dir / "settings.json"
        path.write_text(json.dumps({"tables": 12}), encoding="utf-8")
        self.assertEqual(read_setting(path, "opening_time", "08:00"), "08:00")

    def test_missing_file(self):
        self.assertEqual(read_setting(self.dir / "nope.json", "tables", 4), 4)

    def test_broken_json(self):
        path = self.dir / "broken.json"
        path.write_text("{tables: 12", encoding="utf-8")
        self.assertEqual(read_setting(path, "tables", 4), 4)


class TestAskForQuantity(unittest.TestCase):
    def ask(self, *answers):
        output = io.StringIO()
        with mock.patch("builtins.input", side_effect=list(answers)) as fake_input, redirect_stdout(output):
            result = ask_for_quantity()
        return result, output.getvalue(), fake_input

    def test_valid_first_time(self):
        result, _, fake_input = self.ask("3")
        self.assertEqual(result, 3)
        fake_input.assert_called_with("Quantity: ")

    def test_keeps_asking(self):
        result, output, fake_input = self.ask("lots", "2.5", "0", "-1", "4")
        self.assertEqual(result, 4)
        self.assertEqual(fake_input.call_count, 5)
        self.assertEqual(output.count("Please enter a whole number of at least 1"), 4)


if __name__ == "__main__":
    unittest.main()

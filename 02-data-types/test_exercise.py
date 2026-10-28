import ast
import contextlib
import io
import pathlib
import unittest

with contextlib.redirect_stdout(io.StringIO()):
    import exercise

SOURCE = pathlib.Path(__file__).with_name("exercise.py").read_text()


def assigned_expression(variable):
    for node in ast.walk(ast.parse(SOURCE)):
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == variable for t in node.targets):
            return node.value
    return None


class TestForm(unittest.TestCase):
    def test_age_is_an_int(self):
        self.assertIsInstance(exercise.age, int, "Convert age_text with int()")
        self.assertEqual(exercise.age, 34)

    def test_height_is_a_float(self):
        self.assertIsInstance(exercise.height_m, float, "Convert height_text with float()")
        self.assertEqual(exercise.height_m, 1.75)

    def test_is_member(self):
        self.assertIs(exercise.is_member, True)
        self.assertIsInstance(assigned_expression("is_member"), ast.Compare,
                              "Work out is_member by comparing member_text with \"yes\"")

    def test_clean_name(self):
        self.assertEqual(exercise.clean_name, "Alex Kim")

    def test_clean_email(self):
        self.assertEqual(exercise.clean_email, "alex.kim@example.com")

    def test_age_next_year(self):
        self.assertEqual(exercise.age_next_year, 35)

    def test_welcome(self):
        self.assertEqual(exercise.welcome, "Welcome, Alex Kim!")


if __name__ == "__main__":
    unittest.main()

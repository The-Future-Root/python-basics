import json
import pathlib
import tempfile
import unittest

from exercise import load_json, load_transactions, save_json, total_by_category, write_summary

HERE = pathlib.Path(__file__).parent
SAMPLE = HERE / "transactions.csv"
EXPECTED_TOTALS = {"eating out": 37.9, "groceries": 189.0, "transport": 50.0, "bills": 114.95, "entertainment": 36.99}


class TestLoad(unittest.TestCase):
    def test_one_dictionary_per_row(self):
        rows = load_transactions(SAMPLE)
        self.assertIsInstance(rows, list)
        self.assertEqual(len(rows), 15)

    def test_columns(self):
        first = load_transactions(SAMPLE)[0]
        self.assertEqual(first["date"], "2026-03-01")
        self.assertEqual(first["description"], "Corner Café", "Open the file with encoding=\"utf-8\"")
        self.assertEqual(first["category"], "eating out")

    def test_amount_is_a_float(self):
        first = load_transactions(SAMPLE)[0]
        self.assertIsInstance(first["amount"], float, "Convert amount with float()")
        self.assertEqual(first["amount"], 4.8)


class TestTotals(unittest.TestCase):
    def test_sample_totals(self):
        self.assertEqual(total_by_category(load_transactions(SAMPLE)), EXPECTED_TOTALS)

    def test_small_list(self):
        rows = [{"category": "food", "amount": 1.1}, {"category": "food", "amount": 2.2}, {"category": "bus", "amount": 3.0}]
        self.assertEqual(total_by_category(rows), {"food": 3.3, "bus": 3.0})

    def test_empty(self):
        self.assertEqual(total_by_category([]), {})


class TestFiles(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.dir = pathlib.Path(self.folder.name)

    def tearDown(self):
        self.folder.cleanup()

    def test_summary_csv(self):
        path = self.dir / "summary.csv"
        write_summary(EXPECTED_TOTALS, path)
        lines = path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(lines, [
            "category,total",
            "groceries,189.00",
            "bills,114.95",
            "transport,50.00",
            "eating out,37.90",
            "entertainment,36.99",
        ])

    def test_json_round_trip(self):
        path = self.dir / "totals.json"
        save_json(EXPECTED_TOTALS, path)
        self.assertEqual(load_json(path), EXPECTED_TOTALS)

    def test_json_is_indented(self):
        path = self.dir / "data.json"
        save_json({"a": 1, "b": [1, 2]}, path)
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {"a": 1, "b": [1, 2]})
        self.assertIn("\n  ", path.read_text(encoding="utf-8"), "Use indent=2 so the file is readable")


if __name__ == "__main__":
    unittest.main()

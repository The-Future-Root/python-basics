import unittest

from exercise import add_item, cart_total, item_count, most_expensive, receipt_lines, remove_item


def sample_cart():
    return {
        "Latte": {"price": 3.40, "quantity": 2},
        "Scone": {"price": 2.50, "quantity": 1},
        "Brownie": {"price": 3.95, "quantity": 3},
    }


class TestAddAndRemove(unittest.TestCase):
    def test_add_new_item(self):
        cart = {}
        add_item(cart, "Tea", 2.10)
        self.assertEqual(cart, {"Tea": {"price": 2.10, "quantity": 1}})

    def test_add_with_quantity(self):
        cart = {}
        add_item(cart, "Latte", 3.40, 2)
        self.assertEqual(cart["Latte"]["quantity"], 2)

    def test_adding_again_increases_quantity(self):
        cart = {}
        add_item(cart, "Latte", 3.40, 2)
        add_item(cart, "Latte", 3.40, 3)
        self.assertEqual(len(cart), 1, "Don't add a second Latte entry, increase the quantity")
        self.assertEqual(cart["Latte"]["quantity"], 5)

    def test_remove_existing(self):
        cart = sample_cart()
        self.assertIs(remove_item(cart, "Scone"), True)
        self.assertNotIn("Scone", cart)

    def test_remove_missing(self):
        cart = sample_cart()
        self.assertIs(remove_item(cart, "Juice"), False)
        self.assertEqual(len(cart), 3, "Removing a missing item should leave the cart unchanged")


class TestTotals(unittest.TestCase):
    def test_cart_total(self):
        self.assertEqual(cart_total(sample_cart()), 21.15)

    def test_empty_total(self):
        self.assertEqual(cart_total({}), 0)

    def test_item_count(self):
        self.assertEqual(item_count(sample_cart()), 6)
        self.assertEqual(item_count({}), 0)


class TestMostExpensive(unittest.TestCase):
    def test_highest_unit_price(self):
        self.assertEqual(most_expensive(sample_cart()), "Brownie")

    def test_unit_price_not_line_total(self):
        cart = {"Cookie": {"price": 1.00, "quantity": 10}, "Cake": {"price": 4.00, "quantity": 1}}
        self.assertEqual(most_expensive(cart), "Cake", "Compare unit prices, not price times quantity")

    def test_empty_cart(self):
        self.assertIsNone(most_expensive({}))


class TestReceipt(unittest.TestCase):
    def test_lines_sorted_by_name(self):
        self.assertEqual(receipt_lines(sample_cart()), [
            "3 x Brownie @ $3.95 = $11.85",
            "2 x Latte @ $3.40 = $6.80",
            "1 x Scone @ $2.50 = $2.50",
        ])

    def test_empty_receipt(self):
        self.assertEqual(receipt_lines({}), [])


if __name__ == "__main__":
    unittest.main()

# Exercise 7: shopping cart
#
# A cart is a dictionary. Each key is an item's name, and each value is a
# dictionary with the item's price and quantity:
#
#     cart = {
#         "Latte": {"price": 3.40, "quantity": 2},
#         "Scone": {"price": 2.50, "quantity": 1},
#     }
#
# Replace each `pass` with your code. Test with:  python3 -m unittest -v


def add_item(cart, name, price, quantity=1):
    """Add an item to the cart, or increase its quantity if it's already there."""
    pass


def remove_item(cart, name):
    """Remove an item. Return True if it was in the cart, False if it wasn't."""
    pass


def cart_total(cart):
    """Return the total cost of everything in the cart, rounded to 2 decimal places."""
    pass


def item_count(cart):
    """Return the number of items, counting quantities."""
    pass


def most_expensive(cart):
    """Return the name of the item with the highest unit price, or None if the cart is empty."""
    pass


def receipt_lines(cart):
    """Return a list of lines like "2 x Latte @ $3.40 = $6.80", sorted by item name."""
    pass


if __name__ == "__main__":
    cart = {}
    add_item(cart, "Latte", 3.40, 2)
    add_item(cart, "Scone", 2.50)
    add_item(cart, "Latte", 3.40)
    for line in receipt_lines(cart) or []:
        print(line)
    print("Items:", item_count(cart))
    print("Total:", cart_total(cart))

# Solution to exercise 7: shopping cart


def add_item(cart, name, price, quantity=1):
    """Add an item to the cart, or increase its quantity if it's already there."""
    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {"price": price, "quantity": quantity}


def remove_item(cart, name):
    """Remove an item. Return True if it was in the cart, False if it wasn't."""
    if name in cart:
        del cart[name]
        return True
    return False


def cart_total(cart):
    """Return the total cost of everything in the cart, rounded to 2 decimal places."""
    total = 0
    for details in cart.values():
        total += details["price"] * details["quantity"]
    return round(total, 2)


def item_count(cart):
    """Return the number of items, counting quantities."""
    count = 0
    for details in cart.values():
        count += details["quantity"]
    return count


def most_expensive(cart):
    """Return the name of the item with the highest unit price, or None if the cart is empty."""
    best_name = None
    best_price = 0
    for name, details in cart.items():
        if best_name is None or details["price"] > best_price:
            best_name = name
            best_price = details["price"]
    return best_name


def receipt_lines(cart):
    """Return a list of lines like "2 x Latte @ $3.40 = $6.80", sorted by item name."""
    lines = []
    for name in sorted(cart):
        price = cart[name]["price"]
        quantity = cart[name]["quantity"]
        lines.append(f"{quantity} x {name} @ ${price:.2f} = ${price * quantity:.2f}")
    return lines


if __name__ == "__main__":
    cart = {}
    add_item(cart, "Latte", 3.40, 2)
    add_item(cart, "Scone", 2.50)
    add_item(cart, "Latte", 3.40)
    for line in receipt_lines(cart):
        print(line)
    print("Items:", item_count(cart))
    print("Total:", cart_total(cart))

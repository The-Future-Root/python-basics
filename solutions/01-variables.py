# Solution to exercise 1: a café receipt

product_name = "Blueberry muffin"
unit_price = 2.75
quantity = 4

subtotal = unit_price * quantity
discount_percent = 10
discount = subtotal * discount_percent / 100
total = subtotal - discount

# These lines print the receipt. You don't need to change them.
print("Item:", product_name)
print("Price:", unit_price, "x", quantity)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Total:", total)

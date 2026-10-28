# Exercise 1: a café receipt
#
# Replace each None with the right value or calculation.
# The table in README.md says what each variable should be.
# Then run the tests:  python3 -m unittest -v

product_name = None
unit_price = None
quantity = None

subtotal = None          # unit_price times quantity
discount_percent = None
discount = None          # subtotal times discount_percent, divided by 100
total = None             # subtotal minus discount

# These lines print the receipt. You don't need to change them.
print("Item:", product_name)
print("Price:", unit_price, "x", quantity)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Total:", total)

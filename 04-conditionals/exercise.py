# Exercise 4: shipping calculator
#
# Shipping rules:
#   to the US, $50 or more         -> free
#   to the US, under $50           -> $4.99
#   anywhere else, $100 or more    -> $9.99
#   anywhere else, under $100      -> $19.99
#
# Your program should:
#   1. ask for the order total  (prompt: "Order total: ")
#   2. ask for the country      (prompt: "Country: "), accepting "us", "US", " Us " and so on
#   3. if the total is zero or less, print "Order total must be more than zero" and nothing else
#   4. otherwise print "Shipping: FREE" or "Shipping: $4.99" (and so on),
#      then "Total to pay: $54.99" (total plus shipping, 2 decimal places)


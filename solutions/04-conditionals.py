# Solution to exercise 4: shipping calculator

total = float(input("Order total: "))
country = input("Country: ").strip().upper()

if total <= 0:
    print("Order total must be more than zero")
else:
    if country == "US":
        if total >= 50:
            shipping = 0
        else:
            shipping = 4.99
    elif total >= 100:
        shipping = 9.99
    else:
        shipping = 19.99

    if shipping == 0:
        print("Shipping: FREE")
    else:
        print(f"Shipping: ${shipping:.2f}")
    print(f"Total to pay: ${total + shipping:.2f}")

# Solution to exercise 3: split the bill

bill = float(input("Bill amount: "))
tip_percent = int(input("Tip percent: "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
each = total / people

print(f"Bill: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Each person pays: ${each:.2f}")

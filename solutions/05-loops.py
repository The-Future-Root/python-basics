# Solution to exercise 5: savings goal

saving = float(input("Monthly saving: "))
goal = float(input("Savings goal: "))

if saving <= 0:
    print("Monthly saving must be more than zero")
else:
    balance = 0
    month = 0
    while balance < goal:
        balance += saving
        month += 1
        print(f"Month {month}: ${balance:,.2f}")

    if month == 1:
        print("Goal reached in 1 month")
    else:
        print(f"Goal reached in {month} months")

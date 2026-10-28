# Solution to exercise 2: clean up a sign-up form

age_text = "34"
height_text = "1.75"
member_text = "yes"
raw_name = "   alex KIM  "
raw_email = "  Alex.Kim@Example.COM "

age = int(age_text)
height_m = float(height_text)
is_member = member_text == "yes"
clean_name = raw_name.strip().title()
clean_email = raw_email.strip().lower()
age_next_year = age + 1
welcome = "Welcome, " + clean_name + "!"

print(welcome)
print("Age next year:", age_next_year)
print("Member:", is_member)

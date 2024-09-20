# Day 2 Project: Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Tip per person
calculated_tip = (bill * (tip / 100)) / people

# Bill per person
calculated_bill = bill / people

# Final bill per person
final_bill = calculated_bill + calculated_tip
print(f"Each person should pay: ${final_bill:.2f}")

# Challenge 4 - Tip-calculator

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to split the bill? "))

bill_per_person = total_bill * (1 + (percent/100)) / persons
print(f"Each person should pay: ${round(bill_per_person,2)}")
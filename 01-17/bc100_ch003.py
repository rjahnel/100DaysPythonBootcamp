# Challenge 3
# Create a program the calculates the days, weeks, months left if we live 
# until 90 years old.
age = int(input("What is your current age: "))
max_age = int(input("What is the maxiumum age: "))

# hint 365 days in a year, 52 weeks in a year and 12 month in a year
days = (max_age - age) * 365
weeks = (max_age - age) * 52
month = (max_age - age) * 12

print(f"You have {days} days, {weeks} weeks and {month} months left.")

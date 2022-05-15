# Challenge 2 - BMI-Calculator
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

print(f"Your bmi is {round(bmi,2)}")



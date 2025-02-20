# Write a program that calculates the BMI of an individual using the formula BMI.

weight = float(input("Enter your weight = "))
height = float(input("Enter your height = "))

print(f"Your BMI is {weight / height**2}")
# Write a program that calculates the geometric mean of three numbers entered by the user.

a = float(input("Enter the first number = "))
b = float(input("Enter the second number = "))
c = float(input("Enter the third number = "))

import numpy as np

numbers = np.array([a, b, c])

print(f"The geometric mean of {a}, {b} and {c} is {np.prod(numbers) ** (1 / len(numbers))}")

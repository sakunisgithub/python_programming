# Write a program that calculates the arithmetic mean of two numbers.

a = float(input("Enter your first number = "))
b = float(input("Enter your second number = "))

import numpy as np

print(f"The arithmetic mean of {a} and {b} is {np.mean(np.array([a, b]))}")
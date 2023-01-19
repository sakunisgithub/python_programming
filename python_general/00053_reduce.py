from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = reduce(lambda a, b : a + b, numbers)

print(f"The sum of first 10 natural numbers is {sum}")

product = reduce(lambda a, b : a * b, numbers)

print(f"The product of first 10 natural numbers is {product}")
num1 = float(input("Enter the first number = "))

num2 = float(input("Enter the second number = "))

maximum =  [num1, num2][int(num1 < num2)]

print(f"The maximum number is {maximum}")
number_1 = int(input("Enter the first number = "))
number_2 = int(input("Enter the second number = "))

print("Your first number is", number_1)
print("Your second number is", number_2)

temp = number_1
number_1 = number_2
number_2 = temp 

print("Swapping successful !")
print("Now your first number is", number_1)
print("Now your second number is", number_2)

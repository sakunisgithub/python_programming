print("Option 1 : Addition")
print("Option 2 : Subtraction (first - second)")
print("Option 3 : Multiplication")
print("Option 4 : Division (first/second)")

option = int(input("Choose your option = "))

num_1 = int(input("Enter the first number = "))
num_2 = int(input(("Entr the second number = ")))


if (option == 1) :
    print(f"{num_1} + {num_2} = {num_1+num_2}")
elif (option == 2) :
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
elif (option == 3) :
    print(f"{num_1} * {num_2} = {num_1 * num_2}")
elif (option == 4) :
    print(f"{num_1} / {num_2} = {num_1 / num_2}")

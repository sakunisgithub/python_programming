# problem 1
number = int(input("Enter your number = "))
for i in range(1, 11) :
    print(number ,"X", i, "=", number*i)

# problem 2
l1 = ["Harry", "Soham", "Sachin", "Rahul"]

for item in l1 :
    if (item[0] == "S") :
        print("Welcome", item)

# problem 3
number = int(input("Enter your number = "))
i = 1
while (i<=10) :
    print(number, "X", i, "=", number*i)
    i += 1

# problem 4
number = int(input("Enter your number = "))

for i in range(2, number-1) :
    if (number % i == 0 & number != 2) :
        print(number, "is not a prime number")
        break
else :
    print(number, "is a prime number")

# problem 5
number = int(input("Enter n = "))

i = 1
sum = 0
while (i<=number) :
    sum += i
    i += 1
print("The sum of first", number, "natural numbers is", sum)

# problem 6
number = int(input("Enter n = "))

product = 1
i = 1
for i in range(1, number+1) :
    product *= i
    i += 1
print(number, "! = ", product)

# problem 8
n = int(input("Enter n = "))
for i in range(1, n+1) :
        print("*" * i)
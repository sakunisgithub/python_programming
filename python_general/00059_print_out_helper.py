task_code = 0

print("What do you want to do ? Enter 0 for printing odd numbers, 1 for printing even numbers.")

task_code = int(input("Enter 0 or 1 -- > "))

print("Input the range in which you want to print the numbers ::")

start = int(input("Enter the starting number --> "))

stop = int(input("Enter the number upto which you want to print --> "))

if (task_code == 0) :
    if (start % 2 == 0) :
        start = start + 1
elif (task_code == 1) :
    if (start % 2 != 0) :
        start = start + 1

numbers = []

while (start <= stop) :
    numbers.append(start)

    start = start + 2

for i in range(len(numbers)) :
    print(numbers[i], end = "")

    if (i != len(numbers) - 1) :
        print(",", end = "")
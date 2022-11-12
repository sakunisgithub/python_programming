number = int(input("Enter your number = "))

def get_sum(num) : 
	sum_of_digits = 0
	while(num != 0) :
		sum_of_digits += int(num % 10)
		num = int(num / 10)
	return sum_of_digits

if (number == 0) :
	print("The sum of the digits of 0 is 0")
elif (number < 0) :
	print("Invalid input ! Please enter a non-negative number.")
else :
	print("The sum of the digits of", number, "is", get_sum(number))

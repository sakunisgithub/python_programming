number = int(input("Enter your number = "))

def find_the_number_of_digits(num) :
	counter = 0
	while (num != 0) :
		num = num // 10
		counter = counter + 1
	return counter

def find_sum(num, number_of_digits) :
	""" This function raises the digits of the number to its number of digits and adds the results and returns the total sum """
	sum = 0
	while (num != 0) :
		temp = num % 10
		sum = sum + temp**number_of_digits
		num = num // 10
	return sum

number_of_digits_in_the_number = find_the_number_of_digits(number)
obtained_sum = find_sum(number, number_of_digits_in_the_number)

if (number == obtained_sum) :
	print(f"{number} is an Armstrong number")
else :
	print(f"{number} is not an Armstrong number")

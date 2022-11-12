number = int(input("Enter the number = "))

def number_of_digits(num) :
	digits = 0
	while (num != 0) :
		digits += 1
		num = int(num / 10)
	return digits

def reverse_number(num, digits) :
	rev_num = 0
	while (num != 0) :
		temp = num % 10
		num = int(num / 10)
		rev_num += ( pow(10, digits-1) * temp )
		digits -= 1
	return rev_num

if (number > 0) :
	digits_in_the_number = number_of_digits(number)
	output_number = reverse_number(number, digits_in_the_number)
	print("The reversed number is", output_number)
else :
	print("Invalid input ! Please enter a positive number !")

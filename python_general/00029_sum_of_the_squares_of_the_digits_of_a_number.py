number = int(input("Enter the number = "))

def sum_the_square_of_the_digits(num) :
	sum = 0
	while (num != 0) :
		temp = num % 10
		sum = sum + temp**2
		num = num // 10
	return sum

required_sum = sum_the_square_of_the_digits(number)
print(f"The sum of the square of the digits of {number} is {required_sum}")

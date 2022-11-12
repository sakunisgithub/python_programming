n = int(input("Enter n = "))

def recursively_sum(number) :
	if (number == 1) :
		return 1
	else :
		sum = number + recursively_sum(number-1)
	return sum

if (n > 0) :
	result = recursively_sum(n)
	print("The sum of first", n, "natural numbers is", result)
else :
	print("Enter a positive number")

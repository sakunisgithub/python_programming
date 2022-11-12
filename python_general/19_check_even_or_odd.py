number = int(input("Enter the number = "))

def check_even_or_odd(num) :
	if (num % 2 == 0) :
		return 1
	else :
		return 0

code = check_even_or_odd(number)
if (code == 0) :
	print("The number is odd")
else :
	print("The number is even")

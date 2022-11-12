number = int(input("Enter your number = "))

if (number % 3 == 0) :
	print(f"{number} is divisible by 3")
	if (number % 2 == 0) :
		print(f"{number} is divisible by 6")
	else :
		print(f"{number} is not divisible by 6")

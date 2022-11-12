year = int(input("Enter the year = "))

if (year % 4 != 0) :
	print(f"{year} is not a leapyear.") # if the year is not divisible by 4
elif (year % 100 != 0) :
	print(f"{year} is a leapyear.") # if the year is divisible by 4 but not divisible by 100
elif (year % 400 != 0) :
	print(f"{year} is not a leapyear.") # if the year is divisible by 4, divisible by 100 but not divisible by 400
else :
	print(f"{year} is a leapyear.") # if the year is divisible by 4, divisible by 100 and divisible by 400

# Rules for leapyear are as follows ::
"""
1. If last two digits of the year are evenly divisible by 4, then it is a leapyear.
2. Exception to rule no. 1 occurs when the whole year is evenly divisible by 100.
3. Exception to rule no. 2 occurs when the whole year is evenly divisible by 400.
"""

def is_leap(year) :
	if (year % 4 != 0) :
		return bool(0)
	elif (year % 100 != 0) :
		return bool(1)
	elif (year % 400 != 0) :
		return bool(0)
	else :
		return bool(1)

year = int(input())
print(is_leap(year))
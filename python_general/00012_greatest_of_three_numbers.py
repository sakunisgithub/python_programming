def take_input(number) :
	temp = int(input("Enter number = "))
	return temp

number_1 = take_input(1)
number_2 = take_input(2)
number_3 = take_input(3)

def find_greatest(n1, n2, n3) :
	if (n1 >= n2):
		w1 = n1
	else:
		w1 = n2

	if (w1 >= n3):
		w2 = w1
	else:
		w2 = n3

	return w2

greatest = find_greatest(number_1, number_2, number_3)

print("The greatest of the three numbers is", greatest)

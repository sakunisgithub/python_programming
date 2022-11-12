def take_input() :
	x = float(input("Enter the length in inches = "))	
	return x

def convert_to_centimeters(inches) :
	y = length_in_inch * 2.54
	return y

length_in_inch = take_input()
length_in_centimeters = convert_to_centimeters(length_in_inch)
print(f"{length_in_inch} inch(s) = {length_in_centimeters} centimeter(s)")

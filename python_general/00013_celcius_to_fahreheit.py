def take_input() :
	c = float(input("Enter the celcius temperature = "))
	return c

celcius = take_input()

def convert_to_fahrenheit(cel_temp) :
	f = ((cel_temp / 5) * 9) + 32
	return f

fahrenheit = convert_to_fahrenheit(celcius)
print("The equivalent fahrenheit temperature is", fahrenheit)

temperature = float(input("Enter temperature in celcius = "))
humidity = float(input("Enter humidity in % = "))

if (temperature >= 30) :
	if (humidity >= 90) :
		print("The weather is HOT AND HUMID")
	elif (humidity < 90) :
		print("The weather is HOT")
elif (temperature < 30) :
	if (humidity >= 90) :
		print("The weather is COLD AND HUMID")
	elif (humidity < 90) :
		print("The weather is COLD")

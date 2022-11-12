buying_price = int(input("Enter your buying price = "))
selling_price = int(input("Enter your selling price = "))

if (buying_price < selling_price) :
	print("You are in profit")
elif (buying_price > selling_price) :
	print("You are in loss")
else :
	print("You are neither in loss nor in profit")

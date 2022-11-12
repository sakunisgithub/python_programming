x_1 = int(input("Enter the abscissa of the first point = "))
y_1 = int(input("Enter the ordinate of the first point = "))

x_2 = int(input("Enter the abscissa of the second point = "))
y_2 = int(input("Enter the ordinate of the second point = "))

distance = ( (x_1 - x_2)**2 ) + ( (y_1 - y_2)**2 )

distance = (distance)**(1/2)

print(f"The distance between {x_1, y_1} and {x_2, y_2} is {distance} unit(s)")

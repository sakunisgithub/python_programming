print("Enter the angles in degrees")

angle_1 = int(input("Enter angle 1 = "))
angle_2 = int(input("Enter angle 2 = "))
angle_3 = int(input("Enter angle 3 = "))

total_angle = angle_1 + angle_2 + angle_3

if (total_angle != 180) :
	print(f"The angles {angle_1}, {angle_2} and {angle_3} can not form a triangle")
else :
	print(f"The angles {angle_1}, {angle_2} and {angle_3} can form a triangle")

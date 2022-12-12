import time

# current_time = time.strftime("%H %M %S")
current_hour = int(time.strftime("%H"))

print("The enemy tells", time.strftime("%H Hours : %M Minutes : %S Seconds"))

if (current_hour >= 00 and current_hour <= 11) :
    print("Good Morning !!!")
elif (current_hour >= 12 and current_hour <= 15) :
    print("Good noon !!!")
elif (current_hour >= 16 and current_hour <= 18) :
    print("Good afternoon !!!")
elif (current_hour >= 19 and current_hour <= 21) :
    print("Good evening !!!")
elif (current_hour >= 22) :
    print("Good night !!!")
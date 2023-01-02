a = input("Enter an integer = ")

try :
    b = int(a)

    print(f"{b} multiplied by 5 is equal to {b*5}")

except Exception as e :
    print(e)
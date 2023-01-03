a = input("Enter an integer = ")

try :
    b = int(a)

    print(f"{b} multiplied by 5 is equal to {b*5}")

except Exception as e :
    print(e)

finally :
    print("I am always executed !")

# the code within finally is always executed
# the real significance of 'finally' is when we use try-except-finally chain within a user-defined function definition....
# even if the function gets returned, the code in the finally block is always executed
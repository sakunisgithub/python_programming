capital = int(input("Enter your capital amount = "))
interest_rate = float(input("Enter the interest rate per month = "))
time = float(input("Enter the time in months = "))

simple_interest = (capital * interest_rate * time) / 100
final_amount = capital + simple_interest
print(f"The amount of simple interest is {simple_interest}")
print(f"The total amount i.e. (capital + simple_interest) is {final_amount}")

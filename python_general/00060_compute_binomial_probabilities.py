import math

def factorial(t) :
    if (t == 0 or t == 1) :
        return 1
    else :
        return (t * factorial(t - 1))

def choose(n, x) :

    result = factorial(n) / ( (factorial(x) * (factorial(n - x)) ) )

    return result

def probability_at_a_point(n, p, x) :

    probability = choose(n, x) * (p**x) * ((1-p)**(n-x))

    return probability

print("Enter the binomial parameters ::")

n = int(input("Enter n = "))

print("If you want to enter p in numerator by denominator form Enter 0")
print("If you want to enter p in decimal form Enter 1")

p_code = int(input("Enter your number = "))

p = 0

if (p_code == 0) :

    numerator = int(input("Enter the numerator = "))
    denominator = int(input("Enter the denominator = "))

    p = numerator / denominator

elif (p_code == 1) :

    p = float(input("Enter p = "))
    
print("What do you want to calculate ?")
print("Enter 0 if you want P(X = x)")
print("Enter 1 if you want P(X <= x)")
print("Enter 2 if you want P(X >= x)")
print("Enter 3 if you want P(X < x)")
print("Enter 4 if you want P(X > x)")

task_code = int(input("Enter your number --> "))

x = int(input("Enter x = "))

answer = 0
log_code = 0

if (task_code == 0) :
    answer = probability_at_a_point(n, p, x)
elif (task_code == 1) :
    i = 0
    while (i <= x) :
        answer = answer + probability_at_a_point(n, p, i)
        i = i + 1
elif (task_code == 2) :
    i = x 
    while (i <= n) :
        answer = answer + probability_at_a_point(n, p, i)
        i = i + 1
elif (task_code == 3) :
    i = 0
    while (i < x) :
        answer = answer + probability_at_a_point(n, p, i)
        i = i + 1
elif (task_code == 4) :
    i = x + 1
    while (i <= n) :
        answer = answer + probability_at_a_point(n, p, i)
        i = i + 1

print("Do you want to get the log value of the probability ?")
print("Enter 1 if you want or enter 0 if you do not want")

log_code = int(input("Enter your number = "))

if (log_code == 1) :
    answer = math.log(answer)
    print(f"Your answer = {answer}")    
elif (log_code == 0) :
    print(f"Your answer = {answer}")    
def fibonacci_sequence(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

n = int(input("Enter n = "))

print(f"fibonacci({n}) = {fibonacci_sequence(n)}")
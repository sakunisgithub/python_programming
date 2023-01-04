num = int(input("Enter an integer between 1 and 10 --> "))

if (num < 1 or num > 10) :
    raise ValueError("number should be in between 1 and 10")
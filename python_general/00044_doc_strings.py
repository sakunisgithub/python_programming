def add(a, b) :
    '''This function takes two numbers as inputs and returns their addition'''
    return a+b

value = add(2, 3)
print(value)

print(add.__doc__)
# when there is no docstring, print(add.__doc__) prints None
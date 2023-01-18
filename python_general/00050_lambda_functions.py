# def cube(a) :
#     return a ** 3

cube = lambda a : a ** 3

print(cube(5))

# lambda functions can take multiple arguments as well
average = lambda x, y, z : (x + y + z) / 3
print(average(5, 6, 7))
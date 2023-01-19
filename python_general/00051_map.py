# def cube(a) :
#     return a**3

my_list = [1, 2, 3, 4, 5, 6]

# new_list = []

# for item in my_list :
#     new_list.append(cube(item))

new_list = list(map(lambda x : x**3, my_list))

print(new_list)
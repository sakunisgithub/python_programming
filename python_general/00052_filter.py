my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# def check_condition(a) :
#     return a>4

# filtered_list = list(filter(check_condition, my_list))
filtered_list = list(filter(lambda a : a>4, my_list))
# filters the elements that satisfies the condition

print(filtered_list)
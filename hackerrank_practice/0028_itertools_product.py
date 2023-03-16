from itertools import product

first_list = input().split()
second_list = input().split()

for i in range(len(first_list)) :
    first_list[i] = int(first_list[i])

for i in range(len(second_list)) :
    second_list[i] = int(second_list[i])

output_list = list(product(first_list, second_list))

for i in range(len(output_list)) :
    print(output_list[i], end=" ")
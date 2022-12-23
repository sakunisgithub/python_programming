number_of_integers = int(input())

my_tuple = tuple(map(int, input().split())) 

print(hash(my_tuple))
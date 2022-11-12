my_set = {1, 2, 3, 4, 4, 1, 9, 5}
print(my_set) # only prints the distinct elements(in ascending order), ignores the repetitive elements
print(type(my_set))

another_set = {} # this does not create an empty set, this creats a dictionary
print(type(another_set))

new_set = set() # this creates an empty set named new_set, using set() function
print(type(new_set))

new_set.add(1)
new_set.add(15)
# new_set.add(15, 6) # this will throw error. only 1 element at a time
new_set.add((4, 5, 6)) # tuples can be added
print(new_set)

my_set.add(10) # appends 10 to my_set
print(my_set)

print(len(my_set)) # prints the length of my_set
print(len(new_set)) # prints the length of new_set

my_set.remove(1) # removes 1 from my_set only when 1 is present in my_set otherwise throws error
print(my_set)

print(new_set.remove(15)) # 15 is removed and this gives none as output
print(new_set)

my_set.add(1)
print(my_set)
my_set.pop() # pop does not take any argument, removes an arbitrary element and returns it
print(my_set)


set_2 = {9, 8, 7, 6, 4, 1}
print(set_2)
set_2.clear() # empties the set
print(set_2)

my_set.union({100, 200}) # this does not perform union of my_set and {100, 200}
union_set = my_set.union({100, 200}) # this performs an union of my_set and {100, 200} and assigns to union_set
print(union_set)

intersection_set = my_set.intersection({5, 200}) # this performs an intersection of my_set and {5, 100} and assigns to intersection_set
print(intersection_set)
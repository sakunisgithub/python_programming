my_list = ["swami", "vivekananda", "is", "a", "great", "inspirational", "leader"]

output = ''.join(my_list)
print(output) # concatenates the elements of my_list , sep = ''

output = ' '.join(my_list)
print(output) # concatenates the elements of my_list , sep = ' ' 

output = '-'.join(my_list)
print(output) # concatenates the elements of my_list , sep = '-' 

output = '%'.join(my_list)
print(output) # concatenates the elements of my_list , sep = '%' 
  
output = "<-->".join(my_list)
print(output) # concatenates the elements of my_list , sep = <--> 

# .join function concatenates the elements of a list to a string
# remember that the elements of the list must be string
my_list = []

number_of_instructions = int(input())

for i in range(number_of_instructions) :

    instruction = input().split()

    if instruction[0] == "insert" :
        my_list.insert(int(instruction[1]), int(instruction[2]))
    
    elif instruction[0] == "print" :
        print(my_list)
    
    elif instruction[0] == "remove" :
        my_list.remove(int(instruction[1]))
    
    elif instruction[0] == "append" :
        my_list.append(int(instruction[1]))
    
    elif instruction[0] == "sort" :
        my_list.sort()
    
    elif instruction[0] == "pop" :
        my_list.pop(-1)

    elif instruction[0] == "reverse" :
        my_list.reverse()
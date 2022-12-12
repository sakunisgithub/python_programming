def my_function(normal, *args, ** kwargs) :
    print("\nPrinting the normal")
    print(normal)

    print("\nPrinting the *args")
    for item in args :
        print(item)
    
    print("\nPrinting the **kwargs")
    for key, value in kwargs.items() :
        print(key, ":", value)


my_list_of_names = ["Yudhistir", "Arjun", "Bheem", "Nakul", "Sahadeb"]

my_sentence = "Sakuni was a cunning adviser of Duryodhan"

my_dictionary = {"Ramayan":"Ram-Laxman", "Mahabharat":"Panch-pandav"}

my_function(my_sentence, *my_list_of_names, **my_dictionary)

# the advantage of using *args and **kwargs is that even if you change the elements in the list or the dictionary, you will not need to change the function that are taking the list or dictionary as argument. thus it helps in the maintainibility of the program

# it must be known that normal-*args-**kwargs must occur in this order only, otherwise it will give errors

# you can define a function with *args or **kwargs, but while calling the function, *args and **kwargs are not mandatory inputs, they are optional inputs.

# *args and **kwargs are conventional names, you can use other names, but the * and ** are necessary
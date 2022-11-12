# hindi to english dictionary
""" hindi_to_english_dictionary = {
    "khana" : "food",
    "pyar" : "love",
    "ganit" : "mathematics",
    "swatantrata" : "independence",
    "jal" : "water",
    "vastu" : "item"
}

print("hindi word options are : ", list(hindi_to_english_dictionary.keys()))
A = input("Enter your word : ")
print("The english translation is : ", hindi_to_english_dictionary.get(A)) """

# input 8 numbers and print the unique ones
""" number_1 = int(input("Enter number_1 : "))
number_2 = int(input("Enter number_2 : "))
number_3 = int(input("Enter number_3 : "))
number_4 = int(input("Enter number_4 : "))
number_5 = int(input("Enter number_5 : "))
number_6 = int(input("Enter number_6 : "))
number_7 = int(input("Enter number_7 : "))
number_8 = int(input("Enter number_8 : "))

my_set = {number_1, number_2, number_3, number_4, number_5, number_6, number_7, number_8}

print("The unique numbers are : ", my_set) """

# length of set
""" s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s)) # 20 and 20.0 are equal so set counts only the unique one """

# creating dictionary
name_1 = input("Enter your name : ")
lang_1 = input("Enter your favorite language : ")
name_2 = input("Enter your name : ")
lang_2 = input("Enter your favorite language : ")
name_3 = input("Enter your name : ")
lang_3 = input("Enter your favorite language : ")
name_4 = input("Enter your name : ")
lang_4 = input("Enter your favorite language : ")

my_dictionary = {
    name_1 : lang_1,
    name_2 : lang_2,
    name_3 : lang_3,
    name_4 : lang_4
}

print(my_dictionary)
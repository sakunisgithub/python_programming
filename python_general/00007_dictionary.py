from hashlib import md5
from traceback import print_tb


my_dictionary = {
    "ananda" : "boy",
    "murder" : "kill", 
    "money heist" : "thriller",
    "chemical hearts" : "love story",
    "mathematics" : {"real analysis" : "bartle sherbert", "linear algebra" : "sheldon axler"},
    "numbers" : [7, 18, 183]
}

print(my_dictionary) # printing a dictionary

print(my_dictionary.keys()) # printing the dictionary keys

print(my_dictionary.values()) # printing the dictionary values, including the nested dictionaries

print(my_dictionary["mathematics"]['linear algebra']) # accessing the values of the nested dictionaries
print(my_dictionary["mathematics"]['real analysis'])

print(my_dictionary.items()) # printing the (key, value) in a tuple

update_dictionary = {
    "scores" : [134, 74],
    "numbers" : [1, 2, 3]
} # creating another dictionary
my_dictionary.update(update_dictionary) # updating the dictionary named my_dictionary. here update_dictionary is appended to my_dictionary
# if any of the keys of update_dictionary matches with my_dictionary, the key in my_dictionary gets overwritten 
print(my_dictionary)

my_dictionary["ananda"] = "student" # changing the value of the key "ananda". this overwrites the previous value in the key "ananda"
print(my_dictionary)

print(my_dictionary.get("mathematics")) # printing the value at the key "mathematics"
print(my_dictionary.get("money heist")) # printing the value at the key  "money heist"
print(my_dictionary.get("sports")) # prints none as the key "sports is not present in my_dictionary"
# print(my_dictionary["sports"]) # but this will throw keyerror as the key "sports" is not present in my_dictionary
# this is where .get() becomes significant

print(type(my_dictionary))
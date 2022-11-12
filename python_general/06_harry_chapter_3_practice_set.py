# problem 1
name = input("Enter your name : ")
print("Good Afternoon ! ", name)

#problem 2
name = input("Enter your name : ")
date = input("Enter the date in dd/mm/yyyy format : ")

letter = """Dear <name>, 
\t Your are selected.
Date : <date>""" 

letter = letter.replace("<name>", name) # this is important...you have to assign the change in the letter string. otherwise the replacement won't work.
letter = letter.replace("<date>", date)

print(letter)


#problem 3
string = input("Enter your string : ")
doublespaces = string.find("  ")
print(doublespaces)


#problem 4
string = input("Enter your string : ")
string = string.replace("  ", " ")
print(string)

#problem 5
letter = '''Dear Harry, \n \t This python course is nice. \n \t Thanks!'''
print(letter)
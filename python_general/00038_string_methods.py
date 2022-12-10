a = "Sakuni"
print(a)
print(len(a)) # gives the length of the string

print(a.upper()) # converts all the letters of the string a to upper case and stores the new string in a new variable
# remember that it does not change the initial string a
# it stores the changed string in a new variable

print(a.lower()) # converts all the letters of the string a to lower case and stores the new string in a new variable
# remember that it does not change the initial string a 
# it stores the changed string in a new variable

b = "Hurrah!!!"
print(b.rstrip("!")) # strips the trailing !s
# remember that it does not change the initial string a 
# it stores the changed string in a new variable

c = "Sakuni was a great adviser"
print(c.replace("Sakuni", "Chanakya")) # replaces all occurrences of Sakuni with Chanakya
# remember that it does not change the initial string a 
# it stores the changed string in a new variable

d = "I am a student"
print(d.split(" ")) # splits all the characters seperated by " " < space > and converts them to list items

e = "welcome to My party"
print(e.capitalize()) # capitalizes the first letter of the string and the rest of the characters are converted to lower case

f = "Happy Birthday"
f1 = f.center(50) # when being printed, shifts the string towards the center as per the parameters given, here 50
print(f)
print(len(f))
print(f1)
print(len(f1))

g = "Sakuni was a great adviser. Sakuni used to give cunning advises to Duryodhan. Sakuni had a sister named Gandhari"
print(g.count("Sakuni")) # counts the number of times Sakuni occurs in the string g
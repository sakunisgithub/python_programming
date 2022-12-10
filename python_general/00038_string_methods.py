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

h = "Hurrah!!! We won the match !!!"
print(h.endswith("!!!")) # returns true or false depending upon whether h is ending with "!!!" or not

h1 = "welcome to my party"
print(h1.endswith("to", 4, 10)) # returns true or false depending upon whether h1[4:10] is ending with "to" or not
# there is also a method called startswith

i = "sakuni is a great personality. Duryodhan is boastful"
print(i.find("is")) # returns the first occurrence of "is", if "is" is not found, it returns a negative number
print(i.find("arya"))

j = "sakuni is a great personality. Duryodhan is boastful"
print(j.index("is")) # returns the index number where "is" was found, if "is" is not found in the whole string it will produce an error
# print(i.index("arya")) # this will produce an error

k = "WelcomeToMyHouse"
print(k.isalnum()) # returns true or false depending upon whether all the characters present in the string are alphanumeric characters or not !!
# A-Z, a-z, 0-9 are called alphanumeric characters

l = "hellofriends"
print(l.isalpha()) # returns true or false depending upon whether all the characters present in the string are numberic characters or not !!
l1 = "hello111"
print(l1.isalpha())
# A-Z, a-z are called numeric characters

m = "hello world"
print(m.islower()) # returns true or false depending upon whether all the characters are lower cased or not
m1 = "Hello world"
print(m1.islower())
# there is also a method named isupper

n = "hello world"
print(n.isprintable()) # returns true if all the characters are printable characters
n1 = "hello world\n"
print(n1.isprintable()) # returns false as \n is not a printable character

o = "  "
print(o.isspace()) # returns true is the spaces are white spaces. white spaces are made by spacebar or tab

p = "Hello World"
print(p.istitle()) # returns true if the first characters of all the words are capitalized else returns false

q = "Hello woRlD"
print(q.swapcase()) # swaps the cases of all the letters 

r = "welcome to my party"
print(r.title()) # capitalizes the first letters of all the words

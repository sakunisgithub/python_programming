# problem 1
num_1 = int(input("Enter the first number = "))
num_2 = int(input("Enter the second number = "))
num_3 = int(input("Enter the third number = "))
num_4 = int(input("Enter the fourth number = "))

if(num_1 > num_2) :
    f1 = num_1
else :
    f1 = num_2

if(num_3 > num_4) :
    f2 = num_3
else :
    f2 = num_4

if(f1 > f2) :
    print("The greatest number is ", f1)
else :
    print("The greatest number is ", f2)


# problem 2
marks_1 = int(input("Enter the marks of subject 1 = "))
marks_2 = int(input("Enter the marks of subject 2 = "))
marks_3 = int(input("Enter the marks of subject 3 = "))

total_percentage = ((marks_1 + marks_2 + marks_3) / 300) * 100

if(marks_1 >= 33 and marks_2 >= 33 and marks_3 >= 33 and total_percentage >= 40) :
    print("The student has passed")
else :
    print("The student has failed")


# problem 3
comment = input("Enter your comment : ")

if("make a lot of money" in comment) :
    spam = True
elif("buy now" in comment) :
    spam = True
elif("subscribe this" in comment) :
    spam = True
elif("click this" in comment) :
    spam = True
else :
    spam = False

if(spam) :
    print("This is spam")
else :
    print("This is not spam")


# problem 4
username = input("Enter your username = ")
length = len(username)
if(length < 10) :
    print("The username has less than 10 characters")
else :
    print("The username has more than or equal to 10 characters")


# problem 5
my_list = ["Ananda", "Avimalya", "Tridibesh", "Debopriyo", "Arya", "Arkoprovo"]
your_name = input("Enter your name : ")
if(your_name in my_list) :
    print("Your name is in the list")
else :
    print("Your name is not in the list")


# problem 6
marks = int(input("Enter your marks = "))
if(marks < 50) :
    print("Grade : F")
elif(marks < 60) :
    print("Grade : E")
elif(marks < 70) :
    print("Grade : D")
elif(marks < 80) :
    print("Grade : C")
elif(marks < 90) :
    print("Grade : B")
elif(marks <= 100) :
    print("Grade : A")


# problem 7
post = input("Enter the post : ")    
if("Harry" in post or "harry" in post) :
    print("The post is talking about Harry")
else :
    print("The post is not talking about Harry")
my_string = input()

for i in range(len(my_string)) :
    if my_string[i].isalnum() is True:
        print("True")
        break
else :
    print("False")

for i in range(len(my_string)) :
    if my_string[i].isalpha() is True:
        print("True")
        break
else :
    print("False")

for i in range(len(my_string)) :
    if my_string[i].isdigit() is True:
        print("True")
        break
else :
    print("False")

for i in range(len(my_string)) :
    if my_string[i].islower() is True:
        print("True")
        break
else :
    print("False")

for i in range(len(my_string)) :
    if my_string[i].isupper() is True:
        print("True")
        break
else :
    print("False")

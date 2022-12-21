number_of_students = int((input()))

my_dict = {}

for i in range(number_of_students) :
    read = input().split()

    name = read[0]

    marks = [float(item) for item in read[1:]]

    my_dict.update({name : marks}) 

query_name = input()

query_marks = my_dict.get(query_name)

sum = 0
for number in query_marks :
    sum += number

average = sum/3

print('%.2f' %average)
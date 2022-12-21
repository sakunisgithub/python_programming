number_of_students = int(input())

# creating an empty list 
names_and_marks = []

# taking input 
for i in range(number_of_students) :
    name = input()
    marks = float(input())
    names_and_marks.append([name, marks])

# extracting the marks
all_marks = [item[1] for item in names_and_marks]

unique_marks = []
# extracting the unique marks
for numbers in all_marks :
    if numbers not in unique_marks :
        unique_marks.append(numbers)

# sorting the unique marks
unique_marks = sorted(unique_marks)

# the second lowest score is
second_lowest_score = unique_marks[1]

# the students with second_lowest_score are
students_with_second_lowest_score = [item[0] for item in names_and_marks if item[1] == second_lowest_score]

# sorting the students in alphabetical order
students_with_second_lowest_score = sorted(students_with_second_lowest_score)

for students in students_with_second_lowest_score :
    print(students)
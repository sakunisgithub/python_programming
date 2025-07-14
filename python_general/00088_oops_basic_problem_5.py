# Create a `Student` class with attributes `name`, `roll_no`, and `marks`. Write a method `display()` to show student details and a method `is_pass()` that returns True if marks are 40 or above.

class Student :
    name = 'student name'
    roll_no = 0
    marks = 0

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll_no = roll
        self.marks = marks
    
    def display(self) :
        print(f"Student name : {self.name}, Roll no : {self.roll_no}, Marks : {self.marks}")
    
    def is_pass(self) :
        if self.marks >= 40 :
            print("True")
        else :
            print("False")

s1 = Student('Ananda', 1, 39)

s1.display()

s1.is_pass()

s2 = Student('Shweta', 2, 45)

s2.display()

s2.is_pass()
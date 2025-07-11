class Employee :
    def __init__(self):
        print("Constructor of Employee")

    a = 1

class Programmer(Employee) :
    def __init__(self):
        print("Constructor of Programmer")

    b = 2 

class Manager(Programmer) :
    def __init__(self):
        super().__init__() # prints the constructor of super class (here Programmer)
        print("Constructor of Manager")

    c = 3

o1 = Employee()

print(o1.a)

o2 = Programmer()

print(o2.a, o2.b)

o3 = Manager()

print(o3.a, o3.b, o3.c)
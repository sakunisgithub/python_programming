class Employee :
    a = 1

class Programmer(Employee) :
    b = 2 

class Manager(Programmer) :
    c = 3

o1 = Employee()

print(o1.a)

o2 = Programmer()

print(o2.a, o2.b)

o3 = Manager()

print(o3.a, o3.b, o3.c)
class Employee :
    language = 'Python'
    salary = 100000

    def __init__(self, name, language, salary): # a dunder method, __init__ is automatically called

        self.name = name
        self.language = language
        self.salary = salary
        
        print("I am creating an object.")

    def getInfo(self) :
        print(f"Language : {self.language}, salary : {self.salary}")

    @staticmethod
    def greet() :
        print("Hi ! Welcome !")

ananda = Employee('Ananda', 'R', 120000)

print(ananda.name, ananda.language, ananda.salary)
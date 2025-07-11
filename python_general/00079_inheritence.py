class Employee :
    company = 'Amazon'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self, ) :
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer :
#     company = 'Flipkart'
    
#     def show(self) :
#         print(f"The name is {self.name} and the salary is {self.salary}")
    
#     def showLanguage(self) :
#         print(f"Language is {self.language}")
    
class Programmer(Employee) :
    company = 'Flipkart'

    def showLanguage(self, language) :

        self.language = language

        print(f"{self.name}'s language is {self.language}")
    
a = Employee('Ananda', 100000)

b = Programmer('Shweta', 200000)

print(a.company, b.company)

a.show()
b.show()

b.showLanguage('Python')
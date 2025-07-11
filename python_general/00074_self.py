class Employee :
    language = 'Python'
    salary = 100000

    def getInfo(self) :
        print(f"The language is {self.language}.")
        print(f"The salary is {self.salary}.")

ananda = Employee()

ananda.language = 'R'

ananda.getInfo()

# Employee.getInfo(ananda)
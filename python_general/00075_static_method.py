class Employee :
    language = 'Python'
    salary = 100000

    def getInfo(self) :
        print(f"Language : {self.language}, salary : {self.salary}.")

    @staticmethod
    def greet() :
        print("Hi. Welcome !")

ananda = Employee()

ananda.greet()

ananda.getInfo()
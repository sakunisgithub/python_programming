class Calculator :
    def __init__(self, num):
        self.number = num
    
    def your_number(self) :
        print(f"Your number is {self.number}")
        
    def square(self) :
        print(f"{self.number}^2 = {self.number**2}")
    
    def cube(self) :
        print(f"{self.number}^3 = {self.number**3}")

    def square_root(self) :
        print(f"{self.number}^(1/2) = {self.number**0.5}")

    @staticmethod
    def hello() :
        print("Hi there !")

calc = Calculator(4)

calc.hello()
calc.your_number()
calc.square()
calc.cube()
calc.square_root()
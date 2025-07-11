# Create a `Rectangle` class with attributes `length` and `width`. Add a method `area()` that returns the area of the rectangle, and a method `perimeter()` that returns its perimeter.

class Rectangle :
    length = 1
    width = 1

    def __init__(self, l, w):
       self.length = l
       self.width = w 
    
    def area(self) :
        print(f"Area of your rectangle is {self.length * self.width}")
    
    def perimeter(self) :
        print(f"Perimeter of your rectangle is {(self.length + self.width) * 2}")

rect1 = Rectangle(4, 5)

rect1.area()

rect1.perimeter()
# Create a `Circle` class with a method to calculate the area and circumference of a circle, given the radius.

import numpy as np

class Circle :
    radius = 0

    def __init__(self, radius):
        self.radius = radius
    
    def area(self) :
        print(f"Area = {np.pi * self.radius**2}")

    def circumference(self) :
        print(f"Circumference = {2 * np.pi * self.radius}")
    
circ1 = Circle(4)

circ1.area()

circ1.circumference()
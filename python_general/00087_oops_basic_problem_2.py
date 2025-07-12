# Create a `Car` class with attributes `brand` and `speed`. Add a method `accelerate()` that increases speed by 10, and `brake()` that decreases speed by 10 (but not below 0).

class Car :
    brand = 'car brand'
    speed = 0

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self) :
        self.speed += 10
        print(f"Current speed = {self.speed}")
    
    def brake(self) :
        if self.speed - 10 > 0 :
            self.speed -= 10 
        else :
            self.speed = 0

        print(f"Current speed = {self.speed}")

car1 = Car('kuttus', 2)

car1.accelerate()

car1.brake()

car1.brake()
# Create a `Person` class with attributes `name` and `age`. Write a method `introduce()` that prints "Hi, I'm {name} and I'm {age} years old." Create a few objects and call the method.

class Person :
    name = 'kuttus'
    age = 3

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self) :
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.") 

ananda = Person('Ananda', 22)

ananda.introduce()

shweta = Person('Shweta', 21)

shweta.introduce()

kuttus = Person('Kuttus', 3)
kuttus.introduce()
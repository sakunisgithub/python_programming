class Employee :
    language = 'python'
    salary = 100000

ananda = Employee()

ananda.name = 'Ananda'

print(ananda.name, ananda.language)

# Here name is instance attribute but language, salary are class attributes as they belong to the class

shweta = Employee()

shweta.name = 'Shweta'

print(shweta.name, shweta.salary)
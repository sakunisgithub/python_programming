a = 15
b = 20

print("a is bigger") if a > b else print("a and b are equal") if a == b else print("b is bigger")

greater = a if a >= b else b
print(greater)

x = 10
y = 9 

c = x if x >= y else ""
print(c)
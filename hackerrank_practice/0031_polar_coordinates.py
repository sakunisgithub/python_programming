import cmath

complex_number = input()

number = complex(complex_number)

print("{:.3f}".format(abs(number)))
print("{:.3f}".format(cmath.phase(number)))
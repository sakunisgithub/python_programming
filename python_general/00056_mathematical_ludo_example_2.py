import random
import numpy as np
from matplotlib import pyplot as plt

n = int(input("Enter the number of times you want to play = "))

my_list = [x for x in range(1, 5)]

dice_outcomes = np.empty(n)

for i in range(n) :
    dice_outcomes[i] = random.choice(my_list)

x_coordinates = np.zeros(n+1)
y_coordinates = np.zeros(n+1)

for i in range(1, n+1) :

    if (dice_outcomes[i-1] == 1) :
        x_coordinates[i] = 0
        y_coordinates[i] = 0.16 * y_coordinates[i-1]
    
    elif (dice_outcomes[i-1] == 2) :
        x_coordinates[i] = 0.85 * x_coordinates[i-1] - 0.04 * y_coordinates[i-1]
        y_coordinates[i] = -0.04 * x_coordinates[i-1] + 0.85 * y_coordinates[i-1] + 1.6
    
    elif (dice_outcomes[i-1] == 3) :
        x_coordinates[i] = 0.2 * x_coordinates[i-1] - 0.26 * y_coordinates[i-1]
        y_coordinates[i] = 0.23 * x_coordinates[i-1] + 0.22 * y_coordinates[i-1] + 1.6
    
    elif (dice_outcomes[i-1] == 4) :
        x_coordinates[i] = -0.15 * x_coordinates[i-1] + 0.28 * y_coordinates[i-1]
        y_coordinates[i] = 0.26 * x_coordinates[i-1] + 0.24 * y_coordinates[i-1] + 0.44
    

plt.scatter(x_coordinates, y_coordinates, s=10, c="black")

plt.xlabel("abscissas")
plt.ylabel("ordinates")
plt.title("Mathematical Ludo")

plt.show()
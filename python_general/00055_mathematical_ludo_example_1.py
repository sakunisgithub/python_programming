import random
import numpy as np
from matplotlib import pyplot as plt

n = int(input("Enter the number of times you want to play = "))

my_list = [1, 2, 3, 4]

dice_results = np.empty(n)

for i in range(n) :
    dice_results[i] = random.choice(my_list)

x_coordinates = np.zeros(n+1)
y_coordinates = np.zeros(n+1)

for i in range(1, n+1) :

    if (dice_results[i-1] == 1) :
        x_coordinates[i] = 0.8 * x_coordinates[i-1] + 0.1
        y_coordinates[i] = 0.8 * y_coordinates[i-1] + 0.04

    elif (dice_results[i-1] == 2) :
        x_coordinates[i] = 0.5 * x_coordinates[i-1] + 0.25
        y_coordinates[i] = 0.5 * y_coordinates[i-1] + 0.4

    elif (dice_results[i-1] == 3) :
        x_coordinates[i] = 0.355 * (x_coordinates[i-1] - y_coordinates[i-1]) + 0.266
        y_coordinates[i] = 0.355 * (x_coordinates[i-1] + y_coordinates[i-1]) + 0.078

    elif (dice_results[i-1] == 4) :
        x_coordinates[i] = 0.355 * (x_coordinates[i-1] + y_coordinates[i-1]) + 0.378
        y_coordinates[i] = 0.355 * (y_coordinates[i-1] - x_coordinates[i-1]) + 0.434
 
plt.scatter(x_coordinates, y_coordinates, s=10, c="black")

plt.xlabel("abscissas")
plt.ylabel("ordinates")
plt.title("Mathematical Ludo")

plt.show()
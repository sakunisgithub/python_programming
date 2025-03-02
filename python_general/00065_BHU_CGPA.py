no_of_papers = int(input("Enter the number of papers you have = "))

import numpy as np

credits = np.empty(no_of_papers, dtype = np.int8)

for i in range(no_of_papers) :
    credits[i] = int(input(f"Enter the credit of paper {i + 1} = "))

points = np.empty(no_of_papers, dtype = np.int8)

for i in range(no_of_papers) :
    points[i] = int(input(f"Enter the point you scored in paper {i + 1} = "))

print(f"Your CGPA is {np.sum(credits * points) / np.sum(credits)}")
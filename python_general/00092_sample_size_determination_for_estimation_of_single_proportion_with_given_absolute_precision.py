import numpy as np

p = float(input("Enter anticipated prevalence = "))

d = float(input("Enter absolute precision = "))

def provide_sample_size(p, d) :

    n = ( (1.96)**2 * p * (1-p) ) / (d**2)

    n = np.ceil(n)

    return n

print("At confidence level 0.95, required sample size = {}".format(provide_sample_size(p, d)))
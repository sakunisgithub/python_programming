import numpy as np

mu = float(input("Enter anticipated mean = "))

d = float(input("Enter relative precision = "))

sigma = float(input("Enter standard deviation = "))

def provide_sample_size(mu, sigma, d) :
    n = ((1.96)**2 * sigma**2) / ((d*mu)**2)

    n = np.ceil(n)

    return n

print("At confidence level 0.95, required sample size = {}".format(provide_sample_size(mu, sigma, d)))

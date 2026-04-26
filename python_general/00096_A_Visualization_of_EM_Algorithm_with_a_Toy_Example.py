import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Data generation
np.random.seed(14)

n = 50

u = np.random.uniform(size=n)

x = np.where(
    u < 0.6,
    np.random.normal(loc=0, scale=1, size=n),
    np.random.normal(loc=3, scale=1, size=n)
)

# Log-likelihood function
def l(phi):
    phi = np.atleast_1d(phi)

    values = []
    for p in phi:
        val = np.sum(
            np.log(
                p * norm.pdf(x, loc=0, scale=1) +
                (1-p) * norm.pdf(x, loc=3, scale=1)
            )
        )
        values.append(val)

    return np.array(values)


# ELBO function
def ELBO(theta, x, Q):
    phi = np.atleast_1d(theta)

    values = []

    for p in phi:
        joint_prob = np.zeros((n, 2))

        joint_prob[:, 0] = norm.pdf(x, 0, 1) * p
        joint_prob[:, 1] = norm.pdf(x, 3, 1) * (1-p)

        val = np.sum(Q * np.log(joint_prob / Q))
        values.append(val)

    return np.array(values)


# Plot true likelihood
phi_grid = np.linspace(0.001, 0.999, 200)

plt.figure(figsize=(10,6))
plt.plot(phi_grid, l(phi_grid), linewidth=2, label="Log-Likelihood", color = "black")


# EM algorithm
theta = 0.1
epsilon = 1e-4

iterations = []
posterior_probs = []

while True:

    phi = theta

    # E-step
    joint_prob = np.zeros((n,2))
    joint_prob[:,0] = norm.pdf(x,0,1) * phi
    joint_prob[:,1] = norm.pdf(x,3,1) * (1-phi)

    marginal_prob = joint_prob.sum(axis=1, keepdims=True)

    posterior_prob = joint_prob / marginal_prob

    posterior_probs.append(posterior_prob)

    # M-step
    theta_new = np.mean(posterior_prob[:,0])

    if np.max(np.abs(theta - theta_new)) < epsilon:
        theta = theta_new
        iterations.append(theta)
        break
    else:
        theta = theta_new
        iterations.append(theta)


# Initial point
plt.scatter(
    0.1,
    l(0.1),
    color="red",
    s=100,
    label="Initial value"
)


# Plot successive ELBOs

# ELBO at initial value
elbo_vals = ELBO(phi_grid, x, posterior_probs[0])
plt.plot(phi_grid, elbo_vals, color="red", linewidth=2, label="ELBO 1")
# First Maximization
plt.scatter(iterations[0], ELBO(iterations[0], x, posterior_probs[0]), color="blue", s=80)
plt.scatter(iterations[0], l(iterations[0]), color="blue", s=80)
# ELBO at first maximization
elbo_vals = ELBO(phi_grid, x, posterior_probs[1])
plt.plot(phi_grid, elbo_vals, color="blue", linewidth=2, label="ELBO 2")
# Second Maximization
plt.scatter(iterations[1], ELBO(iterations[1], x, posterior_probs[1]), color="orange", s=80)
plt.scatter(iterations[1], l(iterations[1]), color="orange", s=80)
# ELBO at second maximization
elbo_vals = ELBO(phi_grid, x, posterior_probs[2])
plt.plot(phi_grid, elbo_vals, color="orange", linewidth=2, label="ELBO 3")
# Third Maximization
plt.scatter(iterations[2], ELBO(iterations[2], x, posterior_probs[2]), color="magenta", s=80)
plt.scatter(iterations[2], l(iterations[2]), color="magenta", s=80)

plt.show()
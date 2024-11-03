import matplotlib.pyplot as plt
from part3 import np, generate_simpson_random

lambda_val = 1
beta_val = 3
n_samples = 1000
bins = 30

random_y, random_numbers = generate_simpson_random(lambda_val, beta_val, n=n_samples)
plt.figure()
plt.hist(random_numbers, bins=bins, density=True, alpha=0.5, color='gray', edgecolor='black', label="Sample Histogram")
x_values = np.linspace(lambda_val, beta_val, 1000)
# Теоретическая w(x)
w_values = np.piecewise(x_values,
                        [x_values < (lambda_val + beta_val) / 2, x_values >= (lambda_val + beta_val) / 2],
                        [lambda x: 4 * (x - lambda_val) / (beta_val - lambda_val)**2,
                         lambda x: 4 * (beta_val - x) / (beta_val - lambda_val)**2])
plt.plot(x_values, w_values, 'r-', lw=3, label="Theoretical Density w(x)")
plt.xlabel("x")
plt.ylabel("Density")
plt.title("Sample Histogram and Theoretical Density of Simpson's Distribution")
plt.legend()
plt.show(block=False)

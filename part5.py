import sympy as sp
import numpy as np
from part4 import random_numbers, plt, lambda_val, beta_val, n_samples as N
from scipy.stats import chi2

x = sp.symbols('x')
num_intervals = 10
w1 = 4 * (x - lambda_val) / (beta_val - lambda_val) ** 2
w2 = 4 * (beta_val - x) / (beta_val - lambda_val) ** 2
x_middle = (beta_val + lambda_val) / 2

m1_first_part = sp.integrate(x * w1, (x, lambda_val, x_middle))
m1_second_part = sp.integrate(x * w2, (x, x_middle, beta_val))
m_all = m1_first_part + m1_second_part
print(f'\n\nТеоретическое m1 = {m_all:.4f}')
sample_mean = np.mean(random_numbers)
print(f'Практическое m1 = {sample_mean:.4f}\n')

var_first = sp.integrate((x - m_all) ** 2 * w1, (x, lambda_val, x_middle))
var_second = sp.integrate((x - m_all) ** 2 * w2, (x, x_middle, beta_val))
var_all = var_first + var_second
print(f'Теоретическая μ2 = {var_all:.4f}')
var = np.var(random_numbers)
print(f'Практическая μ2 = {var:.4f}\n')

intervals = np.linspace(lambda_val, beta_val, num_intervals + 1)
observed_counts, _ = np.histogram(random_numbers, bins=intervals)
observed_frequencies = observed_counts / N
p_k = observed_frequencies / ((beta_val - lambda_val) / num_intervals)

centre = [(inter + intervals[i+1]) / 2 for i, inter in enumerate(intervals) if i + 1 <= len(intervals) - 1]
plt.figure()
plt.bar(x=centre, height=p_k, width=intervals[1] - intervals[0],
        color='gray', edgecolor='black', label="Sample Histogram")
plt.title("Simpson's density histogram")
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()

# Расчёт теоретических вероятностей w_k
w_k_values = []
for i in range(num_intervals):
    x_k1, x_k2 = intervals[i], intervals[i + 1]
    w_k = sp.integrate(w1, (x, x_k1, x_k2)) if x_k2 <= x_middle else (
        sp.integrate(w2, (x, x_k1, x_k2))
    )
    w_k_values.append(float(w_k))

# Расчет хи-квадрат
chi_squared_statistic = np.sum((observed_frequencies - w_k_values) ** 2 / w_k_values) * N
degrees_of_freedom = num_intervals - 1 - 2  # два параметра: λ и β
alpha = 0.05
chi_squared_critical = chi2.ppf(1 - alpha, degrees_of_freedom)
print(f'Теоретическая величина хи-квадрат = {chi_squared_critical}')

hi_kv = 0
for k, val in enumerate(observed_frequencies):
    hi_kv += (((val - w_k_values[k]) ** 2) / w_k_values[k]) * N
print(f'Практическая величина хи-квадрат = {hi_kv}')

plt.show()

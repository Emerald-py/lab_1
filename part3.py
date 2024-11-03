import numpy as np


# Генерация случайных чисел на основе обратного преобразования
def generate_simpson_random(lambda_val, beta_val, n=1000):
    random_values = []
    random_y = []
    for _ in range(n):
        y = np.random.uniform(0, 1)
        random_y.append(y)
        if y <= 0.5:  # Первый участок
            x_val = lambda_val + np.sqrt(2) * np.sqrt(y) * (beta_val - lambda_val) / 2
        else:
            x_val = beta_val + np.sqrt(2 * (1 - y)) * (lambda_val - beta_val) / 2
        random_values.append(x_val)
    return random_y, random_values

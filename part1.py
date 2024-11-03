import sympy as sp

x, lambda_val, beta_val = sp.symbols('x lambda_val beta_val')
w1 = 4 * (x - lambda_val) / (beta_val - lambda_val) ** 2  # первый участок
F1 = sp.integrate(w1, (x, lambda_val, x))
w2 = 4 * (beta_val - x) / (beta_val - lambda_val) ** 2  # второй участок
x_middle = (beta_val + lambda_val) / 2
F2 = F1.subs(x, x_middle) + sp.integrate(w2, (x, x_middle, x))
F1 = F1.simplify()
F2 = F2.simplify()

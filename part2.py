from part1 import sp, x, F1, F2

# Обратные функции для F1 и F2(для обеих частей)
y = sp.symbols('y')
inv_F1 = sp.solve(F1 - y, x)
inv_F2 = sp.solve(F2 - y, x)

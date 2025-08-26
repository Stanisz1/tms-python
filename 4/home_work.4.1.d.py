"""
Используя модуль math, вычислите значения по следующим
формулам:
Вычисление по четвертой формуле:
y = 5x + 3x²√(1 + sin²(x))
"""

import math

x = float(input("Введите значение x: "))

# Вычисление промежуточных значений
sin_x = math.sin(x)
sin_sq = sin_x ** 2
inner_expr = 1 + sin_sq
sqrt_inner = math.sqrt(inner_expr)
x_sq = x ** 2
term1 = 5 * x
term2 = 3 * x_sq * sqrt_inner

# Итоговый результат
y = term1 + term2

print(f"""
Результат вычислений по формуле:
y = 5x + 3x²√(1 + sin²(x))

Промежуточные значения:
sin(x) = {sin_x}
sin²(x) = {sin_sq}
√(1 + sin²(x)) = {sqrt_inner}
x² = {x_sq}
5x = {term1}
3x² * √(1 + sin²(x)) = {term2}

Итоговое значение:
y = {y}
""")
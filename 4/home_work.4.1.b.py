"""
Используя модуль math, вычислите значения по следующим
формулам:
Вычисление по второй формуле:
y = ∛(cos²(x²)) + sin²(2x - 1)
"""
import math

x = float(input("Введите значение x: "))

# Вычисляем x² и аргумент для синуса
x_sq = x ** 2
sin_arg = 2 * x - 1

# Вычисляем cos(x²) и его квадрат
cos_val = math.cos(x_sq)
cos_sq = cos_val ** 2

# Вычисляем кубический корень ∛(cos²(x²))
cube_root = cos_sq ** (1/3)  # Эквивалент ∛(cos_sq)

# Вычисляем sin²(2x - 1)
sin_val = math.sin(sin_arg)
sin_sq = sin_val ** 2

# Итоговое значение y
y = cube_root + sin_sq

print(f"""
Результат вычислений по формуле:
y = ∛(cos²(x²)) + sin²(2x - 1)

Промежуточные значения:
cos(x²) = {cos_val}
cos²(x²) = {cos_sq}
∛(cos²(x²)) = {cube_root}
sin(2x - 1) = {sin_val}
sin²(2x - 1) = {sin_sq}

Итоговое значение:
y = {y}
""")
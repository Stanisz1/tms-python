"""
Необходимо разложить синус в ряде Тейлора
радианы = градусы * (пи / 180)
значение должно быть только в радианах
"""
import math


while True:
    unit = input("Введите единицы измерения (1 - радианы, 2 - градусы): ")
    if unit in ('1', '2'):
        break
    print("Ошибка: введите только '1' или '2'")

value = float(input("Введите значение угла: "))
n_terms = int(input("Введите количество членов ряда (рекомендуется 5-20): "))

# Преобразование в радианы при необходимости
if unit == '2':
    value_rad = value * math.pi / 180
    print(f"Угол в радианах: {value_rad:.6f}")
else:
    value_rad = value

# Приведение угла к диапазону [0, π/2] с сохранением знака
sign = 1
if value_rad < 0:
    sign = -1
    value_rad = -value_rad

# Нормализация угла: [0, 2π)
value_rad = value_rad % (2 * math.pi)

# Приведение к [0, π] с коррекцией знака
if value_rad > math.pi:
    value_rad = 2 * math.pi - value_rad
    sign *= -1

# Приведение к [0, π/2] с сохранением значения синуса
if value_rad > math.pi / 2:
    value_rad = math.pi - value_rad

# Вычисление ряда Тейлора
result = 0.0
term = value_rad
for n in range(1, n_terms + 1):
    result += term
    # Рекуррентное вычисление следующего члена
    term = -term * value_rad * value_rad / ((2 * n) * (2 * n + 1))

# Применение знака и сохранение результата
taylor_sin = sign * result

# Точное значение через math.sin
exact_sin = math.sin(value_rad if sign == 1 else -value_rad) * sign
if unit == '2':
    exact_sin = math.sin(value * math.pi / 180)

# Вычисление ошибки
error = abs(taylor_sin - exact_sin)
relative_error = (error / abs(exact_sin)) * 100 if exact_sin != 0 else 0

# Вывод результатов
print("\nРезультаты вычислений:")
print(f"Приближенное значение: {taylor_sin:.10f}")
print(f"Точное значение (math.sin): {exact_sin:.10f}")
print(f"Абсолютная ошибка: {error:.2e}")
print(f"Относительная ошибка: {relative_error:.2e} %")
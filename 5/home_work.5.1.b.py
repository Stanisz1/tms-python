"""
суть та же как и для 5.1а, только для косинуса"""
import math

# Ввод данных от пользователя с проверкой
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

# Приведение угла к диапазону [0, π/2] с сохранением знака косинуса
x = abs(value_rad)  # Используем четность косинуса: cos(-x) = cos(x)
x = x % (2 * math.pi)  # Приведение к интервалу [0, 2π)

# Для углов в [π, 2π] используем свойство периодичности
if x > math.pi:
    x = 2 * math.pi - x  # cos(2π - x) = cos(x)

# Для углов в [π/2, π] используем свойство: cos(x) = -cos(π - x)
sign_cos = 1
if x > math.pi / 2:
    x = math.pi - x
    sign_cos = -1

# Вычисление ряда Тейлора для косинуса
result = 0.0
term = 1.0  # Первый член ряда (n=0)

# Обработка случая с нулевым количеством членов
if n_terms > 0:
    result = term  # Добавляем первый член

    # Вычисляем последующие члены ряда
    for n in range(1, n_terms):
        # Рекуррентное соотношение для следующего члена
        term = term * (-x * x) / ((2 * n - 1) * (2 * n))
        result += term

# Учитываем знак косинуса после преобразований
taylor_cos = sign_cos * result

# Точное значение через math.cos
exact_cos = math.cos(value_rad)

# Вычисление ошибки
error = abs(taylor_cos - exact_cos)
relative_error = (error / abs(exact_cos)) * 100 if abs(exact_cos) > 1e-12 else 0

# Вывод результатов
print("\nРезультаты вычислений:")
print(f"Приближенное значение: {taylor_cos:.10f}")
print(f"Точное значение (math.cos): {exact_cos:.10f}")
print(f"Абсолютная ошибка: {error:.2e}")
print(f"Относительная ошибка: {relative_error:.2e} %")
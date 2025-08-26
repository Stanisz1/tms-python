"""
Дан список чисел. Реализовать программу, которая посчитает
сумму всех чисел в списке, а также найдет минимальный и
максимальный элементы
"""
# Ввод чисел через пробел
input_data = input("Введите числа через пробел: ")

numbers = [float(x) for x in input_data.split()]


if not numbers:
    print("Список чисел пуст")
    exit()

total = 0
minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    total += num
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

# Вывод результатов
print(f"Сумма чисел: {total}")
print(f"Минимальное число: {minimum}")
print(f"Максимальное число: {maximum}")
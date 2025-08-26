"""
Дан список чисел, отсортированных по возрастанию. На вход
принимается значение, равное одному из элементов списка.
Реализовать алгоритм бинарного поиска, на выходе программа
должна вывести позицию искомого элемента в исходном списке
"""

input_list = input("Введите отсортированный список чисел через пробел: ")

sorted_list = list(map(float, input_list.split()))

if sorted_list != sorted(sorted_list):
    print("Ошибка: список не отсортирован по возрастанию")
    exit()

target = input("Введите искомое значение: ")
try:
    target = float(target)
except ValueError:
    print("Ошибка: введено некорректное число")
    exit()

left = 0
right = len(sorted_list) - 1
found = False

while left <= right:
    mid = (left + right) // 2

    if sorted_list[mid] == target:
        print(f"Элемент {target} найден на позиции {mid}")
        found = True
        break
    elif sorted_list[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if not found:
    print(f"Элемент {target} не найден в списке")
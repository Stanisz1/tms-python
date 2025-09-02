"""
Дан список чисел. Реализовать программу, которая проверит, все
ли числа в списке уникальны (встречаются только один раз).
Программа должна вывести результат проверки, и, если не все
элементы уникальны, вывести дублирующиеся элементы и
количество их повторений в списке
"""
# Ввод списка чисел
input_data = input("Введите числа через пробел: ")

numbers = [float(x) for x in input_data.split()]

if not numbers:
    print("Список чисел пуст")
    exit()

count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

all_unique = True
duplicates = {}
for num, count in count_dict.items():
    if count > 1:
        all_unique = False
        duplicates[num] = count

if all_unique:
    print("Все числа в списке уникальны")
else:
    print("Не все числа уникальны. Дубликаты:")
    for num, count in duplicates.items():
        print(f"Число {num} повторяется {count} раз(а)")
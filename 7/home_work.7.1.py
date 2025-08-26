"""
 Дан список чисел. С помощью map() получить список, где
каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
"""
#
# input_data = input("Введите числа через пробел: ")
# numbers = list(map(int, input_data.split()))
# result = list(map(str, numbers))
# print(result)


print(list(map(str, map(int, input("Введите числа через пробел: ").split()))))
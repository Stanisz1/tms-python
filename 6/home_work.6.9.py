"""
Реализовать функцию, которая находит сумму элементов
матрицы (матрица M x N). Определить, какую долю в общей сумме
(процент) составляет сумма элементов каждого столбца
"""

def calculate_matrix_sum_and_column_percentages(matrix):
    """
    Вычисляет общую сумму элементов матрицы и процентное соотношение суммы каждого столбца к общей сумме.
    :param matrix: двумерный список (матрица)
    :return: кортеж (общая сумма, список процентов для каждого столбца)
    """
    if not matrix or not matrix[0]:
        print("Матрица пуста!")
        return 0, []

    total_sum = 0
    for row in matrix:
        for value in row:
            total_sum += value

    if total_sum == 0:
        print("Общая сумма элементов равна нулю, невозможно вычислить проценты")
        return 0, [0] * len(matrix[0])

    col_sums = [0] * len(matrix[0])
    for row in matrix:
        for j, value in enumerate(row):
            col_sums[j] += value

    col_percentages = [(sum_val / total_sum) * 100 for sum_val in col_sums]

    return total_sum, col_percentages

import random

def create_random_matrix(m, n, min_val=0, max_val=100):
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]

try:
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    matrix = create_random_matrix(rows, cols)

    print("\nСгенерированная матрица:")
    for row in matrix:
        print(row)

    total_sum, col_percentages = calculate_matrix_sum_and_column_percentages(matrix)

    print(f"\nОбщая сумма всех элементов: {total_sum}")
    for j, percentage in enumerate(col_percentages):
        print(f"Столбец {j}: {percentage:.2f}% от общей суммы")

except ValueError:
    print("Ошибка: введите целые числа для размеров матрицы")
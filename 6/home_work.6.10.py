"""
Реализовать функцию, которая перемножает элементы
каждого столбца матрицы с соответствующими элементами K-го
столбца (матрица M x N)
"""

import random


def multiply_columns_by_k(matrix, k):
    """
    Умножает элементы каждого столбца матрицы на соответствующие элементы K-го столбца.
    :param matrix: двумерный список (матрица)
    :param k: индекс столбца K (начиная с 0)
    :return: новая матрица с результатами умножения
    """
    if k < 0 or k >= len(matrix[0]):
        print(f"Ошибка: индекс столбца K={k} вне диапазона [0, {len(matrix[0]) - 1}]")
        return None

    result_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(matrix[i][j] * matrix[i][k])
        result_matrix.append(new_row)

    return result_matrix


def create_random_matrix(m, n, min_val=0, max_val=100):
    """Создает случайную матрицу размером m x n"""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]


try:
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    k = int(input(f"Введите индекс столбца K (0-{cols - 1}): "))

    matrix = create_random_matrix(rows, cols)
    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    result = multiply_columns_by_k(matrix, k)

    if result is not None:
        print("\nРезультат умножения:")
        for row in result:
            print(row)

except ValueError:
    print("Ошибка: введите целые числа")
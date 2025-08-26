"""
Реализовать функцию, которая суммирует элементы
каждой строки матрицы с соответствующими элементами L-й строки
(матрица M x N)
"""
import random


def add_l_row_to_all(matrix, l):
    """
    Прибавляет к каждой строке матрицы элементы L-й строки.
    :param matrix: двумерный список (матрица)
    :param l: индекс строки L (начиная с 0)
    :return: новая матрица с результатами сложения
    """
    if l < 0 or l >= len(matrix):
        print(f"Ошибка: индекс строки L={l} вне диапазона [0, {len(matrix) - 1}]")
        return None

    result_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(matrix[i][j] + matrix[l][j])
        result_matrix.append(new_row)

    return result_matrix


def create_random_matrix(m, n, min_val=0, max_val=100):
    """Создает случайную матрицу размером m x n"""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]


try:
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    l = int(input(f"Введите индекс строки L (0-{rows - 1}): "))

    matrix = create_random_matrix(rows, cols)
    print("\nИсходная матрица:")
    for i, row in enumerate(matrix):
        print(f"Строка {i}: {row}")

    result = add_l_row_to_all(matrix, l)

    if result is not None:
        print("\nРезультат сложения каждой строки со строкой L:")
        for i, row in enumerate(result):
            print(f"Строка {i}: {row}")

except ValueError:
    print("Ошибка: введите целые числа")
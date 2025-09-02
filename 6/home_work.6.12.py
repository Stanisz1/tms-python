"""
Программа получает на вход число H. Реализовать
функцию, которая определяет, какие столбцы имеют хотя бы одно
такое же число, а какие не имеют (матрица M x N)
"""

import random


def find_columns_with_number(matrix, H):
    """
    Определяет столбцы матрицы, содержащие хотя бы одно число H.
    :param matrix: двумерный список (матрица)
    :param H: искомое число
    :return: кортеж (столбцы с H, столбцы без H)
    """
    if not matrix or not matrix[0]:
        print("Матрица пуста!")
        return [], []

    cols = len(matrix[0])
    has_h = []
    no_h = []

    for j in range(cols):
        found = False
        for i in range(len(matrix)):
            if matrix[i][j] == H:
                found = True
                break
        if found:
            has_h.append(j)
        else:
            no_h.append(j)

    return has_h, no_h


def create_random_matrix(m, n, min_val=0, max_val=100):
    """Создает случайную матрицу размером m x n"""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]


try:
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    H = int(input("Введите число H для поиска: "))

    matrix = create_random_matrix(rows, cols)

    print("\nСгенерированная матрица:")
    for i, row in enumerate(matrix):
        print(f"Строка {i}: {row}")

    has_h, no_h = find_columns_with_number(matrix, H)

    print("\nРезультаты поиска:")
    print(f"Число {H} найдено в столбцах: {has_h}")
    print(f"Число {H} отсутствует в столбцах: {no_h}")

    print("\nПодробная информация по столбцам:")
    for j in range(cols):
        status = "содержит" if j in has_h else "не содержит"
        print(f"Столбец {j}: {status} число {H}")

except ValueError:
    print("Ошибка: введите целые числа")
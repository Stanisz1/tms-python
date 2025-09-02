"""
Реализовать функцию, которая находит минимальный и
максимальный элементы в матрице (матрица M x N). Вывести в
консоль индексы найденных элементов.
"""
def find_min_max(matrix):
    """
    Находит минимальный и максимальный элементы в матрице.
    Выводит в консоль их значения и индексы.
    :param matrix: двумерный список (матрица)
    """
    if not matrix or not matrix[0]:
        print("Матрица пуста!")
        return

    min_val = matrix[0][0]
    max_val = matrix[0][0]
    min_index = (0, 0)
    max_index = (0, 0)

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value < min_val:
                min_val = value
                min_index = (i, j)
            if value > max_val:
                max_val = value
                max_index = (i, j)

    print(f"Минимальный элемент: {min_val} на позиции {min_index}")
    print(f"Максимальный элемент: {max_val} на позиции {max_index}")

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

    print("\nРезультаты поиска:")
    find_min_max(matrix)

except ValueError:
    print("Ошибка: введите целые числа для размеров матрицы")
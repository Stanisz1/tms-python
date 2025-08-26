"""
Дана матрица M x N. Исходная матрица состоит из нулей и
единиц. Реализовать функцию, которая добавит к матрице ещё
один столбец, элементы которого делает количество единиц в
соответствующей строке чётным
"""

import random


def add_even_parity_column(matrix):
    """
    Добавляет к матрице столбец, который делает количество единиц в каждой строке чётным.
    :param matrix: двумерный список из 0 и 1
    :return: модифицированная матрица с дополнительным столбцом
    """
    result = [row[:] for row in matrix]

    for row in result:
        count_ones = sum(row)
        row.append(1 if count_ones % 2 != 0 else 0)

    return result

def main():
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    matrix = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

    print("\nСгенерированная матрица:")
    for i, row in enumerate(matrix):
        print(f"Строка {i + 1}: {row}")

    modified_matrix = add_even_parity_column(matrix)

    print("\nМатрица с добавленным столбцом четности:")
    for i, row in enumerate(modified_matrix):
        print(f"Строка {i + 1}: {row}")


if __name__ == "__main__":
    main()
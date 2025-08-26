"""
 Реализовать функцию, которая находит сумму элементов
на главной диагонали и сумму элементов на побочной диагонали
(матрица M x N)
"""

import random


def calculate_diagonal_sums(matrix):
    """
    Вычисляет сумму элементов на главной и побочной диагоналях матрицы.
    :param matrix: двумерный список (матрица)
    :return: кортеж (сумма главной диагонали, сумма побочной диагонали)
    """
    if not matrix or not matrix[0]:
        return 0, 0

    rows = len(matrix)
    cols = len(matrix[0])
    n = min(rows, cols)  # Длина диагоналей

    main_sum = 0
    anti_sum = 0

    # Главная диагональ: элементы [i][i]
    for i in range(n):
        main_sum += matrix[i][i]

    # Побочная диагональ: элементы [i][cols-1-i]
    for i in range(n):
        anti_sum += matrix[i][cols - 1 - i]

    return main_sum, anti_sum


def main():
    # Ввод размеров матрицы
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    # Ввод диапазона значений
    min_val = float(input("Введите минимальное значение элементов: ") or "0")
    max_val = float(input("Введите максимальное значение элементов: ") or "100")

    # Создание матрицы со случайными элементами
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Генерация случайного числа в заданном диапазоне
            value = random.uniform(min_val, max_val)
            # Округление до 2 знаков для красоты
            row.append(round(value, 2))
        matrix.append(row)

    # Вывод сгенерированной матрицы
    print("\nСгенерированная матрица:")
    for i, row in enumerate(matrix):
        print(f"Строка {i + 1}: {row}")

    # Вычисление сумм диагоналей
    main_sum, anti_sum = calculate_diagonal_sums(matrix)

    # Вывод результатов
    print("\nРезультаты:")
    print(f"Сумма элементов на главной диагонали: {round(main_sum, 2)}")
    print(f"Сумма элементов на побочной диагонали: {round(anti_sum, 2)}")


if __name__ == "__main__":
    main()
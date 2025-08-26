"""
Реализовать функцию, которая создаёт матрицу размером
M строк на N столбцов и заполняет её рандомными числами
"""
import random


def create_random_matrix(m, n, min_val=0, max_val=100):
    """
    Создает матрицу размером m x n со случайными целыми числами.
    :param m: количество строк
    :param n: количество столбцов
    :param min_val: минимальное значение случайного числа (по умолчанию 0)
    :param max_val: максимальное значение случайного числа (по умолчанию 100)
    :return: двумерный список (матрица)
    """
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(m)]


# Пример использования
if __name__ == "__main__":
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))

        matrix = create_random_matrix(rows, cols)

        print("\nСгенерированная матрица:")
        for row in matrix:
            print(row)

    except ValueError:
        print("Ошибка: введите целые числа для размеров матрицы")
"""
Программа получает на вход число. Реализовать функцию,
которая определяет, является ли это число простым (делится
только на единицу и на само себя).
"""

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

try:
    num = int(input("Введите число для проверки на простоту: "))
except ValueError:
    print("Ошибка: введите целое число!")
    exit()

if is_prime(num):
    print(f"{num} - простое число")
else:
    print(f"{num} - не является простым числом")
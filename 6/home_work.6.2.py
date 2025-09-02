"""
Программа получает на вход число в десятичной системе
счисления. Реализовать функцию, которая переводит входное
число в двоичную систему счисления. Допускается реализация
функции как в рекурсивном варианте, так и с итеративным
подходом
"""
# Рекурсивное решение:
def decimal_to_binary(n):
    if n < 0:
        return "-" + decimal_to_binary(-n)
    if n <= 1:
        return str(n)
    return decimal_to_binary(n // 2) + str(n % 2)

# Ввод числа от пользователя
num = int(input("Введите число в десятичной системе: "))
binary_str = decimal_to_binary(num)
print(f"Двоичное представление: {binary_str}")


"""
Итеративное решение:
def decimal_to_binary(n):
    if n == 0:
        return "0"
    negative = n < 0
    n = abs(n)
    binary_digits = []
    while n:
        binary_digits.append(str(n % 2))
        n //= 2
    binary_str = ''.join(reversed(binary_digits))
    return "-" + binary_str if negative else binary_str

# Ввод числа от пользователя
num = int(input("Введите число в десятичной системе: "))
binary_str = decimal_to_binary(num)
print(f"Двоичное представление: {binary_str}")

"""
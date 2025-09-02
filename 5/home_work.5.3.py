n = int(input("Введите количество чисел Фибоначчи: "))

if n < 0:
    print("Ошибка: количество не может быть отрицательным")
elif n == 0:
    print("")
else:
    a, b = 1, 1
    # Первое число
    print(a, end='')

    for i in range(1, n):
        print('', b, end='')
        a, b = b, a + b
    print()
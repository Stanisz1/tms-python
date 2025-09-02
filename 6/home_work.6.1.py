"""
Дан список чисел, отсортированных по возрастанию. На
вход принимается значение, равное одному из элементов списка.
Реализовать функцию, выполняющую рекурсивный алгоритм
бинарного поиска, на выходе программа должна вывести позицию
искомого элемента в исходном списке.
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

def find_position(arr, target):
    return binary_search(arr, target, 0, len(arr) - 1)

if __name__ == "__main__":
    input_list = input("Введите отсортированный список чисел через пробел: ").split()
    try:
        numbers = list(map(int, input_list))
    except ValueError:
        print("Ошибка: введите только числа, разделенные пробелами!")
        exit()

    if numbers != sorted(numbers):
        print("Ошибка: список не отсортирован по возрастанию!")
        exit()

    try:
        target = int(input("Введите искомое число: "))
    except ValueError:
        print("Ошибка: введите целое число!")
        exit()

    position = find_position(numbers, target)
    if position == -1:
        print(f"Элемент {target} не найден в списке!")
    else:
        print(f"Позиция элемента {target} в списке: {position}")
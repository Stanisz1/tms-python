"""
Реализовать алгоритм бинарного поиска по сдвинутому списку
отсортированных чисел (например, дан список [5, 6, 7, 1, 2, 3, 4])
"""

input_list = input("Введите сдвинутый отсортированный список чисел через пробел: ")
arr = list(map(float, input_list.split()))

target = input("Введите искомое значение: ")
target = float(target)

left = 0
right = len(arr) - 1
found_index = -1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        found_index = mid
        break


    if arr[left] <= arr[mid]:
        if arr[left] <= target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if arr[mid] < target <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1

if found_index != -1:
    print(f"Элемент {target} найден на позиции {found_index}")
else:
    print(f"Элемент {target} не найден в списке")

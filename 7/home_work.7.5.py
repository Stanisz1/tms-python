"""
Используя map() и reduce() посчитать площадь квартиры,
имея на входе характеристики комнат квартиры. Пример входных
данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]
"""

from functools import reduce


def calculate_area(shape, angles):
    if shape == "прямоугольник":
        length = float(input("  Длина (м): "))
        width = float(input("  Ширина (м): "))
        return length * width
    elif shape == "треугольник":
        base = float(input("  Основание (м): "))
        height = float(input("  Высота (м): "))
        return 0.5 * base * height
    elif shape == "круг":
        radius = float(input("  Радиус (м): "))
        return 3.14159 * radius ** 2
    else:
        # Для произвольной формы используем метод ввода площади
        print("  Для произвольной формы введите площадь напрямую")
        return float(input("  Площадь (м²): "))


rooms = []
n = int(input("Введите количество комнат: "))

print("\n" + "=" * 50)
print("Формы комнат и их параметры:")
print("1. Прямоугольник (4 угла) - длина и ширина")
print("2. Треугольник (3 угла) - основание и высота")
print("3. Круг (0 углов) - радиус")
print("4. Произвольная форма - ввод площади напрямую")
print("=" * 50 + "\n")

for i in range(n):
    print(f"\nКомната {i + 1}:")
    name = input("  Название: ")
    angles = int(input("  Количество углов: "))

    # Определение формы по количеству углов
    if angles == 4:
        shape = "прямоугольник"
    elif angles == 3:
        shape = "треугольник"
    elif angles == 0:
        shape = "круг"
    else:
        shape = "произвольная форма"

    print(f"  Форма: {shape}")
    area = calculate_area(shape, angles)

    rooms.append({
        "name": name,
        "shape": shape,
        "angles": angles,
        "area": area
    })
    print(f"  Площадь комнаты: {area:.2f} м²")

# Вывод таблицы комнат
print("\n" + "=" * 50)
print("{:<15} {:<20} {:<10} {:<15}".format(
    "Комната", "Форма", "Углы", "Площадь (м²)"))
print("-" * 50)

for room in rooms:
    print("{:<15} {:<20} {:<10} {:<15.2f}".format(
        room['name'],
        room['shape'],
        room['angles'],
        room['area']
    ))

# Расчет общей площади
total_area = reduce(lambda total, room: total + room["area"], rooms, 0)
print("=" * 50)
print(f"Общая площадь квартиры: {total_area:.2f} м²")
print("=" * 50)
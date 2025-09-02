"""

Программа с классом Sphere для представления сферы в
трёхмерном пространстве.
Реализовать методы:
o Конструктор, принимающий 4 числа: радиус и
координаты центра сферы x, y, z. Если конструктор
вызывается без аргументов, создать объект сферы с
единичным радиусом и центром в начале координат.
Если конструктор вызывается только с радиусом,
создать объект с соответствующим радиусом и центром
в начале координат
o Метод get_volume(), возвращающий число – объем шара,
ограниченного текущей сферой
o Метод get_square(), возвращающий число – площадь
внешней поверхности сферы
Метод get_radius(), возвращающий число – радиус
текущей сферы
o Метод get_center(), возвращающий кортеж с
координатами центра сферы
o Метод set_radius(radius), который принимает новое
значение радиуса, меняет радиус текущей сферы и
ничего не возвращает
o Метод set_center(x, y, z), который принимает новые
значения для координат центра радиуса, меняет
координаты текущей сферы и ничего не возвращает
o Метод is_point_inside(x, y, z), который принимает
координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того,
находится ли точка внутри сферы

"""

import math


class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        """
        Конструктор класса Sphere
        - Без аргументов: создает сферу с радиусом 1 и центром в (0, 0, 0)
        - Только с радиусом: создает сферу с заданным радиусом и центром в (0, 0, 0)
        - С радиусом и координатами: создает сферу с заданными параметрами
        """
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        """Возвращает объем шара, ограниченного сферой"""
        return (4 / 3) * math.pi * (self.radius ** 3)

    def get_square(self):
        """Возвращает площадь внешней поверхности сферы"""
        return 4 * math.pi * (self.radius ** 2)

    def get_radius(self):
        """Возвращает радиус сферы"""
        return self.radius

    def get_center(self):
        """Возвращает кортеж с координатами центра сферы"""
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        """Устанавливает новый радиус сферы"""
        self.radius = radius

    def set_center(self, x, y, z):
        """Устанавливает новые координаты центра сферы"""
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        """
        Проверяет, находится ли точка внутри сферы
        Возвращает True, если точка внутри сферы, иначе False
        """
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2)
        return distance <= self.radius


# Пример использования класса
if __name__ == "__main__":
    # Создаем сферы разными способами
    sphere1 = Sphere()  # Единичная сфера в начале координат
    sphere2 = Sphere(5)  # Сфера с радиусом 5 в начале координат
    sphere3 = Sphere(3, 1, 2, 3)  # Сфера с радиусом 3 и центром в (1, 2, 3)

    # Тестируем методы
    print("Сфера 1:")
    print(f"Радиус: {sphere1.get_radius()}")
    print(f"Центр: {sphere1.get_center()}")
    print(f"Объем: {sphere1.get_volume():.2f}")
    print(f"Площадь поверхности: {sphere1.get_square():.2f}")
    print(f"Точка (0,0,0) внутри: {sphere1.is_point_inside(0, 0, 0)}")
    print(f"Точка (2,0,0) внутри: {sphere1.is_point_inside(2, 0, 0)}")

    print("\nСфера 2:")
    print(f"Радиус: {sphere2.get_radius()}")
    print(f"Центр: {sphere2.get_center()}")
    print(f"Объем: {sphere2.get_volume():.2f}")
    print(f"Площадь поверхности: {sphere2.get_square():.2f}")

    print("\nСфера 3:")
    print(f"Радиус: {sphere3.get_radius()}")
    print(f"Центр: {sphere3.get_center()}")
    print(f"Точка (1,2,3) внутри: {sphere3.is_point_inside(1, 2, 3)}")
    print(f"Точка (5,2,3) внутри: {sphere3.is_point_inside(5, 2, 3)}")

    # Изменяем параметры сферы
    sphere3.set_radius(10)
    sphere3.set_center(0, 0, 0)
    print(f"\nПосле изменения:")
    print(f"Радиус: {sphere3.get_radius()}")
    print(f"Центр: {sphere3.get_center()}")
    print(f"Точка (5,0,0) внутри: {sphere3.is_point_inside(5, 0, 0)}")
    print(f"Точка (11,0,0) внутри: {sphere3.is_point_inside(11, 0, 0)}")
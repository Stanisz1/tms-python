"""

Программа с классом Car. При инициализации объекта ему
должны задаваться атрибуты color, type и year. Реализовать
пять методов. Запуск автомобиля – выводит строку
«Автомобиль заведён». Отключение автомобиля – выводит
строку «Автомобиль заглушен». Методы для присвоения
автомобилю года выпуска, типа и цвета

"""


class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        """Запуск автомобиля"""
        print("Автомобиль заведён")

    def stop(self):
        """Отключение автомобиля"""
        print("Автомобиль заглушен")

    def set_year(self, year):
        """Установка года выпуска автомобиля"""
        self.year = year
        print(f"Год выпуска установлен: {self.year}")

    def set_type(self, type):
        """Установка типа автомобиля"""
        self.type = type
        print(f"Тип автомобиля установлен: {self.type}")

    def set_color(self, color):
        """Установка цвета автомобиля"""
        self.color = color
        print(f"Цвет автомобиля установлен: {self.color}")

    def get_info(self):
        """Дополнительный метод для вывода информации об автомобиле"""
        print(f"Автомобиль: {self.color} {self.type} {self.year} года выпуска")


# Пример использования класса
if __name__ == "__main__":
    # Создаем автомобиль
    my_car = Car("красный", "седан", 2020)

    # Выводим информацию об автомобиле
    my_car.get_info()

    # Используем методы автомобиля
    my_car.start()
    my_car.stop()

    # Меняем атрибуты автомобиля
    my_car.set_color("синий")
    my_car.set_type("хэтчбек")
    my_car.set_year(2022)

    # Снова выводим информацию об автомобиле
    my_car.get_info()
"""

Класс «Автобус».
Класс содержит свойства:
● Скорость
● Максимальное количество посадочных мест
● Максимальная скорость
● Список фамилий пассажиров
● Флаг наличия свободных мест
● Словарь мест в автобусе
Методы:
● Посадка и высадка одного или нескольких пассажиров
● Увеличение и уменьшение скорости на заданное значение
● Операции in, += и -= (посадка и высадка пассажира по
фамилии

"""


class Autobus:
    def __init__(self, speed, max_seats, max_speed):
        self.speed = speed
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []  # Список фамилий пассажиров
        self.has_free_seats = True  # Флаг наличия свободных мест
        self.seats = {i: None for i in range(1, max_seats + 1)}  # Словарь мест

    def board(self, *surnames):
        """Посадка одного или нескольких пассажиров"""
        for surname in surnames:
            if len(self.passengers) >= self.max_seats:
                print(f"Нет свободных мест для {surname}")
                continue

            # Находим первое свободное место
            free_seat = None
            for seat_num, occupant in self.seats.items():
                if occupant is None:
                    free_seat = seat_num
                    break

            if free_seat:
                self.seats[free_seat] = surname
                self.passengers.append(surname)
                print(f"{surname} сел на место {free_seat}")

            # Обновляем флаг свободных мест
            self.has_free_seats = len(self.passengers) < self.max_seats

    def alight(self, *surnames):
        """Высадка одного или нескольких пассажиров"""
        for surname in surnames:
            if surname not in self.passengers:
                print(f"Пассажир {surname} не найден")
                continue

            # Освобождаем место
            for seat_num, occupant in self.seats.items():
                if occupant == surname:
                    self.seats[seat_num] = None
                    break

            self.passengers.remove(surname)
            print(f"{surname} вышел из автобуса")

            # Обновляем флаг свободных мест
            self.has_free_seats = len(self.passengers) < self.max_seats

    def increase_speed(self, value):
        """Увеличение скорости на заданное значение"""
        new_speed = self.speed + value
        self.speed = min(new_speed, self.max_speed)
        print(f"Скорость увеличена до {self.speed}")

    def decrease_speed(self, value):
        """Уменьшение скорости на заданное значение"""
        new_speed = self.speed - value
        self.speed = max(new_speed, 0)
        print(f"Скорость уменьшена до {self.speed}")

    def __contains__(self, surname):
        """Оператор in - проверка наличия пассажира по фамилии"""
        return surname in self.passengers

    def __iadd__(self, surname):
        """Оператор += - посадка пассажира по фамилии"""
        self.board(surname)
        return self

    def __isub__(self, surname):
        """Оператор -= - высадка пассажира по фамилии"""
        self.alight(surname)
        return self

    def __str__(self):
        """Строковое представление автобуса"""
        return (f"Автобус: скорость={self.speed}/{self.max_speed}, "
                f"пассажиры={len(self.passengers)}/{self.max_seats}, "
                f"свободные места={self.has_free_seats}")

if __name__ == "__main__":
    # Создаем автобус
    bus = Autobus(speed=40, max_seats=5, max_speed=100)
    print(bus)

    # Посадка пассажиров
    bus.board("Иванов", "Петров", "Сидоров")
    print(bus)

    # Использование оператора +=
    bus += "Кузнецов"
    print(bus)

    # Проверка наличия пассажира
    print("Иванов в автобусе:", "Иванов" in bus)
    print("Смирнов в автобусе:", "Смирнов" in bus)

    # Изменение скорости
    bus.increase_speed(30)
    bus.decrease_speed(20)

    # Высадка пассажиров
    bus.alight("Петров")
    print(bus)

    # Использование оператора -=
    bus -= "Иванов"
    print(bus)

    # Попытка посадить больше пассажиров, чем есть мест
    bus.board("Васильев", "Николаев", "Орлов", "Яковлев")
    print(bus)

    # Просмотр мест в автобусе
    print("Места в автобусе:", bus.seats)
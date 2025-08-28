"""

Напишите программу с классом Math. При инициализации
атрибутов нет. Реализовать методы addition, subtraction,
multiplication и division. При передаче в методы двух числовых
параметров нужно производить с параметрами
соответствующие действия и печатать ответ

"""


class Math:
    def __init__(self):
        # Конструктор без атрибутов
        pass

    def addition(self, a, b):
        """Сложение двух чисел"""
        result = a + b
        print(f"Результат сложения: {a} + {b} = {result}")
        return result

    def subtraction(self, a, b):
        """Вычитание двух чисел"""
        result = a - b
        print(f"Результат вычитания: {a} - {b} = {result}")
        return result

    def multiplication(self, a, b):
        """Умножение двух чисел"""
        result = a * b
        print(f"Результат умножения: {a} * {b} = {result}")
        return result

    def division(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            print("Ошибка: деление на ноль!")
            return None
        result = a / b
        print(f"Результат деления: {a} / {b} = {result}")
        return result


# Пример использования класса
if __name__ == "__main__":
    math = Math()

    # Тестирование методов
    math.addition(10, 5)
    math.subtraction(10, 5)
    math.multiplication(10, 5)
    math.division(10, 5)
    math.division(10, 0)  # Проверка деления на ноль
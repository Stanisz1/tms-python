"""
Реализовать программу с функционалом калькулятора для
операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать ООП.
Использовать обработку исключений
"""

class Calculator:
    """
    Класс для выполнения арифметических операций над числами.
        Особенности:
    1. Поддерживает основные арифметические операции: +, -, *, /, //, %, **
    2. Обрабатывает все возможные ошибки ввода
    3. Позволяет использовать результат предыдущей операции
    4. Поддерживает русский и английский ввод для подтверждения действий
    5. Предоставляет возможность выхода после каждой операции
    """

    def __init__(self):
        """Инициализация калькулятора."""
        self.result = None

    def add(self, a, b):
        """Сложение двух чисел."""
        return a + b

    def subtract(self, a, b):
        """Вычитание двух чисел."""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел."""
        return a * b

    def divide(self, a, b):
        """Деление двух чисел."""
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль!")
        return a / b

    def floor_divide(self, a, b):
        """Целочисленное деление."""
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль!")
        return a // b

    def modulus(self, a, b):
        """Остаток от деления."""
        if b == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль!")
        return a % b

    def power(self, a, b):
        """Возведение в степень."""
        return a ** b

    def calculate(self, a, b, operation):
        """
        Выполняет указанную операцию над двумя числами.

        Параметры:
            a (float): первое число
            b (float): второе число
            operation (str): символ операции

        Возвращает:
            float: результат операции
        """
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '//': self.floor_divide,
            '%': self.modulus,
            '**': self.power,
        }

        if operation not in operations:
            raise ValueError(f"Неподдерживаемая операция: {operation}")

        return operations[operation](a, b)

    def get_yes_no_input(self, prompt):
        """
        Запрашивает подтверждение у пользователя с поддержкой рус/англ ввода.

        Параметры:
            prompt (str): текст запроса

        Возвращает:
            bool: True если ответ положительный, False если отрицательный
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ['y', 'д', 'yes', 'да']:
                return True
            elif response in ['n', 'н', 'no', 'нет']:
                return False
            else:
                print("Пожалуйста, введите 'y' (да) или 'n' (нет).")

    def run(self):
        """Основной цикл работы калькулятора."""
        print("=" * 50)
        print("_" * 19 + "КАЛЬКУЛЯТОР" + "_" * 20)
        print("=" * 50)
        print("Поддерживаемые операции: +, -, *, /, //, %, **")
        print("Для выхода введите 'q' в любой момент")

        while True:
            try:
                a_input = input("\nВведите первое число: ").strip()
                if a_input.lower() == 'q':
                    print("Выход из программы.")
                    return
                a = float(a_input)

                operation = input("Введите операцию (+, -, *, /, //, %, **): ").strip()
                if operation.lower() == 'q':
                    print("Выход из программы.")
                    return

                b_input = input("Введите второе число: ").strip()
                if b_input.lower() == 'q':
                    print("Выход из программы.")
                    return
                b = float(b_input)

                result = self.calculate(a, b, operation)
                print(f"\nРезультат: {a} {operation} {b} = {result}")
                self.result = result

                use_previous = self.get_yes_no_input(
                    "\nИспользовать результат для следующей операции? (y/n): "
                )

                while use_previous:
                    a = self.result
                    print(f"\nПервое число: {a}")

                    operation = input("Введите операцию (+, -, *, /, //, %, **): ").strip()
                    if operation.lower() == 'q':
                        print("Выход из программы.")
                        return

                    b_input = input("Введите второе число: ").strip()
                    if b_input.lower() == 'q':
                        print("Выход из программы.")
                        return
                    b = float(b_input)

                    result = self.calculate(a, b, operation)
                    print(f"\nРезультат: {a} {operation} {b} = {result}")
                    self.result = result

                    use_previous = self.get_yes_no_input(
                        "\nИспользовать результат для следующей операции? (y/n): "
                    )

                continue_calculator = self.get_yes_no_input(
                    "\nПродолжить вычисления с новыми числами? (y/n): "
                )

                if not continue_calculator:
                    print("\nРабота калькулятора завершена.")
                    return

            except ValueError as e:
                print(f"Ошибка ввода: {e}")
                print("Пожалуйста, вводите числа в правильном формате (например: 5, 3.14, -2.5)")
            except ZeroDivisionError as e:
                print(e)
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
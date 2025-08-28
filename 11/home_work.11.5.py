"""

Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
• Метод is_repeatance(s), который принимает некоторую строку
и возвращает True или False в зависимости от того, может ли
текущая строка быть получена целым количеством повторов
строки s. Считать, что пустая строка не содержит повторов
• Метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.

"""


class SuperStr(str):
    """
    Класс SuperStr, наследуемый от стандартного типа str.
    Добавляет два новых метода: is_repeatance и is_palindrom.
    """

    def is_repeatance(self, s: str) -> bool:
        """
        Проверяет, может ли текущая строка быть получена
        целым количеством повторов строки s.

        Args:
            s: Строка для проверки повторений

        Returns:
            bool: True если строка может быть получена повторениями s, иначе False
        """
        # Если текущая строка пустая или s пустая - возвращаем False
        if not self or not s:
            return False

        # Если длина текущей строки не делится на длину s без остатка,
        # то строка не может быть получена повторениями
        if len(self) % len(s) != 0:
            return False

        # Проверяем, состоит ли строка из повторений s
        repeat_count = len(self) // len(s)
        return self == s * repeat_count

    def is_palindrom(self) -> bool:
        """
        Проверяет, является ли строка палиндромом.
        Регистр символов не учитывается.

        Returns:
            bool: True если строка является палиндромом, иначе False
        """
        # Приводим строку к нижнему регистру для регистронезависимого сравнения
        lower_str = self.lower()
        # Сравниваем строку с ее обратной версией
        return lower_str == lower_str[::-1]


# Демонстрация работы класса
if __name__ == "__main__":
    # Тестирование метода is_repeatance
    s1 = SuperStr("abcabcabc")
    print(f"'{s1}'.is_repeatance('abc') = {s1.is_repeatance('abc')}")  # True

    s2 = SuperStr("abcabcab")
    print(f"'{s2}'.is_repeatance('abc') = {s2.is_repeatance('abc')}")  # False

    s3 = SuperStr("")
    print(f"'{s3}'.is_repeatance('a') = {s3.is_repeatance('a')}")  # False

    s4 = SuperStr("aaa")
    print(f"'{s4}'.is_repeatance('a') = {s4.is_repeatance('a')}")  # True

    # Тестирование метода is_palindrom
    p1 = SuperStr("Radar")
    print(f"'{p1}'.is_palindrom() = {p1.is_palindrom()}")  # True

    p2 = SuperStr("Hello")
    print(f"'{p2}'.is_palindrom() = {p2.is_palindrom()}")  # False

    p3 = SuperStr("")
    print(f"'{p3}'.is_palindrom() = {p3.is_palindrom()}")  # True

    p4 = SuperStr("A")
    print(f"'{p4}'.is_palindrom() = {p4.is_palindrom()}")  # True

    p5 = SuperStr("А роза упала на лапу Азора")
    print(f"'{p5}'.is_palindrom() = {p5.is_palindrom()}")  # False (из-за пробелов)
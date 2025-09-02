"""

ПчёлоСлон
Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону. Класс реализует
следующие методы:
● Fly() – возвращает True, если часть пчелы не меньше части
слона, иначе – False
● Trumpet() – если часть слона не меньше части пчелы,
возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
● Eat(meal, value) – может принимать в meal только ”nectar” или
“grass”. Если съедает нектар, то value вычитается из части
слона, пчеле добавляется. Иначе – наоборот. Не может
увеличиваться больше 100 и уменьшаться меньше 0

"""


class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee = max(0, min(100, bee_part))  # Обеспечиваем границы [0, 100]
        self.elephant = max(0, min(100, elephant_part))  # Обеспечиваем границы [0, 100]

    def fly(self):
        """Возвращает True, если часть пчелы не меньше части слона, иначе False"""
        return self.bee >= self.elephant

    def trumpet(self):
        """Возвращает 'tu-tu-doo-doo', если часть слона не меньше части пчелы, иначе 'wzzzz'"""
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        """
        Принимает meal: 'nectar' или 'grass'
        Если nectar: value вычитается из слона и добавляется пчеле
        Если grass: value вычитается из пчелы и добавляется слону
        Значения не могут выйти за пределы [0, 100]
        """
        if meal not in ["nectar", "grass"]:
            raise ValueError("meal должен быть 'nectar' или 'grass'")

        if value < 0:
            raise ValueError("value не может быть отрицательным")

        if meal == "nectar":
            # Уменьшаем часть слона, но не ниже 0
            self.elephant = max(0, self.elephant - value)
            # Увеличиваем часть пчелы, но не выше 100
            self.bee = min(100, self.bee + value)
        else:  # meal == "grass"
            # Уменьшаем часть пчелы, но не ниже 0
            self.bee = max(0, self.bee - value)
            # Увеличиваем часть слона, но не выше 100
            self.elephant = min(100, self.elephant + value)

    def __str__(self):
        return f"Пчела: {self.bee}, Слон: {self.elephant}"


# Пример использования
if __name__ == "__main__":
    # Создаем ПчёлоСлона
    bee_elephant = BeeElephant(50, 50)
    print(f"Создан: {bee_elephant}")

    # Тестируем методы
    print(f"Может летать: {bee_elephant.fly()}")
    print(f"Звук: {bee_elephant.trumpet()}")

    # Пробуем разные приемы пищи
    bee_elephant.eat("nectar", 10)
    print(f"После nectar(10): {bee_elephant}")
    print(f"Может летать: {bee_elephant.fly()}")
    print(f"Звук: {bee_elephant.trumpet()}")

    bee_elephant.eat("grass", 20)
    print(f"После grass(20): {bee_elephant}")
    print(f"Может летать: {bee_elephant.fly()}")
    print(f"Звук: {bee_elephant.trumpet()}")

    # Тестируем граничные значения
    bee_elephant.eat("nectar", 100)
    print(f"После nectar(100): {bee_elephant}")

    bee_elephant.eat("grass", 100)
    print(f"После grass(100): {bee_elephant}")

    # Создаем другой экземпляр для демонстрации
    bee_elephant2 = BeeElephant(30, 70)
    print(f"\nНовый ПчёлоСлон: {bee_elephant2}")
    print(f"Может летать: {bee_elephant2.fly()}")
    print(f"Звук: {bee_elephant2.trumpet()}")
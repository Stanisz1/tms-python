"""

 Класс «Товар» содержит следующие закрытые поля:
● Название товара
● Название магазина, в котором подаётся товар
● Стоимость товара в рублях
Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
● Вывод информации о товаре со склада по индексу
● Вывод информации о товаре со склада по имени товара
● Сортировка товаров по названию, по магазину и по цене
● Перегруженная операция сложения товаров по цене

"""


class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    # Геттеры
    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price

    # Сеттеры
    def set_name(self, name):
        self.__name = name

    def set_store(self, store):
        self.__store = store

    def set_price(self, price):
        self.__price = price

    # Перегрузка оператора сложения
    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        return self.__price + other

    def __radd__(self, other):
        return self.__price + other

    # Строковое представление
    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__store}, Цена: {self.__price} руб."


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        """Добавление товара на склад"""
        self.__products.append(product)

    def display_by_index(self, index):
        """Вывод информации о товаре по индексу"""
        if 0 <= index < len(self.__products):
            print(self.__products[index])
        else:
            print("Товар с таким индексом не найден")

    def display_by_name(self, name):
        """Вывод информации о товаре по имени"""
        found = False
        for product in self.__products:
            if product.get_name().lower() == name.lower():
                print(product)
                found = True

        if not found:
            print("Товар с таким именем не найден")

    def sort_by_name(self):
        """Сортировка товаров по названию"""
        self.__products.sort(key=lambda x: x.get_name())
        print("Товары отсортированы по названию")

    def sort_by_store(self):
        """Сортировка товаров по магазину"""
        self.__products.sort(key=lambda x: x.get_store())
        print("Товары отсортированы по магазину")

    def sort_by_price(self):
        """Сортировка товаров по цене"""
        self.__products.sort(key=lambda x: x.get_price())
        print("Товары отсортированы по цене")

    def display_all(self):
        """Вывод всех товаров (для удобства тестирования)"""
        if not self.__products:
            print("Склад пуст")
            return

        for i, product in enumerate(self.__products):
            print(f"{i}: {product}")

    # Перегрузка оператора сложения для склада
    def __add__(self, other):
        """Сложение двух складов - объединение их товаров"""
        if isinstance(other, Warehouse):
            new_warehouse = Warehouse()
            for product in self.__products:
                new_warehouse.add_product(product)
            for product in other.__products:
                new_warehouse.add_product(product)
            return new_warehouse
        return self

    def total_price(self):
        """Общая стоимость всех товаров на складе"""
        return sum(product.get_price() for product in self.__products)


if __name__ == "__main__":
    # Создаем товары
    p1 = Product("Ноутбук", "Электросила", 50000)
    p2 = Product("Мышь", "Компьютерный мир", 1500)
    p3 = Product("Клавиатура", "Электросила", 3000)
    p4 = Product("Монитор", "Компьютерный мир", 20000)

    # Создаем склад и добавляем товары
    warehouse = Warehouse()
    warehouse.add_product(p1)
    warehouse.add_product(p2)
    warehouse.add_product(p3)
    warehouse.add_product(p4)

    # Демонстрация работы
    print("Все товары на складе:")
    warehouse.display_all()

    print("\nТовар по индексу 2:")
    warehouse.display_by_index(2)

    print("\nТовары с именем 'Мышь':")
    warehouse.display_by_name("Мышь")

    print("\nСортировка по цене:")
    warehouse.sort_by_price()
    warehouse.display_all()

    print("\nСортировка по названию:")
    warehouse.sort_by_name()
    warehouse.display_all()

    print("\nСортировка по магазину:")
    warehouse.sort_by_store()
    warehouse.display_all()

    # Демонстрация перегрузки оператора сложения для товаров
    print(f"\nСумма цен товаров 1 и 2: {p1 + p2} руб.")

    # Демонстрация перегрузки оператора сложения для складов
    warehouse2 = Warehouse()
    p5 = Product("Наушники", "Аудиотехника", 5000)
    warehouse2.add_product(p5)

    combined_warehouse = warehouse + warehouse2
    print("\nОбъединенный склад:")
    combined_warehouse.display_all()

    print(f"\nОбщая стоимость всех товаров: {warehouse.total_price()} руб.")
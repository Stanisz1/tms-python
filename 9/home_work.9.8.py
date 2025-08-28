"""
JSON и CSV.
Исходные данные:
[
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": true,
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": false,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": true,
        "languages": ["C#", "C++", "C"]
    }
]
Пункты задания:
• Есть данные в формате JSON – взять с диска с исходными
данными.
• Реализовать функцию, которая считает данные из исходного
JSON-файла и преобразует их в формат CSV
• Реализовать функцию, которая сохранит данные в CSV-файл
(данные должны сохраняться независимо от их количества –
если добавить в исходный JSON-файл ещё одного
сотрудника, работа программы не должна нарушаться).
• Реализовать функцию, которая добавит информацию о новом
сотруднике в JSON-файл. Пошагово вводятся все
необходимые данные о сотруднике, формируются данные для
записи.
• Такая же функция для добавления информации о новом
сотруднике в CSV-файл.
TeachMeSkills.by
• Реализовать функцию, которая выведет информацию об
одном сотруднике по имени. Имя для поиска вводится с
клавиатуры.
• Реализовать функцию фильтра по языку: с клавиатуры
вводится язык программирования, выводится список всех
сотрудников, кто владеет этим языком программирования.
• Реализовать функцию фильтра по году: ввести с клавиатуры
год рождения, вывести средний рост всех сотрудников, у
которых год рождения меньше заданного.
• Программа должна представлять собой интерактив –
пользовательское меню с возможностью выбора
определённого действия (действия – функции из предыдущих
пунктов + выход из программы). Пока пользователь не
выберет выход из программы, должен предлагаться выбор
следующего действия.


"""
import json
import csv


JSON_FILE = 'employees.json'
CSV_FILE = 'employees.csv'


def load_json_data():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_json_data(data):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def json_to_csv():
    data = load_json_data()
    if not data:
        return

    with open(CSV_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for item in data:
            writer.writerow([
                item['name'],
                item['birthday'],
                item['height'],
                item['weight'],
                item['car'],
                ';'.join(item['languages'])
            ])


def add_employee_to_json():
    data = load_json_data()
    new_employee = {}

    new_employee['name'] = input("Введите имя: ")
    new_employee['birthday'] = input("Введите дату рождения (dd.mm.yyyy): ")
    new_employee['height'] = int(input("Введите рост: "))
    new_employee['weight'] = float(input("Введите вес: "))
    new_employee['car'] = input("Есть машина? (true/false): ").lower() == 'true'

    languages = input("Введите языки через запятую: ").split(',')
    new_employee['languages'] = [lang.strip() for lang in languages]

    data.append(new_employee)
    save_json_data(data)
    print("Сотрудник добавлен в JSON файл")


def add_employee_to_csv():
    new_employee = {}

    new_employee['name'] = input("Введите имя: ")
    new_employee['birthday'] = input("Введите дату рождения (dd.mm.yyyy): ")
    new_employee['height'] = int(input("Введите рост: "))
    new_employee['weight'] = float(input("Введите вес: "))
    new_employee['car'] = input("Есть машина? (true/false): ").lower() == 'true'

    languages = input("Введите языки через запятую: ").split(',')
    new_employee['languages'] = [lang.strip() for lang in languages]

    with open(CSV_FILE, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            new_employee['name'],
            new_employee['birthday'],
            new_employee['height'],
            new_employee['weight'],
            new_employee['car'],
            ';'.join(new_employee['languages'])
        ])
    print("Сотрудник добавлен в CSV файл")


def find_employee_by_name():
    data = load_json_data()
    name = input("Введите имя для поиска: ")

    found = [emp for emp in data if name.lower() in emp['name'].lower()]

    if not found:
        print("Сотрудник не найден")
        return

    for emp in found:
        print(f"\nИмя: {emp['name']}")
        print(f"Дата рождения: {emp['birthday']}")
        print(f"Рост: {emp['height']}")
        print(f"Вес: {emp['weight']}")
        print(f"Автомобиль: {'Есть' if emp['car'] else 'Нет'}")
        print(f"Языки: {', '.join(emp['languages'])}")


def filter_by_language():
    data = load_json_data()
    language = input("Введите язык программирования: ")

    found = [emp for emp in data if any(lang.lower() == language.lower()
                                        for lang in emp['languages'])]

    if not found:
        print("Сотрудники не найдены")
        return

    for emp in found:
        print(f"\nИмя: {emp['name']}")
        print(f"Языки: {', '.join(emp['languages'])}")


def filter_by_year():
    data = load_json_data()
    try:
        year_filter = int(input("Введите год для фильтрации: "))
    except ValueError:
        print("Некорректный год")
        return

    total_height = 0
    count = 0

    for emp in data:
        birth_year = int(emp['birthday'].split('.')[-1])
        if birth_year < year_filter:
            total_height += emp['height']
            count += 1

    if count == 0:
        print("Нет сотрудников, удовлетворяющих условию")
    else:
        print(f"Средний рост: {total_height / count:.2f} см")


def main_menu():
    while True:
        print("\n1. Конвертировать JSON в CSV")
        print("2. Добавить сотрудника в JSON")
        print("3. Добавить сотрудника в CSV")
        print("4. Поиск сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Фильтр по году рождения")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            json_to_csv()
            print("Данные конвертированы в CSV")
        elif choice == '2':
            add_employee_to_json()
        elif choice == '3':
            add_employee_to_csv()
        elif choice == '4':
            find_employee_by_name()
        elif choice == '5':
            filter_by_language()
        elif choice == '6':
            filter_by_year()
        elif choice == '7':
            break
        else:
            print("Некорректный выбор")


if __name__ == "__main__":
    main_menu()

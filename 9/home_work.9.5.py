"""

В текстовый файл построчно записаны фамилия и имя учащихся
класса и оценка за контрольную. Вывести на экран всех учащихся,
чья оценка меньше трёх баллов

Файл с данными учащихся
students.txt
"""

def find_low_grades():
    filename = input("Введите имя файла с данными учащихся: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print("Учащиеся с оценкой ниже 3 баллов:")
            print("-" * 40)

            found = False
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 3:
                    grade = parts[-1]
                    name = ' '.join(parts[:-1])

                    try:
                        if float(grade) < 3:
                            print(f"{name}: {grade}")
                            found = True
                    except ValueError:
                        continue

            if not found:
                print("Учащихся с оценкой ниже 3 баллов не найдено.")

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")


# Запуск программы
if __name__ == "__main__":
    find_low_grades()
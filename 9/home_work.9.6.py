"""
В файл записано некоторое содержимое (буквы, цифры,
пробелы, специальные символы и т.д.). Числом назовём
последовательность цифр, идущих подряд. Вывести сумму всех
чисел, записанных в файле.
Пример.
Входные данные: 123 ааа456 1x2y3z 4 5 6
Выходные данные: 600
"""

def main():
    total_sum = 0
    current_number = ''

    with open('input_for_9.6.txt', 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break

            if char.isdigit():
                current_number += char
            else:
                if current_number:
                    total_sum += int(current_number)
                    current_number = ''

        if current_number:
            total_sum += int(current_number)

    print(total_sum)

if __name__ == '__main__':
    main()
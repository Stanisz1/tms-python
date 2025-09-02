"""

Дан текстовый файл с несколькими строками. Зашифровать
шифром Цезаря, при этом шаг зависит от номера строки: для
первой строки шаг 1, для второй – 2 и т.д.
Пример.
Входные данные:
Hello
Hello
Hello
Hello
Выходные данные:
Ifmmp
Jgnnq
Khoor
Lipps

"""


def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)
    return ''.join(result)


def main():
    with open('input_for_9.7.txt', 'r') as file:
        lines = file.readlines()

    encrypted_lines = []
    for i, line in enumerate(lines, start=1):
        # Убираем символ новой строки, шифруем, затем добавляем обратно
        encrypted_line = caesar_cipher(line.rstrip('\n'), i)
        encrypted_lines.append(encrypted_line + '\n')

    with open('output_for_9.7.txt', 'w') as file:
        file.writelines(encrypted_lines)


if __name__ == '__main__':
    main()



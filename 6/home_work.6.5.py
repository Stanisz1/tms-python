"""
Программа получает на вход строку – сообщение и
указание, что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное сообщение
шифром Цезаря, вторая – расшифровывает. В зависимости от
выбора пользователя (шифровать или дешифровать) вызывается
соответствующая функция, результат выводится в консоль
"""

def is_latin(text):
    """Проверяет, содержит ли текст только латинские символы и разрешённые знаки препинания"""
    allowed_chars = " .,!?;:'\"-()"
    for char in text:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z' or char in allowed_chars):
            return False
    return True

def caesar_encrypt(text, shift=3):
    """
    Шифрует текст с помощью шифра Цезаря с заданным сдвигом
    3 влево (аналогично шифрованию 23 вправо)
    """
    encrypted_text = []
    for char in text:
        if char.isupper():
            start = ord('A')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.islower():

            start = ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return ''.join(encrypted_text)


def caesar_decrypt(text, shift=3):
    """
    Дешифрует текст, зашифрованный шифром Цезаря с заданным сдвигом
      3 влево (аналогично шифрованию 23 вправо)
    """
    return caesar_encrypt(text, -shift)


# Основная программа
if __name__ == "__main__":
    message = input("Введите сообщение на латинице: ")
    if not is_latin(message):
        print("Ошибка: сообщение должно содержать только латинские символы!")
        exit()

    action = input("Выберите действие ([1] - шифровать, [2] - дешифровать): ")

    if action == '1':
        result = caesar_encrypt(message)
        print(f"Зашифрованное сообщение: {result}")
    elif action == '2':
        result = caesar_decrypt(message)
        print(f"Расшифрованное сообщение: {result}")
    else:
        print("Ошибка: неверный выбор действия. Введите 1 или 2.")

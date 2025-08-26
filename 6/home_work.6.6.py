"""
Программа получает на вход строку – сообщение и
указание, что нужно сделать: шифровать или дешифровать.
Реализовать две функции: первая шифрует заданное сообщение
шифром Виженера вторая – расшифровывает. В зависимости от
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

def encrypt_vigenere(message, key):
    return _vigenere(message, key, True)


def decrypt_vigenere(ciphertext, key):
    return _vigenere(ciphertext, key, False)


def _vigenere(text, key, encrypt):
    cleaned_key = ''.join(filter(str.isalpha, key)).upper()
    if cleaned_key == "":
        cleaned_key = "A"

    j = 0
    result = []
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            offset = ord(char) - ord(base)
            key_char = cleaned_key[j % len(cleaned_key)]
            key_offset = ord(key_char) - ord('A')

            if encrypt:
                new_offset = (offset + key_offset) % 26
            else:
                new_offset = (offset - key_offset) % 26

            new_char = chr(ord(base) + new_offset)
            result.append(new_char)
            j += 1
        else:
            result.append(char)
    return ''.join(result)

action = input("Выберите действие: (e)ncrypt или (d)ecrypt: ").strip().lower()
message = input("Введите сообщение на латинице: ")
if not is_latin(message):
    print("Ошибка: сообщение должно содержать только латинские символы!")
    exit()

key = input("Введите ключ: ")

if action in ['e', 'encrypt']:
    result = encrypt_vigenere(message, key)
    print("Зашифрованное сообщение:", result)
elif action in ['d', 'decrypt']:
    result = decrypt_vigenere(message, key)
    print("Расшифрованное сообщение:", result)
else:
    print("Неизвестное действие")
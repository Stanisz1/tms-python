"""

Напишите программу, которая получает на вход строку с
названием текстового файла и выводит на экран содержимое этого
файла, заменяя все запрещённые слова звездочками.
Запрещённые слова, разделённые символом пробела, должны
храниться в файле stop_words.txt.
Программа должна находить запрещённые слова в любом месте
файла, даже в середине другого слова. Замена независима от
регистра: если в списке запрещённых есть слово exam, то
замениться должны exam, eXam, EXAm и другие вариации.
Пример.
в stop_words.txt записаны слова: hello email python the exam wor is
Текст файла для цензуры выглядит так: Hello, World! Python IS the
programming language of thE future. My EMAIL is... PYTHON as
AwESOME!
Тогда итоговый текст: *****, ***ld! ****** ** *** programming language of
*** future. My ***** **... ****** ** awesome!!!!

Файлик с текстом
______________
incr_text.txt
_____________
"""
import re


class TextCensor:
    def __init__(self, stop_words_file='stop_words.txt'):
        self.stop_words_file = stop_words_file
        self.stop_words = self._load_stop_words()

    def _load_stop_words(self):
        try:
            with open(self.stop_words_file, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                return content.split() if content else []
        except FileNotFoundError:
            print(f"Файл {self.stop_words_file} не найден.")
            return []

    def censor_text(self, text):
        if not self.stop_words:
            return text

        combined_pattern = '|'.join(map(re.escape, self.stop_words))
        pattern = re.compile(combined_pattern, re.IGNORECASE)

        return pattern.sub(lambda match: '*' * len(match.group()), text)

    def process_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            censored_content = self.censor_text(content)
            print(censored_content, end='')
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")


def main():
    filename = input("Введите название текстового файла: ")
    censor = TextCensor()
    censor.process_file(filename)


if __name__ == "__main__":
    main()
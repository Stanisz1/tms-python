import string
import os
from collections import Counter

class LineAnalyzer:
    def __init__(self, line):
        self.line = line
        self.counter = {}
        self.most_common_word = None
        self.max_count = 0

    def _clean_word(self, word):
        return word.strip(string.punctuation + '—«»')

    def process(self):
        words = self.line.split()
        for word in words:
            cleaned_word = self._clean_word(word)
            if cleaned_word and len(cleaned_word) > 1:  # Игнорируем одиночные символы
                self.counter[cleaned_word] = self.counter.get(cleaned_word, 0) + 1

        if self.counter:
            self.most_common_word, self.max_count = Counter(self.counter).most_common(1)[0]

class FileProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.results = []

    def process_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            for line in lines:
                if line.strip():
                    analyzer = LineAnalyzer(line)
                    analyzer.process()
                    self.results.append(analyzer)

    def write_results(self):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for i, result in enumerate(self.results):
                if result.most_common_word:
                    f.write(f"{result.most_common_word} {result.max_count}\n")
                else:
                    f.write(f"No words found in line {i+1}\n")

def main():
    input_filename = 'input.txt'  # Укажите имя вашего входного файла
    output_filename = 'output.txt'

    if not os.path.exists(input_filename):
        print(f"Ошибка: Файл {input_filename} не найден.")
        return

    processor = FileProcessor(input_filename, output_filename)
    processor.process_file()
    processor.write_results()

    print(f"Анализ завершен. Результаты записаны в файл {output_filename}")

if __name__ == "__main__":
    main()
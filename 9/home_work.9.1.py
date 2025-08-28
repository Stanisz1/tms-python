"""
Работа с модулем os
Есть папка, в которой лежат файлы с разными расширениями.
Программа должна:
• Вывести имя вашей ОС
• Вывести путь до папки, в которой вы находитесь
• Рассортировать файлы по расширениям, например, для
текстовых файлов создается папка, в неё перемещаются все
файлы с расширением .txt, то же самое для остальных
расширений
• После рассортировки выводится сообщение типа «в папке с
текстовыми файлами перемещено 5 файлов, их суммарный
размер – 50 гигабайт»
• Как минимум один файл в любой из получившихся
поддиректорий переименовать. Сделать вывод сообщения
типа «Файл data.txt был переименован в some_data.txt»
• Программа должна быть кроссплатформенной – никаких
хардкодов с именем диска и слэшами
"""

import os
import shutil


def main():
    print(f"Имя ОС: {os.name}")

    current_dir = os.getcwd()
    print(f"Текущий путь: {current_dir}")

    files = [f for f in os.listdir(current_dir)
             if os.path.isfile(os.path.join(current_dir, f))]

    extensions = {}
    for file in files:
        name, ext = os.path.splitext(file)
        ext = ext.lower() if ext else 'no_extension'
        if ext not in extensions:
            extensions[ext] = []
        extensions[ext].append(file)

    for ext, files_list in extensions.items():
        folder_name = ext[1:] if ext != 'no_extension' else ext

        folder_path = os.path.join(current_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        total_size = 0
        for file in files_list:
            src = os.path.join(current_dir, file)
            dst = os.path.join(folder_path, file)
            total_size += os.path.getsize(src)
            shutil.move(src, dst)

        size_gb = total_size / (1024 ** 3)
        print(f"В папке '{folder_name}' перемещено {len(files_list)} файлов, "
              f"их суммарный размер - {size_gb:.2f} гигабайт")

    target_ext = '.txt'
    folder_name = target_ext[1:]
    folder_path = os.path.join(current_dir, folder_name)

    if os.path.exists(folder_path):
        files_in_dir = os.listdir(folder_path)
        if files_in_dir:
            old_name = files_in_dir[0]
            name, ext = os.path.splitext(old_name)
            new_name = f"new_{name}{ext}"

            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)

            print(f"Файл {old_name} был переименован в {new_name}")


if __name__ == "__main__":
    main()
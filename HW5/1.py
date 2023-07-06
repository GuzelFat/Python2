"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""


def file_path_split(text: str) -> tuple:
    *file_path, file_name, file_ext = text.replace('.', '\\').split('\\')
    file_path = '/'.join(file_path)
    return file_path, file_name, file_ext


if __name__ == '__main__':
    path = 'E:\Geek Brains\Git\Python_education2\HW5\hw1.py'
    print(file_path_split(path))

"""Добавьте в пакет, созданный на семинаре, шахматный модуль. Внутри него напишите код, решающий
задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих
друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты
8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки."""

from datetime import datetime as date
from random import randint as rnd

__all__ = ['good_queens_variants']

MIN_COORD = 0
MAX_COORD = 7
QUEEN_NUM = 8


def is_queens_beating_each_other(coordinates: list[list[int]]) -> bool:
    for i in range(len(coordinates)):

        for j in range(len(coordinates)):
            row1 = coordinates[i][0]
            col1 = coordinates[i][1]
            row2 = coordinates[j][0]
            col2 = coordinates[j][1]

            if not (row1 == row2 and col1 == col2):
                if row1 == row2 or col1 == col2 or row1 + col1 == row2 + col2 or row1 - row2 == col1 - col2:
                    return False

    return True


def queens_coord_gen():
    coordinates = []

    while len(coordinates) < 8:
        coord1 = rnd(MIN_COORD, MAX_COORD)
        coord2 = rnd(MIN_COORD, MAX_COORD)
        if not [coord1, coord2] in coordinates:
            coordinates.append([coord1, coord2])
            yield coordinates[-1]


def good_queens_variants() -> None:
    good_vars = 1
    attempt = 1

    print(f'Старт в {date.now().hour}:{date.now().minute}:{date.now().second}')
    while good_vars < 5:
        #  coord = [[0, 1], [1, 3], [2, 5], [3, 7], [4, 2], [5, 0], [6, 6], [7, 4]]
        coord = [q_coord for q_coord in queens_coord_gen()]

        if is_queens_beating_each_other(coord):
            print(f'Успешная расстановка {good_vars}: {coord} ... '
                  f'в {date.now().hour}:{date.now().minute}:{date.now().second} на попытке {attempt}')
            good_vars += 1

        attempt += 1


if __name__ == '__main__':
    good_queens_variants()
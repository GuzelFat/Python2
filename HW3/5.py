"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите, какие
вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
✔ *Верните все возможные варианты комплектации рюкзака.
"""
import itertools

BACKPACK_LOAD = 30
current_mass = 0

stuff_mass = {'уголь': 3, 'спички': 0.1, 'плавки': 0.5, 'туалетная бумага': 0.4,
              'очки': 0.3, 'карта': 0.1, 'ящик пива': 15, 'планшет': 0.8,
              'палатка': 20, 'мяч': 2.1, 'котелок': 3, 'вода': 1.5,
              'хлеб': 0.5, 'сосиски': 0.7, 'арбуз': 5.5, 'набор посуды': 2,
              'шампуры': 1.2, 'готовый шашлык': 5, 'крем от комаров': 0.5, 'одеяло': 4.3}

stuff_in_backpack = []

for key, value in stuff_mass.items():
    if current_mass <= BACKPACK_LOAD:
        if current_mass + value <= BACKPACK_LOAD:
            current_mass += value
        else:
            break

        stuff_in_backpack.append(key)

print('Комплектация рюкзака: ', end='')

for i in range(len(stuff_in_backpack)):
    if i < len(stuff_in_backpack) - 1:
        print(f'{stuff_in_backpack[i]}, ', end='')
    else:
        print(f'{stuff_in_backpack[i]}', end=' ')

print(f'({current_mass} кг.)')
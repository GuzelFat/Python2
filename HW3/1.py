"""
Задание №7 с семинара
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях
"""

inp = input('Введите текст... ').replace(' ', '')
counter = dict()
counter_with_count = dict()

for sym in inp:
    if sym not in counter:
        counter[sym] = 1
    else:
        counter[sym] += 1

print(counter)

for el in inp:
    el_count = inp.count(el)
    counter_with_count[el] = el_count

print(counter_with_count)

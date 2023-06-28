"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
"""
import collections


MAX_COUNT = 10

paper = 'Python (в русском языке встречаются названия пито́н или па́йтон) — высокоуровневый язык программирования \n' \
        'общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный \n' \
        'на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение \n' \
        'переносимости написанных на нём программ. Язык является полностью объектно-ориентированным в том плане, \n' \
        'что всё является объектами. Особенностью языка является выделение блоков кода пробельными отступами. \n' \
        'Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться \n' \
        'к документации. Сам же язык известен как интерпретируемый, используется в том числе для написания \n' \
        'скриптов. \nНедостатками языка являются зачастую более низкая скорость работы и более высокое потребление \n' \
        'памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, \n' \
        'таких как C или C++; \n' \
        'Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, \n' \
        'структурное, объектно-ориентированное программирование, метапрограммирование и функциональное \n' \
        'программирование. Задачи обобщённого программирования решаются за счёт динамической типизации. Аспектно-\n' \
        'ориентированное программирование частично поддерживается через декораторы, более полноценная поддержка \n' \
        'обеспечивается дополнительными фреймворками. Такие методики как контрактное и логическое программирование \n' \
        'реализовываются с помощью библиотек и расширений. Основные архитектурные черты — динамическая типизация, \n' \
        'автоматическое управление памятью, полная интроспекция, механизм обработки исключений, поддержка \n' \
        'многопоточных вычислений с глобальной блокировкой интерпретатора (GIL), высокоуровневые структуры данных. \n' \
        'Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты.'

formatted_paper = paper.lower().replace(';', '').replace(',', '').replace('.', '').replace('!', '').replace(':', '') \
    .replace('?', '').replace('(', '').replace(')', '').replace(' -', '').replace(' —', '').replace('\n', '').split()

words_count = dict()

for item in formatted_paper:
    count = formatted_paper.count(item)
    if item not in words_count:
        words_count[item] = count

most_count_words = dict()

for count in range(MAX_COUNT):
    max_key = ''
    max_value = 0

    for key, value in words_count.items():
        if value > max_value:
            max_value = value
            max_key = key

    most_count_words[max_key] = max_value
    words_count.pop(max_key)

print(f'Введённый текст:\n\n{paper}\n\nНаиболее часто встречающиеся {MAX_COUNT} слов в тексте:')
i = 1

for key, value in most_count_words.items():
    print(f'{i}. Слово \"{key}\" - {value} раз')
    i += 1

print(f'\nВторой вариант (через библиотеку collections):\n{collections.Counter(formatted_paper).most_common(10)}')
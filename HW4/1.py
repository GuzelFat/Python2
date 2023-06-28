"""Задание №8 с семинара № 4
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""


def variables_without_s(*args) -> None:
    print(globals())
    ending_s_variables = dict()

    for key, value in globals().items():
        if value in args and key[-1] == 's' and len(key) > 1:
            ending_s_variables[key] = value
            globals()[key] = None

    print(f'Переменные, имена которых более одного символа и оканчиваются на "s": {ending_s_variables}')

    for key, value in ending_s_variables.items():
        globals()[key[:-1:]] = value

    print(globals())


if __name__ == '__main__':
    mercury = 'Mercury'
    venus = 'Venus'
    earth = 'Earth'
    mars = 'Mars'
    jupiter = 'Jupiter'
    saturn = 'Saturn'
    uranus = 'Uranus'
    s = 7

    variables_without_s(mercury, venus, earth, mars, jupiter, saturn, uranus, s)
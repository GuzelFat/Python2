"""
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

SYSTEM = 16


def dec_to_hex(number: int):
    tmp_num: int = number
    new_num: str = ''

    while tmp_num != 0:
        mod = tmp_num % SYSTEM

        if 0 <= mod <= 9:
            new_num = str(mod) + new_num
        elif mod == 10:
            new_num = 'a' + new_num
        elif mod == 11:
            new_num = 'b' + new_num
        elif mod == 12:
            new_num = 'c' + new_num
        elif mod == 13:
            new_num = 'd' + new_num
        elif mod == 14:
            new_num = 'e' + new_num
        elif mod == 15:
            new_num = 'f' + new_num

        tmp_num //= SYSTEM

    new_num = '0x' + new_num

    return new_num


def check_hex(number_hex: str, number: int):
    if number_hex == hex(number):
        check_result = 'пройдена'

    else:
        check_result = 'результат ошибочен'

    return check_result
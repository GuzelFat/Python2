"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

def add_fraction(fraction_number):
    return input(f'Введите дробь №{fraction_number} в виде “a/b”:  ')


def str_fraction_split(fraction: str):
    frac_array = fraction.split("/")
    return frac_array


def fraction_sum(frac1: list, frac2: list):
    numerator1 = int(frac1[0])
    numerator2 = int(frac2[0])
    denominator1 = int(frac1[1])
    denominator2 = int(frac2[1])

    common_numerator = numerator1 * denominator2 + numerator2 * denominator1
    common_denominator = denominator1 * denominator2

    return numbers_reduction(common_numerator, common_denominator)


def fraction_mult(frac1: list, frac2: list):
    numerator1 = int(frac1[0])
    numerator2 = int(frac2[0])
    denominator1 = int(frac1[1])
    denominator2 = int(frac2[1])

    common_numerator = numerator1 * numerator2
    common_denominator = denominator1 * denominator2

    return numbers_reduction(common_numerator, common_denominator)


def numbers_reduction(num1, num2):
    end = 1
    start = min(num1, num2)

    while start != end:
        if num1 % start == 0 and num2 % start == 0:
            num1 = int(num1 / start)
            num2 = int(num2 / start)
            break
        start -= 1

    return [int(num1), int(num2)]


def list_fractions_to_str(fraction: list):
    return '1' if fraction[0] == fraction[1] else f'{fraction[0]}/{fraction[1]}'
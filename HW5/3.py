"""Создайте функцию генератор чисел Фибоначчи"""


def fibonacci_gen(max_count: int):
    fib1, fib2 = 0, 1
    yield fib1
    yield fib2

    count = 2

    while count < max_count:
        count += 1
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
        yield fib


for num in fibonacci_gen(30):
    print(num, end=' ')
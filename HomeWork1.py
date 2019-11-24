import math
from random import randint
import timeit

# Первое задание - словарь
def task1():
    d = {}

    for i in range(44, 90, 5):
        y = i * i + 1
        d[i] = str(i) + str(" * ") + str(i) + " + 1 = " + str(y)

    print(d)


# Второе задание - числа Фиббоначчи

fib_lambda = lambda n: fib_lambda(n - 1) + fib_lambda(n - 2) if n > 2 else 1

def fib(n):
    a = 0
    b = 1

    for __ in range(n):
        a, b = b, a + b

    return a

n = randint(10, 26)

def task2():
    print(str(n) + "-ое число Фиббоначчи = " + str(fib(n)))
    print("fib отработало за " + str(timeit.timeit('fib(n)', 'from __main__ import fib, n')))
    print("fib_lambda отработало за " + str(timeit.timeit('fib_lambda(n)', 'from __main__ import fib_lambda, n')))


# Третье задание - ряд Тейлора

def my_cos(x, n = 30):
    x = x / 180 * math.pi

    q = 1
    s = 0

    for i in range(1, n + 1):
        s = s + q
        q = q * (-1) * (x * x) / ((2 * i - 1) * (2 * i))

    return s


def my_sin(x, n = 30):
    x = x / 180 * math.pi

    q = x
    s = 0

    for i in range(1, n + 1):
        s = s + q
        q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))

    return s

def my_ln(x, n = 30):
    x -= 1
    s = 0

    for i in range(1, n + 1):
        s += ((-1) ** (i+1) * (x ** i)) / i

    return s

def my_exp(x, n = 30):
    s = 0

    for i in range(n):
        s += x ** i / math.factorial(i)

    return s

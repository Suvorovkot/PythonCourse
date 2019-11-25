import math
import cmath
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

    q = 1
    s = 0

    for i in range(1, n + 1):
        s = s + q
        q = q * (-1) * (x * x) / ((2 * i - 1) * (2 * i))

    return s


def my_sin(x, n = 30):

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

def task3():
    mc = my_cos(math.radians(60))
    ms = my_sin(math.radians(45))
    mln = my_ln(0.5)
    mex = my_exp(0.2)
    print("my_cos(60): " + str(mc) + ", math.cos(60): " + str(math.cos(math.radians(60))) + ", difference is: " + str(abs(math.cos(math.radians(60)) - mc)))
    print("my_sin(45): " + str(ms) + ", math.sin(45): " + str(math.sin(math.radians(45))) + ", difference is: " + str(abs(math.sin(math.radians(45)) - ms)))
    print("my_ln(0.5): " + str(mln) + ", math.ln(0.5): " + str(math.log(0.5, math.e)) + ", difference is: " + str(abs(math.log(0.5, math.e) - mln)))
    print("my_exp(0.2): " + str(mex) + ", math.exp(0.2): " + str(math.exp(0.2)) + ", difference is: " + str(abs(math.exp(0.2) - mex)))

    cx = complex(2, 3)
    mc = my_cos(cmath.phase(cx))
    print("my_cos from complex number", cx,": ", mc, " math.cos", cx, ": ", math.cos(cmath.phase(cx)), ", difference is: ", abs(mc - math.cos(cmath.phase(cx))))

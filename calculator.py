#https://github.com/aanelluri/lab11-AN-AT
# Partner 1: Anish Nelluri
# Partner 2: Alexander Tariam


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError("square_root: a must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("log: base must be > 0 and != 1, and argument must be > 0")
    return math.log(b, a)


def exp(a, b):
    return a ** b
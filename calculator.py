# https://github.com/aanelluri/lab11-AN-AT

import math

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b): return a*b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("second cannot be 0")
    else:
        return a/b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("log: base must be > 0 and != 1, and argument must be > 0")
    return math.log(b, a)


def exp(a, b):
    return a ** b
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

def log(a,b):
    if b <= 0:
        raise ValueError("base must be positive")
    else:
        return math.log(a,b)

def exp(a,b):
    return a ** b



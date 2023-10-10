def add(a, b):
    res = a + b
    return res

def subtract(a, b):
    res = a - b
    return res

def multiply(a, b):
    res = a * b
    return res

def power(a, b):
    res = a ** b
    return res

def square(a):
    res = a ** 2
    return res

def modulo(a, b):
    res = a % b
    return res

def divide(a, b):
    if b == 0:
        return 0
    res = a / b
    return res

def integer_division(a, b):
    res = a // b
    return res
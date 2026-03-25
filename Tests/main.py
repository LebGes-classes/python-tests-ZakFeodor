def check_types(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Оба аргумента должны быть int или float')


def add(a, b):
    check_types(a, b)

    return a + b


def subtract(a, b):
    check_types(a, b)

    return a - b


def multiply(a, b):
    check_types(a, b)

    return a * b


def divide(a, b):
    check_types(a, b)

    if b == 0:
        raise ZeroDivisionError('Нельзя делить на 0')

    return a / b

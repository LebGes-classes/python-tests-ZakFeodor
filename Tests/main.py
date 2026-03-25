def add(a, b):
    try:
        result = a + b

    except TypeError:
        return 'Оба числа должны иметь числовой тип'

    else:
        return result


def subtract(a, b):
    try:
        result = a - b

    except TypeError:
        return 'Оба числа должны иметь числовой тип'

    else:
        return result


def multiply(a, b):
    result = a * b

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('Оба числа должны иметь числовой тип')
    else:
        return result


def divide(a, b):
    try:
        result = a / b

    except TypeError:
        return 'Оба числа должны иметь числовой тип'

    except ZeroDivisionError:
        return 'Нельзя делить на 0'

    else:
        return result

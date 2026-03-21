from main import (
    add,
    subtract,
    multiply,
    divide
)
import pytest

inaccuracy = 10 ** -8


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, -5, -5),
    (-2, 5, 3),
    (-2.5, 4, 1.5),
    (-8, -1.4, -9.4),
    (8.2, -1.4, 6.8)
])
def test_add(a, b, expected):
    assert abs(add(a, b) - expected) < inaccuracy


@pytest.mark.parametrize("a,b,expected", [
    ('ads', 5, TypeError),
    ('3', '6', TypeError),
    (3.2, 'Bob', TypeError),
])
def test_add_non_int_or_float(a, b, expected):
    with pytest.raises(expected):
        add(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, -1),
    (0, -5, 5),
    (-2, 5, -7),
    (-2.5, 4, -6.5),
    (2.5, -4.4, 6.9),
    (-8, -1.4, -6.6),
    (8.2, -1.4, 9.6)
])
def test_subtract(a, b, expected):
    assert abs(subtract(a, b) - expected) < inaccuracy


@pytest.mark.parametrize("a,b,expected", [
    ('ads', 5, TypeError),
    ('3', '6', TypeError),
    (3.2, 'Bob', TypeError),
])
def test_subtract_non_int_or_float(a, b, expected):
    with pytest.raises(expected):
        subtract(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (0, -5, 0),
    (-2, 5, -10),
    (-2.5, 4, -10),
    (2.5, -4.4, -11),
    (-8, -1.4, 11.2),
    (8.2, -1.4, -11.48)
])
def test_multiply(a, b, expected):
    assert abs(multiply(a, b) - expected) < inaccuracy


@pytest.mark.parametrize("a,b,expected", [
    ('ads', 5, TypeError),
    ('3', '6', TypeError),
    (3.2, 'Bob', TypeError),
])
def test_multiply_non_int_or_float(a, b, expected):
    with pytest.raises(expected):
        multiply(a, b)


@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 1.5),
    (0, -5, 0),
    (-2, 5, -0.4),
    (-2.8, 4, -0.7),
    (8.8, -4.4, -2),
    (-15.68, -1.4, 11.2),
    (16.072, -1.4, -11.48)
])
def test_divide(a, b, expected):
    assert abs(divide(a, b) - expected) < inaccuracy


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize("a,b,expected", [
    ('ads', 5, TypeError),
    ('3', '6', TypeError),
    (3.2, 'Bob', TypeError),
])
def test_divide_non_int_or_float(a, b, expected):
    with pytest.raises(expected):
        divide(a, b)

from main import (
    add,
    subtract,
    multiply,
    divide
)
import unittest


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 6), 8)
        self.assertRaises(TypeError, add, 'a', 2)
        self.assertRaises(TypeError, add, 2.4, '2')

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(2, 6.5), -4.5)
        self.assertRaises(TypeError, subtract, 'a', 2)
        self.assertRaises(TypeError, subtract, 2.4, '2')

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(2.5, 6), 15)
        self.assertRaises(TypeError, multiply, 'a', 2)
        self.assertRaises(TypeError, multiply, 2.4, '2')

    def test_divide(self):
        self.assertEqual(divide(3, 2), 1.5)
        self.assertEqual(divide(1.5, 5), 0.3)
        self.assertRaises(TypeError, divide, 'a', 2)
        self.assertRaises(TypeError, divide, 2.4, '2')
        self.assertRaises(ZeroDivisionError, divide, 2, 0)


if __name__ == "__main__":
    unittest.main()

import unittest
from Assignment5 import assignment_5_Functions
class test_Functions(unittest.TestCase):
    def setUp(self):
        self.a = assignment_5_Functions()
    def test_fahrenheit_to_celcius(self):
        self.assertEqual(self.a.fahrenheit_To_Celsius(32), 0)
        self.assertEqual(self.a.fahrenheit_To_Celsius(212), 100)

    def test_fahrenheit_to_celsius_error(self):
        with self.assertRaises(TypeError):
            self.a.fahrenheit_To_Celsius("100F")

    def test_Fibonacci_Sequence(self):
        self.assertEqual(self.a.fibonacci_Sequence(0), 0)
        self.assertEqual(self.a.fibonacci_Sequence(1), 1)
        self.assertEqual(self.a.fibonacci_Sequence(10), 55)

    def test_Fibonaccie_Sequence(self):
        with self.assertRaises(ValueError):
            self.a.fibonacci_Sequence(-1)

if __name__ == '__main__':
    unittest.main()
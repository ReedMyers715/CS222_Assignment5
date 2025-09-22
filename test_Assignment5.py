import unittest
from Assignment5 import assignment_5_Functions
class test_Functions(unittest.TestCase):
    fahrenheit_input = int(input("Enter the temperature in fahrenheit: "))
    fibonacci_input = int(input("Enter a number in the fibonacci sequence: "))

    def setUp(self):
        self.a = assignment_5_Functions()
    def test_fahrenheit_to_celcius(self):
        self.assertEqual(self.a.fahrenheit_To_Celsius())
    def test_Fibonacci_Sequence(self):
        self.assertEqual(self.a.fibonacci_Sequence)
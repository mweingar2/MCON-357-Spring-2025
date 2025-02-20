import math
import unittest

from calculate_factorial import *


class MyTestCase(unittest.TestCase):

    def test_factorial_recursive_0(self):
        self.assertEqual(1, factorial_recursive(0))
    def test_factorial_recursive_1(self):
        self.assertEqual(1, factorial_recursive(1))  # add assertion here

    def test_process_input_negative_value(self):
        value, error_message = process_input("-7")
        self.assertIsNone(value)
        self.assertEqual(error_message, "Number cannot be negative")

    def test_process_input_fraction_value(self):
        value, error_message = process_input("3.5")
        self.assertIsNone(value)
        self.assertEqual("Number must be an integer", error_message)

    def test_factorial_recursive_with_positive_number(self):
        self.assertEqual(math.factorial(5), factorial_recursive(5))

    def test_factorial_recursive_number_larger_than_10(self):
        self.assertEqual(math.factorial(11), factorial_recursive(11))

    def test_handle_recursive_limit_with_number_right_before_recursion_limit(self):
        self.assertEqual(math.factorial(998), handle_recursive_limit(998))

    def test_handle_recursion_limit_with_number_at_recursion_limit(self):
        self.assertEqual(math.factorial(999), handle_recursive_limit(999))

    def test_handle_recursion_limit_with_number_after_recursion_limit(self):
        self.assertEqual(math.factorial(1000), handle_recursive_limit(1000))

if __name__ == '__main__':
    unittest.main()

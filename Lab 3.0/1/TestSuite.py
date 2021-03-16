# Implement Test functions for math.ceil()
# author: Saul DLD

import unittest
import math


class TestMathCeilSuite(unittest.TestCase):

    # Right: The ceil value of any number with decimals, rounds a number UP to the nearest integer
    # C: The ceil value uf any integer number is the same number
    def test_basic(self):
        self.assertTrue(math.ceil(1.1) == 2)
        self.assertEqual(math.ceil(4), 4)

    # B: Verify bigger or smallest numbers still complies rules
    def test_boundaries(self):
        # Neutral case
        self.assertEqual(math.ceil(0), 0)

        # Positive numbers
        self.assertEqual(math.ceil(-10000000001), -10000000001)
        self.assertEqual(math.ceil(-10000000001.1), -10000000001)

        # Negative numbers
        self.assertEqual(math.ceil(10000000001), 10000000001)
        self.assertEqual(math.ceil(10000000001.1), 10000000002)

    # I: The opposite operation of the ceil() function for a given number is floor() function
    # For en integer number (with no decimals) the ceil() and floor() function will return the same value
    # floor(x) == x == ceil(x)
    # For a number with decimals, the ceil() rounds a number UP to the nearest integer
    # For a number with decimals, the floor() rounds a number DOWN to the nearest integer
    # A decimal number should be lower than the ceil() value but greater than the floor() value
    # floor(x.y) < x.y < ceil(x.y)
    def test_inverse(self):
        self.assertEqual(math.ceil(4), math.floor(4))
        self.assertTrue(math.floor(4) < 4.3 < math.ceil(5))

    # E: Forcing error conditions
    # Strings are not allowed (even when the string is a number)
    @unittest.expectedFailure
    def test_string_not_allowed(self):
        math.ceil("1")

    # P: Math.ceil() performance is in charge of a third party developer (Python core)


if __name__ == '__main__':
    unittest.main()

"""
Sample test
"""


from django.test.testcases import SimpleTestCase
from app import calc


class CalcTestCase(SimpleTestCase):
    """
    Test case for calc module
    """

    def test_add_numbers(self):
        """
        Function to add two numbers
        """
        result = calc.add(5, 6)
        self.assertEqual(result, 11)

    def test_subtract_numbers(self):
        """
        Function to subtract two numbers
        """
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)

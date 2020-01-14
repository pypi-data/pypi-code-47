"""
Unitary testing for gpio_calculator.calculator

"""

import logging
from unittest import mock, TestCase

from gpio_calculator.calculator import Calculator


class TestCalculator(TestCase):

    def setUp(self):
        """
        Test setUp
        """
        self.calculator = Calculator()

    def test_get_pin(self):
        """Test the `Calculator.get_pin` method."""
        expected = "H18"
        obtained = self.calculator.get_pin(242)

        self.assertEqual(expected, obtained, msg="Expected: {}, Obtained: {}".format(expected, obtained))

    def test_get_pins(self):
        """Test the `Calculator.get_pins` method."""
        expected = {
            242: "H18",
            243: "H19"
        }
        obtained = self.calculator.get_pins([242, 243])

        self.assertEqual(expected, obtained, msg="Expected: {}, Obtained: {}".format(expected, obtained))

    def test_get_chardev(self):
        """Test the `Calculator.get_chardev` method."""
        expected = 242
        obtained = self.calculator.get_chardev("H", 18)

        self.assertEqual(expected, obtained, msg="Expected: {}, Obtained: {}".format(expected, obtained))

    def test_get_chardev_lowercase(self):
        """Test the `Calculator.get_chardev` method.

        Check that is converts the letter into uppercase.
        """
        expected = 242
        obtained = self.calculator.get_chardev("h", 18)

        self.assertEqual(expected, obtained, msg="Expected: {}, Obtained: {}".format(expected, obtained))

    def test_get_chardevs(self):
        """Test the `Calculator.get_chardevs` method."""
        expected = {
            "H18": 242,
            "H19": 243
        }
        obtained = self.calculator.get_chardevs(["H18", "H19"])

        self.assertEqual(expected, obtained, msg="Expected: {}, Obtained: {}".format(expected, obtained))

    def test_get_pin_from_string(self):
        """Test the `Calculator._get_pin_from_string` method."""

        expected = 18
        obtained = self.calculator._get_pin_from_string("H18")

        self.assertEqual(expected, obtained, msg="Expected: {}, Obtained: {}".format(expected, obtained))

    def test_get_pin_from_string_abnormal(self):
        """Test the `Calculator._get_pin_from_string` method.

        Abnormal case when value is not possible to be converted.
        """

        with self.assertRaises(ValueError):
            self.calculator._get_pin_from_string("HAX")

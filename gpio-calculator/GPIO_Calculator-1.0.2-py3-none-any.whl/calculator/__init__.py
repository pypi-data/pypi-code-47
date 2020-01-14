"""

formula:
chardev = (alphabet_letter - 1) * 32 + pin
"""
from string import ascii_uppercase


class Calculator:
    base = 32

    @staticmethod
    def __get_letter_index(letter):
        return [x for x in ascii_uppercase].index(letter) + 1

    @staticmethod
    def _get_pin_from_string(pin_string):
        """Retrieve the pin from a string.

        With a format like `H18` return the digits of it.

        Args:
            pin_string (str):

        Returns:
            (int) pin letter.
        """
        try:
            pin = int(pin_string[1:])

        except ValueError:
            raise ValueError(
                "Seems like {} cannot be translated into a pin.".format(pin_string[1:])
            )

        else:
            return pin

    @staticmethod
    def __get_letter_from_string(pin_string):
        """Retrieve the pin letter from a given string.

        Args:
            pin_string: string to get the letter from.

        Returns:
            (int) pin number.
        """
        return pin_string[0]

    def __guess_pin(self, chardev):
        """Guess the pin based on a chardev.

        Use the formula below in order to guess the pin
        looping through the letters.
        `pin = chardev - (32 * alphabet_letter) + 32`

        Returns:
            (list) possible_pins
        """
        possible_pins = list()

        for letter in ascii_uppercase:
            pin = chardev - (self.base * self.__get_letter_index(letter)) + self.base

            if self.get_chardev(letter, pin) == chardev and self.base >= pin >= 0:
                # Only append those that are below base and positive.
                possible_pins.append(pin)

        return possible_pins

    def get_pin(self, chardev):
        """Obtain a pin based on a chardev.

        Using the formula below obtain the pin number.
        `alphabet_letter = (chardev + 32 - pin) / 32`

        Returns:
            list with possible pins.
        """
        pins = self.__guess_pin(chardev)
        letters = [letter for letter in ascii_uppercase]

        combinations = list()

        for letter in letters:
            for pin in pins:

                if self.get_chardev(letter, pin) == chardev:
                    combinations.append("{letter}{pin}".format(letter=letter, pin=pin))

        if len(combinations) == 1:
            return combinations[0]

        else:
            return combinations

    def get_pins(self, input):
        """Get pins from list of chardev.

        Args:
            input (list): chardev to be converted.

        Returns:
            (dict) chardev: pin
        """
        pins = dict()

        for chardev in input:
            pins[chardev] = self.get_pin(chardev=chardev)

        return pins

    def get_chardev(self, letter, pin):
        """Calculate the chardev from a given letter and pin.

        Use the formula below to get the chardev with given pin and letter.
        `chardev = (alphabet_letter - 1) * 32 + pin`

        Returns:
            (int) chardev.
        """
        if letter.islower():
            letter = letter.upper()

        chardev = (self.__get_letter_index(letter) - 1) * self.base + pin

        return chardev

    def get_chardevs(self, input):
        """Get the chardev of given list of pins.

        Args:
            input (list): pins to get the chardev of.

        Returns:
            (dict) with the calculated chardevs.
        """

        chardevs = dict()

        for item in input:
            letter = self.__get_letter_from_string(item)
            pin = self._get_pin_from_string(item)
            chardevs[item] = self.get_chardev(letter, pin)

        return chardevs

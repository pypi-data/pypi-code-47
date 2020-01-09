from enum import IntFlag
from jdog.placeholder.faker import FakerPlaceholder


class NamePlaceholderOption(IntFlag):
    FULL_NAME = 1
    FIRST_NAME = 2
    LAST_NAME = 4
    GENDER_BOTH = 8
    GENDER_MALE = 16
    GENDER_FEMALE = 32


class NamePlaceholder(FakerPlaceholder):
    """Generates random name, with specified parameter it can be set to generate specific type of name"""

    def __init__(self, full_name, fake_provider, option=NamePlaceholderOption.FULL_NAME):
        """
        Parameters
        ----------
        full_name : str
            The full name, non parsed of placeholder
        fake_provider: Faker
            Faker object to generate name
        option: NamePlaceholderOption
            Indicates which kind of name should be generated and if gender matters
            Possible values are FULL_NAME, FIRST_NAME, LAST_NAME
            and for gender  GENDER_BOTH, GENDER_MALE or GENDER_FEMALE
            Combining first and latter is accepted. E.g. FULL_NAME + GENDER_MALE will
            generate male full names.
            FULL_NAME and GENDER_BOTH are default
        """
        super().__init__(full_name, [], fake_provider)
        self.option = option

    def exec(self):
        """
        :return: Name based on provided options.
        :rtype string
        """
        if NamePlaceholderOption.FIRST_NAME in self.option:
            return f'"{self._first_name()}"'
        elif NamePlaceholderOption.LAST_NAME in self.option:
            return f'"{self._last_name()}"'
        else:
            return f'"{self._name()}"'

    def _name(self):
        if NamePlaceholderOption.GENDER_MALE in self.option:
            return self.faker.name_male()
        elif NamePlaceholderOption.GENDER_FEMALE in self.option:
            return self.faker.name_female()
        else:
            return self.faker.name()

    def _first_name(self):
        if NamePlaceholderOption.GENDER_MALE in self.option:
            return self.faker.first_name_male()
        elif NamePlaceholderOption.GENDER_FEMALE in self.option:
            return self.faker.first_name_female()
        else:
            return self.faker.first_name()

    def _last_name(self):
        if NamePlaceholderOption.GENDER_MALE in self.option:
            return self.faker.last_name_male()
        elif NamePlaceholderOption.GENDER_FEMALE in self.option:
            return self.faker.last_name_female()
        else:
            return self.faker.last_name()

from AppleTrailersWrapper import LocaleHero


class LocaleHeros:
    def __init__(self, locales_dict: dict):
        self.locales_dict = locales_dict

    def list_locales(self):
        """
        gets a list of locate keys

        :return: list
        """
        return [key for key in self.locales_dict]

    def get_all_locales(self):
        """
        gets original locales dict

        :return: dict
        """
        return self.locales_dict

    def get_locale(self, locale: str):
        """
        Get a locale by key

        :param locale: the locale to get
        :return: Instance of LocaleHero
        :raises: Exception
        """
        try:
            return LocaleHero(self.locales_dict[locale])
        except KeyError:
            raise Exception("Invalid Locale!")
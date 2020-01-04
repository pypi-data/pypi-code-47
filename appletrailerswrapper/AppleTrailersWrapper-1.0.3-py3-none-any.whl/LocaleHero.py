class LocaleHero:
    def __init__(self, local_dict: dict):
        self.locale_dict = local_dict

    def get_locale_dict(self):
        """
        Returns the original local_dict

        :return: dict
        """
        return self.locale_dict

    def get_backgrounds(self):
        """
        Returns a list of json objects containing an imageurl key
        :return: list
        """
        return self.locale_dict["backgrounds"]

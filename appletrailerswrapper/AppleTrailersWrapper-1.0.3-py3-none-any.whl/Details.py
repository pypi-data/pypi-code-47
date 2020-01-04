import AppleTrailersWrapper


class Details:
    def __init__(self, details_dict: dict):
        self.details_dict = details_dict

    def get_details_dict(self):
        """
        gets the original details_dict

        :return: dict
        """
        return self.details_dict

    def get_official_url(self):
        """
        get official url

        :return: string
        """
        return self.details_dict["official_url"]

    def get_all_locale(self):
        """
        get all locale

        :return: dict
        """
        return self.details_dict["locale"]

    def get_locale(self, locale: str):
        """
        get locale by key

        :param locale: string
        :return: instance of Locale
        :raises: Exception
        """
        try:
            locale = self.details_dict["locale"][locale]
            return AppleTrailersWrapper.Locale(locale)
        except KeyError:
            raise Exception("Invalid Locale!")

    def get_genres(self):
        """
        Returns list of genres

        :return: list
        """
        return self.details_dict["genres"]

    def get_run_time(self):
        """
        Returns run time

        :return: string
        """
        return self.details_dict["run_time"]


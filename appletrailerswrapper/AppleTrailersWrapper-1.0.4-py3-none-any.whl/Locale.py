from AppleTrailersWrapper import CastCrew


class Locale:
    def __init__(self, locale_dict: dict):
        self.locale_dict = locale_dict

    def get_movie_title(self):
        """
        Returns the movie title

        :return: string
        """
        return self.locale_dict["movie_title"]

    def get_synopsis(self):
        """
        Returns synopsis

        :return: string
        """
        return self.locale_dict["synopsis"]

    def get_cast_and_crew(self):
        """
        Returns Instance of CastCrew class

        :return: Instance of CastCrew class
        """
        return CastCrew(self.locale_dict["castcrew"])


import requests

from AppleTrailersWrapper import Hero, Details, Related, Featured, LocaleHero, Reviews, Review, Clip
from AppleTrailersWrapper.Locale import Locale


class Title:
    def __init__(self, search_dict: dict):
        self.search_dict = search_dict
        self.title_dict = self.get_title()

    def get_search_dict(self):
        """
        Returns the search dict

        :return: dict
        """
        return self.search_dict

    def get_title_dict(self):
        """
        Returns the title dict

        :return: dict
        """
        return self.title_dict

    def get_title(self):
        """
        Returns the title json

        :return: dict
        :raises RequestException
        """
        location = self.search_dict["location"].replace("\/", "/")
        try:
            result = requests.get(f"https://trailers.apple.com{location}data/page.json")
            return result.json()
        except requests.exceptions.RequestException as e:
            raise e

    def get_movie_title(self):
        """
        Returns the movie title

        :return: string
        """
        return self.title_dict["page"]["movie_title"]

    def get_title_url(self):
        """
        Returns the titles page url

        :return: string
        """
        return self.title_dict["page"]["trailer_url"]

    def get_movie_rating(self):
        """
        Returns movie rating

        :return: string
        """
        return self.title_dict["page"]["movie_rating"]

    def get_release_date(self):
        """
        Returns release date

        :return: string
        """
        return self.title_dict["page"]["release_date"]

    def get_release_copy(self):
        """
        Returns release copy

        :return: string
        """
        return self.title_dict["page"]["release_copy"]

    def get_copyright(self):
        """
        Returns the copyright

        :return: string
        """
        return self.title_dict["page"]["copyright"]

    def get_all_heros(self):
        """
        Returns all heros

        :return: list of Hero class instances
        """
        heros = [Hero(self.title_dict["heros"][x]) for x in self.title_dict["heros"] if x != "locale"]
        return heros

    def get_hero(self, key: str):
        """
        Returns a hero dict by key

        :param key: string
        :return: instance of Hero
        :raises Exception
        """
        try:
            hero = self.title_dict["heros"][key]
            return Hero(hero)
        except KeyError:
            raise Exception("Invalid Hero")

    def get_locale_hero(self, key: str):
        """
        Returns a locale hero dict by key

        :param key: string
        :return: instance of LocaleHero
        :raises Exception
        """
        try:
            hero = self.title_dict["heros"]["locale"][key]
            return LocaleHero(hero)
        except KeyError:
            raise Exception("Invalid Hero")

    def get_showtimes(self):
        """
        Returns showtimes

        :return: list
        """
        return self.title_dict["showtimes"]

    def get_details(self):
        """
        get instance of Details class

        :return: instance of Details class
        """
        return Details(self.title_dict["details"])

    def get_related(self):
        """
        get list of instance of Related class

        :return: list of instances of Related class
        """
        return [Related(x) for x in self.title_dict["related"]["items"]]

    def get_featured(self):
        """
        get instance of Featured class

        :return: instance of Featured class
        """
        return Featured(self.title_dict["related"]["featured"])

    def get_reviews(self):
        """
        gets instance of Reviews class

        :return: instance of Reviews class
        """
        return Reviews(self.title_dict["reviews"])

    def get_review(self, review_index: int):
        """
        Gets a review by index

        :param review_index: int
        :return: instance of Review class
        :raises: Exception
        """
        try:
            review = Review(self.title_dict["reviews"]["reviews"][review_index])
            return review
        except KeyError:
            raise Exception("Invalid Review!")

    def get_clips(self):
        """
        gets list of all clips as instance of Clip class

        :return: list of instances of Clip class
        """
        return [Clip(clip_dict) for clip_dict in self.title_dict["clips"]]

    def get_clip(self, clip_index: int):
        """
        get a clip by index

        :param clip_index:
        :return: instance of Clip class
        :raises: Exception
        """
        try:
            clip = self.title_dict["clips"][clip_index]
            return Clip(clip)
        except KeyError:
            raise Exception("Invalid Clip!")

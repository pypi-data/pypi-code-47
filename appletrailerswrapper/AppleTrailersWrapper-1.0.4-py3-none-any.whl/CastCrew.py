class CastCrew:
    def __init__(self, castcrew_dict: dict):
        self.castcrew_dict = castcrew_dict

    def get_castcrew_dict(self):
        """
        Returns the original castcrew_dict

        :return: dict
        """
        return self.castcrew_dict

    def get_directors(self):
        """
        Returns list of directors

        :return: list
        """
        return self.castcrew_dict["directors"]

    def get_writers(self):
        """
        Returns list of writers

        :return: list
        """
        return self.castcrew_dict["writers"]

    def get_actors(self):
        """
        Returns list of actors

        :return: list
        """
        return self.castcrew_dict["actors"]

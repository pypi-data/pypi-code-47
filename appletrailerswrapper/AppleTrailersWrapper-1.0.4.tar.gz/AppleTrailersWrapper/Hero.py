class Hero:
    def __init__(self, hero_dict: dict):
        self.hero_dict = hero_dict

    def get_hero_dict(self):
        """
        get original hero_dict
        :return: dict
        """
        return self.hero_dict

    def get_image_url(self):
        """
        get image url

        :return: string
        """
        return self.hero_dict["imageurl"]

class Related:
    def __init__(self, related_item_dict: dict):
        self.related_item_dict = related_item_dict

    def get_item(self):
        """
        Returns the original related_item_dict

        :return: dict
        """
        return self.related_item_dict

    def get_thumbnail(self):
        """
        get thumbnail (full url to image)

        :return: string
        """
        return self.related_item_dict["thumb"]

    def get_itunes_link(self):
        """
        get itunes link

        :return: string
        """
        return self.related_item_dict["link"]

    def get_title(self):
        """
        get title

        :return: string
        """
        return self.related_item_dict["title"]

    def get_type(self):
        """
        get type

        :return: string
        """
        return self.related_item_dict["type"]

    def get_all_locale(self):
        """
        gets dict of all locale

        :return: dict
        """
        return self.related_item_dict["locale"]  # this is not returning a class because the dict is different from details locale

    def get_locale(self, locale: str):
        """
        Get dict of a local by key

        :param locale: string
        :return: dict
        :raises: Exception
        """
        try:
            locale = self.related_item_dict["locale"][locale]
            return locale
        except KeyError:
            raise Exception("Invalid Locale!")

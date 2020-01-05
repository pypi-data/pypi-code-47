class Featured:
    def __init__(self, featured_dict: dict):
        self.featured_dict = featured_dict

    def get_item(self):
        """
        Returns the original featured_dict
        :return: dict
        """
        return self.featured_dict

    def get_thumbnail(self):
        """
        get thumbnail (full url to image)

        :return: string
        """
        return self.featured_dict["thumb"]

    def get_itunes_link(self):
        """
        get itunes link

        :return: string
        """
        return self.featured_dict["link"]

    def get_title(self):
        """
        get title

        :return: string
        """
        return self.featured_dict["title"]

    def get_available_date(self):
        """
        gets the available date

        :return: string
        """
        return self.featured_dict["available_date"]

    def get_heading(self):
        """
        gets the heading

        :return: string
        """
        return self.featured_dict["heading"]

    def get_locale(self):
        """
        gets locale dict

        :return: dict
        """
        return self.featured_dict["locale"]  # this is not returning a class because the dict is different from details locale

class Review:
    def __init__(self, review_dict: dict):
        self.review_dict = review_dict

    def get_text(self):
        """
        get review text

        :return: string
        """
        return self.review_dict["copy"]

    def get_reviewer(self):
        """
        get reviewer name

        :return: name
        """
        return self.review_dict["reviewer"]

    def get_publisher(self):
        """
        get publisher name

        :return: string
        """
        return self.review_dict["publisher"]

    def get_date(self):
        """
        get date

        :return: string
        """
        return self.review_dict["date"]

    def get_rating(self):
        """
        gets rating

        :return: string
        """
        return self.review_dict["rated"]

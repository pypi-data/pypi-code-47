from AppleTrailersWrapper.Review import Review


class Reviews:
    def __init__(self, reviews_dict: dict):
        self.reviews_dict = reviews_dict

    def get_reviews_dict(self):
        return self.reviews_dict

    def get_rating(self):
        return self.reviews_dict["rating"]

    def get_count(self):
        """
        get total reviews

        :return: int
        """
        return self.reviews_dict["count"]

    def get_positive(self):
        """
        get positive count

        :return: int
        """
        return self.reviews_dict["positive"]

    def get_negative(self):
        """
        gets negative count

        :return: int
        """
        return self.reviews_dict["negative"]

    def get_average(self):
        """
        get average

        :return: string
        """
        return self.reviews_dict["average"]

    def is_fresh(self):
        """
        get is_fresh

        :return: boolean
        """
        return self.reviews_dict["is_fresh"]

    def get_rotten_tomatoes_link(self):
        """
        get rotten tomato link

        :return: string
        """
        return self.reviews_dict["rt_link"]

    def get_review(self, review_index):
        """
        get review by index

        :param review_index: int
        :return: instance of Review class
        :raises: Exception
        """
        try:
            review = Review(self.reviews_dict["reviews"][review_index])
            return review
        except KeyError:
            raise Exception("Invalid Review!")

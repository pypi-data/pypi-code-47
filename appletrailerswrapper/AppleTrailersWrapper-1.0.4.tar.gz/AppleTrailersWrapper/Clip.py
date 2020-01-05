from AppleTrailersWrapper.ClipVersion import ClipVersion


class Clip:
    def __init__(self, clip_dict: dict):
        self.clip_dict = clip_dict

    def get_clip_dict(self):
        """
        get original clip_dict

        :return: dict
        """
        return self.clip_dict

    def get_title(self):
        """
        get title

        :return: stirng
        """
        return self.clip_dict["title"]

    def get_screenshot(self):
        """
        get screenshot (full url to image)

        :return: string
        """
        return self.clip_dict["screen"]

    def get_thumbnail(self):
        """
        get thumbnail (full url to image)

        :return: string
        """
        return self.clip_dict["thumb"]

    def get_runtime(self):
        """
        get runtime

        :return: string
        """
        return self.clip_dict["runtime"]

    def get_kind(self):
        """
        get kind

        :return: string
        """
        return self.clip_dict["kind"]

    def get_artist(self):
        """
        get artist

        :return: string
        """
        return self.clip_dict["artist"]

    def get_faded(self):
        """
        get faded

        :return: string
        """
        return self.clip_dict["faded"]

    def get_posted(self):
        """
        get posted date

        :return: string
        """
        return self.clip_dict["posted"]

    def get_all_locale(self):
        """
        get all locale

        :return: dict
        """
        return self.clip_dict["locale"]

    def get_locale(self, locale: str):
        """
        get locale dict by key

        :param locale: string
        :return: dict
        :raises: Exception
        """
        try:
            locale = self.clip_dict["locale"][locale]
            return locale
        except KeyError:
            raise Exception("Invalid Locale!")

    def get_versions(self):
        """
        gets list of instances to ClipVersion class

        :return: list of ClipVersion
        """
        return [ClipVersion(self.clip_dict["versions"]["enus"]["sizes"][clip_version]) for clip_version in self.clip_dict["versions"]["enus"]["sizes"]]

    def get_version(self, version):
        """
        Gets a version by key

        :param version: string
        :return: dict
        :raises: Exception
        """
        try:
            version = self.clip_dict["versions"]["enus"]["sizes"][version]
            return ClipVersion(version)
        except KeyError:
            raise Exception("Invalid Clip Version!")

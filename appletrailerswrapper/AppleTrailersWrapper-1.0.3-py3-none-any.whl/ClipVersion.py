class ClipVersion:
    def __init__(self, clip_version_dict: dict):
        self.clip_version_dict = clip_version_dict

    def get_clip_version_dict(self):
        """
        get original clip_version_dict
        :return: dict
        """
        return self.clip_version_dict

    def get_name(self):
        """
        get name

        :return: string
        """
        return self.clip_version_dict["name"]

    def get_src(self):
        """
        get src url
        :return: string
        """
        return self.clip_version_dict["src"]

    def get_src_alt(self):
        """
        get src alt url

        :return: string
        """
        return self.clip_version_dict["srcAlt"]

    def get_height(self):
        """
        get height

        :return: string
        """
        return self.clip_version_dict["height"]

    def get_width(self):
        """
        get width

        :return: int
        """
        return self.clip_version_dict["width"]

    def get_filename(self):
        """
        get filename

        :return: string
        """
        return self.clip_version_dict["filename"]

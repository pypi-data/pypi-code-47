"""
polyquack translation utilities
"""
from typing import List


def get_closest_translation(
    wanted: str,
    target: dict,
    default: str = None,
    match_level: str = None,
    suppress_errors: bool = False,
) -> dict:
    """
    Function to get the best translation from a dictionary with locales as keys.

    Args:
        - wanted: preferred locale string (e.g. "en-us")
        - target: a dict with languaged keyed translation strings, e.g.
              { "en-ca": "Post title", "es-mx": "Título de la entrada" }
        - default: str - the default language to return if others fail (and possible), e.g. "en-us"
        - match_level: str
            - "exact": match only the exact language and locale
            - "language": match only the exact language, but accept country variations,
              e.g. requesting "en-us" might match and return "en-ca"
            - "default": allows returning default language, if passed (this option is the
              default and can be omitted), e.g. requesting "zh-cn" mighr default to "en-us"

    Returns:
        dict with the matched language's key, and the translated text, e.g.
        { matched_key: "en-ca", "text": "Post title" }

    Raises:
        - KeyError if the selected translation cannot be found (can be disabled with `suppress_errors = True`,
          in which case, you should check the returned dict for `matched_key is None`)
    """
    # Exact match
    if wanted in target:
        return {"matched_key": wanted, "text": target[wanted]}

    if match_level in [None, "language", "default"]:
        # Match language without the locale
        language, *_ = wanted.split("-", 1)
        for key in target.keys():
            key_language, *_ = key.split("-", 1)
            if language == key_language:
                return {"matched_key": key, "text": target[key]}
        # Return default language
        if default is not None and match_level in [None, "default"]:
            if default in target:
                return {"matched_key": default, "text": target[default]}

    # If all fails, return or raise an error
    if suppress_errors:
        return {"matched_key": None, "text": "Could not get field translation."}
    raise KeyError(f"Language {wanted} was not found in {list(target.keys())}.")


def get_text_from_translation(translation: dict) -> str:
    return translation["text"]


class Translatable:
    """
    This class can be used for translatable words, sentences, or texts.
    """

    def __init__(
        self, translations: dict = None, match_level: str = None, default: str = None
    ) -> None:
        """
        Args:
            - translations: a dict of mappings
            - match_level: a str, as in get_closest_translation()
            - default: default locale to return if applicable, as in get_closest_translation()
        """
        if translations is None:
            raise ValueError(
                "`translations` argument is required for Translatable class."
            )
        self.translations = translations
        self.match_level = match_level
        self.default_language = default

    def get_languages(self) -> List[str]:
        """
        Return a list of languages fromas per self.translations.keys()
        """
        return list(self.translations.keys())

    def translate(self, language: str) -> str:
        """
        Method to return the translated string.

        Args:
            - language: the language code for which to get the translation, e.g. "en-ca"

        Returns:
            str with the value matching the chosen language if possible

        Raises:
            - KeyError if string could not be translated
        """
        return get_text_from_translation(
            get_closest_translation(
                language,
                self.translations,
                match_level=self.match_level,
                default=self.default_language,
            )
        )


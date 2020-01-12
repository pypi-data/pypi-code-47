"""
polyquack pluralization utilities.
"""
from typing import List

from .rules import FORMS_BY_RULE, PLURALIZATION_BY_LANGUAGE


def get_rule_number_from_language_code(language_code: str) -> int:
    """
    This function returns the appropriate pluralization rule number from the provided language code.

    Args:
        - language_code (str): the language code for which to get the rule number. It should be in ISO
          639-1 format if available (e.g. "en", or "zh"), or ISO 639-2 for languages that are not listed
          in 639-1 (e.g. "frr"). Country codes can be used for words with different spellings (e.g.
          tire/tyre, or whisky/whiskey).

          Note that according to the MDN, Brazilian Portuguese differs from Portuguese, so "pt" and "pt-pt"
          use rule 1, whereas "pt-br" uses rule 2. Brazilian Portuguese is currently the only case where a
          country code should be provided.

          If you pass a code with a country locale, the function will extract the language from it whenever
          possible (e.g. "en-ca" or "en-us" will both be treated the same as "en").

          The language_code is case-insensitive (e.g. "EN" will be treated the same as "en").

    Returns:
        rule_number (int): the index of the rule to use.
    """
    lower_code = language_code.lower()

    # Exact match
    if lower_code in PLURALIZATION_BY_LANGUAGE.keys():
        return PLURALIZATION_BY_LANGUAGE[lower_code]

    # If user passed a country variation
    split_code, *_ = lower_code.split("-")
    if split_code in PLURALIZATION_BY_LANGUAGE.keys():
        return PLURALIZATION_BY_LANGUAGE[split_code]

    raise ValueError(f"{language_code} is not a supported language code.")


def get_form_from_rule(rule_number: int, count: int) -> int:
    """
    This function returns the index of the appropriate form based on the chosen rule.

    Args:
        - rule_number (int): the index of the rule to use. See PLURALIZATION_BY_LANGUAGE in the rules module.
        - count (int): the number on which to base the form. For instance, to pluralize "zero songs", pass a
          count of 0. To pluralize "trzy piosenki", pass a count of 3. To pluralize "une chanson", pass a
          count of 1.

    Returns:
        - rule_form (int): the index of the tokenized string to return. For instance, with the Polish
          language (rule 9) translation string "piosenka;piosenki;piosenek", a count of 1 would return form 0
          (piosenka), a count of 3 would return form 1 (piosenki), and a count of 30 would return form 2
          (piosenek).
    """
    if rule_number in FORMS_BY_RULE.keys():
        return FORMS_BY_RULE[rule_number](count)

    # Oops, didn't implement this rule yet
    raise NotImplementedError(f"Rule #{rule_number} could not be found.")


def get_plural_form(form_number: int, forms: List[str]) -> str:
    """
    This function returns the selected plural form from a list of forms.

    Args:
        - form_number (int): the index of the form to use. This can usually be retrieved by using the
          get_form_from_rule function.
        - forms (list): a list of forms (e.g. ["song", "songs"] for English, which uses rule 1 (2 forms), or
          ["piosenka", "piosenki", "piosenek"] for Polish, which uses rule 9 (3 forms).)

    Returns:
        - plural_form (str): the selected plural form. Note that the term "plural" here does not imply that
          the word will necessarily be plural in the sense that there are many of the same object... Some
          languages only have one form regardless of count, and in other languages, this function may return
          the singular form (e.g. English language with the form for a count of 1).
    """
    # Make sure the selected form is valid
    if form_number >= len(forms):
        raise IndexError(
            f"Error getting form {form_number} from forms with len({len(forms)}. Please verify your forms list.)"
        )

    return forms[form_number]


class Pluralizable:
    """
    This class can be used for translatable and/or pluralizable words.
    """

    def __init__(self, forms=None):
        """
        Args:
            - forms: a dict of form mappings with languages as keys.

        Example args:
            forms = {
                "en": ["song", "songs"],
                "pl": ["piosenka", "piosenki", "piosenek"],
            }
        """
        if forms is None:
            raise ValueError("`forms` argument is required for Pluralizable class.")
        self.forms = forms

    def get_languages(self) -> List[str]:
        """
        Return a list of languages, as per self.forms.keys()
        """
        return list(self.forms.keys())

    def pluralize_by_language(self, language_code: str, count: int) -> str:
        """
        Return the appropriately pluralized form for langue {language_code} based on {count}.
        """
        rule_number = get_rule_number_from_language_code(language_code)
        form_number = get_form_from_rule(rule_number, count)
        return get_plural_form(form_number, self.forms[language_code])

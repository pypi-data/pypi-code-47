"""
main
"""

import re


def string_validation(func):
    def wrapper(param):
        if not param:
            return("Enter the string to convert..")
        else:
            return (func(str(param)))
    return (wrapper)


@string_validation
def camelcase(string):
    """ Convert string into camel case.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Camel case string.
        failure:
            string: Enter the string to convert..
    """

    string = re.sub(r"^[\-_\.]+", '', str(string))
    return string[0].lower() + re.sub(r"[\-_\.\s]([a-z])",
                        lambda matched: uppercase(matched.group(1)),
                        string[1:]
                )


@string_validation
def capitalcase(string):
    """Convert string into capital case.
    First letters will be uppercase.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Capital case string.
        failure:
            string: Enter the string to convert..
    """

    return string.capitalize()


@string_validation
def constcase(string):
    """Convert string into upper snake case.
    Join punctuation with underscore and convert letters into uppercase.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Const cased string.
        failure:
            string: Enter the string to convert..
    """

    return uppercase(snakecase(string))


@string_validation
def lowercase(string):
    """Convert string into lower case.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Lowercase case string.
        failure:
            string: Enter the string to convert..
    """

    return string.lower()


@string_validation
def pascalcase(string):
    """Convert string into pascal case.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Pascal case string.
        failure:
            string: Enter the string to convert..
    """

    return capitalcase(camelcase(string))


@string_validation
def pathcase(string):
    """Convert string into path case.
    Join punctuation with slash.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Path cased string.
        failure:
            string: Enter the string to convert..
    """
    string = snakecase(string)
    return re.sub(r"_", "/", string)


@string_validation
def backslashcase(string):
    """Convert string into spinal case.
    Join punctuation with backslash.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Spinal cased string.
        failure:
            string: Enter the string to convert..
    """
    str1 = re.sub(r"_", r"\\", snakecase(string))

    return str1
    # return re.sub(r"\\n", "", str1))  # TODO: make regex fot \t ...


@string_validation
def sentencecase(string):
    """Convert string into sentence case.
    First letter capped and each punctuations are joined with space.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Sentence cased string.
        failure:
            string: Enter the string to convert..
    """
    joiner = ' '
    string = re.sub(r"[\-_\.\s]", joiner, string)
    return capitalcase(trimcase(
        re.sub(r"[A-Z]", lambda matched: joiner +
                                         lowercase(matched.group(0)), string)
    ))


@string_validation
def snakecase(string):
    """Convert string into snake case.
    Join punctuation with underscore
    Args:
        string: String to convert.
    Returns:
        output:
            string: Snake cased string.
        failure:
            string: Enter the string to convert..
    """

    string = re.sub(r"[\-\.\s]", '_', string)
    return string[0].lower() + re.sub(r"[A-Z]",
                        lambda matched: '_' + matched.group(0).lower(),
                        string[1:]
        )


@string_validation
def spinalcase(string):
    """Convert string into spinal case.
    Join punctuation with hyphen.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Spinal cased string.
        failure:
            string: Enter the string to convert..
    """

    return re.sub(r"_", "-", snakecase(string))


@string_validation
def dotcase(string):
    """Convert string into dot case.
    Join punctuation with dot.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Dot cased string.
        failure:
            string: Enter the string to convert..
    """

    return re.sub(r"_", ".", snakecase(string))


@string_validation
def titlecase(string):
    """Convert string into sentence case.
    First letter capped while each punctuations is capitalsed
    and joined with space.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Title cased string.
        failure:
            string: Enter the string to convert..
    """

    return ' '.join(
        [capitalcase(word) for word in snakecase(string).split("_")]
    )


@string_validation
def trimcase(string):
    """Convert string into trimmed string.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Trimmed case string
        failure:
            string: Enter the string to convert..
    """

    return string.strip()


@string_validation
def uppercase(string):
    """Convert string into upper case.
    Args:
        string: String to convert.
    Returns:
        output:
            string: Uppercase case string.
        failure:
            string: Enter the string to convert..
    """

    return string.upper()


@string_validation
def alphanumcase(string):
    """Cuts all non-alphanumeric symbols,
    i.e. cuts all expect except 0-9, a-z and A-Z.
    Args:
        string: String to convert.
    Returns:
        output:
            string: String with cutted non-alphanumeric symbols.
        failure:
            string: Enter the string to convert..
    """
    
    return ''.join(filter(str.isalnum, str(string)))

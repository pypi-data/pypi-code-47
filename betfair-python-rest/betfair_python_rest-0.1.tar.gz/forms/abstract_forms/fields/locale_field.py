from dataclasses import dataclass


@dataclass
class LocaleField:
    '''
    The language used for the response.
    If not specified, the default is returned.
    '''
    locale: str = None

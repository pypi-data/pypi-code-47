import requests
import io
from .utils import parse_response

LANGUAGE = [
    "cat", "deu", "eng", "fin", "hat", "hun", "ita", "mlt", "nld", "nze",
    "pol", "aus-AU", "afr-ZA", "sqi-AL", "eus-ES", "eus-FR", "cat-ES",
    "cze-CZ", "nld-NL", "eng-US", "eng-AU", "eng-GB", "eng-NZ", "ekk-EE",
    "fin-FI", "fra-FR", "kat-GE", "deu-DE", "gsw-CH-BE", "gsw-CH-BS",
    "gsw-CH-GR", "gsw-CH-SG", "gsw-CH-ZH", "gsw-CH", "hat-HT", "hun-HU",
    "ita-IT", "jpn-JP", "gup-AU", "ltz-LU", "mlt-MT", "nor-NO", "pol-PL",
    "ron-RO", "rus-RU", "slk-SK", "spa-ES", "swe-SE", "tha-TH", "guf-AU", "und"
]
OUTFORMAT = [
    "txt", "tab", "exttab", "lex", "extlex", "bpf", "bpfs", "extbpf",
    "extbpfs", "tcf", "exttcf", "tg", "exttg"
]


def g2p(text, language, outformat):
    assert isinstance(text, str)
    assert language in LANGUAGE
    assert outformat in OUTFORMAT

    files = {
        'i': ('file.txt', text),
        'lng': (None, language),
        'oform': (None, outformat),
    }

    response = requests.post(
        'https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/runG2P',
        files=files)
    return parse_response(response)
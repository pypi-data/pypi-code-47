import requests
from .utils import parse_response

LANGUAGE = [
    "aus-AU", "afr-ZA", "eus-ES", "eus-FR", "cat-ES", "nld-BE", "nld-NL",
    "eng-US", "eng-AU", "eng-GB", "eng-SC", "eng-NZ", "ekk-EE", "fin-FI",
    "fra-FR", "kat-GE", "deu-DE", "gsw-CH", "gsw-CH-BE", "gsw-CH-BS",
    "gsw-CH-GR", "gsw-CH-SG", "gsw-CH-ZH", "hun-HU", "ita-IT", "jpn-JP",
    "sampa", "ltz-LU", "mlt-MT", "nor-NO", "pol-PL", "por-PT", "ron-RO",
    "rus-RU", "spa-ES", "swe-SE", "tha-TH"
]
OUTFORMAT = ["par", "bpf", "csv", "mau", "TextGrid", "emuDB", "eaf", "exb"]
MODUSES = ["standard", "align"]


def maus(signal, bpf, language, modus, outformat):
    assert language in LANGUAGE
    assert outformat in OUTFORMAT
    assert modus in MODUSES

    files = {
        'SIGNAL': ('file.wav', signal),
        'BPF': ('file.par', bpf),
        'LANGUAGE': (None, language),
        'MODUS': (None, modus),
        'OUTFORMAT': (None, outformat),
    }

    response = requests.post(
        'https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/runMAUS',
        files=files)
    return parse_response(response)
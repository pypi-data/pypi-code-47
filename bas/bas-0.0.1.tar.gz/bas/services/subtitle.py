import requests
from .utils import parse_response

OUTFORMAT = ["srt", "sub", "bpf+trn"]
MARKER = ["punct", "newline", "tag"]


def subtitle(transcription, bpf, maxlength, marker, outformat):
    assert maxlength >= 0 and maxlength <= 999.0
    assert marker in MARKER
    assert outformat in OUTFORMAT

    files = {
        'transcription': ('file.txt', transcription),
        'bpf': ('file.par', bpf),
        'maxlength': (None, maxlength),
        'marker': (None, marker),
        'outformat': (None, outformat),
    }

    response = requests.post(
        'https://clarin.phonetik.uni-muenchen.de/BASWebServices/services/runSubtitle',
        files=files)
    return parse_response(response)
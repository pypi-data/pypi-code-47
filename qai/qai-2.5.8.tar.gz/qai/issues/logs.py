import nltk
from qai.issues.add_issues import parse_new_format, parse_old_format

def get_payload_stats(json_data):

    try:
        _ = json_data.items()
        els = [json_data]
    except AttributeError:
        els = json_data

    n_seg = len(els) if els else 0
    n_sent = 0
    n_word = 0

    try:
        for el in els:
            try:
                segment,_,_ = parse_new_format(el)
            except:
                segment,_,_ = parse_old_format(el)
            
            n_sent += len(nltk.sent_tokenize(segment))
            n_word += len(segment.split())
    except:
        # this will cause escaped exception in sanic logger
        # do nothing
        pass

    return n_seg, n_sent, n_word

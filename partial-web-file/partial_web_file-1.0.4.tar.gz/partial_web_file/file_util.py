import logging
import requests


log = logging.getLogger('partial_web_file')

session = requests.Session()

def get_partial_web_file(url, start_position, length):
    headers = {"Range": "bytes=%d-%d" % (start_position, start_position + length - 1)}
    r = session.get(url, headers=headers)
    data = r.content
    data_len = len(data)
    if data_len != length:
        log.warning(
            'Web returned %d while asked only for %d... Does this Web server support the "Range" header?'
            % (data_len, length)
        )
        return data[start_position:start_position + length]
    else:
        return data

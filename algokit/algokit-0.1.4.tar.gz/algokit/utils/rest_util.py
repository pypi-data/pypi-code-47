import urllib
from urllib import parse
from urllib.request import urlopen


def post(url, params):
    data = parse.urlencode(params).encode("utf-8")
    request = urllib.request.Request(url=url, data=data)
    res = urlopen(request)
    return res.read().decode("utf-8")


def get(url, params):
    data = parse.urlencode(params)
    url = url + "?" + data
    res = urlopen(url)
    return res.read().decode("utf-8")


if __name__ == '__main__':
    parmas = {}
    print(parse.urlencode(parmas))

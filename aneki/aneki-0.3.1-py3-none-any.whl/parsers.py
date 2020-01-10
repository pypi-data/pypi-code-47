import requests as rq
import html
import re
import random
import os


class Parser():
    def __init__(self):
        self.url = 'https://github.com/'

    def _request_html(self, url, verify=True):
        headers = {'user-agent': 'usr agnt'}
        try:
            res = rq.request('GET', url=url, verify=verify, headers=headers)
        except (rq.exceptions.ConnectionError, rq.exceptions.ContentDecodingError):
            return -1, ''
        return res.status_code, res.text

    def get_text(self, url):
        return self._request_html(url)

    def ping(self):
        res, text = self.get_text(self.url)
        if res == 200:
            return True
        return False


class Bash(Parser):
    def __init__(self):
        self.url = 'https://bash.im/'

    def get_text(self, url):
        return self._request_html(url)

    def clear_anek(self, text):
        start = text.find('#21201e">') + 9
        end = text.find('/div>')
        text = text[start: end] + 'br>'
        text = text.replace("<' + 'br>", '\n')
        text = text.replace("<' + 'br />", '\n')
        text = html.unescape(text)
        return text

    def get_url(self):
        return 'https://bash.im/forweb/?u'

    def get_anek(self):
        res, raw = self.get_text(self.get_url())
        max_tries = 5
        while res != 200 and max_tries > 0:
            res, raw = self.get_text(self.get_url())
            max_tries -= 1
        if max_tries == 0:
            return -1
        text = self.clear_anek(raw)[:-1]
        return text

    def get_name(self):
        return 'Bash.im'


class AnekdotRu(Parser):
    def __init__(self):
        self.possible_tags = [  # repeats for frequency adjustment
            'apple',
            'telegram',
            'windows',
            'Билл Гейтс',
            'ии',
            'ии',
            'интернет',
            'интернет',
            'интернет',
            'программист'
            'программист'
            'программист'
        ]
        self.url = 'https://pda.anekdot.ru'

    def get_text(self, url):
        return self._request_html(url)

    def clear_anek(self, anek):
        anek = anek[13:-6]
        anek = anek.replace('<br>  ', ' ')
        anek = anek.replace('<br>-', '\n-')
        anek = anek.replace('<br>', ' ')
        anek = html.unescape(anek)
        return anek

    def get_url(self):
        tag = self.possible_tags[random.randint(0, len(self.possible_tags) - 1)]
        page = random.randint(1, 5)
        url = 'https://pda.anekdot.ru/tags/{}/{}?type=anekdots&sort=sum'.format(tag, page)
        return url

    def get_anek(self):
        res, raw = self.get_text(self.get_url())
        max_tries = 5
        while res != 200 and max_tries > 0:
            res, raw = self.get_text(self.get_url())
            max_tries -= 1
        if res != 200:
            return -1
        alls = re.findall('class="text">.*?</div>', raw)
        alls = [self.clear_anek(anek) for anek in alls]
        if len(alls) == 0:
            return -1
        elif len(alls) == 1:
            return alls[0]
        else:
            anek_number = random.randint(0, len(alls) - 1)
            return alls[anek_number]

    def get_name(self):
        return 'anekdot.ru'


class Nekdo(Parser):
    def __init__(self):
        self.possible_tags = [
            'internet',
            'life',
        ]
        self.url = 'https://nekdo.ru'

    def get_text(self, url):
        return self._request_html(url)

    def clear_anek(self, anek):
        anek = anek[3:-6]
        anek = anek.replace('<br>', '\n')
        anek = html.unescape(anek)
        return anek

    def get_url(self):
        tag = self.possible_tags[random.randint(0, len(self.possible_tags) - 1)]
        page = random.randint(1, 80)  # 80 - last page for internet
        url = 'https://nekdo.ru/{}/{}'.format(tag, page)
        return url

    def get_anek(self):
        res, raw = self.get_text(self.get_url())
        max_tries = 5
        while res != 200 and max_tries > 0:
            res, raw = self.get_text(self.get_url())
            max_tries -= 1
        if res != 200:
            return -1
        alls = re.findall('[0-9]">.*?</div>', raw)  # anek
        alls = [self.clear_anek(anek) for anek in alls]
        cats = re.findall('<div class="cat">.*?</div>', raw)  # anek's categories
        ban = ['policy' in cat or 'vulgar' in cat or 'religion' in cat or 'national' in cat for cat in cats]
        if len(alls) == 0:
            return -1
        elif len(alls) == 1:
            return alls[0]
        else:
            anek_number = random.randint(0, len(alls) - 1)
            max_tries = 20
            while ((len(alls[anek_number]) < 5 or ban[anek_number] is True) and max_tries > 0):
                anek_number = random.randint(0, len(alls) - 1)
                max_tries -= 1
            return alls[anek_number]

    def get_name(self):
        return 'nekdo.ru'


class ShytokNet(Parser):
    def __init__(self):
        self.possible_tags = [  # repeats for frequency adjustment
            'anekdots-pro-programmistov',
            'anekdots-pro-programmistov',
            'anekdots-pro-brauzeri',
            'kompjuternye-anekdoty',
            'kompjuternye-anekdoty',
            'kompjuternye-anekdoty',
            'anekdots-pro-komputer',
            'anekdots-pro-komputer',
            'anekdots-pro-komputer',
        ]
        self.url = 'https://shytok.net/'

    def get_text(self, url):
        this_dir, this_filename = os.path.split(__file__)
        cert_path = os.path.join(this_dir, 'shytok_net.cert')
        return self._request_html(url, verify=cert_path)

    def clear_anek(self, anek):
        anek = anek[15:-14]
        anek = anek.replace('<br />', '<br>')
        anek = anek.replace('<br>', '\n')
        anek = html.unescape(anek)
        return anek

    def get_url(self):
        tag = self.possible_tags[random.randint(0, len(self.possible_tags) - 1)]
        page = random.randint(1, 20)
        url = 'https://shytok.net/anekdots/{}-{}.html'.format(tag, page)
        return url

    def get_anek(self):
        res, raw = self.get_text(self.get_url())
        max_tries = 5
        while res != 200 and max_tries > 0:
            res, raw = self.get_text(self.get_url())
            max_tries -= 1
        if res != 200:
            return -1
        raw = raw.replace('<br />\r\n', '<br>')
        raw = raw.replace('<br />\r', '<br>')
        raw = raw.replace('<br />\n', '<br>')
        alls = re.findall('"text">.*?</div>', raw)
        alls = [self.clear_anek(anek) for anek in alls]
        if len(alls) == 0:
            return -1
        elif len(alls) == 1:
            return alls[0]
        else:
            anek_number = random.randint(0, len(alls) - 1)
            max_tries = 20
            while len(alls[anek_number]) < 5 and max_tries > 0:
                anek_number = random.randint(0, len(alls) - 1)
                max_tries -= 1
            return alls[anek_number]

    def get_name(self):
        return 'shytok.net'

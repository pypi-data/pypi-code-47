from webgatewayapi.tools import mergeDict
from collections import OrderedDict

import urllib.parse

class process(object):
    """
    process class object will process the list data extracted from MWG servers, Each function has a specific operation.
    This class require data initializer, which pass the particulars to call any methods available.
    """

    def __init__(self, data):
        self.data = data


    def isFeedData(self):
        return 'feed' in self.data

    def processPages(self):
        """
            processPages will generate list of remaining pages.
        :return: number of remaining pages.
        """
        d = self.data['feed']['link']
        f, l = None, None
        if len(d) is not 1:
            for i in d:
                n = urllib.parse.urlparse(i['@href']).query
                n = int(urllib.parse.parse_qs(n)['page'][0])
                if i['@rel'] == 'first':
                    f = n
                if i['@rel'] == 'last':
                    l = n
        if f + 1 == l:
            out = [f]
        else:
            out = list(range(f + 1, l))
        return out

    def processList(self):
        out = {}
        out['source'] = self.data['feed']['title']
        out['data'] = self.processListEntry()
        return out

    def processListCombine(self):
        out = {'data': {}}
        for item in self.data:
            out['source'] = item['source']
            out['data'] = mergeDict(out['data'], item['data'])
        return out

    def processListEntry(self):
        o = {}
        for e in self.data['feed']['entry']:
            tag = e['id']
            o[tag] = {}
            o[tag]['title'] = e['title']
            o[tag]['type'] = e['listType']
        return o

    def processListID(self):
        """
            processListID will take the class data as self variable, that can parse and
        :return: list attributes accordingly.
        """
        out = {'data': {}}
        d = self.data['entry']
        out['source'] = d['id']
        out['title'] = d['title']
        out['type'] = d['type']
        out['listType'] = d['listType']
        if d['content']['list']['content'] is None:
                return d['title']

        elif isinstance(d['content']['list']['content']['listEntry'], OrderedDict):
                e = d['content']['list']['content']['listEntry']["entry"]
                d = d['content']['list']['content']['listEntry']["description"]
                out['data'][e] = d
                return out
        else:
                for item in d['content']['list']['content']['listEntry']:
                    e = item['entry']
                    d = item['description']
                    out['data'][e] = d
                return out








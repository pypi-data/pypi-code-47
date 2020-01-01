import json

import Levenshtein


class SubdistrictPayload:

    def __init__(self, lang):
        pass

    @classmethod
    def load_subdistricts(cls, lang='id', filename=None):
        if filename is None:
            path = "{}-{}.json".format("subdistricts", lang)
        else:
            path = filename

        with open(path) as json_file:
            data = json.load(json_file)
        return data


class AddressChecker:

    def __init__(self, string_matics=None):
        self.string_matrics = string_matics or Levenshtein

    def get_sim_subdistrict(self, keyword, subdistricts, count=10):
        '''
            get list subdistricts with scored by subdistrict
        :param keyword: your subdistrict name
        :param subdistricts: list of subdistrict please reference this file
        :param count: how many records do you want to get
        :return: list of subdistrict with lowest score
        '''
        # print(subdistricts)
        results = [
            {'score': self.string_matrics.distance(keyword, a['subdistrict_name'].lower()), 'city_name': a['city_name'].lower(),
             'subdistrict_name': a['subdistrict_name'].lower(), 'subdistrict_code': a['subdistrict_code']} for a in
            subdistricts]
        d = sorted(results, key=lambda i: i['score'])
        return list(filter(lambda x: x['score'] < 5, d))

    def get_sim_city(self, key, subdistricts, count=10):
        '''
            get list subdistrict with scored by city
        :param keyword: your subdistrict name
        :param subdistricts: list of subdistrict please reference this file
        :param count: how many records do you want to get
        :return: list of subdistrict with lowest score
        '''
        results = [{'score': self.string_matrics.distance(key, a['city_name'].lower()), 'city_name': a['city_name'].lower(),
                    'subdistrict_name': a['subdistrict_name'].lower(), 'subdistrict_code': a['subdistrict_code']} for a
                   in
                   subdistricts]
        return sorted(results, key=lambda i: i['score'])[0:count]

    def check_if_extact_string(self, subdistricts):
        '''
            get only exact match : 0 => same
        :param subdistricts: list of subdistrict please reference this file
        :return:
        '''
        return list(filter(lambda x: x['score'] == 0, subdistricts))

    def suggest(self, subdistrict_name, city_name, subdistricts):
        """
            suggest subdistrict when user typo
        :param subdistrict_name:
        :param city_name:
        :return:
        """

        cities = self.get_sim_subdistrict(subdistrict_name, subdistricts, 5)
        other_cities = self.check_if_extact_string(cities)

        if other_cities == []:
            result = self.get_sim_city(city_name, cities, 1)
        else:
            result = self.get_sim_city(city_name, other_cities, 1)
        return result

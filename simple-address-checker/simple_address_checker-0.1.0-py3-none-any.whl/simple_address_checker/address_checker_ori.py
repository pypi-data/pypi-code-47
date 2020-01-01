import Levenshtein
from pymongo import MongoClient


def get_subdistrict_from_mongo(col):
    return [{'city_name': a['city_name'], 'subdistrict_name': a['subdistrict_name'].lower(),
             'code': a['subdistrict_code']} for a in col.find()]


def get_sim_subdistrict(key, subdistricts, count=10):
    results = [{'score': Levenshtein.distance(key, a['subdistrict_name']), 'city_name': a['city_name'].lower(),
                'subdistrict_name': a['subdistrict_name'].lower(), 'code': a['code']} for a in
               subdistricts]
    d = sorted(results, key=lambda i: i['score'])[0:count]
    return list(filter(lambda x: x['score'] < 5, d))


def get_sim_city(key, subdistricts, count=10):
    results = [{'score': Levenshtein.distance(key, a['city_name']), 'city_name': a['city_name'],
                'subdistrict_name': a['subdistrict_name'].lower(), 'code': a['code']} for a in
               subdistricts]
    return sorted(results, key=lambda i: i['score'])[0:count]


def check_if_extact_string(subdistricts):
    return list(filter(lambda x: x['score'] == 0, subdistricts))


def main(sd, c):
    client = MongoClient(
        'mongodb://clodeo-extsrv-shipping-user:Cl0de0ExtsrvShipping!@internal-mongodb-proxy.clodeo.com/clodeo-extsrv-shipping-prod?ssl=false&readPreference=secondary')

    db = client['clodeo-extsrv-shipping-prod']

    col = db['mapping_subdistrict']

    subdistricts = get_subdistrict_from_mongo(col)

    cities = get_sim_subdistrict(sd, subdistricts, 5)

    other_cities = check_if_extact_string(cities)

    if other_cities == []:
        result = get_sim_city(c, cities, 1)
    else:
        result = get_sim_city(c, other_cities, 1)


    print(result)


if __name__ == '__main__':
    main('ilir barat i', 'palembang')

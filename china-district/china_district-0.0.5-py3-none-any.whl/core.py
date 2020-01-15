import requests
import json
import pandas as pd

# from shapely.geometry import Point, Polygon

country_colname = ['countryName', 'countryCenter', ]
province_colname = ['provName', 'provAdcode', 'provCenter', ]
city_colname = ['cityName', 'cityCode', 'cityAdcode', 'cityCenter']
district_colname = ['districtName', 'districtAdcode', 'districtCenter']
polyline_colname = ['polyLine']

select_colname = [country_colname, province_colname, city_colname, district_colname, polyline_colname]
level_lst = ['country', 'city', 'district', 'street']


class District(object):
    def __init__(self,
                 subdistrict=3,
                 extensions="base",
                 key='182ad5d7061ed1e421091c22089c3677',
                 ) -> list:
        """
        :param keywords:需要查询的城市（代码）或者省份（代码），eg:成都市
        :param key:高德地图开发者key
        :param subdistrict:设置显示下级行政区级数（行政区级别包括：国家、省/直辖市、市、区/县、乡镇/街道多级数据）

        :return:该区域的经纬度边界线坐标字符串，eg:114.2134521,29.59778924;114.281,29.575924
        """
        self.key = key
        self.subdistrict = subdistrict
        self.extensions = extensions
        self.district_list = []
        self.keywords = ""

    def getdf(self, keywords):
        _json = self.get(keywords)
        return self.json2df(_json)

    def get(self, keywords):
        self.keywords = keywords
        _parms = {
            'keywords': keywords,
            'key': self.key,
            'subdistrict': self.subdistrict,
            'extensions': self.extensions,
            'output': 'JSON',
        }
        url = 'http://restapi.amap.com/v3/config/district'
        resp = requests.get(url, params=_parms)
        _json = resp.json()
        return _json

    def to_json(self, keywords):
        _json = self.get(keywords)
        with open("./%s.json" % keywords, "w") as f:
            json.dump(_json.get("districts"), f, ensure_ascii=False)
        print("写入本地完成...")
        return _json.get['districts']


if __name__ == "__main__":
    d = District(subdistrict=1)
    result = d.get("河南")
    d.to_json("成都市高新区")
    print(result)

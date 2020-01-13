import requests
from typing import NamedTuple, List
from datetime import datetime


# This dataclass is going to be used together with create_list_of_ts_api_defs to define lists of api requests
# that retrieve time series data from Analytics
class TSApiDef(NamedTuple):
    item_id: int
    item_type: str
    measure: str
    measure_period: int
    data_type: str
    day: datetime
    from_date: datetime
    to_date: datetime


class PyAnalyticsApi:
    def __init__(self, host: str, endpoint: str, datasource: str):
        """
        Initialise the API object
        :param datasource: the datasource to be used for this API wrapper
        :param host: the IP of the Analytics Service
        :param endpoint: the name of the endpoint for the service e.g. tdfana, predictive...
        """
        self.host = host
        self.endpoint = 'http://{0}:8080/{1}/rest/'.format(host, endpoint)
        self.datasource = datasource
        self.ts_endpoint = '/getTimeSeries'
        self.cluster_endpoint = '/getCluster'
        self.roadways_endpoint = '/getRoadwaysWithItems'
        self.items_for_roadways_endpoint = '/getItemsOfRoadway'

    def get_ts_for_item(self, item_id: int, item_type: str, measure: str,  measure_period = 5, data_type='real', horizon=5,
                        from_time : str ='20180724050000', to_time : str ='20180724090000'):
        """
        Get a Time Series of values for a given item from one timestamp to another
        :param item_id: integer with the item id
        :param item_type: e.g. link, measurement_site
        :param measure: e.g. volume, speed, los
        :param measure_period: e.g. 5, 15
        :param data_type: e.g. real, forecasth, normal
        :param horizon: the horizon to be used in case of forecasth e.g. 5, 15, 30
        :param from_time: get values from a given timestamp. The format is YYYYMMDDhhmmss
        :param to_time: get values to a given timestamp. The format is YYYYMMDDhhmmss
        :return: list of integers
        """
        params = {
            'datasourceName': self.datasource,
            'itemType': item_type,
            'itemId': item_id,
            'measureName': measure,
            'dataType': data_type,
            'dateTimeFrom': from_time,
            'dateTimeToInclusive': to_time,
            'measurePeriod': measure_period,
            'forecastAheadMinutes': [horizon]
        }
        response = requests.get(self.endpoint + self.ts_endpoint,
                                params=params).json()
        # response has one key for each of the measures queried e.g. 'etx:measurement_site:16:volume:5:real'.
        try:
            for k, v in response.items():
                res = v['values']
        # if values cannot be retrieved then we will have an empty dict and response.items() will raise a TypeError
        except TypeError:
            res = []
        return res

    def get_day_ts_for_item(self, item_id: int, item_type: str, measure: str, measure_period: int = 5, data_type: str ='real', horizon: int =5, day: str ='20180724'):
        """
        It returns the time series for a given item id and day
        :param item_id: integer with the item id
        :param item_type: e.g. link, measurement_site
        :param measure: e.g. volume, speed, los
        :param measure_period: e.g. volume, speed, los
        :param data_type: e.g. real, forecasth, normal
        :param horizon: the horizon to be used in case of forecasth e.g. 5, 15, 30
        :param day: the day of interest. The format is YYYYMMDD
        :return: list of integers
        """
        from_time = day + '000000'
        to_time = day + '235959'
        return self.get_ts_for_item(item_id, item_type, measure, measure_period, data_type,
                                    horizon, from_time=from_time, to_time=to_time)

    def get_all_roadways(self, item_type : str):
        """
        Roadways is the first combo you select in analytics. It gives the ids and the names of these roadways
        :param item_type: e.g. link, measurement_site
        :return: a list with pairs of {id,name} e.g. {'id': '8651', 'name': 'Paseo de Zorrilla (E)'}
        """
        params = {'datasourceName': self.datasource, 'itemType': item_type}
        # el roadways endpoint solo te da los ids de los roadways
        response = requests.get(self.endpoint + self.roadways_endpoint,
                                params=params).json()
        return response

    def get_items_for_roadway(self, roadway_id: int, measure: str, item_type: str):
        """
        Each roadway has a series of items attached. This returns a list of their ids, the names and the available data
        :param roadway_id: int with the id of the roadway
        :param measure: e.g. volume, speed
        :param item_type: e.g. link, measurement_site
        :return: a list with tuples of {itemId, itemName, availableDataTypes}
        e.g. {'itemId': 12, 'itemName': 'PM032306 (CTRA. ESPERANZA -> ARIZA) (LT/ST)',
        'availableDataTypes': ['real', 'normal', 'forecast']}
        """
        # Aqui se le puede pasar el itemType = measurement_site para que te devuelva el item ID del MSS
        params = {'roadwayId': roadway_id, 'datasourceName': self.datasource, 'measureName': measure,
                  'measurePeriod': 5, 'itemType': item_type}
        response = requests.get(self.endpoint + self.items_for_roadways_endpoint,
                                params=params).json()
        return response

    def get_all_items(self, itemtype : str ='link', measure : str='volume'):
        """
        It returns the ids of all the items of a given type for a given measure
        :param itemtype: e.g. link, measurement_site
        :param measure: e.g. volume, speed
        :return: a list of ints for that item type that have that measure
        """
        items = set()
        req_all_roadways = self.get_all_roadways(itemtype)
        for roadway in req_all_roadways:
            req_items = self.get_items_for_roadway(roadway['id'], measure, itemtype)
            for item in req_items:
                items.add(item['itemId'])
        return list(items)

    def get_all_items_roadways_and_name(self, itemtype : str ='link', measure : str='volume'):
        """
        It returns a dictionary with keys representing the itemid and a value which is a pair {roadway, itemName}
        :param itemtype: the type of item
        :param measure: the measure of interest
        :return: dict{itemid : dict{roadway,itemName}}
        """
        result_dict = {}
        req_all_roadways = self.get_all_roadways(itemtype)
        for roadway in req_all_roadways:
            req_items = self.get_items_for_roadway(roadway['id'], measure, itemtype)
            for item in req_items:
                result_dict[item['itemId']] = {'roadway': roadway['name'], 'itemName': item['itemName']}
        return result_dict

    def get_cluster_data(self, item_id : int, item_type, measure: str, measure_period: int):
        """
        It gets all the information related to the clusterisation of an item_id :param item_id: integer with the item
        id :param item_type: e.g. link, measurement_site :param measure: e.g. volume, speed :return: a tuple with {
        min_value, max_value, list[horizons],
        dict{'MAE' : [int], 'MASE' : [int] ...} global_quality_metrics,
        dict{'MAE' : [int], 'MASE' : [int] ...} quality_metrics,
        dict{id: {'id', 'name' , 'itemId', 'valueList' ...}} patterns_dict,
        dict{'YYYYMMDD000000' : 'strDate', 'tagList', 'patternId' ...}
        """
        params = {
            'datasourceName': self.datasource,
            'itemType': item_type,
            'itemId': item_id,
            'measureName': measure,
            'measurePeriod': measure_period,
            'lang': 'en'
        }
        response = requests.get(self.endpoint + self.cluster_endpoint,
                                params=params).json()
        min_value = response.get('minValue', 0)
        max_value = response.get('maxValue', 0)
        horizons = response.get('predictionHorizons', 0)
        global_quality_metrics = response.get('globalPredictionQualityMetrics', {})
        quality_metrics = response.get('predictionQualityMetrics', {})
        # Since the REST API returns a patternList we would have to traverse the whole list to find the values for a
        # pattern ID. We build a dictionary instead with patterns_dict
        patterns_dict = {d['id']: d for d in response.get('patternList', [])}
        # Same with the list of days. We build a dictionary
        calendar_dict = {d['strDate']: d for d in response.get('patternDateList', [])}
        return min_value, max_value, horizons, global_quality_metrics, quality_metrics, patterns_dict, calendar_dict

    @staticmethod
    def create_list_of_ts_api_defs(item_ids: List[int], item_type: str, measure_name: str, measure_period: int, data_type: str,
                                   day: datetime = None,
                                   from_date: datetime = None, to_date: datetime = None) -> List[TSApiDef]:
        """
        Creates a list of TSinfos from a list of item ids and the common information for them
        :param item_ids:
        :param item_type:
        :param measure_name:
        :param measure_period:
        :param data_type:
        :param day:
        :param from_date:
        :param to_date:
        :return:
        """
        list_res = []
        for it_id in item_ids:
            list_res.append(
                TSApiDef(it_id, item_type, measure_name, measure_period, data_type, day, from_date, to_date))
        return list_res

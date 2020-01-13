import algokit.utils.rest_util as rest


def request(key, address, city=None, batch=False, sig=None, output="JSON"):
    batch = "true" if batch else "false"
    params = {k: v for k, v in locals().items() if v is not None} #过滤掉为None的参数
    url = "https://restapi.amap.com/v3/geocode/geo"
    return rest.get(url, params)


class GeocodeAPI(object):

    def __init__(self, key):
        self._key = key

    def geocode(self, address):
        return request(self._key, address)

    def geocode_batch(self, addresses):
        if isinstance(addresses, list):
            addresses = "|".join(addresses)
        return request(self._key, addresses, batch=True)


if __name__ == '__main__':
    import algokit as ak
    import json
    key = "551008fd722823c51290753166a95e8e"
    addresses = ["江苏省南京市雨花台区软件大道", "安徽省蚌埠市龙子湖区"]
    api = ak.amap.GeocodeAPI(key)
    jsondata = json.loads(api.geocode_batch(addresses))
    print(jsondata)

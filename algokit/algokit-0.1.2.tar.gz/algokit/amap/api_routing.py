import algokit.utils.rest_util as rest


def walk_request(key, origin, destination, sig=None, output="JSON"):
    """
    :param key: key
    :param origin: start point format: "lon,lat" 小数点位数不超过6位
    :param destination: destination point format: "lon,lat" 小数点位数不超过6位
    :param sig: signature
    :param output:
    :return: walk routing result
    """
    params = {k:v for k, v in locals().items() if v is not None}
    url = "https://restapi.amap.com/v3/direction/walking"
    return rest.get(url, params)


def bus_request(key, origin, destination, city, cityd=None,
                extensions='base', strategy=0, nightflag=0, date=None, time=None, sig=None, output="JSON" ):
    """
    :param key:
    :param origin:          出发点 required
    :param destination:     目的地 required
    :param city:            城市/跨城规划时的起点城市 required
    :param cityd:           跨城公交规划时的终点城市 optional(跨城必填)
    :param extensions:      返回结果详略 optional
                                base:返回基本信息 (default)
                                all：返回全部信息
    :param strategy:        公交换乘策略 optional
                                0：最快捷模式 (default)
                                1：最经济模式
                                2：最少换乘模式
                                3：最少步行模式
                                5：不乘地铁模式
    :param nightflag:       是否计算夜班车 optional
                                0：不计算夜班车(default) 1：计算夜班车
    :param date:            出发日期 optional eg: date=2014-3-19
    :param time:            出发时间 optional 据出发时间和日期，筛选可乘坐的公交路线，eg：time=22:34
    :param sig:
    :param output:
    :return:
    """
    params = {k:v for k, v in locals().items() if v is not None}
    url = "https://restapi.amap.com/v3/direction/transit/integrated"
    return rest.get(url, params)


def drive_request():
    # TODO
    pass


def bike_request():
    #TODO
    pass


def truck_request(key, origin, destination, size, originid=None, originidtype=None, destinationid=None, destinationidtype=None,
                  diu=None, strategy=1, waypoints=None, height=1.6, width=2.5, load=0.9, weight=10, axis=2,
                  province=None, number=None, cartype=0, avoidpolygons=None, showpolyline=1, nosteps=0):
    """
    :param key:                 *authorized key
    :param origin:              *出发点经纬度 required "lon,lat"
    :param originid:            出发POI唯一编号。optional 当起点为POI时，建议填充此值。
                                填充此值以后，会影响路径规划的结果，
                                举例来说，当起点的经纬度在高架桥上面，若填充了此值我们会以此POI的经纬度作为更高优的处理。
    :param originidtype:        出发POI的类型 optional 当起点为POI时，建议填充此值。
    :param destination:         *目的地经纬度 required "lon,lat"
    :param destinationid:       终点POI的唯一编号
    :param destinationidtype:   终点POI的类型
    :param diu:                 设备唯一编号 optional default( 无 ) android的imei, ios的idfa
    :param strategy:            驾车选择策略 optional default( 1 )
                                1，返回的结果考虑路况，尽量躲避拥堵而规划路径；对应导航SDK货导策略12；
                                2，返回的结果考虑路况，不走高速；对应导航SDK货导策略13；
                                3，返回的结果考虑路况，尽可能规划收费较低甚至免费的路径；对应导航SDK货导策略14；
                                4，返回的结果考虑路况，尽量躲避拥堵，并且不走高速；对应导航SDK货导策略15；
                                5，返回的结果考虑路况，尽量不走高速，并且尽量规划收费较低甚至免费的路径结果；对应导航SDK货导策略16；
                                6，返回的结果考虑路况，尽量的躲避拥堵，并且规划收费较低甚至免费的路径结果；对应导航SDK货导策略17；
                                7，返回的结果考虑路况，尽量躲避拥堵，规划收费较低甚至免费的路径结果，并且尽量不走高速路；对应导航SDK货导策略18；
                                8，返回的结果考虑路况，会优先选择高速路；对应导航SDK货导策略19；
                                9，返回的结果考虑路况，会优先考虑高速路，并且会考虑路况躲避拥堵；对应导航SDK货导策略20；
                                10，不考虑路况，返回速度优先的路线，此路线不一定距离最短；如果不需要路况干扰计算结果，推荐使用此策略；（导航SDK货导策略无对应，真实导航时均会考虑路况）
                                11，返回的结果会考虑路况，躲避拥堵，速度优先以及费用优先；500Km规划以内会返回多条结果，500Km以外会返回单条结果；考虑路况情况下的综合最优策略，推荐使用；对应导航SDK货导策略10；
    :param waypoints:           途径点 optional
                                "规则：经度和纬度用“,”分隔，坐标点之间用";"分隔
                                默认值：无
                                最大数目：16个坐标点，如果输入多个途径点，则按照用户输入的顺序进行路径规划"
    :param size:                *车辆大小 required 1：微型车，2：轻型车（默认值），3：中型车，4：重型车
    :param height:              车辆高度 optional 单位米，取值[0 – 25.5]米，默认 1.6 米，会严格按照填写数字进行限行规避
    :param width:               车辆宽度 optional 单位米，取值[0 – 25.5]米，默认 2.5 米，会严格按照填写数字进行限行规避
    :param load:                车辆总重    单位吨，取值[0 – 6553.5]吨，默认 0.9 吨，会严格按照填写数字进行限行规避，
                                            请按照车辆真实信息合理填写。 总重的含义是核定载重加上车辆自重的总质量。
    :param weight:              货车核定载重 单位吨，取值[0 – 6553.5]吨，默认 10 吨，会严格按照填写数字进行限行规避，
                                            请按照车辆真实信息合理填写。 核定载重的含义是可装载货物的最大重量。
    :param axis:                车辆轴数    单位个，取值[0 –255]个，默认 2个轴，会严格按照填写数字进行限行规避
    :param province:            车牌省份    optional default( 无 ) 用汉字填入车牌省份缩写。用于判断是否限行
    :param number:              车牌详情    optional default( 无 ) 填入除省份及标点之外的字母和数字（需大写），用于判断限行相关。
                                            支持6位传统车牌和7位新能源车牌。
    :param cartype:             车辆类型     0：普通货车（默认值）
                                            1：纯电动货车
                                            2：插电混动货车
    :param avoidpolygons:       避让区域    区域避让，支持100个避让区域，每个区域最多可有16个顶点，每个区域的最大面积是100平方公里。
                                            经度和纬度用"",""分隔，坐标点之间用";"分隔，区域之间用"|"分隔。
                                            如果是四边形则有四个坐标点，如果是五边形则有五个坐标点。
    :param showpolyline:        是否返回路线数据 optional default 1
                                当取值为1时，steps与tmcs下的polyline数据会正常返回；当取值为0时，steps与tmcs下的polyline数据返回""；
    :param nosteps:             是否返回steps字段内容 optional default 0
                                当取值为0时，steps字段内容正常返回；当取值为1时，steps字段内容为空；
    :return:
    """
    params = {k:v for k, v in locals().items() if v is not None}
    url = "https://restapi.amap.com/v4/direction/truck"
    return rest.get(url, params)


class RoutingAPI:
    pass


if __name__ == '__main__':
    import algokit as ak
    import json
    res = ak.amap.api_routing.truck_request("551008fd722823c51290753166a95e8e","116.434307,39.90909","116.434446,39.90816",3)
    print(json.loads(res))
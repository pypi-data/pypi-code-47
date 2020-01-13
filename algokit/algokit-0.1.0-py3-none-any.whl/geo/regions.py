"""
china administrative regions name and codes
"""
import pandas as pd
import os
_ROOT = os.path.abspath(os.path.dirname(__file__))
_regions_df = None
_regions_provs = None
_regions_cities = None
_regions_districts = None


def _get_df() -> pd.DataFrame:
    """
    read region infos from csv file to Dataframe
    """
    global _regions_df
    if _regions_df is None:
        _regions_df = pd.read_csv(_get_path('adcodes.csv'))
    return _regions_df


def _get_regions_provs() -> dict:
    global _regions_provs
    if _regions_provs is None:
        df = _get_df()
        df = df[["prov_id", "prov_name"]]
        df = df.drop_duplicates()
        _regions_provs = df.set_index(["prov_id"]).to_dict()["prov_name"]
    return _regions_provs


def _get_regions_cities() -> dict:
    global _regions_cities
    if _regions_cities is None:
        df = _get_df()
        df = df[["city_id", "city_name"]]
        df = df.drop_duplicates()
        _regions_cities = df.set_index(["city_id"]).to_dict()["city_name"]
    return _regions_cities


def _get_regions_districts() -> dict:
    global _regions_districts
    if _regions_districts is None:
        df = _get_df()
        df = df[["district_id", "district_name"]]
        df = df.drop_duplicates()
        _regions_districts = df.set_index(["district_id"]).to_dict()["district_name"]
    return _regions_districts


def iter_all_china_provinces():
    """
    all china provinces code and name
    :return iterator of tuple(prov_code, prov_name)
    """
    df = _get_df()
    df = df[["prov_id","prov_name"]]
    df = df.drop_duplicates()
    for r in df.iterrows():
        yield r[1].to_list()


def iter_all_china_cities(province_code=None, province_name=None):
    """
    all china cities code and name
    :param province_code: filter by province code
    :param province_name: filter by province name, skip it if province code was set
    :return iterator of tuple(prov_code, prov_name, city_code, city_name)
    """
    df = _get_df()
    if province_code is not None: df = _filter_by_prov_code(df, province_code)
    elif province_name is not None: df = _filter_by_prov_name(df, province_name)
    df = df[["prov_id","prov_name","city_id","city_name"]]
    df = df.drop_duplicates()
    for r in df.iterrows():
        yield r[1].to_list()


def iter_all_china_districts(province_code=None, province_name=None, city_code=None, city_name=None):
    """
    all china districts code and name
    :param province_code: filter by province code
    :param province_name: filter by province name, skip it if province code was set
    :param city_code: filter by city code
    :param city_name: filter by city name, skip it if city code was set
    :return iterator of tuple(prov_code, prov_name, city_code, city_name, distinct_code, district_name, phone_code)

    when both province and city parameter are set, must guarantee the city located in the province.
    """
    df = _get_df()
    if province_code is not None: df = _filter_by_prov_code(df, province_code)
    elif province_name is not None: df = _filter_by_prov_name(df, province_name)
    if city_code is not None: df = _filter_by_city_code(df, city_code)
    elif city_name is not None: df = _filter_by_city_name(df, city_name)
    df = df.drop_duplicates()
    for r in df.iterrows():
        yield r[1].to_list()


def province_name_to_code(province_name):
    """ province name to code """
    for theid, thename in _get_regions_provs().items():
        if thename == province_name:
            return theid
    return 0


def province_code_to_name(province_code):
    """ province code to name """
    return _get_regions_provs().get(province_code, None)


def city_name_to_code(city_name):
    """ city name to code """
    for theid, thename in _get_regions_cities().items():
        if thename == city_name:
            return theid
    return 0


def city_code_to_name(city_code):
    """ province code to name """
    return _get_regions_cities().get(city_code, None)


def district_name_to_code(district_name):
    """ district name to code """
    for theid, thename in _get_regions_districts().items():
        if thename == district_name:
            return theid
    return 0


def district_code_to_name(district_code):
    """ district code to name"""
    return _get_regions_districts().get(district_code, None)


def _filter_by_prov_code(df: pd.DataFrame, prov_code) -> pd.DataFrame:
    prov_id = int(prov_code)
    df = df[df["prov_id"] == prov_id]
    return df


def _filter_by_prov_name(df: pd.DataFrame, prov_name) -> pd.DataFrame:
    df = df[df["prov_name"] == prov_name]
    return df


def _filter_by_city_code(df: pd.DataFrame, city_code) -> pd.DataFrame:
    city_id = int(city_code)
    df = df[df["city_id"] == city_id]
    return df


def _filter_by_city_name(df: pd.DataFrame, city_name) -> pd.DataFrame:
    df = df[df["city_name"] == city_name]
    return df


def _get_path(path):
    return os.path.join(_ROOT, path)


if __name__ == '__main__':
    city_infos = iter_all_china_cities(province_name="山西省")
    city_codes = [x for x in city_infos]

    print(city_codes)






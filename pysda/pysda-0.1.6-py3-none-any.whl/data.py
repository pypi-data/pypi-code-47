# -*- encoding: utf-8 -*-
import datetime
from dateutil.parser import parse

import shapely.geometry as sg
import pandas as pd
import geopandas as gpd

#from pysda import tapitas


def __checkColName(pointDF, t, lat=None, lon=None):
    check = True
    col_key = [t, lat, lon]
    for k in col_key:
        if k is None:
            continue
        else:
            if k in pointDF.columns:
                pass
            else:
                raise AttributeError('The given column names are not in the data!')


def readCSV(csvPath, latColumn="lat", lonColumn="lon", timeColumn="time", epsgProjected=4326, timeUnit="day", encoding='utf-8'):
    pointDF = pd.read_csv(csvPath, encoding=encoding)
    pointDF.dropna(axis=0, how='any', inplace=True)
    return readDF(pointDF, latColumn, lonColumn, timeColumn, epsgProjected, timeUnit)


def readDF(pointDF, latColumn="lat", lonColumn="lon", timeColumn="time", epsgProjected=4326, timeUnit="day"):
    __checkColName(pointDF, timeColumn, lonColumn, latColumn)

    # create geometry
    geometry = []
    for index, row in pointDF.iterrows():
        coord = sg.Point(float(row[lonColumn]), float(row[latColumn]))
        geometry.append(coord)

    pointGDF = gpd.GeoDataFrame(pointDF, geometry=geometry, crs="+init=epsg:4326")
    pointGDF.to_crs(epsg=epsgProjected, inplace=True)

    d = PysdaData(pointGDF, timeColumn, timeUnit)
    return d


def readSHP(shpPath, timeColumn="time", timeUnit="day", encoding='utf-8'):
    pointGDF = gpd.read_file(shpPath, encoding=encoding)
    return readGDF(pointGDF, timeColumn, timeUnit)


def readGDF(pointGDF, timeColumn="time", timeUnit="day"):
    __checkColName(pointGDF, timeColumn)

    d = PysdaData(pointGDF, timeColumn, timeUnit)
    return d



###############################################################################
class PysdaData():
    def __init__(self, gdf, ttitle, tunit):
        self.tunit = self.__transformTimeUnit(tunit)
        if self.tunit == "int":
            gdf["intTime"] = gdf[ttitle]

            intDates = gdf[ttitle].tolist()
            intDates = list(set(intDates))
            intDates.sort()

            timeDict = {}
            for i in intDates:
                timeDict[i] = i

        else:
            # deal with time unit
            strDates = gdf[ttitle].tolist()
            dates = [parse(i) for i in strDates]
            intDates = [None]*len(dates)

            start = min(dates)
            end = max(dates)
            dateRange = [i.to_pydatetime() for i in pd.date_range(start, end, freq=self.tunit)]

            for i in range(len(dates)):
                for j in range(len(dateRange)-1,-1,-1):
                    if dates[i] >= dateRange[j]:
                        intDates[i] = j
                        break

            gdf["intTime"] = intDates

            timeDict = {}
            for i in range(len(dateRange)):
                timeDict[str(i)] = dateRange[i].strftime("%Y/%m/%d-%H:%M:%S")

        self.gdf = gdf
        self.dateIndex = timeDict

    def __transformTimeUnit(self, tunit):
        if tunit == "int":
            pass
        elif tunit == "hour":
            tunit = "1h"
        elif tunit == "day":
            tunit = "1D"
        elif tunit == "week":
            tunit = "7D"
        elif tunit == "month":
            tunit = "30D"
        elif tunit == "year":
            tunit = "365D"
        else:
            pass

        return tunit

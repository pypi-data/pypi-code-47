from geographiclib.geodesic import Geodesic
import math

def distance(lon1, lat1, lon2, lat2):
    """calculate distance between two longitude, latitude point"""
    d = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)
    return d["s12"]
    # return geodesic((lat1,lon1),(lat2,lon2)).m


def bearing(lon1, lat1, lon2, lat2, type="degree"):
    d = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)
    b = d["azi1"]
    if type=='radian': b = math.radians(b)
    return b


if __name__ == '__main__':
    s = "116.547504,38.805191;116.54697,38.806111;116.546706,38.806445"
    ps = s.split(";")
    ds = 0
    for i in range(1, len(ps)):
        lon2, lat2 = ps[i].split(",")
        lon1, lat1 = ps[i-1].split(",")
        ds += distance(float(lon1), float(lat1), float(lon2), float(lat2))
        print(bearing(float(lon1), float(lat1), float(lon2), float(lat2)))

    print(ds)




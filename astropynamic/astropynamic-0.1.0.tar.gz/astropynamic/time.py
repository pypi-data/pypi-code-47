

def julian_date(year, month, day, hour, minute, second):
    times = [year, month, day, hour, minute]

    if not all(isinstance(times, int) for i in times):
        times = [int(x) for x in times]

    if not isinstance(second, float):
        second = float(second)

    j_date = 367 * times[0] - \
        (7 * (times[0] + (times[1] + 9) / 12)) / 4 + \
        (275 * times[1]) / 9 + times[2] + 1721013.5 + (((second / 60 + times[4]) / 60) + times[3]) / 24

    return j_date


def greenwich_sidereal(julian_date):
    tu = (julian_date - 2451545.0) / 36525.0

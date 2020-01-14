
import time

def human_readable_size(size_bytes):
    value = size_bytes

    value = int(value) / 1024
    unit = "KiB"
    if value > 1023:
        value = value / 1024
        unit = "MiB"
    if value > 1023:
        value = value / 1024
        unit = "GiB"
    if value > 1023:
        value = value / 1024
        unit = "TiB"
    if value > 1023:
        value = value / 1024
        unit = "PiB"

    return "%.2f %s" % (value, unit)

def human_readable_time(size_ns):
    val = []

    ms_ns = 1000*1000
    sec_ns = 1000*ms_ns
    min_ns = 60*sec_ns
    hr_ns = 60*min_ns
    day_ns = 24*hr_ns
    # days, rem = divmod(size_ns, day_ns)
    # if days:
    #     val.append("{} day(s)".format(days))

    hrs, rem = divmod(size_ns, hr_ns)
    if hrs:
        val.append("{} hour(s)".format(hrs))

    mins, rem = divmod(rem, min_ns)
    if mins:
        val.append("{} min".format(mins))

    secs, rem = divmod(rem, sec_ns)
    if secs:
        val.append("{} sec".format(secs))

    if rem:
        val.append("{} ns".format(rem))

    try:
        return "{} {}".format(val[0], val[1])
    except:
        return "{}".format(val[0])


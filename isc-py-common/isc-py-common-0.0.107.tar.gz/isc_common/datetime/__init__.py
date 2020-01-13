import datetime


def DateToStr(date, mask='%d.%m.%Y'):
    return datetime.datetime.strftime(date, mask)


def StrToDate(str, mask='%Y-%m-%dT%H:%M:%S'):
    res = datetime.datetime.strptime(str.replace('.000', ''), mask)
    return res + datetime.timedelta(hours=3)

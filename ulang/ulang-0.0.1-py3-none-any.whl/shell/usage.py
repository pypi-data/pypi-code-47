from time import ctime

from ulang.version import VERSION


def run():
    cur_time = ctime()
    text = f"""
    # ulang

    Version {VERSION} ({cur_time} +0800)
    """
    print(text)

from time import ctime

from mulan.version import VERSION


def run():
    cur_time = ctime()
    text = f"""
    # mulan
    
    Version {VERSION} ({cur_time} +0800)
    """
    print(text)

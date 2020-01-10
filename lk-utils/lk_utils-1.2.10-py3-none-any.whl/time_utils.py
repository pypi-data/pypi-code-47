import time
from os import stat


def generate_timestamp(style='y-m-d h:n:s', ctime=0.0) -> str:
    """
    生成时间戳.
    
    转换关系:
        year  : %Y
        month : %m
        day   : %d
        hour  : %H
        minute: %M
        second: %S
    
    IN: 'y-m-d h:n:s'
    OT: '2018-12-27 15:13:45'
    
    注: 本方法仅支持补零数字, 比如6月2日, 会生成为 "06-02".
    """
    ctime = time.localtime(ctime or time.time())
    style = style \
        .replace('y', '%Y').replace('m', '%m').replace('d', '%d') \
        .replace('h', '%H').replace('n', '%M').replace('s', '%S')
    time_stamp = time.strftime(style, ctime)
    return time_stamp


def seconds_to_hms(second: int):
    """
    将秒数转换成 hms 格式.
    REF: https://www.jb51.net/article/147479.htm
    """
    m, s = divmod(second, 60)
    h, m = divmod(m, 60)
    hms = "%02d%02d%02d" % (h, m, s)
    return hms


def get_file_modified_time(filepath, style='y-m-d h:n:s'):
    """
    REF: demos/os_demo#get_file_created_time
    """
    time_float = stat(filepath).st_mtime
    if style == '' or style == 'float':
        return time_float
    else:
        return generate_timestamp(style, time_float)


def get_file_created_time(filepath, style='y-m-d h:n:s'):
    """
    REF: demos/os_demo#get_file_created_time
    """
    time_float = stat(filepath).st_ctime
    if style == '' or style == 'float':
        return time_float
    else:
        return generate_timestamp(style, time_float)

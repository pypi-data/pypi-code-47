import socket
from .ip_func import is_ip, format_ip, in_line
import time
from ..config import setting


def get_ip_address(host_or_ip):
    '''
    使用2分查找法寻找ip的具体地址
    :param host_or_ip: 域名或者是ip字符串
    :return: 返回ip的具体地址
    '''
    if not is_ip(host_or_ip):
        ret = socket.getaddrinfo(host_or_ip, 'http')
        rel_ip = ret[0][4][0]
    else:
        rel_ip = host_or_ip
    with open(setting.data_dir, mode='r', encoding='gbk') as f:
        ip_data = f.readlines()
    lines_num = len(ip_data)
    start_line = 0
    end_line = lines_num - 1
    for i in range(lines_num):
        middle = int((start_line + end_line) / 2)
        if in_line(ip_data[middle], rel_ip) == 0:
            return format_ip(ip_data[middle])[2]
            break
        elif in_line(ip_data[middle], rel_ip) == -1:
            end_line = middle - 1
        else:
            start_line = middle + 1


def main():
    '''
    测试使用的main函数
    :return: 无返回值
    '''
    start_time = time.time()
    print(get_ip_address('www.google.com'))
    print(time.time() - start_time)


if __name__ == '__main__':
    main()

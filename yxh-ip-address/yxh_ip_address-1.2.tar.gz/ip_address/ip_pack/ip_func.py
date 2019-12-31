import socket, struct
import re


def ip2int(ip):
    """
    :param ip: ip字符串
    :return: 将ip转为int返回
    """
    return struct.unpack('!I', socket.inet_aton(ip))[0]


def is_ip(ip):
    '''
    判断是否是ip格式
    :param ip: ip字符串
    :return: 如果不是返回None
    '''
    re_str = re.compile(r'\d+\.\d+\.\d+\.\d+')
    return re_str.search(ip)


def format_ip(line_ip):
    '''
    :param line_ip: 一行字符串 格式：255.255.255.0  255.255.255.255 地址
    :return: 返回转为元组的行ip
    '''
    ret = re.findall(r'(\d+\.\d+\.\d+\.\d+)\s+(\d+\.\d+\.\d+\.\d+)\s*(.*)', line_ip)
    if ret:
        return (ip2int(ret[0][0]), ip2int(ret[0][1]), ret[0][2])


def in_line(line_ip, ip):
    '''
    :param line_ip: 行ip 格式：255.255.255.0  255.255.255.255 地址
    :param ip: ip字符串
    :return: 在行ip中返回0 小于返回 -1 大于返回 1
    '''
    if format_ip(line_ip)[0] <= ip2int(ip) and format_ip(line_ip)[1] >= ip2int(ip):
        return 0
    elif format_ip(line_ip)[0] > ip2int(ip):
        return -1
    else:
        return 1

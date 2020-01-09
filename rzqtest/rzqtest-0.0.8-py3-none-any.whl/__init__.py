import threading
import argparse
from rzqtest.lib import *
def main():
    # 全局配置
    # 默认值由argpares模块解析后自动设置
    global_setting = {
    'user': '',  # smtp帐号
    'key': '',  # smtp帐号授权码
    'receivers': [],  # 收信人列表
    'file_path': '',  # url文件路径，无效路径会使程序关闭
    'expire': -1,  # 筛选小于给定有效日期的证书，设置为-1关闭筛选功能
    'func': '',  # 程序运行方式，cert开启证书检测功能，url开启连接有效性检测，all启用所有功能
    'temp_path': '',  # 模版文件路径，无效的路径会让程序以纯文本方式发送结果
    'smtp_addr': '',  # smtp服务器地址
    'smtp_port': '',  # smtp服务器端口，本程序使用SSL连接
    }
    p = argparse.ArgumentParser(description="Url test")
    p.add_argument("-u", help="SMTP服务的寄信人", dest='user',default=None)
    p.add_argument("-k", help="SMTP的授权码", dest='key', default=None)
    p.add_argument("-s", help="SMTP服务器地址，默认使用smtp.qq.com", dest='smtp_addr', default='smtp.qq.com')
    p.add_argument("-p", help="SMTP服务器端口", dest='smtp_port', default='465')
    p.add_argument("-f", help="包含了URL所在的文件路径", dest='file_path', required=True)
    p.add_argument("-l", help="收件邮箱地址，多个地址间以英文符号;来分隔", dest='to_list', default=None)
    p.add_argument("-e", help="设置证书的剩余天数期限，默认值-1将返回所有可用的URL证书有效期限", dest='expire', type=int, default=-1)
    p.add_argument('-t', help='模板文件路径，支持UTF8，默认或无法读取文件的情况下发送纯文本', dest='temp_path', default=None)
    p.add_argument('--func', help="设置程序的工作方式，参数cert启动证书检测，参数url启动url有效性检测，默认参数all启用所有功能 ",
                   choices=['cert', 'url', 'all'], dest="func", default='all')
    args = p.parse_args()
    # 根据参数初始化全局设置
    global_setting['user'] = args.user
    global_setting['key'] = args.key
    if args.to_list:
    	global_setting['receivers'] = args.to_list.split(';')
    else:
    	global_setting['receivers'] = args.to_list
    global_setting['file_path'] = args.file_path
    global_setting['expire'] = args.expire
    global_setting['func'] = args.func
    global_setting['temp_path'] = args.temp_path
    global_setting['smtp_addr'] = args.smtp_addr
    global_setting['smtp_port'] = args.smtp_port


    mailer = Mailer(global_setting)
    # 根据文件路径生成UrlsInfo
    url_info = UrlsInfo(global_setting['file_path'])

    # 线程池
    threadpool = []
    if global_setting['func'] != 'cert':
        # 生成URL测试对象
        t1 = TestUrl(mailer,global_setting)
        # 创建一个线程处理UrlsInfo实例提供url的连接有效性测试
        threadpool.append(threading.Thread(target=t1.test, args=(url_info,), name='_a'))
    if global_setting['func'] != 'url':
        # 生成证书检测对象
        t2 = TestCert(mailer,global_setting)
        # 创建一个线程处理UrlsInfo实例提供url的证书
        threadpool.append(threading.Thread(target=t2.test, args=(url_info,), name='_b'))

    for thre in threadpool:
        thre.start()
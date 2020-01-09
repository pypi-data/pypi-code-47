import argparse
p = argparse.ArgumentParser(description="Url test")
p.add_argument("-u", help="SMTP服务的寄信人", dest='user', default='1581327660@qq.com')
p.add_argument("-k", help="SMTP的授权码", dest='key', default='')
p.add_argument("-S", help="SMTP服务器地址", dest='smtp_addr', default='smtp.qq.com')
p.add_argument("-P", help="SMTP服务器端口", dest='smtp_port', default='465')
p.add_argument("-p", help="包含了URL所在的文件路径", dest='file_path', required=True)
p.add_argument("-l", help="收件邮箱地址，多个地址间以英文符号;来分隔", dest='to_list', required=True)
p.add_argument("-e", help="设置证书的剩余天数期限，默认值-1将返回所有可用的URL证书有效期限", dest='expire', type=int, default=-1)
p.add_argument('-t', help='模板文件路径，支持UTF8，默认或无法读取文件的情况下发送纯文本', dest='temp_path', default=None)
p.add_argument('-f', '--func', help="设置程序的工作方式，参数cert启动证书检测，参数url启动url有效性检测，参数all启用所有功能 ",
               choices=['cert', 'url', 'all'], dest="func", default='all')
args = p.parse_args()
# 根据参数初始化全局设置
global_setting['user'] = args.user
global_setting['key'] = args.key
global_setting['receivers'] = args.to_list.split(';')
global_setting['file_path'] = args.file_path
global_setting['expire'] = args.expire
global_setting['func'] = args.func
global_setting['temp_path'] = args.temp_path
global_setting['smtp_addr'] = args.smtp_addr
global_setting['smtp_port'] = args.smtp_port
main()
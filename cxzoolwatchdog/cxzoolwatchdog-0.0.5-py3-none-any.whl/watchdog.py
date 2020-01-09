import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
from urllib import parse, request
import idna
import socket
from OpenSSL import SSL
import argparse
import sys
import re
from abc import ABC, abstractmethod
import threading

# 本程序仅使用单个SMTP帐号发送邮件
# 该锁用来控制线程的发送顺序
lock = threading.Lock()


def log(string, out='screen'):
    """
    辅助显示运行日志
    :param string: 要显示的字符串
    :param out: 字符串输出目标
    :return: None
    """
    if out == 'screen':
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + threading.currentThread().name + "  : " + string)


class Mailer:
    """
    邮件发送器

    """

    def __init__(self, **kw):
        self._sender = kw['user']
        self._receivers = kw['receivers']
        self._key = kw['key']
        self._content = None  # 邮件主体内容
        try:
            self._connect = smtplib.SMTP_SSL(global_setting['smtp_addr'], global_setting['smtp_port'], None, None, None,
                                             3)
            if global_setting['temp_path']:
                try:
                    hander = open(global_setting['temp_path'], 'r', encoding='utf-8')
                    self._template = hander.read()
                except IOError:
                    global_setting['temp_path'] = None
            else:
                global_setting['temp_path'] = None
        except Exception:
            log('smtp服务器：{0}:{1} 无法访问'.format(global_setting['smtp_addr'], global_setting['smtp_port']))
            sys.exit(-1)

    @property
    def sender(self):
        return self._sender

    @property
    def receivers(self):
        return self._receivers

    @property
    def key(self):
        return self._key

    def set_msg(self, text, subject):
        """
        设置邮件内容

        :param text: 邮件正文 str类型
        :param subject: 设置邮件主题
        :return: None
        """
        if global_setting['temp_path']:
            text = re.sub(r'\.content', text, self._template)
            text = re.sub(r'\.title', subject, text)
            text = MIMEText(text, 'html', 'utf-8')
        else:
            text = MIMEText(text)
        self._content = MIMEMultipart()
        self._content['Subject'] = subject
        self._content['From'] = self.sender
        self._content['to'] = ';'.join(self.receivers)
        self._content.attach(text)
        # att1 = MIMEText(open('urls.txt', 'r').read(), 'base64', 'utf-8')
        # att1["Content-Type"] = 'application/octet-stream'
        # att1["Content-Disposition"] = 'attachment; filename="url.txt"'
        # self._content.attach(att1)

    def send_mail(self):
        log("核对SMTP身份......")
        self._connect.login(self.sender, self.key)
        log("核对SMTP身份成功")
        log("邮件发送中......")
        self._connect.sendmail(self.sender, self.receivers, self._content.as_string())
        log('成功发送结果邮件至{0}'.format(self.receivers))


class UrlsInfo:
    """
    UrlsInof类描述从文件中读取的URLS信息
    """

    def __init__(self, filename):
        self._urls_list = []  # 保存已解析URL列表
        try:
            with open(filename, 'r', encoding='utf-8') as hander_urls:
                log("开始解析 {0} ......".format(filename))
                self._urls_list = hander_urls.read().split("\n")
                log("url解析完成")
        except FileNotFoundError:
            log('文件无法打开或文件不存在，请核对输入的文件路径')
            sys.exit(-1)

    def get_urls(self):
        """
        :return:返回一个内置的list类型
        """
        return self._urls_list
class Test(ABC):
    """
    测试接口，仅供继承，不应被实例化
    """

    def __init__(self, mailer):
        """
        :param mailer: 应为Mailer的一个实例
        """
        self._result = ''  # 测试结果
        self._type = ''  # 测试类型
        self._template = "<tr><td>{0}</td><td>{1}</td></tr>"  # 单条数据模版
        self._mailer = mailer

    @property
    def result(self):
        return self._result

    def test(self, Urls):
        """
        对UrlsInfo中的url进行测试，测试的方式和类型依赖于子类的实现
        :param Urls:应该UrlsInfo的一个实例
        :return:None
        """
        log(self._type)
        content = ''
        for url in Urls.get_urls():
            log('测试 {0} ......'.format(url))
            content += self._run(url)
        self._result = content
        self._send(self._result, self._type)

    @abstractmethod
    def _run(self, url):
        """
        :param url: 应为str类型的单个url
        """
        pass

    def _send(self, text, subject):
        """
        发送测试的结果，依赖于类被实例化时传入的邮件发送器
        :param text: str类型的邮件正文
        :param subject: str类型的邮件主题
        :return:None
        """
        global lock
        lock.acquire()
        try:
            self._mailer.set_msg(text, subject)
            self._mailer.send_mail()
        except smtplib.SMTPRecipientsRefused:
            log("邮件发送失败，收件人地址错误")
            sys.exit(-1)
        except (smtplib.SMTPAuthenticationError, smtplib.SMTPServerDisconnected):
            log("身份验证失败，请核对发件邮箱和授权码")
            sys.exit(-1)
        finally:
            lock.release()


class TestCert(Test):
    """
    测试证书有效期
    """

    def __init__(self, mailer):
        Test.__init__(self, mailer)
        self._type = "证书测试"

    # 测试
    def _run(self, url):
        """
        Args:
            url: 应为str类型的单个url
        Returns:
            返回一个保存当前测试结果的HTML格式的字符串
        """
        try:
            url = parse.urlparse(url)
            url = (url.hostname, url.port or 443)
            sock = socket.socket()
            sock.connect(url)
            cxt = SSL.Context(SSL.SSLv23_METHOD)
            cxt.check_hostname = False
            cxt.verify_mode = SSL.VERIFY_NONE
            sock_ssl = SSL.Connection(cxt, sock)
            sock_ssl.set_tlsext_host_name(idna.encode(url[0]))
            sock_ssl.set_connect_state()
            sock_ssl.do_handshake()
            cert = sock_ssl.get_peer_certificate()
            sock_ssl.close()
            sock.close()
        except Exception:
            cert = None
        return self._log(cert, url[0])
    def _log(self, cert, url):
        """
        根据证书信息，辅助生成str类型的结果，不应被在外部被调用
        :param cert:证书信息
        :param url:该证书对应的url，str格式
        :return:
        """
        template = self._template
        if not global_setting['temp_path']:
            template = "url：{0}  剩于有效期{1}\n"
        if not cert:
            return template.format(url, '无法访问')
        deadline = datetime.datetime.strptime(str(cert.get_notAfter()[:-1], encoding='utf-8'),
                                              '%Y%m%d%H%M%S') + datetime.timedelta(hours=8)
        days = deadline - datetime.datetime.now()
        if days.days > global_setting['expire'] != -1:
            return ''
        return template.format(url, str(days.days) + '天')


class TestUrl(Test):
    """
    测试url链接有效性
    """

    def __init__(self, mailer):
        Test.__init__(self, mailer)
        self._type = "URL链接检测"

    def _run(self, url):
        """
        Args:
            url: 应为str类型的单个url
        Returns:
            返回一个保存当前测试结果的HTML格式的字符串
        """
        template = self._template
        if not global_setting['temp_path']:
            template = 'url：{0} 链接状态：{1}\n'
        try:
            num = request.urlopen(url, timeout=5).getcode()
            if num > 400:
                return template.format(url, '链接失效')
        except Exception:
            return template.format(url, '链接失效')
        return template.format(url, '链接正常')


def main():
    mailer = Mailer(user=global_setting['user'], key=global_setting['key'],
                    receivers=global_setting['receivers'])
    # 根据文件路径生成UrlsInfo
    url_info = UrlsInfo(global_setting['file_path'])

    # 线程池
    threadpool = []
    if global_setting['func'] != 'cert':
        # 生成URL测试对象
        t1 = TestUrl(mailer)
        # 创建一个线程处理UrlsInfo实例提供url的连接有效性测试
        threadpool.append(threading.Thread(target=t1.test, args=(url_info,), name='_a'))
    if global_setting['func'] != 'url':
        # 生成证书检测对象
        t2 = TestCert(mailer)
        # 创建一个线程处理UrlsInfo实例提供url的证书
        threadpool.append(threading.Thread(target=t2.test, args=(url_info,), name='_b'))

    for thre in threadpool:
        thre.start()
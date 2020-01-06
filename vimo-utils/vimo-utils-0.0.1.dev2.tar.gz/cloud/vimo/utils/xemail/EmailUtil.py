#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from cloud.vimo.utils.properties import PropertiesUtil

charset = 'utf-8'


class Sender:

    def __init__(self, config_path = None, properties_name = None):
        if config_path is None:
            config_path = os.getcwd()
        if properties_name is None:
            properties_name = "config.properties"

        file_name = '%s/%s' % (config_path, properties_name)
        print("load configs from %s" % file_name)
        self.properties = PropertiesUtil.Properties(file_name = file_name)
        self.smtp_server = self.properties.get(key = 'smtp.server',
                                               default_value = 'smtp.mxhichina.com')
        self.smtp_port = self.properties.get(key = 'smtp.port', default_value = 25)
        self.smtp_user = self.properties.get(key = 'smtp.user')
        self.smtp_password = self.properties.get(key = 'smtp.password')

        try:
            self.server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.server.login(self.smtp_user, self.smtp_password)
        except Exception as e:
            print("ERROR: Server 登录异常 - %s" % e)
            self.server = None
            raise e

    def close(self):
        if self.server is not None:
            self.server.close()

    def send_email(self, subject = '', receivers = None, content = ''):
        if receivers is None:
            receivers = []
        msg = MIMEText(_text = content, _subtype = 'html', _charset = charset)
        msg['From'] = Header(s = self.smtp_user)
        msg['To'] = Header(s = ",".join(receivers))
        msg['Subject'] = Header(s = subject, charset = charset)
        try:
            if self.server is not None:
                self.server.sendmail(self.smtp_user, receivers, msg.as_string())
        except Exception as e:
            print("ERROR: 无法发送邮件 - %s" % e)

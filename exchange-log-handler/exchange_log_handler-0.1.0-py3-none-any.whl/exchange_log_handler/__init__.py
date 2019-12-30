#!/usr/bin/env python3
# coding: utf-8
'''
Author: Park Lam <lqmonline@gmail.com>
'''

import json
from exchangelib import DELEGATE, Account, Credentials, Configuration, Mailbox, \
        Message
from logging import Handler

class ExchangeHandler(Handler):
    """
    A handler class which send logging records as email via ExChange server.
    """
    def __init__(self, credentials, toaddrs, fromaddr=None, \
            subject=None, access_type=DELEGATE, \
            ews_url='https://outlook.office365.com/ews/exchange.asmx'):
        """
        Initialize the handler
        """
        Handler.__init__(self)
        if isinstance(credentials, (list, tuple)):
            self._username, self._password = credentials
            self._credentials = Credentials(username=self._username, \
                    password=self._password)
        elif isinstance(credentials, Credentials):
            self._credentials = credentials
        else:
            raise TypeError('Invalid credentials Type')

        self._config = Configuration(service_endpoint=ews_url, \
                credentials=self._credentials)
        if fromaddr:
            self._fromaddr = fromaddr
        else:
            self._fromaddr = self._credentials.username
        if isinstance(toaddrs, str):
            self._toaddrs = [ i.strip() for i in toaddrs.replace(';', ',') \
                    .strip(',').split(',') ]
        self._subject = subject
        self._access_type = access_type

    def get_account(self):
        return Account(primary_smtp_address=self._fromaddr, \
                config=self._config, autodiscover=False, \
                access_type=self._access_type)

    def get_subject(self, record):
        if callable(self._subject):
            return self._subject(record)
        elif isinstance(self._subject, str):
            return self._subject
        return self._subject or 'No subject'

    def get_content(self, record):
        return self.format(record)

    def emit(self, record):
        """
        Emit a record.
        """
        try:
            acct = self.get_account()
            subject = self.get_subject(record)
            cont = self.get_content(record)
            msg = Message(
                    account=acct,
                    folder=acct.sent,
                    subject=subject,
                    body=cont,
                    to_recipients=[ Mailbox(email_address=addr) \
                            for addr in self._toaddrs ])
            msg.send_and_save()
        except Exception:
            self.handleError(record)

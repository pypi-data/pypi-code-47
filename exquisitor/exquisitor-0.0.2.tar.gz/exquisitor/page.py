#!/usr/bin/env python2
#
# Copyright (C) 2015-2019 David J. Beal, All Rights Reserved
#

#
# TODO: use GraphType system for these types
#

import json
import sys
import pprint
import os
from collections import OrderedDict
from collections import *
from queue import *
import socket
import errno
from gom.queue import *

class Page(namedtuple('Page', ('prototype',
    'uuid',
    'url',
    'x',
    'y',
    'z',
    'width',
    'height',
    'is_open',
    'is_deleted',
    'is_run_in_background',
    'scale',
))):
    @classmethod
    def gen_uuid(self):
        import uuid
        return uuid.uuid4().hex[:8]

    def get_hostname(self):
        result = None
        if self.url and '/' in self.url:
            result = self.url.split('/')[2]
        return result

    def get_ip(self):
        result = None
        hostname = self.get_hostname()
        if hostname is not None:
            # Queue.debug(hostname = hostname)
            ip = None
            for i in range(10):
                try:
                    ip = socket.gethostbyname(hostname)
                except socket.gaierror as e:
                    Queue.debug(hostname = hostname, exception = e)
                    import time
                    time.sleep(1)
            # Queue.debug(hostname = hostname, ip = ip)
            result = ip
        return result

    @classmethod
    def create_from_url(self, url):
        return Page._default._replace(uuid = Page.gen_uuid(), url = url, is_open = True)

#
# page has 3 dimensions for z-stacking
#
Process.register_class(Page, uuid = '', url = '', is_open = False, x = None, y = None, z = None, width = None, height = None, is_run_in_background = False, scale = 1.0, is_deleted = False)

#
# edge class representing link from page to parent or prior page
#
# FromUUID
# ToUUID
#
# TODO: rename this UuidToUuid or something similar since it relates uuids, not
# pages.
#
class PageToPage(namedtuple('PageToPage', ('prototype', 'uuid', 'prior_uuid'))):
    #
    # TODO: use this for building next/prev navigation chains
    #
    @classmethod
    def create_from_pages(self, page, prior_page):
        return Process.create('PageToPage', uuid = page.uuid, prior_uuid = prior_page.uuid)
        #
    #
#
Process.register_class(PageToPage, uuid = '', prior_uuid = '')

class Session(namedtuple('Session', ('prototype', 'path', 'pages', 'edges'))):
    #
    SESSION_BASE_DIR = '/dev/shm/Exquisitor/Session'
    #
    @classmethod
    def get_page_path(Session, page, *components):
        return os.path.join(Session.SESSION_BASE_DIR, page.uuid, *components)
        #
    #
    @classmethod
    def make_page_dir(Session, page):
        try:
            os.makedirs(Session.get_page_path(page))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            #
        #
        stdin_path = Session.get_stdin_path(page)
        stdout_path = Session.get_stdout_path(page)
        #
        Pipe.create_from_path(stdin_path)
        Pipe.create_from_path(stdout_path)
        #
    #
    @classmethod
    def get_stdin_path(Session, page):
        return Session.get_page_path(page, 'stdin')
    #
    @classmethod
    def get_stdout_path(Session, page):
        return Session.get_page_path(page, 'stdout')
    #
    @classmethod
    def remove_page_dir(Session, page):
        stdin_path = Session.get_stdin_path(page)
        stdout_path = Session.get_stdout_path(page)
        os.unlink(stdin_path)
        os.unlink(stdout_path)
        os.rmdir(Session.get_page_path(page))
    #
#
Process.register_class(Session, path = '', pages = (), edges = ())

class Open(namedtuple('Open', ('prototype', 'uuid'))):
    pass

class Close(namedtuple('Close', ('prototype', 'uuid', 'is_permanent'))):
    pass

class CloseAll(namedtuple('Close', ('prototype',))):
    pass

class OpenClient(namedtuple('OpenClient', ('prototype', 'input_path', 'output_path'))):
    pass

class Progress(namedtuple('Progress', ('prototype', 'uuid', 'progress'))):
    pass

class Transform(namedtuple('Transform', ('prototype', 'uuid', 'matrix'))):
    pass

class Window(namedtuple('Window', ('prototype', 'uuid', 'xid'))):
    pass


Process.register_class(Close)
Process.register_class(Open)
Process.register_class(CloseAll)
Process.register_class(OpenClient)
Process.register_class(Progress)
Process.register_class(Transform)
Process.register_class(Window)

class InputFile(namedtuple('Input', ('prototype', 'path'))):
    pass
Process.register_class(InputFile)

class OutputFile(namedtuple('Input', ('prototype', 'path'))):
    pass
Process.register_class(OutputFile)

class FindTextInDocument(namedtuple('FindTextInDocument', ('prototype', 'regex'))):
    pass
Process.register_class(FindTextInDocument)

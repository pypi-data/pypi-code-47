#!/usr/bin/env python2
#
# Copyright (C) 2015-2019 David J. Beal, All Rights Reserved
#

import os
import sys
import binascii
import json
import pprint
import stat

from gom.queue import *

from collections import *
from collections import namedtuple
from collections import OrderedDict

# import epoll as poll
import select as poll

from .page import *
from gom.osutil import OSUtil

import time
import subprocess
import signal
import numpy

import math
import numpy as np

from .display import *
import array

# import Xlib
# import Xlib.display
# from Xlib import X

import errno

import heapq

from .wmx import WMX

import random

class ImportSessionBuddy(namedtuple('ImportSessionBuddy', ('prototype', 'input_path', 'output_path'))):
    pass

Process.register_class(ImportSessionBuddy)

_NET_WM_WINDOW_TYPE_NORMAL = Display.display.intern_atom('_NET_WM_WINDOW_TYPE_NORMAL')
_NET_WM_PID = Display.display.intern_atom('_NET_WM_PID')

is_use_desktop_geometry = True

class EventLoop(namedtuple('EventLoop', ('prototype',))):
    #
    # message that starts the event loop
    #
    pass
#
Process.register_class(EventLoop)

class WebSession(object):
    #
    BASE_DIR = os.path.expanduser('~/.exquisitor')
    SESSION_PATH = os.path.join(BASE_DIR, 'Session')
    #
    # form path to browser executable
    #
    BROWSER_FILENAME = 'webkitgtk.py'
    BROWSER_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), BROWSER_FILENAME)
    #
    assert os.path.exists(BROWSER_PATH)
    #
    def __init__(self, *args, **kwargs):
        #
        # can replace session array
        #
        self.uuid_to_page = OrderedDict()
        #
        self.uuid_to_process = OrderedDict()
        self.xid_to_process = OrderedDict()
        #
        # page edges
        #
        # NOTE: value type of uuid_to_prior_uuid is OrderedDict
        #
        self.uuid_to_prior_uuid = OrderedDict()
        self.pid_to_process = {}
        self.pgid_to_process = {}

        self.fd_to_process = {}
        self.fd_to_file = {}

        self.poll = poll.epoll()
        self.poll.register(0, poll.EPOLLIN)
        #
        # session
        #
        self.is_updated = False
        self.is_loading_session = False

        if 1:
            Display.root.change_attributes(event_mask = Xlib.X.FocusChangeMask | Xlib.X.SubstructureNotifyMask)

        if 1:
            self.poll.register(Display.display.fileno(), poll.EPOLLIN)

        self.process_output = {}

        self.compiz_fd = None
        self.is_animating = False
        self.timers = []
        self.last_animation_time = 0
        self.animation_interval = 1.0 / 30.0
        #
        if self.is_animating:
            #
            #
            #
            self.anim_lambda = self.create_animation_lambda()

        if self.is_animating:
            #
            # Enable this for animation effect (requires Compiz Server plugin to be installed and enabled)
            #
            self.add_timeout(time.time(), self.animate)

        if True:
            # self.check_focus()
            self.add_timeout(time.time() + 1, self.check_focus)

        if 0:
            #
            # print a periodic dot
            #
            self.add_timeout(0, self.tick)

        is_auto_adjust_gamma = 0
        if is_auto_adjust_gamma:
            self.add_timeout(time.time() + 1, self.check_gamma_by_focus)

        # Create empty session
        self.session = Process.create('Session', path = 'session.json', pages = [], edges = [])

        self.is_running = True

        self.to_save = {}

        self.initial_progress = (time.time(), Process.create('Progress', uuid = 'root', progress = 0))

        if 1:
            self.is_reposition_complete = 0
            self.add_fixup_windows_timeout()
            #
            self.is_restack_complete = 0
            self.add_restack_timer()
            
        if 1:
            #
            self.is_save_stacking_timer_running = 0
            self.is_save_position_timer_running = 0
        #
    #
    def get_open_pages(self):
        return list(filter(lambda page: self.is_page_open(page), self.uuid_to_page.values()))
    #
    def collect_all_windows_by_pid(self):
        #
        for page in self.get_open_pages():
            #
            process = self.uuid_to_process[page.uuid]
            #
            pid = process.pid
            #
            clients = WMX.get_clients_by_pid(process.pid)
            #
            for xid in clients:
                #
                wm_name = WMX.get_client_name(xid)
                #
                # if client has a name
                #
                if wm_name is not None:
                    #
                    self.bind_window_to_process(xid, process)
                #
            #
        #
    #
    def reposition_windows(self):
        #
        # Queue.debug(fixing = 1)
        #
        result = 1
        #
        self.collect_all_windows_by_pid()
        #
        for page in self.get_open_pages():
            #
            process = self.uuid_to_process[page.uuid]
            #
            clients = list(WMX.get_clients_by_pid(process.pid))
            #
            if len(clients) > 1:
                #
                Queue.errod([('multiple clients for pid', process.pid)])
                #
            #
            if clients:
                #
                for xid in clients:
                    #
                    window = WMX.get_window_by_xid(xid)
                    #
                    self.moveresize_window(window, page)
                    #
                #
            else:
                #
                Queue.errod([('missing_window', page)])
                #
                result = 0
            #
        #
        return result
    #
    #
    def verify_all_window_positions(self):
        #
        result = 0
        #
        ok_count = 0
        window_count = 0
        page_count = 0
        #
        for page in self.get_open_pages():
            page_count += 1
            process = self.uuid_to_process[page.uuid]
            xid = process.xid
            #
            if xid is not None:
                #
                window = WMX.get_window_by_xid(xid)
                #
                geom = WMX.get_absolute_desktop_window_geometry(xid)
                #
                if geom is not None:
                    #
                    x = geom[0][0]
                    y = geom[0][1]
                    #
                    width = geom[1][0]
                    height = geom[1][1]
                    #
                    # page = self.xid_to_process[xid].page
                    #
                    window_count += 1
                    #
                    if page.x == x and page.y == y and page.width == width and page.height == height:
                        #
                        ok_count += 1
                        #
                        # Queue.infod([('page_ok', page)])
                        #
                    else:
                        #
                        diff = (x - page.x, y - page.y, width - page.width, height - page.height)
                        #
                        # uuid = '2726dac4'
                        #
                        Queue.errod([('bad position', page), ('geom', geom), ('diff', diff), ('xid', hex(xid))])
                        #
                        # self.moveresize_window(window, page)
                        #
                    #
                #
            #
            else:
                #
                Queue.errod([('missing_window', page)])
                #
            #
        #
        # Queue.debug(ok_count = ok_count, page_count = page_count, window_count = window_count)
        #
        if ok_count == page_count:
            #
            # Queue.infod([('info', 'reposition_complete')])
            #
            result = 1
            #
        #
        return result
    #
    #
    def fixup_windows_timeout(self):
        #
        self.reposition_windows()
        #
        if self.verify_all_window_positions():
            #
            # Queue.infod([('info', 'reposition_complete')])
            #
            self.is_reposition_complete = 1
            #
        else:
            #
            # redo fixup
            #
            self.add_fixup_windows_timeout()
            #
        #
    #
    def add_fixup_windows_timeout(self):
        self.add_timeout(time.time() + 1.0, self.fixup_windows_timeout)
        #
    #
    def restack_windows_timer(self):
        #
        if self.verify_stacking():
            #
            # Queue.infoex(comment = 'restack complete')
            #
            self.is_restack_complete = 1
        else:
            self.restack_windows()
            self.add_restack_timer()
        #
    #
    def add_restack_timer(self):
        self.add_timeout(time.time() + 1.0, self.restack_windows_timer)
        #
    #
    def tick(self):
        os.write(2, '.\n')
        dt = 1.0
        self.add_timeout(time.time() + dt, self.tick)

    @classmethod
    def is_local_pdf_path(WebSession, url):
        #
        result = 0
        #
        if url.endswith('.pdf'):
            if url.startswith('/') or url.startswith('file://'):
                result = 1
            #
        #
        return result
        #
    #
    def register_process(self, process):
        #
        fd_stdout = process.stdout.fileno()
        #
        self.poll.register(fd_stdout, poll.EPOLLIN)
        #
        self.fd_to_process[fd_stdout] = process
        self.fd_to_file[fd_stdout] = process.stdout
        #
        fd_stdin = process.stdin.fileno()
        #
        self.fd_to_process[fd_stdin] = process
        self.fd_to_file[fd_stdin] = process.stdin
        #
    #
    def unregister_process(self, process):
        #
        del self.pid_to_process[process.pid]
        del self.pgid_to_process[process.pgid]

        self.forget_fd(process.stdout.fileno())
        self.forget_fd(process.stdin.fileno())
        #
        if process.xid is not None:
            del self.xid_to_process[process.xid]
    #
    def kill_process(self, process):
        #
        process.kill()
        #
        result = process.wait()
        #
        return result
    #
    def spawn_process(self, page):
        #
        progress = Process.create('Progress', uuid = page.uuid, progress = 0.0)
        #
        if 1:
            argpage = page._replace(x = None, y = None, width = None, height = None)
            #
            if self.is_local_pdf_path(argpage.url):
                #
                pipeline = ['evince', argpage.url]
                #
                # TODO: get progress from evince
                #
                progress = progress._replace(progress = 1.0)
                #
            else:
                if 1:
                    if 1:
                        if 0:
                            pipeline = ['./gdkkeytest.py']
                        else:
                            if 1:
                                pipeline = [self.BROWSER_PATH]
                            else:
                                pipeline = ['./webkitgtk.py']
                    else:
                        pipeline = ['./browser.py']
                else:
                    pipeline = ['./chromaster.py']

                pipeline.append(Code.dumps(argpage))
                #
            #
        #
        #
        # Queue.debug(pipeline = pipeline)
        #
        if 1:
            #
            # create directory for page session
            #
            Session.make_page_dir(page)
            #
            # create named pipes under Page session directory
            #
            stdin_path = Session.get_stdin_path(page)
            stdout_path = Session.get_stdout_path(page)
            #
            # Queue.infoex('stdin_path', 'stdout_path')
            #
            # if true, child will open named pipe as stdin before invoking
            # execve.  otherwise, child will open the named pipe "stdin"
            # separately.
            #
            is_child_use_stdin_pipe = 0

            def _preexec():
                #
                # make new process group
                #
                if 1:
                    os.setpgid(0, 0)
                #
                # use named pipes to communicate with child process
                #
                if is_child_use_stdin_pipe:
                    #
                    stdin_pipe = Pipe.open_read(Pipe.create_from_path(stdin_path))
                    stdout_pipe = Pipe.open_write(Pipe.create_from_path(stdout_path))
                    #
                    os.close(0)
                    os.close(1)
                    #
                    os.dup(stdin_pipe.fd)
                    os.dup(stdout_pipe.fd)
                    #
                #
                # leave stderr alone for now
                #
            #
            # fork and exec child process
            #
            process = subprocess.Popen(pipeline, preexec_fn = _preexec)

            #
            # invert read & write arity
            #
            stdin_pipe = Pipe.open_write(Pipe.create_from_path(stdin_path))
            stdout_pipe = Pipe.open_read(Pipe.create_from_path(stdout_path))

            #
            process.pgid = os.getpgid(process.pid)
            #
            # Queue.debug(pid = process.pid, pgid = process.pgid)
            #

            process.stdin_fd = stdin_pipe.fd
            process.stdout_fd = stdout_pipe.fd
            #
            # we write to process stdin
            #
            process.stdin = os.fdopen(stdin_pipe.fd, 'wb')
            #
            # we read from process stdout
            #
            process.stdout = os.fdopen(stdout_pipe.fd, 'rb')
            #
        #

        #
        # Queue.debug(pipeline = ' '.join(pipeline), pid = process.pid)
        #
        process.start_time = time.time()
        process.page = page
        process.xid = None
        process.progress = progress
        process.is_mapped = 0
        process.was_focused = 0
        process.is_window_placed = 0
        #
        self.pid_to_process[process.pid] = process
        self.pgid_to_process.setdefault(process.pgid, []).append(process)
        #
        self.register_process(process)
        #
        self.uuid_to_process[page.uuid] = process
        #
        return process

    @classmethod
    def import_session_buddy(self, path):
        import random
        display_width = 1920 * 2
        display_height= 1080 * 2
        pages = []
        with open(path) as infile:
            infile.seek(3)
            input_session = json.load(infile)
            for session in input_session['sessions']:
                if session['type'] == 'current':
                    for window in session['windows']:
                        for tab in window['tabs']:
                            x = random.randint(0, display_width - tab['width'])
                            y = random.randint(0, display_height - tab['height'])
                            pages.append(Process.create('Page', uuid = Page.gen_uuid(), url = tab['url'], x = x, y = y, width = tab['width'], height = tab['height'], is_open = False, is_run_in_background = False))
        return pages

    def add_save_session_timeout(self):
        self.add_timeout(time.time() + 0.1, self.save_session_timeout)
        #
    #
    def save_data_to_session_object(self):
        #
        # save data to session
        #
        self.session = self.session._replace(pages = self.uuid_to_page.values())
        #
        edges = []
        #
        for (uuid, prior_uuids) in self.uuid_to_prior_uuid.items():
            for (prior_uuid, p2p) in prior_uuids.items():
                edges.append(p2p)
            #
        #
        self.session = self.session._replace(edges = edges)
        #
    #
    def save_session_timeout(self):
        if not self.is_loading_session:
            #
            # Queue.debug(save_session_timeout = True)
            #
            self.save_data_to_session_object()
            #
            self.save_session(self.session)
            #
            # save individual page directories
            #
            self.save_page_dirs()
            #
            # clear flag so updates can proceed
            #
            self.is_updated = False
        else:
            self.add_save_session_timeout()

    @classmethod
    def clamp_page(WebSession, page):
        #
        # _NET_MOVERESIZE_WINDOW doesn't accept negative x or y values
        #
        m = 50
        #
        if page.x < m:
            page = page._replace(x = m)
        #
        if page.y < m:
            page = page._replace(y = m)
        #
        screen_width = Display.screen.width_in_pixels
        screen_height = Display.screen.height_in_pixels
        #
        if page.x > screen_width - m:
            page = page._replace(x = screen_width - m)
        #
        if page.y > screen_height - m:
            page = page._replace(y = screen_height - m)
        #
        #
        return page
        #
    #
    def change_null_dimensions_to_default(self, page):
        #
        # self.get_page_by_uuid(page.)
        # self.uuid_to_page
        #
        if page.x is None or page.y is None or page.width is None or page.height is None:
            #
            #
            screen_width = Display.screen.width_in_pixels
            screen_height = Display.screen.height_in_pixels
            #
            # make page portrait aspect
            #
            phi = 1.6180339887
            #
            dh = int(screen_height * 0.75)
            dw = int(dh / phi)
            #
            # center within screen
            #
            dx = int((screen_width - dw) * 0.5)
            dy = int((screen_height - dh) * 0.5)
            #
            page = page._replace(x = dx, y = dy, width = dw, height = dh)
            #
        #
        return page
        #
    #
    @classmethod
    def is_any_page_dimension_none(self, page):
        result = page.x is None or page.y is None or page.width is None or page.height is None
        return result
        #
    #
    def move_null_page_to_prior(self, page):
        #
        # self.get_page_by_uuid(page.)
        # self.uuid_to_page
        #
        if self.is_any_page_dimension_none(page):
            #
            prior_pages = self.get_prior_pages(page)
            #
            # Queue.infoex('page', 'prior_pages', comment = 'checking for prior pages')
            #
            for prior_page in prior_pages:
                #
                # Queue.debug(prior_page = prior_page, page = page)
                #
                if not self.is_any_page_dimension_none(prior_page):
                    #
                    px = prior_page.x + 64
                    py = prior_page.y + 64
                    pw = prior_page.width
                    ph = prior_page.height
                    #
                    # position given page to be nearby prior in some respect
                    #
                    page = page._replace(x = px, y = py, width = pw, height = ph)
                    #
                    # Queue.debug(new_page = page)
                    #
                    break
                    #
                #
            #
        else:
            #
            # Queue.debug(page_not_null = page)
            pass
            #
        #
        return page
        #
    #
    def save_page(self, page):
        #
        self.to_save[page.uuid] = page
        #
        # update process page
        #
        if not self.is_updated:
            #
            self.is_updated = True
            #
            self.add_save_session_timeout()
            #
        #
    #
    def get_page_by_uuid(self, uuid):
        result = None
        for page in self.session.pages:
            if page.uuid == uuid:
                result = page
                break
        return result

    def Open(self, _open):
        #
        page = self.uuid_to_page[_open.uuid]
        page = page._replace(is_open = True)
        #
        self.Page(page)
        #
        return True

    def close_process_fd(self, fd):
        #
        # Queue.debug(fd = fd)
        #
        if fd == 0:
            self.CloseAll(Process.create('CloseAll'))
            #
            self.is_running = False
        else:
            #
            process = self.fd_to_process.get(fd)
            #
            if process is not None:
                #
                # Queue.debug(closing = process.page.uuid)
                #
                self.Close(Process.create('Close', uuid = process.page.uuid, is_permanent = False))
        pass

    def write_to_process(self, uuid, outbuf):
        #
        # Queue.debug(writing_to_uuid = uuid, outbuf = outbuf)
        #
        process = self.uuid_to_process[uuid]
        #
        if 1:
            #
            fd = process.stdin.fileno()
            #
            buf = self.process_output.pop(fd, None)
            #
            if buf is None:
                buf = outbuf
            else:
                buf += outbuf
            #
            # Queue.edumps(pollout_fd = fd)
            #
            try:
                self.poll.register(fd, poll.EPOLLOUT)
            except IOError as e:
                if e.errno != errno.EEXIST:
                    raise
            #
            self.process_output[fd] = buf
            #
            # Queue.edumps(process_output = self.process_output)
            #

    def get_timeout(self):
        if self.is_animating:
            return 0
        else:
            return -1

    def get_mouse_pos(self):
        d = Display.root.query_pointer()._data
        return (d['root_x'], d['root_y'])

    def get_focus_window_pid(self):
        result = None

        focus = self.get_focus_window()

        while True:
            pid = self.get_window_pid(focus)
            #
            # Queue.debug(focus = focus, pid = pid)
            #
            parent = focus.query_tree().parent
            if parent == Display.root:
                # found toplevel
                break
            else:
                #
                # Queue.debug(moving_to_parent = parent)
                #
                focus = parent

        return result

    def check_gamma_by_focus(self):
        #
        focus_window = self.get_focus_window()

        focus_pid = self.get_window_pid(focus_window)

        #
        # Queue.debug(focus_window = focus_window, focus_pid = focus_pid)
        #

        gamma = 2.3
        #
        for (pid, process) in self.pid_to_process.items():
            if focus_pid == pid:
                gamma = 1.0
            else:
                pass

        #
        # Queue.debug(gamma = gamma)
        #
        self.set_gamma(gamma)
        #
        self.add_timeout(time.time() + 1, self.check_gamma_by_focus)

    def check_focus(self):
        #
        # Queue.infoex(comment = 'checking focus')
        #
        focus_window = self.get_focus_window()
        #
        # Queue.infoex('focus_window')

        focus_pid = self.get_window_pid(focus_window)

        #
        # Queue.debug(focus_window = focus_window, focus_pid = focus_pid)
        #

        for (pid, process) in self.pid_to_process.items():
            if focus_pid == pid or process.page.is_run_in_background:
                #
                # Queue.infoex('process.page', comment = 'resuming focused process')
                #
                self.resume_process(process.page.uuid)
            else:
                #
                # Queue.infoex('process.page', comment = 'suspending unfocused process')
                #
                self.suspend_process(process.page.uuid)

        self.add_timeout(time.time() + 10, self.check_focus)

    @classmethod
    def set_gamma(self, gamma):
        """
        change display gamma in order to read web pages designed for 1.0 gamma
        """
        # if not hasattr(self, '_gamma') or self._gamma != gamma:
        if 1:
            self._gamma = gamma
            #
            argv = ['xgamma', '-gamma', str(self._gamma)]
            #
            command = ' '.join(argv)
            #
            print('command', command)
            #
            retcode = os.system(command)
            #
            if retcode != 0:
                #
                # Queue.debug(0, command = command, retcode = retcode)
                #
                pass
                #
            #
        #
    #
        
    @classmethod
    def get_focus_window(self):
        focus_window = Display.display.get_input_focus().focus
        return focus_window

    @classmethod
    def get_window_pid(self, window):
        result = None
        loop = True
        while loop:
            #
            # Queue.debug(window = window)
            #
            # master = WMX.get_master_window(window.id)
            if isinstance(window, Display.root.__class__):
                try:
                    result = window.get_full_property(_NET_WM_PID, 0)
                except Xlib.error.BadWindow as e:
                    #
                    # Queue.debug(fn = self.get_window_pid, bad_window = window)
                    #
                    loop = False
                else:
                    if not result:
                        parent = window.query_tree().parent
                        if parent != Display.root:
                            window = parent
                        else:
                            loop = False
                    else:
                        result = result.value[0]
                        #
                        # Queue.debug(found_pid = result)
                        #
                        loop = False
            else:
                break

        return result

    def suspend_process(self, uuid):
        #
        if not self.is_animating:
            #
            # self.set_event_mask(uuid, False)
            #
            process = self.uuid_to_process.get(uuid)
            #
            if process is not None:
                #
                is_suspend = not process.page.is_run_in_background
                #

                if 1:
                    #
                    process_time = time.time() - process.start_time
                    #
                    # avoid suspending new windows
                    #
                    if is_suspend:
                        if process_time < 180:
                            #
                            # Queue.debug(progress = process.progress)
                            #
                            if process.progress.progress < 1.0:
                                #
                                # Queue.infoex('process.progress', comment = 'not suspending new process while loading')
                                #

                                #
                                is_suspend = False
                            else:
                                #
                                # is_suspend = False
                                #
                                pass


                #
                # Queue.infoex('is_suspend')
                #
                if 1:
                    #
                    # cancel suspending active window
                    #
                    if is_suspend:
                        #
                        focus_window = self.get_focus_window()
                        #
                        if focus_window is not None:
                            #
                            if 0:
                                focus_process = self.get_process_by_xid(focus_window.id)
                                if focus_process is not None:
                                    focus_window_pid = focus_process.pid
                                else:
                                    focus_window_pid = None
                            else:
                                focus_window_pid = self.get_window_pid(focus_window)

                            if focus_window_pid is not None:
                                #
                                # Queue.debug(focus_window_pid = focus_window_pid, process_pid = process.pid)
                                #
                                if process.pid == focus_window_pid:
                                    #
                                    # Queue.infoex('process.pid', 'process.page', comment = 'not suspending focused process')
                                    #
                                    #
                                    is_suspend = False

                # is_suspend = False
                # Queue.debug(disable_suspend = True)
                # Queue.debug(is_suspend = is_suspend)
                #
                if is_suspend:
                    #
                    # Queue.infoex('process.page', 'process.pgid', 'process.pid', comment = 'suspending process')
                    #
                    os.kill(-process.pgid, signal.SIGSTOP)
                    pass
                else:
                    # Queue.debug(not_suspending = uuid, is_run_in_background = process.page.url)
                    pass
            else:
                #
                Queue.errex('uuid', comment = 'no process to suspend')
                #
                pass

    def resume_process(self, uuid):
        process = self.uuid_to_process.get(uuid)
        if process is not None:
            #
            #
            #
            # Queue.infoex('process.page', 'process.pgid', 'process.pid', comment = 'resuming process')
            #
            os.kill(-process.pgid, signal.SIGCONT)
            #
        # self.set_event_mask(uuid, True)

    def get_process_by_xid(self, xid):
        process = self.xid_to_process.get(xid)
        return process
        #
    #
    @classmethod
    def set_normal_hints(WebSession, window):
        #
        window.set_wm_normal_hints(flags = Xlib.Xutil.PPosition | Xlib.Xutil.PSize)
        #

    def setup_window(self, xid):
        #
        # Queue.debug(added_new_focus_watch = xid)
        #
        window = WMX.get_window_by_xid(xid)
        #
        window.change_attributes(event_mask = Xlib.X.FocusChangeMask | Xlib.X.StructureNotifyMask)
        #
        if 1:
            #
            self.set_normal_hints(window)
    #
    def bind_window_to_process(self, xid, process):
        #
        if xid != process.xid:
            if_rebind_window = 0
            if if_rebind_window:
                if process.xid is not None:
                    #
                    # break prior binding
                    #
                    Queue.infoex('xid', 'process.xid', comment = 'xid changed, ignoring')
                    #
                    del self.xid_to_process[process.xid]
                    #
                    # rebind xid and process
                    #
                #
            #
            if if_rebind_window or process.xid is None:
                #
                # only accept the first window
                #
                # process to xid
                #
                process.xid = xid
                #
                # xid to process
                #
                self.xid_to_process[process.xid] = process
                #
                if 1:
                    self.setup_window(xid)
                    #
                #
            else:
                #
                Queue.infoex('xid', 'process.xid', 'process.page.uuid', comment = 'ignoring new xid for process')
                #
            #
        else:
            #
            # Queue.debug(already_added = hex(xid), process = process)
            #
            pass
        #
    #
    @classmethod
    def moveresize_window(WebSession, window, page):
        #
        WebSession.set_normal_hints(window)
        #
        # ensure the window conforms to page dimensions
        #
        xid = window.id
        #
        # page = self.adjust_page_for_frame_extents(xid, page)
        #
        # Queue.debug(resizing_window = page, window = hex(window.id))
        #
        px = int(page.x)
        py = int(page.y)
        pw = int(page.width)
        ph = int(page.height)
        #
        # Queue.infod([('moveresize', page), ('xid', hex(xid)), ('position', (px, py, pw, ph))])
        #
        WMX.moveresize_window(xid, px, py, pw, ph)
        #
    #
    def get_all_pending_events(self):
        #
        xevents = [Display.display.next_event() for i in range(Display.display.pending_events())]
        #
        return xevents
    #
    def save_stacking_timer(self):
        self.save_stacking()
        self.is_save_stacking_timer_running = 0
        
    def add_save_stacking_timer(self):
        if not self.is_save_stacking_timer_running:
            self.is_save_stacking_timer_running = 1
            self.add_timeout(time.time() + 0.1, self.save_stacking_timer)
    #
    def save_position(self):
        #
        result = 1
        #
        for page in self.get_open_pages():
            process = self.uuid_to_process[page.uuid]
            #
            xid = process.xid
            #
            if xid is not None:
                #
                window = WMX.get_window_by_xid(xid)
                #
                geom = WMX.get_absolute_desktop_window_geometry(xid)
                #
                if geom is not None:
                    #
                    x = geom[0][0]
                    y = geom[0][1]
                    #
                    width = geom[1][0]
                    height = geom[1][1]
                    #
                    newpage = page._replace(x = x, y = y, width = width, height = height)
                    #
                    if newpage != page:
                        #
                        # Queue.infoex('newpage', 'page', comment = 'page moved')
                        #
                        self.Page(newpage)
                    #
                else:
                    #
                    Queue.errex('page', 'hex(xid)', comment = 'failed to get geometry')
                    #
                    result = 0
                #
            #
            else:
                #
                Queue.errex('page', comment = 'missing_window')
                #
                result = 0
            #
        #
        return result
    #
    #
    def save_position_timer(self):
        self.save_position()
        self.is_save_position_timer_running = 0
        #
    #
    def add_save_position_timer(self):
        if not self.is_save_position_timer_running:
            self.is_save_position_timer_running = 1
            self.add_timeout(time.time() + 0.1, self.save_position_timer)
            #
        #
    #
    #
    def get_process_by_pid(self, pid):
        #
        # given a window pid, find the process
        # by pid directly or process group id
        # if the pid is not found.
        #
        process = self.pid_to_process.get(pid)
        #
        if process:
            #
            # Queue.infoex('process', 'pid', comment = 'found by pid')
            #
            pass
        else:
            #
            pgid = os.getpgid(pid)
            #
            processes = self.pgid_to_process.get(pgid)
            #
            if processes:
                #
                # pick first process in group
                #
                process = processes[0]
                #
                # Queue.infoex('pid', 'pgid', 'process.pid', 'len(processes)', comment = 'found by pgid')
                #
                if len(processes) > 1:
                    #
                    Queue.infoex('pid', 'pgid', comment = 'multiple processes')
                    #
                #
            #
        #
        return process
    #
    #
    def handle_xevent(self):
        #
        xevents = self.get_all_pending_events()
        #
        # Queue.debug(0, xevents = xevents)
        #
        for xevent in xevents:
            #
            # Queue.debug(xevent = xevent)
            #
            if hasattr(xevent, 'window'):

                window = xevent.window

                if xevent.type == Xlib.X.CreateNotify:
                    #
                    # print the xid like xwininfo
                    #
                    xid = '0x% 8x' % window.id
                    #
                    attrs = WMX.get_attributes(window.id)
                    #
                    if attrs is not None:
                        #
                        # window_name = WMX.get_client_name(window.id)
                        #
                        # Queue.infod([('CreateNotify', xevent), ('xid', hex(window.id)), ('attrs', attrs), ('window_name', window_name)])
                        #
                        is_toplevel = attrs.override_redirect == 0
                        #
                        # Queue.debug(is_toplevel = is_toplevel, xid = hex(window.id))
                        #
                        if is_toplevel:
                            #
                            # compiz sets this to _NET_WM_WINDOW_TYPE_NORMAL for the main window
                            #
                            window_type = WMX.get_property_value_by_name('_NET_WM_WINDOW_TYPE', window.id)
                            #
                            if type(window_type) is array.array:
                                #
                                window_type = int(window_type[0])
                                #
                            #
                            window_type_normal = window_type == _NET_WM_WINDOW_TYPE_NORMAL
                            #
                            # Queue.infod([('window_type_normal', window_type_normal), ('xid', hex(window.id))])
                            #
                            if 1 or window_type_normal:
                                #
                                window_pid = WMX.get_property_value_by_name('_NET_WM_PID', window.id)
                                #
                                # Queue.infod([('xid', hex(window.id)), ('window_pid', window_pid)])
                                #
                                if window_pid is not None:
                                    #
                                    window_pid = int(window_pid[0])
                                    #
                                    process = self.get_process_by_pid(window_pid)
                                    #
                                    # Queue.debug(process = process)
                                    #
                                    if process is not None:
                                        if 1:
                                            #
                                            transient_for = WMX.get_property_value_by_name('WM_TRANSIENT_FOR', window.id)
                                            #
                                            # Queue.infoex('transient_for', 'xid')
                                            #
                                        #
                                        if_has_attrs = attrs is not None
                                        assert if_has_attrs
                                        #
                                        if_input_output = attrs.win_class == X.InputOutput
                                        #
                                        client_name = WMX.get_client_name(window.id)
                                        #
                                        # Queue.infoex('xid', 'process.pid', 'process.pgid', 'client_name', 'if_input_output')
                                        #
                                        if if_has_attrs and if_input_output:
                                            #
                                            if 0:
                                                #
                                                master = WMX.get_master_window(window.id)
                                                #
                                                # Queue.debug(master = hex(master.id), window = hex(window.id))
                                                #
                                                if master.id != window.id:
                                                    #
                                                    Queue.debug(msg = 'window was not master', window = hex(window.id), master = hex(master.id))
                                                    #
                                                #
                                            #
                                            self.bind_window_to_process(window.id, process)
                                            #
                                            # only moveresize first window encountered by an app
                                            #
                                            if 1:
                                                if not process.is_window_placed:
                                                    #
                                                    self.moveresize_window(window, process.page)
                                                    #
                                                #
                                            #
                                        #
                                        else:
                                            #
                                            # bad attrs
                                            #
                                            pass
                                    #
                                else:
                                    #
                                    # no window pid
                                    #
                                    pass
                                    #
                                #
                            else:
                                #
                                # Queue.debug(not_normal = hex(window.id))
                                #
                                pass
                            #
                        #
                    else:
                        #
                        # failed to get attributes
                        #
                        pass
                #
                elif xevent.type == Xlib.X.PropertyNotify:
                    property_name = Display.display.get_atom_name(xevent.atom)
                    #
                    value = WMX.get_property_value_by_atom(xid = window.id, atom = xevent.atom)
                    #
                    # Queue.debug(property_name = property_name, property_value = value, xid = hex(window.id))
                #
                elif xevent.type == Xlib.X.MapNotify:
                    #
                    process = self.get_process_by_xid(window.id)
                    #
                    if process is not None:
                        #
                        process.is_mapped = 1
                        process.map_sequence = xevent.sequence_number
                        #
                        self.moveresize_window(window, process.page)
                    #
                #
                elif xevent.type == Xlib.X.ConfigureNotify:
                    #
                    # Queue.debug(ConfigureNotify = xevent)
                    #
                    process = self.get_process_by_xid(window.id)
                    #
                    if process is not None:
                        #
                        #
                        # one of our windows has resized or moved
                        #
                        # Queue.debug(msg = 'found process by ConfigureNotify window')
                        #
                        # import xpy; xpy.start_console()
                        #
                        page = process.page
                        #
                        # change position and size of page
                        #
                        npage = page._replace(x = xevent.x, y = xevent.y, width = xevent.width, height = xevent.height)
                        #
                        # Queue.infoex('xevent', 'page', 'process.pid', comment = 'ConfigureNotify')
                        #
                        diff = (npage.x - page.x, npage.y - page.y, npage.width - page.width, npage.height - page.height)
                        if 1:
                            #
                            #
                            attrs = WMX.get_attributes(window.id)
                            #
                            # Queue.infoex('process.was_focused', 'attrs.map_state if attrs else None', comment = 'process.is_mapped')
                            #
                            # if process.is_mapped and process.was_focused:
                            if 1:
                                #
                                process_time = time.time() - process.start_time
                                #
                                minprocesstime = 1.0
                                #
                                # Queue.infoex('process_time', 'process_time > minprocesstime', 'hex(window.id)', comment = 'checking process_time')
                                #
                                if process_time > minprocesstime:
                                    #
                                    is_fixup_complete = self.is_reposition_complete and self.is_restack_complete
                                    #
                                    # Queue.infoex('is_fixup_complete', 'self.is_reposition_complete', 'self.is_restack_complete', comment = 'check fixup')
                                    #
                                    if is_fixup_complete:
                                        #
                                        # assert not any(diff)
                                        #
                                        # Queue.debug(xid = hex(window.id), diff = diff)
                                        #
                                        # npage = self.adjust_page_for_frame_extents(window.id, npage)
                                        #
                                        # adjust dimensions
                                        #
                                        # Queue.debug(allow_position = npage)
                                        #
                                        #
                                        if 1:
                                            self.add_save_position_timer()
                                        else:
                                            self.Page(npage)
                                        #
                                        if 1:
                                            self.add_save_stacking_timer()
                                            #
                                else:
                                    #
                                    # assert position
                                    #
                                    # Queue.debug(assert_position = process.page, xid = hex(window.id), diff = (npage.x - page.x, npage.y - page.y, npage.width - page.width, npage.height - page.height))
                                    #
                                    if 0:
                                        self.moveresize_window(window, process.page)
                                        #
                                        # force restack
                                        #
                                        self.restack_windows()
                                    pass
                            else:
                                #
                                # Queue.debug(msg = 'ignoring ConfigureNotify on unmapped window')
                                pass
                                #
                                # self.moveresize_window(window, process.page)
                                #
                            #
                        #
                    #
                #
                elif xevent.type == Xlib.X.FocusIn:
                    #
                    process = self.get_process_by_xid(window.id)
                    #
                    if process is not None:
                        #
                        process.was_focused = True
                        #
                    #
                #
                if 0:
                    #
                    # debug focus events
                    #
                    if xevent.type == Xlib.X.FocusOut:
                        Queue.debug(xevent = xevent)

                    if xevent.type == Xlib.X.FocusIn:
                        Queue.debug(xevent = xevent)

                #
                process = self.get_process_by_xid(window.id)
                #
                if process is not None:
                    #
                    uuid = process.page.uuid
                    #
                    # Queue.debug(xevent = xevent)
                    #
                    if xevent.type == Xlib.X.FocusOut and xevent.detail == 4 and (xevent.mode == 0 or xevent.mode == 3):
                        #
                        # Queue.debug(FocusOut = process.page)
                        #
                        self.add_timeout(time.time() + 1, (lambda uuid: lambda: self.suspend_process(uuid))(uuid))
                        #
                    if xevent.type == Xlib.X.FocusIn and xevent.detail == 3:
                        #
                        # Queue.debug(FocusIn = process.page)
                        #
                        self.add_timeout(time.time() + 1e-2, (lambda uuid: lambda: self.resume_process(uuid))(uuid))
                    #
                #
            #
            else:
                #
                # no window
                #
                # Queue.infoex('xevent', comment = 'no window')
                #
                pass
                #
            #
        #
        if 1:
            #
            Display.display.flush()
            Display.display.sync()
            #
        #
    #
    #
    def add_timeout(self, t1, fn):
        heapq.heappush(self.timers, (t1, fn))

    def EventLoop(self, msg):
        while self.is_running:
            #
            # wait forever
            #
            timeout = -1
            #
            while len(self.timers):
                #
                # Queue.debug(timers = len(self.timers))
                #
                #
                # fetch the next timer
                #
                at = self.timers[0][0]
                #
                # compute time error
                #
                err = at - time.time()
                #
                # Queue.debug(err = err)
                #
                # if (err - (1.0 / 240)) < 0:
                # if err < 0:
                #
                if err <= 0:
                    (at, fn) = heapq.heappop(self.timers)
                    #
                    # Queue.debug(running_timer = fn)
                    #
                    fn()
                    #
                    # reset timeout
                    #
                    # timeout = -1
                else:
                    #
                    # no timers are ready
                    #
                    #
                    # Queue.debug(remainder = err)
                    #
                    timeout = err
                    #
                    break
            #
            # Queue.debug(polling = True, timeout = timeout)
            #
            assert timeout == -1 or timeout >= 0
            #
            # poll
            #
            self.do_poll(timeout)

    def do_poll(self, timeout):
        #
        result = False
        #
        is_flush = True
        if is_flush:
            # Queue.debug(flushing = Display.display)
            Display.display.flush()
            # Queue.debug(done_flushing = Display.display)
        is_sync = True
        if is_sync:
            #
            # not sure what this helps
            #
            Display.display.sync()
        #
        try:
            # Queue.debug(polling = timeout)
            events = self.poll.poll(timeout)
        except IOError as e:
            if e.errno != errno.EINTR:
                raise
            else:
                events = []
        #
        # Queue.debug(done_polling = len(events))
        # Queue.debug(events = len(events))
        #
        if len(events):
            #
            # Queue.debug(events = events)
            #
            for (fd, event) in events:
                #
                process = self.fd_to_process.get(fd)
                #
                # Queue.debug(event = event, fd = fd)
                #
                if event & poll.EPOLLIN:
                    self.handle_input_data(fd)

                if event & poll.EPOLLOUT:
                    #
                    # Queue.debug(event = event)
                    #
                    buf = self.process_output.pop(fd, None)
                    #
                    if buf:
                        #
                        # Queue.edumps(writing = buf)
                        #
                        buf = buf[os.write(fd, buf):]
                        self.process_output[fd] = buf
                    else:
                        #
                        Queue.debug(unregistering = fd)
                        #
                        self.poll.unregister(fd)

                if event & poll.EPOLLHUP:
                    #
                    Queue.debug(EPOLLHUP = fd)
                    #
                    self.close_process_fd(fd)
                    #
            result = True
        return result

    def handle_input_data(self, fd):
        if fd == Display.display.fileno():
            self.handle_xevent()
        else:
            if fd == 0:
                infile = sys.stdin
            else:
                infile = self.fd_to_file.get(fd)
            # buf = os.read(fd, int(1e6))
            try:
                buf = infile.readline()
            except IOError as e:
                #
                Queue.debug(exception = e)
                #
                if e.errno != errno.EAGAIN:
                    raise
                buf = None
            else:
                if buf:
                    if 0:
                        if not Process.process_argv([buf], self):
                            #
                            Queue.debug(error = buf)
                            #
                    else:
                        #
                        # Queue.debug(buf = buf)
                        #
                        msg = Code.loads(buf)
                        #
                        if msg is not None:
                            if hasattr(msg, 'prototype'):
                                #
                                # Queue.debug(msg = msg)
                                #
                                if 1:
                                    Process.invoke_handler(msg, self)
                                else:
                                    cb = getattr(self, msg.prototype, None)
                                    if cb is not None:
                                        #
                                        # Queue.debug(got_cb = msg.prototype, cb = cb)
                                        #
                                        if not cb(msg):
                                            Queue.debug(error = msg)
                                    else:
                                        Queue.debug(unhandled = msg)
                else:
                    #
                    self.close_process_fd(fd)
                    #
                    # process will POLLHUP
                    #
                    pass

    def CloseAll(self, arg):
        #
        for uuid in list(self.uuid_to_page.keys()):
            #
            self.Close(Process.create('Close', uuid = uuid, is_permanent = False))
            #
        #
        return True

    def Close(self, close):
        #
        page = self.uuid_to_page[close.uuid]
        #
        page = page._replace(is_open = False)
        #
        if close.is_permanent:
            page = page._replace(is_deleted = True)
            #
        #
        self.Page(page)
        #
        return True

    def forget_fd(self, fd):
        #
        # Queue.debug(forget = fd)
        #

        self.fd_to_file.pop(fd, None)
        self.fd_to_process.pop(fd, None)
        self.process_output.pop(fd, None)

        if 1:
            #
            # Queue.debug(forget_unregister = fd)
            #
            try:
                self.poll.unregister(fd)
            except IOError as e:
                if e.errno == errno.ENOENT:
                    #
                    # process stdin is only registered when we have something
                    # to write to it
                    #
                    Queue.debug(0, not_registered = fd)
                else:
                    raise

    def open_compiz_server(self):
        if self.compiz_fd is None:
            self.compiz_fd = os.open('/tmp/compiz-server.input', os.O_WRONLY)
        return self.compiz_fd is not None

    @classmethod
    def adjust_page_for_frame_extents(WebSession, xid, page):
        #
        for i in range(10):
        # while True:
            #
            try:
                extents = WMX.get_property_value_by_name('_NET_FRAME_EXTENTS', xid)
            except Xlib.error.BadWindow as e:
                extents = None
            else:
                #
                if extents is not None:
                    #
                    Queue.debug(found_extents = extents)
                    #
                    break
                else:
                    #
                    Queue.debug(notice = 'waiting for frame extents...')
                    #
                    time.sleep(1e-3)
                    #
        #
        if extents is not None:
            (frame_left, frame_right, frame_top, frame_bottom) = extents
            #
            px = page.x - frame_left
            py = page.y - frame_top
            pw = page.width
            ph = page.height
            #
            newpage = page._replace(x = px, y = py, width = pw, height = ph)
        else:
            newpage = None
        #
        return newpage

    @classmethod
    def create_animation_lambda(self):
        # This improves performance greatly over using np.matrix
        # multiplication.
        import sympy as sp
        s, tx, ty, tz = sp.symbols('s tx ty tz')
        scale = sp.Matrix([
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])
        translation = sp.Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [tx, ty, tz, 1],
        ])
        return sp.lambdify(sp.symbols('s tx ty tz'), sp.flatten(translation.inv() * scale * translation))

    def animate(self):

        a = time.time()

        self.add_timeout(a + self.animation_interval, self.animate)

        self.last_animation_time = a

        # Queue.debug(timers = self.timers)

        if 1:
            (mx, my) = self.get_mouse_pos()

        if 0:
            # Ordered stacking (too slow)
            stacking = []

        lines = []
        t = 0.0
        v = 2 * math.pi / len(self.uuid_to_process)
        i = 0
        screen_width = Display.screen.width_in_pixels
        screen_height = Display.screen.height_in_pixels
        scx = screen_width * 0.5
        scy = screen_height * 0.5

        is_use_compiz = False

        # Queue.debug(screen_width = screen_width, screen_height = screen_height)
        for (i, process) in enumerate(self.uuid_to_process.values()):
            xid = process.xid
            if xid is not None:
                window = WMX.get_window_by_xid(xid)
                page = process.page

                #
                # dimensions of page window
                #
                x = page.x
                y = page.y
                #
                width = page.width
                height = page.height

                #
                # center point of window
                #
                cx = x + width * 0.5
                cy = y + height * 0.5
                cz = 0

                # t += v

                s = 0.5 + 0.5 * math.cos(a + t * 0)

                tx = screen_width * 0.5 + width * 0.5
                ty = screen_height * 0.5 + height * 0.5
                tz = 0

                tx = -x
                ty = -y

                tx = 0
                ty = 0

                # s = 1

                # Queue.debug(tx = tx, ty = ty)

                # s = max(min(s, 1), 0)

                if 0:
                    md = math.sqrt((mx - cx) ** 2 + (my - cy) ** 2)

                    md /= 500.0

                    Queue.debug(md = md)
                    # Queue.debug(mx = mx, my = my)
                    # Queue.debug(tx = tx, ty = ty)
                    s = min(max(2 - md, 0.25), 2)
                    # s = min(max(1 - md, .2), 1)
                    # s = 1

                    tx = 0
                    ty = 0

                if 0:
                    tz = s

                    tx0 = tx
                    ty0 = ty

                    tx1 = tx0 + (tx - 1920) * 0.25
                    ty1 = ty0 + (ty - 1080) * 0.25

                    tx = tx0 + s * (tx1 - tx0)
                    ty = ty0 + s * (ty1 - ty0)

                if 0:
                    # s = 1
                    s *= 1
                    s += 0
                    # s = 1
                    # cx = scx
                    # cy = scy
                    s = 0.1
                    mdx = cx - mx
                    mdy = cy - my
                    tx = int(0.01 * (mdx * s) ** 3)
                    ty = int(0.01 * (mdy * s) ** 3)
                    # tx = 0
                    # ty = 0
                    s = 1

                    if 0:
                        md = math.sqrt(mdx ** 2 + mdy ** 2)
                        stacking.append((md, process.win))
                if 1:
                    # circle
                    theta = time.clock() * 0.1
                    #
                    px = scx + math.cos(theta + i * v) * scy * 0.5
                    tx = px - width * 0.5
                    py = scy + math.sin(theta + i * v) * scy * 0.5
                    ty = py - height * 0.5
                    #
                    s = 0.2
                    # tz = i

                if 1:
                    scale = np.matrix([
                        [s, 0, 0, 0],
                        [0, s, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                    ])

                    center = np.matrix([
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [cx, cy, cz, 1],
                    ])

                    translation = np.matrix([
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [tx, ty, tz, 1],
                    ])

                    mat = center.getI() * scale * center * translation

                    flat_mat = np.array(mat).flatten()
                else:
                    flat_mat = self.anim_lambda(s, tx, ty, tz)

                    print('flat_mat', flat_mat)

                if is_use_compiz:
                    msg = str(time.time()) + ' ' + str(window.id) + ' ' + ' '.join(map(str, flat_mat)) + '\n'
                else:
                    #
                    # Queue.debug(tx = tx, ty = ty)
                    #
                    tx = int(tx)
                    ty = int(ty)
                    #
                    page = page._replace(x = tx, y = ty)
                    #
                    msg = page
                    #
                #
                lines.append(msg)
                i += 1

        if is_use_compiz:
            if self.open_compiz_server():
                #
                msg = ''.join(lines)
                #
                while len(msg):
                    msg = msg[os.write(self.compiz_fd, msg):]
            else:
                Queue.debug(error = 'no compiz server')
        else:
            #
            for page in lines:
                #
                # Queue.debug(page = page)
                #
                self.write_to_process(page.uuid, Code.dumps(page) + '\n')

        if 0:
            # set stacking
            stacking.sort()
            for (md, window) in stacking:
                window.configure(None, stack_mode = X.Above)

    def is_uuid_active(self, uuid):
        result = False
        #
        xid = WMX.get_active_window()
        process = self.get_process_by_xid(xid)
        if process is not None:
            result = process.page.uuid == uuid
        #
        return result

    def Progress(self, progress):
        process = self.uuid_to_process.get(progress.uuid)
        if process is not None:
            process.progress = progress

        if progress.progress == 1:
            #
            # Queue.debug(progress = progress)
            #

            total_progress_value = sum(process.progress.progress for process in self.uuid_to_process.values()) / len(filter(lambda page: page.is_open, self.session.pages))
            total_progress = Process.create('Progress', uuid = 'root', progress = total_progress_value)

            Queue.emit(total_progress)

            if total_progress_value == 1:
                if not hasattr(self, 'final_progress'):
                    t1 = time.time()
                    self.final_progress = (t1, total_progress)
                    if hasattr(self, 'initial_progress'):
                        (t0, initial_progress) = self.initial_progress
                        load_time = t1 - t0
                        #
                        # Queue.debug(load_time = load_time)
                        #

        if False:
            for process in self.uuid_to_process.values():
                if process.progress.progress < 1:
                    if process.page.is_open:
                        Queue.debug(page = process.page, progress = process.progress)
                        
        if False:
            if hasattr(self, 'initial_progress'):
                total_progress_value = sum(process.progress.progress for process in self.uuid_to_process.values()) / len(filter(lambda page: page.is_open, self.session.pages))
                total_progress = Process.create('Progress', uuid = 'root', progress = total_progress_value)
                (t0, initial_progress) = self.initial_progress
                t1 = time.time()
                load_time = t1 - t0
                Queue.debug(progress_rate = total_progress_value / load_time)

        #
        # self.save_session(self.session)
        #
        return True

    #
    def get_prior_uuids(self, uuid):
        """
        Return prior uuids for given uuid.
        """
        #
        result = []
        #
        prior_uuids = self.uuid_to_prior_uuid.get(uuid)
        #
        if prior_uuids is not None:
            #
            result.extend(prior_uuids.keys())
            #
        #
        return result
        #
    #
    def get_prior_pages(self, page):
        """
        Return parent of page w.r.t. PageToPage edge.
        """
        #
        result = []
        #
        for uuid in self.get_prior_uuids(page.uuid):
            #
            # find prior page
            #
            priorpage = self.uuid_to_page[uuid]
            #
            result.append(priorpage)
            #
        #
        return result
        #
    #
    def get_posterior_uuids(self, prior_uuid):
        """
        Return direct children of uuid with respect to PageToPage edge.
        """
        #
        result = []
        #
        for (uuid, prior_uuids) in self.uuid_to_prior_uuid.items():
            for (_prior_uuid, p2p) in prior_uuids.items():
                if _prior_uuid == prior_uuid:
                    result.append(uuid)
                    #
                #
            #
        #
        return result
        #
    #
    def PageToPage(self, p2p):
        #
        # save link in session
        #
        # p2p.uuid
        # p2p.prior_uuid
        #
        # Queue.infoex('p2p')
        # Queue.debug(p2p = p2p)
        #
        edge = self.uuid_to_prior_uuid.setdefault(p2p.uuid, OrderedDict())
        #
        edge[p2p.prior_uuid] = p2p
        #
        # update session
        #
        # import xpy; xpy.start_console()
        #
        if 0:
            if not any(p2p == _p2p for _p2p in self.session.edges):
                self.session.edges.append(p2p)
        #
        return True

    @classmethod
    def rescale_page(WebSession, page):
        #
        # use geometry of screen that page dimensions were defined in
        #
        sx = 1.0 / 3840
        sy = 1.0 / 2160
        #
        is_normalized_size = 0
        if is_normalized_size:
            #
            # convert integer page dimensions to screen space normalized
            # floating point values
            #
            #
            # adjust page scaling for screen
            #
            if (type(page.x) is not float and page.x is not None or
                type(page.y) is not float and page.y is not None):
                #
                newpage = page._replace(
                    x = page.x * sx,
                    y = page.y * sy,
                    width = page.width * sx,
                    height = page.height * sy,
                )
                #
                # Queue.debug(newpage = newpage, oldpage = page)
                #
                page = newpage
                #
            #
            # fix page being positioned off screen for some reason
            #
            if page.x is not None:
                minx = 0.0
                maxx = 0.9
                #
                if page.x < minx:
                    page = page._replace(x = minx)
                if page.x > maxx:
                    page = page._replace(x = maxx)
                #
            #
            if page.y is not None:
                miny = 0.0
                maxy = 0.9
                #
                if page.y < miny:
                    page = page._replace(y = miny)
                if page.y > maxy:
                    page = page._replace(y = maxy)
                #
            #
        else:
            if (page.x is not None and type(page.x) is float or
                page.y is not None and type(page.y) is float or
                page.width is not None and type(page.width) is float or
                page.height is not None and type(page.height) is float):
                #
                npage = page
                #
                npage = npage._replace(x = int(npage.x / sx))
                npage = npage._replace(y = int(npage.y / sy))
                #
                npage = npage._replace(width = int(npage.width / sx))
                npage = npage._replace(height = int(npage.height / sy))
                #
                # Queue.debug(npage = npage, page = page)
                #
                page = npage
                #
        #
        return page

    def open_page(self, page):
        #
        # spawn process
        #
        if page.uuid not in self.uuid_to_process:
            #
            process = self.spawn_process(page)
            #
            assert page.uuid in self.uuid_to_process

        if 0:
            #
            # Queue.debug(writing_page = page)
            #
            self.write_to_process(page.uuid, Code.dumps(page) + '\n')
        #
        # self.Open(Process.create('Open', uuid = page.uuid))
    #
    def close_page(self, page):
        #
        # Queue.debug(closing = page)
        #
        # remove process from uuid_to_process
        #
        process = self.uuid_to_process.pop(page.uuid)
        #
        self.unregister_process(process)
        #
        ret = self.kill_process(process)
        #
        del process
        #
        # remove page directories
        #
        Session.remove_page_dir(page)
        #
    #
    def get_current_page_stacking(self):
        stacking = []
        #
        for xid in WMX.get_property_value_by_name('_NET_CLIENT_LIST_STACKING', Display.root):
            #
            process = self.get_process_by_xid(xid)
            #
            if process is not None:
                #
                stacking.append(process.page)
                #
            #
        #
        return stacking
    #
    def save_stacking(self):
        #
        # Queue.infoex(comment = 'saving stacking')
        #
        stacking_pages = self.get_current_page_stacking()
        #
        open_pages = self.get_open_pages()
        #
        if len(stacking_pages) == len(open_pages):
            #
            for (z, page) in enumerate(stacking_pages):
                #
                # set page z
                #
                page = self.uuid_to_page[page.uuid]
                #
                if page.z != z:
                    #
                    # Queue.infoex('z', 'page.z', 'page')
                    #
                    # modify page
                    #
                    page = page._replace(z = z)
                    #
                    # save page
                    #
                    self.Page(page)
                    #
                else:
                    #
                    #Queue.infoex('z', 'page.z', 'page', comment = 'already correct')
                    #
                    pass
            #
            # Queue.infod([('info', 'saved stacking'), ('stacking', [page.uuid for page in stacking_pages])])
            #
            # reorder session pages
            #
        else:
            #
            Queue.errod([('info', 'not enough pages stacked')])
            #
        #
    #
    def verify_stacking(self):
        #
        page_stack = self.get_current_page_stacking()
        sorted_pages = self.get_z_sorted_pages()
        #
        result = 1
        #
        for (i, page) in enumerate(sorted_pages):
            #
            if i < len(page_stack):
                #
                spage = page_stack[i]
                if page.uuid == spage.uuid:
                    # result &= 1
                    # Queue.infod([('stack_ok', page)])
                    pass
                else:
                    #
                    Queue.errex('page', 'spage', comment = 'stacking wrong')
                    #
                    result = 0
                    #
            else:
                #
                Queue.errod([('short page_stack', i), ('len(page_stack)', len(page_stack)), ('len(sorted_pages)', len(sorted_pages))])
                #
                result = 0
                #
                break
                #
            #
        #
        #
        if len(page_stack) < len(sorted_pages):
            #
            Queue.errod([('len(page_stack)', len(page_stack)), ('len(sorted_pages)', len(sorted_pages))])
            #
        #
        return result
    #
    def get_z_sorted_pages(self):
        #
        # sort pages by their z coordinate
        #
        sorted_pages = list(sorted(self.get_open_pages(), key = lambda page: page.z))
        #
        return sorted_pages
        #
    #
    @classmethod
    def is_page_open(self, page):
        return page.is_open and not page.is_deleted
    #
    def restack_windows(self):
        #
        sibling = None
        #
        stack_count = 0
        #
        sorted_pages = self.get_z_sorted_pages()
        #
        for page in sorted_pages:
            #
            process = self.uuid_to_process[page.uuid]
            #
            xid = process.xid
            #
            if xid is not None:
                #
                window = WMX.get_window_by_xid(xid)
                #
                stack_count += 1
                #
                if sibling:
                    #
                    # Queue.infoex('hex(xid)', 'hex(sibling)', comment = 'stacking')
                    #
                    WMX.stack_window(xid, sibling, X.Above)
                    #
                    pass
                #
                sibling = xid
                #
            else:
                Queue.debug(premature_stack = 1, missing_window_pid = process.pid, page = page)
                break
                #
            #
        #
    #
    def restore_null_dimensions(self, page):
        """
        ignore null if page already has dimensions set
        """
        if self.is_any_page_dimension_none(page):
            """
            why is this docstring here
            """
            prior = self.uuid_to_page.get(page.uuid)
            #
            if prior is not None:
                #
                page = page._replace(x = prior.x, y = prior.y, width = prior.width, height = prior.height)
            #
        return page
    #
    def fixup_page(self, page):
        #
        # ignore null if page already has dimensions set
        #
        page = self.restore_null_dimensions(page)
        #
        # find prior page
        #
        page = self.move_null_page_to_prior(page)
        #
        # if that failed
        #
        page = self.change_null_dimensions_to_default(page)
        #
        return page
    #
    def Page(self, page):
        #
        # Queue.infod([('received page', page)])
        #
        prior = self.uuid_to_page.get(page.uuid)
        #
        if page is not prior and page != prior:
            #
            page = self.fixup_page(page)
            #
            assert not self.is_any_page_dimension_none(page)
            #
            if 1:
                if 0:
                    #
                    # ignore position and size from child process
                    #
                    opage = self.get_page_by_uuid(page.uuid)
                    #
                    if opage is not None:
                        #
                        # replacement
                        #
                        page = page._replace(x = opage.x, y = opage.y, width = opage.width, height = opage.height)
                    else:
                        page = page._replace(x = None, y = None, width = None, height = None)
                    #
                if 1:
                    #
                    #
                    #
                    page = self.rescale_page(page)
                #
            #
            #
            if 1:
                #
                if prior is not None and (page.x is None or page.y is None or page.width is None or page.height is None):
                    #
                    # prevent null
                    #
                    page = page._replace(x = prior.x, y = prior.y, width = prior.width, height = prior.height)
                    #
                #
                if 0:
                    #
                    page = self.clamp_page(page)
                    #
                #
                #
                if (prior is None or not prior.is_open) and (page.is_open and not page.is_deleted):
                    self.open_page(page)
                    #
                #
                if prior is not None and prior.is_open and (not page.is_open or page.is_deleted):
                    self.close_page(page)
                    #
                #
                if page.uuid in self.uuid_to_process:
                    #
                    # save process mapping
                    #
                    self.uuid_to_process[page.uuid].page = page
                    #
                    # Queue.debug(updated_uuid_to_process = page)
                    #
            #
            # write results
            #
            self.uuid_to_page[page.uuid] = page
            #
            #
            # save to file
            #
            self.save_page(page)
            #
            # write page to standard error
            #
            Queue.emitfd(Queue.err_fd, page)
            #
        #
        return True

    @classmethod
    def load_session(self, session_path):
        #
        session = None
        #
        try:
            with open(session_path) as infile:
                session = Code.loads(infile.read())
        except IOError as e:
            if e.errno == errno.ENOENT:
                Queue.debug(no_path = session_path)
            else:
                raise
        #
        return session

    @classmethod
    def save_session(self, session):
        #
        # session path is a relative path
        #
        session_relpath = session.path
        #
        session_path = self.get_full_session_path_by_relative_path(session_relpath)
        #
        import time
        #
        t0 = time.time()
        #
        # give the session indentation so it can be diffed linewise
        #
        code = json.dumps(json.loads(Code.dumps(session)), indent = 2) + '\n'
        #
        assert OSUtil.atomic_overwrite(session_path, code, 0o600)
        #
        Queue.debug(wrote = session_path)
        #
        t1 = time.time()
        #
        # Queue.debug(dt = t1 - t0)
        #
        return True

    def save_page_dirs(self):
        #
        for (uuid, page) in self.to_save.items():
            #
            Session.make_page_dir(page)
            #
            # Queue.debug(wrote = page_path)
            #
        #
        self.to_save.clear()

    def open_session_pages(self, session):
        #
        limit = 1000
        #
        for p2p in session.edges:
            self.PageToPage(p2p)
            #
        for page in session.pages[:limit]:
            self.Page(page)
            #
        #
        # Queue.debug(open_count = len(self.uuid_to_process))
        #

    def Session(self, session):
        #
        self.is_loading_session = True
        #
        # make sure edges is a list
        #
        session = session._replace(edges = list(session.edges))
        #
        # Queue.debug(session = session)
        #
        self.session = session
        #
        self.open_session_pages(session)
        #
        # self.EventLoop()
        #
        self.is_loading_session = False
        #
        return True

    @classmethod
    def ImportSessionBuddy(self, msg):
        msg.input_path
        msg.output_path
        pages = self.import_session_buddy(msg.input_path)
        output_session = Process.create('Session', path = msg.output_path, pages = pages)
        self.save_session(output_session)
        # Queue.debug(session = session)
        return True

    @classmethod
    def run(self, argv):
        session = self.import_session_buddy(argv[1])

    @classmethod
    def run_session(self, session):
        """
        launch session
        """
        #
        assert session is not None
        #
        ws = WebSession()
        #
        result = Process.invoke_handler(session, ws)
        #
        eventloop = Process.create('EventLoop')
        #
        result = Process.invoke_handler(eventloop, ws)
        #

    @classmethod
    def create_session_by_path(self, session_path):
        #
        page = Page.create_from_url('about:blank')
        #
        session = Process.create('Session', path = self.get_filename_by_session_path(session_path), pages = [page])
        #
        Queue.debug('session', comment = 'created new session')
        #
        return session
    #
    @classmethod
    def run_session_by_path(self, session_path):
        """
        launch session by loading session file at path or create new session
        file at path
        """
        session = self.load_session(session_path)
        #
        if session is None:
            session = self.create_session_by_path(session_path)
            #
        #
        return self.run_session(session)
        #
    #
    @classmethod
    def get_filename_by_session_path(self, session_path):
        #
        # return path relative to SESSION_PATH, which includes subdirs of SESSION_PATH
        #
        return os.path.relpath(session_path, self.SESSION_PATH)
    #
    @classmethod
    def get_full_session_path_by_relative_path(self, session_relpath):
        """
        form full path with SESSION_PATH and filename
        """
        session_path = os.path.join(self.SESSION_PATH, session_relpath)
        return session_path
    #
    @classmethod
    def get_session_path_by_name(self, session_name):
        session_relpath = session_name + '.json'
        session_path = self.get_full_session_path_by_relative_path(session_relpath)
        return session_path
    #
    @classmethod
    def run_session_by_name(self, session_name):
        """
        load and run a session by name

        if the session does not exist, then one will be created (by run_session_by_path)
        """
        assert not session_name.endswith('.json')
        #
        session_path = self.get_session_path_by_name(session_name)
        #
        return self.run_session_by_path(session_path)
    #
#
class SessionDot(object):
    @classmethod
    def write_dot(self, session):
        #
        nodes = OrderedDict()
        #
        for page in session.pages:
            if page.is_open:
                nodes[page.uuid] = page
            else:
                print('dead page', page)
        #
        edges = OrderedDict()
        for edge in session.edges:
            if edge.uuid in nodes and edge.prior_uuid in nodes:
                if edge.prior_uuid in nodes:
                    key = (edge.uuid, edge.prior_uuid)
                    edges[key] = edge
                else:
                    #
                    print('edge prior missing', edge, edge.prior_uuid)
                    #
            else:
                #
                print('edge source missing', edge, edge.uuid)
                #
        #
        lines = []
        #
        print('edges', edges)
        #
        # write a dot file like this:
        #
        # strict digraph G {
        # "uuid" [label="url"]
        # "uuid" -> "prior_uuid"
        # }
        #
        # "nodes.graphtype.Ending" [label="Ending"];
        #
        print('nodes', nodes)
        #
        lines.append(['strict', ' ', 'digraph', ' ', 'G', ' ', '{'])
        #
        lines.append([' ', 'rankdir', '=', 'LR'])
        #
        for (uuid, page) in nodes.items():
            assert '"' not in uuid
            assert '"' not in page.url
            lines.append([' ', '"', uuid, '"', ' ', '[', 'label', '=', '"', page.url, '"', ']'])
        #
        for edge in edges.values():
            lines.append([' ', '"', edge.uuid, '"', ' ', '->', ' ', '"', edge.prior_uuid, '"'])
        #
        lines.append(['}'])
        #
        return ''.join([''.join(line + ['\n']) for line in lines])

mod = __import__(__name__)
# Process.register_class(WebSession)

if __name__ == '__main__':
    classname = sys.argv[1]
    cls = mod.__dict__[classname]
    #
    if cls is not None:
        #
        # instantiate object
        #
        obj = cls(classname)
        #
        argv = sys.argv[2:]
        #
        # decode json arguments as objects and apply them to subject
        #
        result = Process.process_argv(argv, obj)
        #
    else:
        Queue.debug(unknown_class = classname)
        
    # WebSession.run(sys.argv)

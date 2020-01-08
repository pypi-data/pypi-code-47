#!/usr/bin/env python2
#
# Copyright (C) 2015-2019 David J. Beal, All Rights Reserved
#

import sys
import gi
import os

os.environ['WEBKIT_DISABLE_COMPOSITING_MODE'] = '1'

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import WebKit2
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gio
from gi.repository import JavaScriptCore

from gom.queue import *
from page import *
#
from display import *
#
# use stdin pipe under page session directory rather than fd 0
#
is_open_stdin_pipe = 1

class BrowserTab(Gtk.VBox):
    #
    DEFAULT_PAGE = Page.create_from_url('https://www.google.com')._replace(uuid = None)
    #
    #
    # 4k standard
    #
    zoom_scale = 1.5 * float(Display.screen_width) / 3840.0

    def set_zoom(self, zoom):
        self.webview.set_zoom_level(zoom * self.zoom_scale)

    def get_zoom(self):
        return self.webview.get_zoom_level() / self.zoom_scale

    def _zoom_in(self):
        self.set_zoom(self.get_zoom() * 1.0 + 0.1)
        #
    #
    def _zoom_out(self):
        self.set_zoom(self.get_zoom() * 1.0 - 0.1)
        #
    #
    def _zoom_default(self):
        self.set_zoom(1.0)
        #
    #
    def __init__(self, *args, **kwargs):
        super(BrowserTab, self).__init__(*args, **kwargs)

        tools = []
        #
        self.page = None

        self.label = Gtk.Label("Hello There")

        #
        if 1:
            #
            home_button = Gtk.Button("home")
            def _home(button):
                self.open_new_page(self.page._replace(url = BrowserTab.DEFAULT_PAGE.url))
            home_button.connect("clicked", _home)
            tools.append(home_button)
            self.home_button = home_button
            #
        #
        #
        if 1:
            #
            self.go_back = Gtk.Button("prev")
            self.go_back.connect("clicked", lambda x: self.webview.go_back())
            tools.append(self.go_back)
            #
        #
        #
        if 1:
            #
            self.reload_button = Gtk.Button("reload")
            self.reload_button.connect("clicked", lambda *args, **kwargs: self._reload_tab())
            tools.append(self.reload_button)
            #
        #
        #
        if 1:
            #
            self.go_forward = Gtk.Button("next")
            self.go_forward.connect("clicked", lambda x: self.webview.go_forward())
            tools.append(self.go_forward)
            #
        #
        #
        if 1:
            #
            # fork creates a duplicate process with a link to parent
            #
            fork_button = Gtk.Button("fork")
            def _fork(button):
                #
                self.open_new_page(self.page)
                #
            fork_button.connect("clicked", _fork)
            tools.append(fork_button)
            #
        #
        #
        if 1:
            #
            # execute python code in terminal
            #
            exec_button = Gtk.Button("exec")
            exec_button.connect("clicked", self._exec_code)
            tools.append(exec_button)
            #
            # self.resizable = True
            #
        #
        #
        if 1:
            #
            # permanently close a page
            #
            self.kill_button = Gtk.Button("kill")
            def _kill(button):
                self.do_kill_page()
            self.kill_button.connect("clicked", _kill)
            tools.append(self.kill_button)
            #
        #
        #
        if 0:
            #
            # TODO: kill and restart a page
            #
            self.restart_button = Gtk.Button("restart")
            #
            def _restart(self, button):
                #
                page = self.page
                #
                if page is not None:
                    #
                    newpage = page._replace(is_open = False)
                    #
                    self._setpage(newpage)
                    #
                #
            #
            self.restart_button.connect("clicked", (lambda self: lambda button: _restart(self, button))(self))
            tools.append(self.restart_button)
            #
        #
        #
        if 1:
            #
            # zoom out
            #
            self.smaller_button = Gtk.Button("smaller")
            def _smaller(button):
                self._zoom_out()
            self.smaller_button.connect("clicked", _smaller)
            tools.append(self.smaller_button)
            #
        #
        #
        if 1:
            #
            # zoom default
            #
            self.normal_button = Gtk.Button("normal")
            def _normal_button(button):
                self._zoom_default()
            self.normal_button.connect("clicked", _normal_button)
            tools.append(self.normal_button)
            #
        #
        #
        if 1:
            #
            # zoom in
            #
            self.bigger_button = Gtk.Button("bigger")
            def _bigger(button):
                self._zoom_in()
            self.bigger_button.connect("clicked", _bigger)
            tools.append(self.bigger_button)
            #
        #
        #
        self.uri_field = Gtk.Entry()
        self.uri_field.connect("activate", self._uri_field_activate)

        self.webview = WebKit2.WebView(is_ephemeral = True)
        #
        assert self.webview.props.is_ephemeral
        #
        settings = WebKit2.Settings()
        #
        # settings.props.enable_smooth_scrolling = True
        # settings.props.enable_dns_prefetching = True
        # settings.props.enable_private_browsing = True
        settings.props.enable_write_console_messages_to_stdout = True
        settings.props.enable_offline_web_application_cache = False
        #
        self.webview.set_settings(settings)

        self._zoom_default()

        self.show()


        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)

        self.create_finder()

        if 1:
            #
            # background button toggles running the web page in the background
            #
            self.background_button = Gtk.CheckButton()
            self.background_button.props.label = 'bg'
            self.background_button.props.active = False
            def _clicked(button):
                #
                newpage = self.page._replace(is_run_in_background = self.background_button.props.active)
                #
                self._setpage(newpage)
                #
            self.background_button.connect("clicked", _clicked)
            tools.append(self.background_button)

        padding = 3
        #
        if 1:
            tool_box = Gtk.HBox()
            #
            for tool in tools:
                tool_box.pack_start(tool, False, False, padding)
                #
            #
            tool_box.show_all()
            #
        else:
            tool_box = Gtk.HBox()
            tool_box.pack_start(home_button, False, False, 0)
            tool_box.pack_start(self.go_back, False, False, 0)
            tool_box.pack_start(self.go_forward, False, False, 0)
            tool_box.pack_start(exec_button, False, False, 0)
            tool_box.pack_start(fork_button, False, False, 0)
            tool_box.pack_start(self.kill_button, False, False, 0)
            tool_box.pack_start(self.bigger_button, False, False, 0)
            tool_box.pack_start(self.smaller_button, False, False, 0)
            tool_box.pack_start(self.background_button, False, False, 0)
            tool_box.show_all()

        url_box = Gtk.HBox()
        url_box.pack_start(self.uri_field, True, True, padding)

        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_text('progress')
        self.progress_bar.set_show_text(False)

        self.pack_start(tool_box, False, False, padding)
        self.pack_start(url_box, False, False, padding)
        self.pack_start(scrolled_window, True, True, padding)
        self.pack_start(self.progress_bar, False, False, padding)
        self.pack_start(self.find_box, False, False, padding)

        url_box.show_all()
        scrolled_window.show_all()

        self.webview.connect('load-changed', self._load_changed)
        self.webview.connect('notify::title', self._title_changed)
        self.webview.connect('notify::uri', self._uri_changed)
        self.webview.connect('notify::zoom-level', self._zoom_level_changed)
        #
        def _create(webview, nav):
            #
            result = None
            #
            Queue.infoex('webview', 'nav', comment = '_create')
            #
            # Queue.debug(create = nav)
            #
            nav_type = nav.get_navigation_type()
            #
            uri = nav.get_request().get_uri()
            #
            # Queue.debug(nav_type = nav_type, uri = uri)
            #
            if nav_type == WebKit2.NavigationType.LINK_CLICKED:
                # The navigation was triggered by clicking a link.
                #
                # self.open_new_page(uri)
                pass
                #
            #
            if nav_type == WebKit2.NavigationType.FORM_SUBMITTED:
                # The navigation was triggered by submitting a form.
                pass
            #
            if nav_type == WebKit2.NavigationType.BACK_FORWARD:
                # The navigation was triggered by navigating forward or backward.
                pass
            #
            if nav_type == WebKit2.NavigationType.RELOAD:
                # The navigation was triggered by reloading.
                pass
            #
            if nav_type == WebKit2.NavigationType.FORM_RESUBMITTED:
                # The navigation was triggered by resubmitting a form.
                pass
            #
            if nav_type == WebKit2.NavigationType.OTHER:
                # The navigation was triggered by some other action.
                # uri = nav.get_request().get_uri()
                #
                # emit new page
                #
                # self.open_new_page(uri)
                #
                # block further propagation
                #
                pass
            #
            # create new process by emitting Page object with newly generated
            # uuid
            #
            page = self.page
            #
            newpage = page._replace(url = uri)
            #
            self.open_new_page(newpage)
            #
            return result
        #
        self.webview.connect("create", _create)
        #
        #
        def _pointer_button_press(widget, event):
            result = False
            #
            # Queue.debug(event = event)
            #
            # print('button', event.get_button())
            # import xpy; xpy.xpy_start_console()
            (is_button, index) = event.get_button()
            if is_button:
                if index == 8:
                    # go back
                    self.webview.go_back()
                    result = True
                if index == 9:
                    # go back
                    self.webview.go_forward()
                    result = True

            return result


        self.webview.connect("button-press-event", _pointer_button_press)

        def _estimated_load_progress(webview, progress):
            # print('progress', progress)
            # print('progress', webview.props.estimated_load_progress)
            progressval = webview.props.estimated_load_progress
            #
            progress = Process.create('Progress', uuid = self.page.uuid, progress = progressval)
            #
            Queue.emit(progress)
            #
            # set progress bar in address bar
            #
            self.uri_field.set_progress_fraction(progress.progress)
            self.progress_bar.set_fraction(progress.progress)
            #
        #
        self.webview.connect('notify::estimated-load-progress', _estimated_load_progress)
        #
        def _mouse_target_changed(webview, hit_test_result, modifiers):
            #
            # import xpy; xpy.xpy_start_console()
            #
            link_uri = hit_test_result.get_link_uri()
            #
            # if link_uri != self.hover_link_uri:
            if 1:
                #
                self.hover_link_uri = link_uri
                #
                if 1:
                    if self.hover_link_uri is not None:
                        #
                        # Queue.debug(link_uri = self.hover_link_uri)
                        #
                        self.uri_field.set_text(self.hover_link_uri)
                    else:
                        self.uri_field.set_text(self.page.url)

        self.webview.connect("mouse-target-changed", _mouse_target_changed)

        #
        # modify context menu for link
        #
        self.webview.connect("context-menu", self._context_menu)
        #
    #
    def create_finder(self):
        #
        finder = self.webview.get_find_controller()
        #
        def _found_text(finder, match_count):
            #
            Queue.edumps(match_count = match_count)
            #
            pass
        #
        finder.connect("found-text", _found_text)
        #
        #
        def _find_start(text):
            finder.search(text, WebKit2.FindOptions.CASE_INSENSITIVE | WebKit2.FindOptions.WRAP_AROUND, 1024)
            #
        def _find_prev():
            finder.search_previous()
            #
        def _find_next():
            finder.search_next()
            #
        def _find_stop():
            finder.search_finish()
            #
            pass


        find_box = Gtk.HBox()

        def _find_close():
            _find_stop()
            #
            find_box.hide()
            #
            # restore focus
            #
            self.webview.grab_focus()

        close_button = Gtk.Button("exit")
        #
        def _close_button_clicked(button):
            #
            _find_close()
        #
        close_button.connect("clicked", _close_button_clicked)

        self.find_entry = Gtk.Entry()
        #
        def _find_entry_activate(entry):
            _find_start(entry.get_text())
        #
        self.find_entry.connect("activate", _find_entry_activate)

        prev_button = Gtk.Button("find prev")
        #
        def _prev_button_clicked(button):
            _find_prev()
        #
        prev_button.connect("clicked", _prev_button_clicked)

        next_button = Gtk.Button("find next")
        #
        def _next_button_clicked(button):
            _find_next()
        #
        next_button.connect("clicked", _next_button_clicked)

        def _close_find_dialog():
            #
            # close search
            #
            _find_close()
            #
            Queue.edumps(closing = True)
            #
            # block further key propagation
            #
            return True

        self.finder = finder

        #
        # close button might cause crash
        #
        # find_box.pack_start(close_button, False, False, 0)
        find_box.pack_start(self.find_entry, False, False, 0)
        find_box.pack_start(prev_button, False, False, 0)
        find_box.pack_start(next_button, False, False, 0)
        #
        find_box.hide()
        #
        def _key_press_event(widget, event):
            mapping = {
                Gdk.KEY_Escape: lambda event: (_close_find_dialog() or True) if event.type == Gdk.EventType.KEY_RELEASE else True,
                Gdk.KEY_p: lambda event: (_find_prev() or True) if event.type == Gdk.EventType.KEY_PRESS else True,
                Gdk.KEY_n: lambda event: (_find_next() or True) if event.type == Gdk.EventType.KEY_PRESS else True,
            }
            return mapping.get(event.keyval, lambda event: False)(event)
            #
        #
        find_box.connect("key-press-event", _key_press_event)
        find_box.connect("key-release-event", _key_press_event)
        #
        self.find_box = find_box
        #
    #
    def _make_alert(self, *args):
        #
        print('_make_alert args', args)
        #
        def _asyncresult(webview, asyncresult):
            result = webview.run_javascript_finish(asyncresult)
            # import xpy; xpy.xpy_start_console()
        #
        self.webview.run_javascript("alert('hello')", None, _asyncresult)
        #
    #
    def _context_menu(self, webview, context_menu, event, hit_test_result):
        #
        Queue.debug(context_menu = context_menu, event = event, hit_test_result = hit_test_result)
        #
        if 1:
            #
            link_uri = hit_test_result.get_link_uri()
            #
            # import xpy; xpy.xpy_start_console()
            #
        #
        if 1:
            #
            action = Gio.SimpleAction.new("test alert")
            #
            action.connect("activate", self._make_alert)
            #
            menu_item = WebKit2.ContextMenuItem.new_from_gaction(action, "foo")
            #
        #
        if 1:
            #
            action = Gio.SimpleAction.new("copy link")
            #
            def activate_copy_link(action, *args):
                #
                # print('args', args)
                #
                os.system('echo "' + link_uri + '" | xsel')
                #
            #
            action.connect("activate", activate_copy_link)
            #
            menu_item = WebKit2.ContextMenuItem.new_from_gaction(action, "Copy Link")
            #
            context_menu.append(menu_item)
        #
        if 1:
            #
            action = Gio.SimpleAction.new("open link")
            #
            def activate_open_link(action, *args):
                #
                # print('args', args)
                #
                # os.system('echo "' + link_uri + '" | xsel')
                #
                self.open_new_page(self.page._replace(url = link_uri))
                #
            #
            action.connect("activate", activate_open_link)
            #
            menu_item = WebKit2.ContextMenuItem.new_from_gaction(action, "Open Link")
            #
            context_menu.append(menu_item)
        #
        return False
        #
    #
    def open_new_page(self, page):
        """
        Make a carbon copy of the given page, but assign a new unique
        id.

        Link new page to original page.
        """
        #
        if page is not None:
            #
            # assign a new uuid
            #
            newpage = page._replace(uuid = Page.gen_uuid())
            #
            # first create link from newpage to prior page
            #
            # Emit the new link.  Implies that an abstract graph can exist
            # without attributes such as Page.
            #
            p2p = PageToPage.create_from_pages(newpage, page)
            #
            Queue.emit(p2p)
            #
            # Emit the new_page with different uuid.  This should trigger a new
            # browser to be spawned by the master process.
            #
            self.emitpage(newpage)
            #
        #
    #
    @classmethod
    def emitpage(self, page):
        """
        serialize page to stdout
        """
        #
        #
        assert page.x is None and page.y is None and page.width is None and page.height is None
        #
        Queue.emit(page)
        #
    #
    def _setpage(self, newpage):
        #
        priorpage = self.page
        #
        if_prior_none = priorpage is None
        #
        if newpage != priorpage:
            #
            self.page = newpage
            #
            #
            # update button setting
            #
            if if_prior_none or newpage.is_run_in_background != priorpage.is_run_in_background:
                #
                # update toggle switch to indicate current setting
                #
                self.background_button.props.active = newpage.is_run_in_background
                #
            #
            # set WebView scale from Page
            #
            if if_prior_none or newpage.scale != priorpage.scale:
                #
                self.set_zoom(newpage.scale)
                #
            #
            if if_prior_none or newpage.url != priorpage.url:
                #
                prioruri = self.webview.get_uri()
                #
                newuri = newpage.url
                #
                if prioruri != newuri:
                    #
                    Queue.infoex('newuri', 'prioruri', comment = 'loading newuri')
                    #
                    result = self.webview.load_uri(newuri)
                    #
                #
            #
            self.emitpage(self.page)
            #
    #
    def do_kill_page(self):
        #
        page = self.page
        #
        if page is not None:
            #
            newpage = page._replace(is_open = False)
            #
            self._setpage(newpage)
            #
        #
    #
    def _zoom_level_changed(self, webview, uri):
        #
        scale = self.get_zoom()
        #
        page = self.page
        #
        if page is not None:
            #
            newpage = page._replace(scale = scale)
            #
            self._setpage(newpage)
            #

    def _uri_changed(self, webview, uri):
        #
        uri = self.webview.props.uri
        #
        self.uri_field.set_text(uri)
        #
        if self.page is not None:
            #
            newpage = self.page._replace(url = uri)
            #
            self._setpage(newpage)
            #
        #
    #
    #
    def _title_changed(self, *args):
        # print('title', self.webview.get_title())
        #
        self.label.set_text(self.webview.get_title())

    def _load_changed(self, webview, load_event, *args):
        #
        # Queue.debug(event = '_load_changed', load_event = load_event)
        # print('load_event', load_event)
        #
        if load_event == WebKit2.LoadEvent.STARTED:
            pass
            self.progress_bar.show()
        if load_event == WebKit2.LoadEvent.REDIRECTED:
            pass
        if load_event == WebKit2.LoadEvent.COMMITTED:
            pass
        if load_event == WebKit2.LoadEvent.FINISHED:
            self.progress_bar.hide()
            pass

    def _uri_field_activate(self, widget):
        #
        uri = self.uri_field.get_text()
        #
        Queue.infoex('uri', comment = 'uri_field activating')
        #
        self._setpage(self.page._replace(url = uri))
        #

    def _exec_code(self, widget):
        import xpy; xpy.xpy_start_console()

    def Page(self, page):

        is_allow = self.page is None
        #
        if not is_allow:
            if self.page.uuid == page.uuid:
                if self.page != page:
                    is_allow = True
                else:
                    Queue.errex('page', comment = 'ignoring page, identical')
            else:
                Queue.errex('page', comment = 'ignoring page, uuid mismatch')
        #
        if is_allow:
            #
            # Queue.debug(page = page)
            #
            self._setpage(page)
            #
        else:
            pass

        return self

    def _reload_tab(self):
        self.webview.reload()

    def _focus_url_bar(self):
        self.uri_field.grab_focus()

    def _raise_find_dialog(self):
        self.find_box.show_all()
        self.find_entry.grab_focus()

    def _go_prev(self):
        self.webview.go_back()

    def _go_next(self):
        self.webview.go_forward()

class Browser(Gtk.Window):
    #
    is_normalized_size = 0
    if_modify_dims = 0

    def setup_key_bindings(self):
        #
        self.key_bindings = [
            # ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType(0), Gdk.KEY_Escape), self.tab._close_find_dialog),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_0), self.tab._zoom_default),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_equal), self.tab._zoom_in),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_f), self.tab._raise_find_dialog),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_h), self.tab.home_button.activate),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_l), self.tab._focus_url_bar),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_minus), self.tab._zoom_out),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_q), Gtk.main_quit),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_r), self.tab._reload_tab),
            # ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_w), Gtk.main_quit),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_p), self.tab._go_prev),
            ((Gdk.EventType.KEY_PRESS, Gdk.ModifierType.CONTROL_MASK, Gdk.KEY_n), self.tab._go_next),
        ]
        #
        # form dictionary of key key_bindings
        #
        self.key_mapping = dict(self.key_bindings)
        #
        # create binding to key_mapping
        #
        self.key_handler = self._get_key_mapping_handler(self.key_mapping)
        #
        self.connect("key-press-event", self.key_handler)
        self.connect("key-release-event", self.key_handler)
        #
    #
    def __init__(self, *args, **kwargs):
        #
        #
        #
        super(Browser, self).__init__(*args, **kwargs)
        #
        self.page = None

        #
        # help with window positioning
        #
        self.set_gravity(Gdk.Gravity.STATIC)

        #
        # initial position and size of window
        #
        self.resize(1, 1)
        self.move(0, 0)

        #
        # create a single tab
        #
        self.tab = self._create_tab()
        #
        #
        #
        self.add(self.tab)

        self.connect("destroy", Gtk.main_quit)

        self.setup_key_bindings()

        #
        #
        #
        self.show()
        #
        if Browser.if_modify_dims:
            #
            self.connect('configure-event', self.on_configure_event)

    def _create_tab(self):
        tab = BrowserTab()
        def _title_changed(webview, title):
            self.set_title(webview.props.title)
            #
            # Queue.debug(title = tab.webview.props.title)
            #
        tab.webview.connect("notify::title", _title_changed)
        return tab

    @classmethod
    def _get_key_mapping_handler(self, key_mapping):
        """
        create a closure for key_mapping key-function map
        """
        return lambda widget, event: self._key_pressed(key_mapping, widget, event)

    @classmethod
    def _key_pressed(cls, key_mapping, widget, event):
        #
        result = None
        #
        all_modifiers = Gtk.accelerator_get_default_mod_mask()
        #
        # ignore unknown modifiers
        #
        event_state = event.state & all_modifiers
        #
        #
        # form key tuple
        #
        key = (event.type, event_state, event.keyval)

        #
        # Queue.infoex('key', 'event')
        #

        #
        # search dictionary for exact modifier key combination
        #
        fn = key_mapping.get(key)
        #
        # Queue.infoex('fn')
        #
        if fn is not None:
            #
            # invoke function
            #
            # Queue.infoex(comment = 'invoking function')
            #
            # TODO: return proper result
            #
            fn()
            #
            result = True
            #
        elif (Gdk.EventType.KEY_PRESS, event_state, event.keyval) in key_mapping:
            #
            # this event is a KEY_RELEASE event for a bound KEY_PRESS event so
            # consider it handled as part of the prior bound event
            #

            # Queue.infoex(comment = 'RELEASE')
            #
            # use the prior result
            #
            result = True
        else:
            #
            # Queue.infoex('key', comment = 'unknown key binding')
            #
            pass
        #
        # Queue.infoex('result')

        return result
        
    def Page(self, page):
        #
        # Queue.infoex('page')
        #
        prior = self.page
        #
        if prior is None:
            #
            if is_open_stdin_pipe:
                #
                # open stdin pipe from page session dir
                #
                stdin_path = Session.get_stdin_path(page)
                stdout_path = Session.get_stdout_path(page)
                #
                # open nonblocking
                #
                # Queue.infoex('stdin_path', comment = 'opening stdin')
                #
                stdin_pipe = Pipe.open_read(Pipe.create_from_path(stdin_path))
                stdout_pipe = Pipe.open_write(Pipe.create_from_path(stdout_path))
                #
                self.add_io_in(stdin_pipe.fd, os.fdopen(stdin_pipe.fd))
                #
                # replace Queue output fd for Queue.emit
                #
                Queue.output_fd = stdout_pipe.fd
                #
                # Queue.infoex('stdin_pipe', comment = 'opened stdin')
                #
            #
        #

        self.page = page
        #
        # filter page parameters
        #
        if page.url is None:
            page = page._replace(url = BrowserTab.DEFAULT_PAGE.url)
        #
        if Browser.if_modify_dims:
            #
            if not page.width or not page.height:
                #
                # replace zero size page with sensible default values
                #
                page = page._replace(width = 0.25)
                page = page._replace(height = 0.5)
                page = page._replace(x = (1.0 - page.width) * 0.5)
                page = page._replace(y = (1.0 - page.height) * 0.5)
                #
            #
        #
        #
        # get tab index from Notebook
        #
        tab = self.tab
        #
        # trigger load uri
        #
        tab = tab.Page(page)

        if hasattr(self, 'status_label'):
            self.status_label.set_text(Code.dumps(page))

        #
        if Browser.if_modify_dims:
            #
            if Browser.is_normalized_size:
                #
                # change window properties according to page setting
                #
                scale = float(self.get_scale_factor())
                #
                Queue.debug(scale = scale)
                #
                sw = float(Display.screen_width) / float(scale)
                sh = float(Display.screen_height) / float(scale)
                #
                rw = int(page.width * sw)
                rh = int(page.height * sh)
                rx = int(page.x * sw)
                ry = int(page.y * sh)
                #
            else:
                rx = int(page.x)
                ry = int(page.y)
                rw = int(page.width)
                rh = int(page.height)

        is_moveresize = 0
        if is_moveresize:
            #
            # Queue.debug(resizex = rx, resizey = ry, resizew = rw, resizeh = rh)
            #
            self.resize(rw, rh)
            self.move(rx, ry)
            #
        #
        # self.show_all()
        #
        if 0:
            #
            # parent should catch window creation automatically
            #
            Queue.emit(Process.create('Window', uuid = page.uuid, xid = self.get_window().get_xid()))
            #

        if hasattr(self, 'toolbar'):
            if self.toolbar.run_in_background_check_button is not None:
                self.toolbar.run_in_background_check_button.set_active(page.is_run_in_background)

        return self

    def on_configure_event(self, obj, config):
        #
        # Queue.debug(_self = self, obj = obj, config = config)
        #
        # import xpy; xpy.xpy_start_console()
        #
        tab = self.tab
        #
        page = tab.page
        #
        # Queue.debug(page = page)
        #
        if page is not None:
            #
            # print('xlib position', self.get_window().get_position())
            # print('position', self.get_position())
            # print('size', self.get_size())
            #
            x = config.x
            y = config.y
            w = config.width
            h = config.height
            #
            # Queue.debug(note = 'config', x = x, y = y, w = w, h = h)
            # Queue.debug(note = 'config', page = page)
            #
            if Browser.is_normalized_size:
                #
                scale = self.get_scale_factor()
                #
                sw = float(Display.screen_width) / float(scale)
                sh = float(Display.screen_height) / float(scale)
            else:
                sw = 1.0
                sh = 1.0
                #
            #
            ipw = int(page.width * sw)
            iph = int(page.height * sh)
            #
            # Queue.debug(ipw = ipw, iph = iph)

            #
            # the configure event should be somewhere near our requested size
            #
            # otherwise, ignore it
            #
            is_reject_large_resize = 0
            #
            if is_reject_large_resize:
                if abs(w - ipw) < 50 and abs(h - iph) < 50:
                    is_accept = 1
                else:
                    is_accept = 0
            else:
                is_accept = 1
            #
            if is_accept:
                #
                # print(dict(width = w, height = h, x = x, y = y))
                # print('*' * 10)
                #
                if Browser.is_normalized_size:
                    fpx = x / sw
                    fpy = y / sh
                    fpw = w / sw
                    fph = h / sh
                else:
                    fpx = x
                    fpy = y
                    fpw = w
                    fph = h
                #
                page = page._replace(x = fpx, y = fpy, width = fpw, height = fph)
                #
                # Queue.debug(page = page)
                #
                if page != tab.page:
                    #
                    # Queue.debug(current_page = tab.page)
                    # Queue.debug(new_page = page)
                    #
                    # tab = tab.Page(page)
                    tab = tab.Page(page)
                    #
                    # tab.page = page
                    #
                    # Queue.emit(nullpagedims(tab.page))
                    #
                    # self.status_label.set_text(Code.dumps(child.page))

    def add_io_in(self, fd, infile):
        #
        GObject.io_add_watch(fd, GLib.IO_IN, self.handle_input_data, infile)
        #
        if not hasattr(self, 'files'):
            self.files = {}
        #
        # for readline
        #
        self.files[fd] = infile

    def handle_input_data(self, fd, in_or_out, fileobj):
        #
        infile = self.files.get(fd)
        #
        try:
            buf = infile.readline()
        except IOError as e:
            #
            Queue.debug(exception = e)
            #
            if e.errno != errno.EAGAIN:
                #
                infile.close()
                #
                raise
            #
            buf = None
        else:
            if buf:
                result = Process.process_argv([buf], self)
            else:
                #
                infile.close()
                #
                # handle HUP by exiting process
                #
                if fd == 0:
                    Gtk.main_quit()
                #
                result = True
        #
        return result

class BrowserLauncher(object):
    @classmethod
    def start(self):
        Gtk.init(sys.argv)

        browser = Browser()

        result = Process.process_argv(sys.argv[1:], browser)

        if not is_open_stdin_pipe:
            #
            browser.add_io_in(0, sys.stdin)

        Gtk.main()

if __name__ == "__main__":
    BrowserLauncher.start()

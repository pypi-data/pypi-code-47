#!/usr/bin/env python
#
# Copyright (C) 2015-2019 David J. Beal, All Rights Reserved
#

from display import *
import cytoolz
from cytoolz.curried import *
import re
import sys
import os
import array

from gom.queue import Queue

import ctypes

#
# TODO: move windows with script
# TODO: move windows to anywhere on virtual desktop
# TODO: resize windows with script
#


def reduceinitial(fn, initial, seq):
    return reduce(fn, seq, initial)

reduceinitial = cytoolz.curry(reduceinitial)

class WmSizeHints(object):
    allflags = [
        # USPosition: User-specified x, y
        ('USPosition', Xlib.Xutil.USPosition),
        # USSize: User-specified width, height
        ('USSize', Xlib.Xutil.USSize),
        # PPosition: Program-specified position
        ('PPosition', Xlib.Xutil.PPosition),
        # PSize: Program-specified size
        ('PSize', Xlib.Xutil.PSize),
        # PMinSize: Program-specified minimum size
        ('PMinSize', Xlib.Xutil.PMinSize),
        # PMaxSize: Program-specified maximum size
        ('PMaxSize', Xlib.Xutil.PMaxSize),
        # PResizeInc: Program-specified resize increments
        ('PResizeInc', Xlib.Xutil.PResizeInc),
        # PAspect: Program-specified min and max aspect ratios
        ('PAspect', Xlib.Xutil.PAspect),
        # PBaseSize: Program-specified base size
        ('PBaseSize', Xlib.Xutil.PBaseSize),
        # PWinGravity: Program-specified window gravity
        ('PWinGravity', Xlib.Xutil.PWinGravity),
    ]
    #
    @classmethod
    def showflags(self, flags):
        #
        result = []
        #
        for (flagname, flag) in self.allflags:
            if flag & flags:
                result.append(flagname)
        #
        return result

class WMX(object):
    @classmethod
    def get_property_value_by_any_name(self, atomnameit, xid):
        #
        atomit = []
        #
        for atom_name in atomnameit:
            atom = Display.display.get_atom(atom_name)
            atomit.append(atom)
        #
        result = self.get_property_value_by_first_atom(atomit, xid)
        #
        return result

    @classmethod
    def get_property_value_by_name(self, atom_name, xid):
        #
        return self.get_property_value_by_any_name([atom_name], xid)

    @classmethod
    def get_supported_property_names(self, xid):
        result = []
        supported = self.get_property_value_by_name('_NET_SUPPORTED', xid)
        if supported is not None:
            for atom in supported:
                name = Display.display.get_atom_name(atom)
                result.append(name)
        return result

    @classmethod
    def get_desktop_geometry(self):
        result = None
        value = self.get_property_value_by_name('_NET_DESKTOP_GEOMETRY', Display.root.id)
        if value is not None:
            result = tuple(map(int, value))
        return result

    @classmethod
    def get_desktop_viewport(self):
        result = None
        value = self.get_property_value_by_name('_NET_DESKTOP_VIEWPORT', Display.root.id)
        if value is not None:
            off = tuple(map(int, value))
            dim = (Display.screen.width_in_pixels, Display.screen.height_in_pixels)
            result = (off, dim)
        return result

    @classmethod
    def get_workarea(self):
        result = None

        value = self.get_property_value_by_name('_NET_WORKAREA', Display.root.id)
        if value is not None:
            result = tuple(map(int, value))

        return result

    @classmethod
    def get_desktop_arrangement(self):
        #
        # return number of rows and columns in desktop
        #
        (desktop_width, desktop_height) = self.get_desktop_geometry()

        column_count = desktop_width // Display.screen.width_in_pixels
        row_count = desktop_height // Display.screen.height_in_pixels

        return {'column_count': column_count, 'row_count': row_count}

    @classmethod
    def viewport_index_to_offset(self, col, row):
        shape = self.get_desktop_arrangement()
        #
        column_count = shape['column_count']
        row_count = shape['row_count']

        col = min(max(col, 0), column_count - 1)
        row = min(max(row, 0), row_count - 1)

        x = Display.screen.width_in_pixels * col
        y = Display.screen.height_in_pixels * row

        return (x, y)

    @classmethod
    def get_viewport_size(self):
        width = Display.screen.width_in_pixels
        height = Display.screen.height_in_pixels
        return dict(zip(('width', 'height'), (width, height)))
        #
    #
    @classmethod
    def get_absolute_desktop_offset_to_viewport_relative(self, abs_x, abs_y):
        #
        vps = self.get_viewport_size()
        #
        column_index = abs_x // vps['width']
        row_index = abs_y // vps['height']
        #
        vp = self.get_desktop_viewport()
        #
        x = vp[0][0]
        y = vp[0][1]
        #
        vp_x = abs_x - x
        vp_y = abs_y - y
        #
        return {
            'column_index': column_index,
            'row_index': row_index,
            'vp_x': vp_x,
            'vp_y': vp_y,
        }
        #
    #
    @classmethod
    def set_viewport(self, column_index, row_index):
        #
        (x, y) = self.viewport_index_to_offset(column_index, row_index)
        #
        WMX.send_client_message(Display.root, '_NET_DESKTOP_VIEWPORT', [x, y])
        #
    #
    @classmethod
    def send_event(self, event):
        Display.root.send_event(event)
        Display.display.flush()

    @classmethod
    def send_client_message(self, win, atom_name, data):
        if type(data) is not array.array:
            data = data + [0] * max((5 - len(data)), 0)
        fmt = 32
        event = Xlib.protocol.event.ClientMessage(window = win, client_type = Display.display.get_atom(atom_name), data = (fmt, data))
        mask = X.SubstructureRedirectMask | X.SubstructureNotifyMask
        Display.root.send_event(event, event_mask = mask)
        Display.display.flush()

    @classmethod
    def get_active_window(self):
        result = self.get_property_value_by_name('_NET_ACTIVE_WINDOW', Display.root.id)
        if result is not None:
            result = int(result[0])
        return result

    @classmethod
    def get_window_by_xid(self, xid):
        win = Display.display.create_resource_object('window', xid)
        return win

    @classmethod
    def set_active_window(self, xid):
        win = self.get_window_by_xid(xid)
        WMX.send_client_message(win, '_NET_ACTIVE_WINDOW', [2, 0, 0])

    @classmethod
    def get_clients(self):
        result = ()
        clients = self.get_property_value_by_name('_NET_CLIENT_LIST', Display.root.id)
        if clients is not None:
            result = tuple(map(int, clients))
        return result

    @classmethod
    def maybexerror(self, fn):
        #
        # TODO: should this return some unique Error object instead of None?
        #
        try:
            result = fn()
        except Xlib.error.XError as e:
            #
            Queue.errod([('exception', str(e))])
            #
            result = None
        #
        return result

    @classmethod
    def get_property_value_by_atom(WMX, atom, xid):
        #
        result = None
        #
        # creating a window resource doesnt throw an exception
        #
        win = WMX.get_window_by_xid(xid)
        #
        get = lambda: win.get_full_property(atom, 0)
        #
        prop = WMX.maybexerror(get)
        #
        if prop is not None:
            result = prop.value
        #
        return result

    @classmethod
    def get_property_value_by_first_atom(self, atomit, xid):
        #
        result = None

        for atom in atomit:
            result = self.get_property_value_by_atom(atom, xid)
            if result is not None:
                break

        return result

    @classmethod
    def get_client_name(self, xid):
        return WMX.get_property_value_by_any_name(['_NET_WM_NAME', 'WM_NAME'], xid)
        #
    #
    @classmethod
    def get_clients_by_any_property_name(self, atomnameit):
        return pipe(
            WMX.get_clients(),
            map(lambda xid: (WMX.get_property_value_by_any_name(atomnameit, xid), xid)),
            filter(lambda (atom_value, xid): atom_value is not None)
        )
        #
    #
    @classmethod
    def get_clients_by_name(self, name):
        return filter(lambda (wname, xid): wname == name, WMX.get_clients_by_any_property_name(['_NET_WM_NAME', 'WM_NAME']))

    @classmethod
    def get_pointer(self):
        d = Display.root.query_pointer()._data
        return (d['root_x'], d['root_y'])

    @classmethod
    def get_point_rect_distance(self, p, geom):

        (x, y) = p
        ((wx, wy), (ww, wh)) = geom

        wx0 = wx
        wx1 = wx + ww

        wy0 = wy
        wy1 = wy + wh

        if x > wx0:
            if x < wx1:
                dx = 0
            else:
                dx = x - wx1
        else:
            dx = wx0 - x

        if y > wy0:
            if y < wy1:
                # left side
                dy = 0
            else:
                dy = y - wy1
        else:
            dy = wy0 - y

        d = int((dx ** 2 + dy ** 2) ** 0.5)

        return d

    @classmethod
    def get_absolute_desktop_window_geometry(self, xid):
        """Return geometry relative to entire desktop."""
        geom = WMX.get_relative_window_geometry(xid)

        # add the current viewport
        vp = WMX.get_desktop_viewport()

        ((gx, gy), (gw, gh)) = geom
        ((vx, vy), (vw, vh)) = vp

        result = ((gx + vx, gy + vy), (gw, gh))

        return result

    @classmethod
    def get_relative_window_geometry(self, xid):
        """Return geometry relative to entire desktop."""
        win = self.get_window_by_xid(xid)
        geom = win.get_geometry()
        tsl = Display.root.translate_coords(win, geom.x, geom.y)._data
        (wx, wy) = (tsl['x'], tsl['y'])

        return ((wx, wy), (geom.width, geom.height))
        #
    #
    @classmethod
    def get_absolute_window_geometry(WMX, xid):
        #
        # absolute from root instead of parent window
        #
        result = None
        #
        win = WMX.get_window_by_xid(xid)
        #
        geom = WMX.maybexerror(lambda: win.get_geometry())
        #
        if geom is not None:
            #
            tsl = WMX.maybexerror(lambda: Display.root.translate_coords(win, geom.x, geom.y))

            if tsl is not None:
                #
                # adj = WMX.adjust_coords_for_frame(xid, tsl.x, tsl.y)
                #
                result = ((tsl.x, tsl.y), (geom.width, geom.height))
                #
        #
        return result
        #
    #
    @classmethod
    def is_window_within_viewport(self, xid):
        result = False
        geom = WMX.get_absolute_desktop_window_geometry(xid)
        ((x, y), (w, h)) = geom
        vp = WMX.get_desktop_viewport()
        ((vx, vy), (vw, vh)) = vp
        if x >= vx:
            if x < vx + vw:
                if y >= vy:
                    if y < vy + vh:
                        result = True
        return result

    @classmethod
    def get_client_distance_to_pointer(self, xid):
        ptr = WMX.get_pointer()
        geom = WMX.get_absolute_desktop_window_geometry(xid)
        result = WMX.get_point_rect_distance(ptr, geom)
        return result

    @classmethod
    def get_nearest_client(self, clients):
        result = None

        if clients is not None:
            it = pipe(
                clients,
                filter(lambda xid: WMX.is_window_within_viewport(xid)),
                map(lambda xid: (xid, WMX.get_client_distance_to_pointer(xid))),
                # reduceinitial(lambda x, y: x if y is None else (y if x is None else (x if x[1] < y[1] else y)), None)
            )
            first = next(it, None)
            if first is not None:
                result = reduce(lambda x, y: x if x[1] < y[1] else y, it, first)[0]

        return result

    #
    @classmethod
    def get_clients_by_pid(self, pid):
        #
        return pipe(
            WMX.get_clients_by_any_property_name(['_NET_WM_PID']),
            filter(lambda (pidval, xid): pidval[0] == pid),
            map(get(1)),
        )
        #
    #
    @classmethod
    def find_by_atom_regex(self, atomnameit, atom_value_regex):
        pat = re.compile(atom_value_regex)
        return pipe(
            WMX.get_clients_by_any_property_name(atomnameit),
            filter(lambda (atom, xid): pat.match(atom))
        )

    @classmethod
    def find_nearest_by_atom_regex(self, atomnameit, atom_value_regex):
        return pipe(
            WMX.find_by_atom_regex(atomnameit, atom_value_regex),
            map(get(1)),
            WMX.get_nearest_client,
        )

    @classmethod
    def find_by_name(self, name):
        return WMX.find_by_atom_regex(['_NET_WM_NAME', 'WM_NAME'], '^' + name + '$')

    @classmethod
    def find_nearest_by_name(self, name):
        return pipe(
            WMX.find_by_name(name),
            map(get(1)),
            WMX.get_nearest_client,
        )

    @classmethod
    def activate_nearest_by_name(self, name):
        xid = WMX.find_nearest_by_name(name)
        if xid is not None:
            WMX.set_active_window(xid)
        else:
            os.write(2, 'wmx: cannot find window ' + str(name) + '\n')

    @classmethod
    def activate_by_name(self, name):
        result = WMX.find_by_name(name)
        for (name, xid) in result:
            WMX.set_active_window(xid)

    @classmethod
    def stack_window(WMX, xid, sibling, aboveorbelow):
        WMX.send_client_message(xid, '_NET_RESTACK_WINDOW', [2, sibling, aboveorbelow])

    @classmethod
    def stack_bottom(WMX, xid):
        return WMX.stack_window(xid, 0, X.Below)

    @classmethod
    def stack_top(WMX, xid):
        return WMX.stack_window(xid, 0, X.Above)

    @classmethod
    def stack_nearest_window_by_name(WMX, name, aboveorbelow):
        xid = WMX.find_nearest_by_name(name)
        if xid is not None:
            WMX.stack_window(xid, 0, aboveorbelow)
        else:
            os.write(2, 'wmx: cannot find window ' + str(name) + '\n')

    @classmethod
    def stack_active_window(WMX, aboveorbelow):
        #
        xid = WMX.get_active_window()
        #
        if xid is not None:
            WMX.stack_window(xid, 0, aboveorbelow)
        else:
            os.write(2, 'wmx: no active window\n')

    @classmethod
    def get_master_window(WMX, xid):
        #
        window = WMX.get_window_by_xid(xid)
        #
        loop = True
        #
        while loop:
            #
            # Queue.debug(window = window)
            #
            parent = window.query_tree().parent
            #
            if parent != Display.root:
                window = parent
            else:
                loop = False
            #
        #
        return window
    #
    @classmethod
    def get_descendants(WMX, xid):
        #
        result = []
        #
        rootwin = WMX.get_window_by_xid(xid)
        #
        roots = [rootwin]
        #
        while roots:
            win = roots.pop()
            #
            result.append(win)
            #
            roots.extend(win.query_tree().children)
        #
        return result
    #
    @classmethod
    def set_window_ppositionsize(WMX, xid):
        win = WMX.get_window_by_xid(xid)
        wm_normal_hints = win.get_wm_normal_hints()
        if 1:
            #
            print('before')
            #
            print(WmSizeHints.showflags(wm_normal_hints.flags))
            #
        wm_normal_hints.flags |= Xlib.Xutil.PPosition
        win.set_wm_normal_hints(wm_normal_hints)
        if 1:
            print('verify')
            wm_normal_hints = win.get_wm_normal_hints()
            print(WmSizeHints.showflags(wm_normal_hints.flags))
        #
    #
    @classmethod
    def get_frame_extents(WMX, xid):
        #
        extents = WMX.maybexerror(lambda: WMX.get_property_value_by_name('_NET_FRAME_EXTENTS', xid))
        #
        return extents
        #
    #
    @classmethod
    def get_attributes(WMX, xid):
        window = WMX.get_window_by_xid(xid)
        attributes = WMX.maybexerror(lambda: window.get_attributes())
        return attributes
        #
    #
    @classmethod
    def moveresize_window(WMX, xid, x, y, w, h):
        #
        dt = WMX.get_absolute_desktop_offset_to_viewport_relative(x, y)
        #
        x = dt['vp_x']
        y = dt['vp_y']
        #
        if 0:
            #
            # set PPosition in WM_SIZE_HINTS
            #
            WMX.set_window_ppositionsize(xid)
            #
        #
        ix = int(x)
        iy = int(y)
        iw = int(w)
        ih = int(h)
        #
        gravity = X.NorthWestGravity
        #
        # ignores decoration
        #
        gravity = X.StaticGravity
        #
        cwmask = X.CWX|X.CWY|X.CWWidth|X.CWHeight
        #
        source = 1
        #
        data = gravity | cwmask << 8 | source << 12
        #
        evdata = [data, ix, iy, iw, ih]
        #
        # convert signed to unsigned
        #
        evdatau32 = [ctypes.c_uint32(x).value for x in evdata]
        #
        # Queue.infod([('evdatau32', evdatau32)])
        #
        evdata = array.array('I', evdatau32)
        #
        WMX.send_client_message(xid, '_NET_MOVERESIZE_WINDOW', evdata)
        #
    #
    @classmethod
    def adjust_coords_for_frame(WMX, xid, x, y):
        #
        result = None
        #
        extents = WMX.get_frame_extents(xid)
        #
        if extents:
            (frame_left, frame_right, frame_top, frame_bottom) = extents
            #
            adjx = x + frame_left
            adjy = y + frame_top
            #
            result = (adjx, adjy)
            #
        #
        return result
        #
    #
    @classmethod
    def get_absolute_window_coords(WMX, xid):
        #
        result = None
        #
        absgeom = WMX.get_absolute_window_geometry(xid)
        #
        if absgeom is not None:
            #
            result = (absgeom[0], absgeom[1])
            #
        #
        return result
        #
    #
#



if __name__ == '__main__':
    if sys.argv[1] == 'activate_nearest_by_name':
        window_name = sys.argv[2]
        WMX.activate_nearest_by_name(window_name)
    elif sys.argv[1] == 'activate_by_name':
        window_name = sys.argv[2]
        WMX.activate_by_name(window_name)
    elif sys.argv[1] == 'exec':
        #
        # example : "wmx.py exec 'WMX.stack_nearest_window_by_name(\"(xterm|tmux)\", X.Below)'"
        #
        exec(sys.argv[2])

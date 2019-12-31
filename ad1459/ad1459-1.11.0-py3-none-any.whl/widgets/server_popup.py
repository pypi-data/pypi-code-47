#!/usr/bin/env python3

""" AD1459, an IRC Client

  This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/.

  A popover for connecting to servers.
"""

import configparser
import keyring as Keyring
import os
import pathlib

USER_HOME_PATH = str(pathlib.Path.home())
CONFIG_DIR_PATH = os.path.join(USER_HOME_PATH, '.config')
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR_PATH, 'ad1459.ini')

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class ServerPopover(Gtk.Popover):

    def __init__(self):
        super().__init__()

        self.config = configparser.ConfigParser()
        self.keyring = Keyring.get_keyring()

        self.config.read(CONFIG_FILE_PATH)
        
        layout_grid = Gtk.Grid()
        layout_grid.set_column_spacing(6)
        layout_grid.set_row_spacing(12)
        layout_grid.props.margin = 6
        self.add(layout_grid)
        
        # Saved Networks
        self.saved_combo = Gtk.ComboBoxText()
        self.init_saved_combo()
        self.saved_combo.set_active(-1)
        Gtk.StyleContext.add_class(
            self.saved_combo.get_style_context(), 'connect-entry'
        )
        self.saved_combo.connect('changed', self.on_saved_combo_changed)
        layout_grid.attach(self.saved_combo, 0, 0, 2, 1)

        self.connect_grid = Gtk.Grid()
        self.connect_grid.set_orientation(Gtk.Orientation.VERTICAL)
        Gtk.StyleContext.add_class(self.connect_grid.get_style_context(), 'linked')
        Gtk.StyleContext.add_class(self.connect_grid.get_style_context(), 'connect-entry')
        layout_grid.attach(self.connect_grid, 0, 1, 2, 1)

        # Network Name
        self.name_entry = Gtk.Entry()
        self.name_entry.simple_entry = True
        self.name_entry.set_placeholder_text('Network Name')
        self.connect_grid.attach(self.name_entry, 0, 0, 2, 1)

        # nickname
        self.nick_entry = Gtk.Entry()
        self.nick_entry.simple_entry = True
        self.nick_entry.set_placeholder_text('Nickname')
        self.connect_grid.attach(self.nick_entry, 0, 1, 2, 1)

        # username
        self.username_entry = Gtk.Entry()
        self.username_entry.simple_entry = True
        self.username_entry.set_placeholder_text('Username/Ident')
        self.connect_grid.attach(self.username_entry, 0, 2, 2, 1)

        # realname
        self.realname_entry = Gtk.Entry()
        self.realname_entry.simple_entry = True
        self.realname_entry.set_placeholder_text('Real Name')
        self.connect_grid.attach(self.realname_entry, 0, 3, 2, 1)

        # server
        self.server_entry = Gtk.Entry()
        self.server_entry.simple_entry = True
        self.server_entry.set_placeholder_text('Server')
        self.connect_grid.attach(self.server_entry, 0, 4, 1, 1)

        # port
        port_adj = Gtk.Adjustment.new(
            value=6697,
            lower=1,
            upper=65535,
            step_increment=1,
            page_increment=1,
            page_size=0
        )

        self.port_entry = Gtk.SpinButton()
        self.port_entry.simple_entry = True
        self.port_entry.configure(port_adj, 1, 0)
        self.port_entry.set_numeric(True)
        self.port_entry.set_placeholder_text('Port')
        self.connect_grid.attach(self.port_entry, 1, 4, 1, 1)

        # auth
        self.auth_combo = Gtk.ComboBoxText()
        self.auth_combo.simple_entry = True
        self.auth_combo.append_text('SASL Authentication')
        self.auth_combo.append_text('Server Password')
        self.auth_combo.append_text('No Authentication')
        self.auth_combo.set_active(0)
        Gtk.StyleContext.add_class(
            self.auth_combo.get_style_context(), 'connect-entry'
        )
        self.connect_grid.attach(self.auth_combo, 0, 5, 2, 1)

        # password
        self.password_entry = Gtk.Entry()
        self.password_entry.simple_entry = True
        self.password_entry.set_placeholder_text('Password')
        self.password_entry.set_visibility(False)
        self.connect_grid.attach(self.password_entry, 0, 6, 2, 1)

        # TLS Check
        self.tls_check = Gtk.CheckButton()
        self.tls_check.simple_entry = True
        self.tls_check.set_label('TLS')
        self.tls_check.set_active(True)
        layout_grid.attach(self.tls_check, 0, 2, 1, 1)

        # Save check
        self.save_check = Gtk.CheckButton()
        self.save_check.set_label('Save')
        self.save_check.set_active(True)
        layout_grid.attach(self.save_check, 1, 2, 1, 1)

        # Server entry
        self.server_line_entry = Gtk.Entry()
        self.server_line_entry.simple_entry = False
        self.server_line_entry.set_placeholder_text('Server line')
        layout_grid.attach(self.server_line_entry, 0, 3, 2, 1)

        # Connect Button
        self.connect_button = Gtk.Button()
        self.connect_button.set_label('Connect')
        Gtk.StyleContext.add_class(
            self.connect_button.get_style_context(), 'suggested-action'
        )
        layout_grid.attach(self.connect_button, 0, 4, 2, 1)

        self.widgets = [
            self.name_entry,
            self.nick_entry,
            self.username_entry,
            self.realname_entry,
            self.server_entry,
            self.password_entry
        ]

    @property 
    def name(self):
        return self.name_entry.get_text()

    @property 
    def nick(self):
        return self.nick_entry.get_text()

    @property 
    def username(self):
        if self.username_entry.get_text() != '':
            return self.username_entry.get_text()
        else:
            return self.nick

    @property 
    def realname(self):
        if self.realname_entry.get_text() != '':
            return self.realname_entry.get_text()
        else:
            return self.nick

    @property 
    def server(self):
        return self.server_entry.get_text()

    @property 
    def port(self):
        return self.port_entry.get_value()

    @property 
    def auth(self):
        auth = self.auth_combo.get_active_text()
        print(auth)
        if auth == 'SASL Authentication':
            return 'sasl'

        elif auth == 'Server Password':
            return 'pass'

        else:
            return 'none'

    @property 
    def password(self):
        return self.password_entry.get_text()

    @property 
    def tls(self):
        return self.tls_check.get_active()

    @property 
    def save(self):
        return self.save_check.get_active()

    @property 
    def server_line(self):
        return self.server_line_entry.get_text()
    
    def on_saved_combo_changed(self, combo, data=None):
        """ changed signal handler for saved_combo."""
        network = combo.get_active_text()

        if network == 'New...':
            self.reset_all_text()
        
        else:
            self.config.read(CONFIG_FILE_PATH)
            self.name_entry.set_text(
                self.config[network]['name']
            )
            self.nick_entry.set_text(
                self.config[network]['nickname']
            )
            self.username_entry.set_text(
                self.config[network]['username']
            )
            self.realname_entry.set_text(
                self.config[network]['realname']
            )
            self.server_entry.set_text(
                self.config[network]['host']
            )
            self.port_entry.set_value(
                int(self.config[network]['port'])
            )
            if self.config[network]['auth'] == 'sasl':
                self.auth_combo.set_active(0)
            elif self.config[network]['auth'] == 'pass':
                self.auth_combo.set_active(1)
            else:
                self.auth_combo.set_active(2)
            if self.config[network]['tls'] == 'True':
                self.tls_check.set_active(True)
            else:
                self.tls_check.set_active(False)
            keyring_service = (
                f'{self.config[network]["name"]}-{self.config[network]["host"]}'
            )
            keyring_username = (
                f'{self.config[network]["nickname"]}'
                f'!{self.config[network]["username"]}'
                f'@{self.config[network]["name"]}'
            )
            self.password_entry.set_text(
                self.keyring.get_password(keyring_service, keyring_username)
            )
            self.save_check.set_active(True)

    def init_saved_combo(self):
        """Clears any existing items from the saved network combo and sets it 
        up with new ones.
        """
        self.saved_combo.remove_all()
        self.saved_combo.append_text('New...')
        for network in self.config.sections():
            self.saved_combo.append_text(network)

    def reset_all_text(self):
        self.saved_combo.set_active(0)
        self.name_entry.set_text('')
        self.nick_entry.set_text('')
        self.username_entry.set_text('')
        self.realname_entry.set_text('')
        self.server_entry.set_text('')
        self.port_entry.set_value(6697)
        self.auth_combo.set_active(0)
        self.password_entry.set_text('')
        self.tls_check.set_active(True)
        self.save_check.set_active(True)
        self.server_line_entry.set_text('')

    def get_all_widgets_text(self):
        """ Returns the text of all widgets, formatted as a serverline."""

        line = ''
        if self.auth_combo.get_active_text() == 'SASL Authentication':
            line = 'sasl'
            
        elif self.auth_combo.get_active_text() == 'Server Password':
            line = 'pass'

        else:
            line = 'none'

        line = f'{line} {self.name_entry.get_text()}'
        line = f'{line} {self.server_entry.get_text()}'
        line = f'{line} {int(self.port_entry.get_value())}'
        line = f'{line} {self.nick_entry.get_text()}'
        line = f'{line} {self.username_entry.get_text()}'
        line = f'{line} {self.realname_entry.get_text()}'
        line = f'{line} {self.password_entry.get_text()}'
        
        return line.strip()

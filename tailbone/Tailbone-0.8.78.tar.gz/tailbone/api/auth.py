# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2018 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Tailbone Web API - Auth Views
"""

from __future__ import unicode_literals, absolute_import

from rattail.db.auth import authenticate_user

from tailbone.api import APIView, api
from tailbone.db import Session
from tailbone.auth import login_user, logout_user


class AuthenticationView(APIView):

    def user_info(self, user):
        return {
            'ok': True,
            'user': {
                'uuid': user.uuid,
                'username': user.username,
                'display_name': user.display_name,
                'short_name': user.get_short_name(),
            },
        }

    @api
    def check_session(self):
        """
        View to serve as "no-op" / ping action to check current user's session.
        This will establish a server-side web session for the user if none
        exists.  Note that this also resets the user's session timer.
        """
        data = {'ok': True}
        if self.request.user:
            data = self.user_info(self.request.user)
            data['user']['is_admin'] = self.request.is_admin
            data['user']['is_root'] = self.request.is_root

        data['permissions'] = list(self.request.tailbone_cached_permissions)

        # background color may be set per-request, by some apps
        if hasattr(self.request, 'background_color') and self.request.background_color:
            data['background_color'] = self.request.background_color
        else: # otherwise we use the one from config
            data['background_color'] = self.rattail_config.get(
                'tailbone', 'background_color')

        return data

    @api
    def login(self):
        """
        API login view.
        """
        if self.request.method == 'OPTIONS':
            return self.request.response

        username = self.request.json.get('username')
        password = self.request.json.get('password')
        if not (username and password):
            return {'error': "Invalid username or password"}

        user = self.authenticate_user(username, password)
        if not user:
            return {'error': "Invalid username or password"}

        login_user(self.request, user)
        return self.user_info(user)

    def authenticate_user(self, username, password):
        return authenticate_user(Session(), username, password)

    @api
    def logout(self):
        """
        API logout view.
        """
        if self.request.method == 'OPTIONS':
            return self.request.response

        logout_user(self.request)
        return {'ok': True}

    @api
    def become_root(self):
        """
        Elevate the current request to 'root' for full system access.
        """
        if not self.request.is_admin:
            raise self.forbidden()
        self.request.user.record_event(self.enum.USER_EVENT_BECOME_ROOT)
        self.request.session['is_root'] = True
        return self.user_info(self.request.user)

    @api
    def stop_root(self):
        """
        Lower the current request from 'root' back to normal access.
        """
        if not self.request.is_admin:
            raise self.forbidden()
        self.request.user.record_event(self.enum.USER_EVENT_STOP_ROOT)
        self.request.session['is_root'] = False
        return self.user_info(self.request.user)

    @classmethod
    def defaults(cls, config):

        # session
        config.add_route('api.session', '/session', request_method='GET')
        config.add_view(cls, attr='check_session', route_name='api.session', renderer='json')

        # login
        config.add_route('api.login', '/login', request_method=('OPTIONS', 'POST'))
        config.add_view(cls, attr='login', route_name='api.login', renderer='json')

        # logout
        config.add_route('api.logout', '/logout', request_method=('OPTIONS', 'POST'))
        config.add_view(cls, attr='logout', route_name='api.logout', renderer='json')

        # become root
        config.add_route('api.become_root', '/become-root', request_method=('OPTIONS', 'POST'))
        config.add_view(cls, attr='become_root', route_name='api.become_root', renderer='json')

        # stop root
        config.add_route('api.stop_root', '/stop-root', request_method=('OPTIONS', 'POST'))
        config.add_view(cls, attr='stop_root', route_name='api.stop_root', renderer='json')


def includeme(config):
    AuthenticationView.defaults(config)

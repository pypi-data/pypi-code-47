#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2009-2015:
#    Gabes Jean, naparuba@gmail.com
#    Gerhard Lausser, Gerhard.Lausser@consol.de
#    Gregory Starck, g.starck@gmail.com
#    Hartmut Goebel, h.goebel@goebel-consult.de
#    Frederic Mohier, frederic.mohier@gmail.com
#    Bjorn, @Simage
#
# This file is part of Shinken.
#
# Shinken is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Shinken is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

"""
This class is for linking the WebUI with Graphite,
for mainly get graphs and links.
"""
import os
import re
import socket
import time

from .graphite_utils import GraphStyle
from .util import GraphFactory

# Check if Alignak is installed
ALIGNAK = os.environ.get('ALIGNAK_DAEMON', None) is not None
print("[UI-Graphite] Underlying monitoring framework: %s" % ('Alignak' if ALIGNAK else 'Shinken'))

# Alignak / Shinken base module are slightly different
if ALIGNAK:
    # Specific logger configuration
    import logging
    from alignak.log import ALIGNAK_LOGGER_NAME

    logger = logging.getLogger(ALIGNAK_LOGGER_NAME + ".webui.ui_graphite")

    from alignak.basemodule import BaseModule
    from alignak.misc.perfdata import PerfDatas
else:
    # Shinken logger configuration
    from shinken.log import logger
    from shinken.basemodule import BaseModule
    from shinken.misc.perfdata import PerfDatas


properties = {
    'daemons': ['webui'],
    'type': 'graphite_webui'
}


# called by the plugin manager
def get_instance(mod_conf):
    if ALIGNAK:
        logger.info("Give an instance of Graphite_Webui for alias: %s", mod_conf.module_alias)
    else:
        logger.info("Give an instance of Graphite_Webui for alias: %s", mod_conf.module_name)

    return Graphite_Webui(mod_conf)


class Graphite_Webui(BaseModule):
    def __init__(self, modconf):
        BaseModule.__init__(self, modconf)
        self._uri = ''
        self.app = None

        # load styles
        self.styles = dict(default=GraphStyle())
        self._load_styles(modconf)

        self.uri = getattr(modconf, 'uri', '')
        logger.info("[Graphite UI] Graphite uri: %s", self.uri)

        # optional "sub-folder" in graphite to hold the data of a specific host
        self.prefix = getattr(modconf, 'prefix', '')
        logger.info("[Graphite UI] Graphite prefix: %s", self.prefix)

        # optional host "sub-folder" in graphite to hold the data of a specific host
        self.graphite_data_source = getattr(modconf, 'graphite_data_source', '')
        logger.info("[Graphite UI] Graphite data source: %s", self.graphite_data_source)

        # service name to use for host check
        self.hostcheck = getattr(modconf, 'hostcheck', '')
        logger.info("[Graphite UI] host check service name: %s", self.hostcheck)

        self.templates_path = getattr(modconf, 'templates_path', '/tmp')
        logger.info("[Graphite UI] templates path: %s", self.templates_path)

        # Use warning, critical, min, max
        for s in ('warning', 'critical', 'min', 'max'):
            n = 'use_%s' % s
            setattr(self, n, bool(getattr(modconf, n, True)))
            logger.info("[Graphite UI] %s metrics: %d", n, getattr(self, n))

            n = 'color_%s' % s
            setattr(self, n, getattr(modconf, n, 'black'))
            logger.info("[Graphite UI] %s metrics: %s", n, getattr(self, n))

        # Graphs parameters
        self.tz = getattr(modconf, 'tz', 'Europe/Paris')
        logger.info("[Graphite UI] Graphite time zone: %s", self.tz)

    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        uri = value.strip()
        if not uri:
            raise ValueError('Invalid URI provided to the WebUI Graphite module.')
        if not uri.endswith('/'):
            uri += '/'

        # Change YOURSERVERNAME by our server name if we got it
        if 'YOURSERVERNAME' in uri:
            my_name = socket.gethostname()
            uri = uri.replace('YOURSERVERNAME', my_name)
        self._uri = uri

    def _load_styles(self, modconf):
        lineMode = getattr(modconf, 'lineMode', 'connected')

        # Specify font and picture size for dashboard widget
        font = getattr(modconf, 'dashboard_view_font', '8')
        width = getattr(modconf, 'dashboard_view_width', '320')
        height = getattr(modconf, 'dashboard_view_height', '240')
        self.styles['dashboard'] = GraphStyle(width=width, height=height, font_size=font, line_style=lineMode)

        # Specify font and picture size for element view
        font = getattr(modconf, 'detail_view_font', '8')
        width = getattr(modconf, 'detail_view_width', '586')
        height = getattr(modconf, 'detail_view_height', '308')
        self.styles['detail'] = GraphStyle(width=width, height=height, font_size=font, line_style=lineMode)

    def init(self):
        """Called by Broker so we can do init stuff"""
        logger.info("Initializing ...")
        # Return True to confirm correct initialization
        return True

    def do_loop_turn(self):
        """Defined because it is an abstract method in our base class"""
        time.sleep(0.1)

    # To load the webui application
    def load(self, app):
        self.app = app

    # Give the link for the GRAPHITE UI, with a Name
    def get_external_ui_link(self):
        return {'label': 'Graphite', 'uri': self.uri}

    # For a perf_data like /=30MB;4899;4568;1234;0  /var=50MB;4899;4568;1234;0 /toto=
    # return ('/', '30'), ('/var', '50')
    # TODO - ask graphite for the metrics it knows about by posting to {graphiteserver}/find
    # This really belongs in the factory, however by leaving it in here we decouple the factory from any direct shinken
    # dependencies and can test without the shinken libraries installed
    def get_metric_and_value(self, service, perf_data):
        result = []
        metrics = PerfDatas(perf_data)

        # Separate perfdata multiple values
        multival = re.compile(r'_(\d+)$')

        for e in metrics:
            name = multival.sub(r'.\1', e.name)

            # bailout if no value
            if name == '':
                continue

            # get metric value and its thresholds values if they exist
            metric = dict(
                name=name,
                uom=e.uom
            )

            # Get or ignore extra values depending upon module configuration
            for s in ('warning', 'critical', 'min', 'max'):
                if getattr(e, s) is not None and getattr(self, 'use_%s' % s):
                    metric[s] = getattr(e, s)

            result.append(metric)

        logger.debug("[Graphite UI] get_metric_and_value: %s", result)
        return result

    def get_relative_graph_uris(self, element, duration, source='detail'):
        logger.debug("[Graphite UI] get_relative_graph_uris, duration: %d", duration)
        graph_end = time.time()
        graph_start = graph_end - duration
        factory = GraphFactory(element, graph_start, graph_end, source, cfg=self, log=logger)
        return factory.get_graph_uris()

    def get_graph_uris(self, element, graph_start=None, graph_end=None, source='detail'):
        logger.debug("[Graphite UI] get_graph_uris, start/end: %d/%d", graph_start, graph_end)
        factory = GraphFactory(element, graph_start, graph_end, source, cfg=self, log=logger)
        return factory.get_graph_uris()

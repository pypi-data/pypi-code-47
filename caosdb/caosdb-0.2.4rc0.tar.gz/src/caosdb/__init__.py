# -*- coding: utf-8 -*-
#
# ** header v3.0
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2018 Research Group Biomedical Physics,
# Max-Planck-Institute for Dynamics and Self-Organization Göttingen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ** end header
#

# Import of the connection function (which is used to connect to the DB):
from os.path import expanduser, join
from os import getcwd, environ
from caosdb.configuration import configure, get_config

from caosdb.common import administration
from caosdb.connection.connection import configure_connection, get_connection
# Import of the basic  API classes:
from caosdb.common.models import (QueryTemplate, Permissions, ACL, File, Record,
                                  RecordType, Property, Message, Container,
                                  DropOffBox, Entity, Query, Info, LIST,
                                  DOUBLE, REFERENCE, TEXT, DATETIME, INTEGER,
                                  FILE, BOOLEAN, TIMESPAN, OBLIGATORY,
                                  SUGGESTED, RECOMMENDED, FIX, ALL, NONE)
# Import of exceptions
from caosdb.exceptions import *
from caosdb.common.models import (delete, execute_query, raise_errors,
                                  get_global_acl, get_known_permissions)
# Import of convenience methods:
import caosdb.apiutils

# read configuration these files
if "PYCAOSDBINI" in environ:
    configure(expanduser(environ["PYCAOSDBINI"]))
else:
    configure(expanduser('~/.pycaosdb.ini'))
configure(join(getcwd(), "pycaosdb.ini"))

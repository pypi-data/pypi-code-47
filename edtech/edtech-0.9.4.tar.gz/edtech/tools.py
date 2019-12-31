'''
This file is part of the EdTech library project at Full Sail University.

    Foobar is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

    Copyright (C) 2014, 2015 Full Sail University.
    Copyright (C) 2019 Cacti Council Inc.
'''

import random
import string
import re
import urllib.parse as urlparse
import time
import calendar

global stringCodecs
defaultCodecs = ['utf8', 'cp437']


def getRandomPassword(rangeLow = 7, rangeHigh = 16):
    size = int(round(random.SystemRandom().uniform(rangeLow, rangeHigh)))
    return ''.join(random.SystemRandom().choice(string.uppercase + string.lowercase + string.digits) for _ in xrange(size))


def transposeData(dataset):
    return [list(i) for i in zip(*dataset)]


def decodeString(value, codecs=defaultCodecs):
    for encoding in codecs:
        try:
            return value.decode(encoding)
        except:
            pass
    print("Couldn't decode string: " + value)


def parse_http_log_line(line):
    row = list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line)))

    if len(row) == 0:
        return None

    if len(row) < 9:
        print("bad log format:", row)
    ip_address, local_user, remote_user, timestamp, request, status, bytes_sent, referer, user_agent = row

    # Parse the timestamp
    diff_sec = int(timestamp[-5:-4] + "1") * (int(timestamp[-2:]) + int(timestamp[-4:-2]) * 60) * 60
    access_time = calendar.timegm(time.strptime(timestamp[:-6], "%d/%b/%Y:%H:%M:%S")) - diff_sec

    # Parse the request
    if request.find(' ') == -1:
        request_type = request
        resource_url = None
        document = None
        query_string = None
        query = None
    else:
        request_type, resource_url, = request.split(" ", 1)

        if resource_url.find(' ') == -1:
            http_version = None
        else:
            resource_url, http_version = resource_url.split(" ", 1)
            if http_version[:4].upper() != "HTTP":
                resource_url = resource_url + " " + http_version
                http_version = None

        resource = urlparse.urlparse(resource_url)
        document = resource.path
        query_string = urlparse.unquote(resource.query)
        query = urlparse.parse_qs(resource.query, True)

    return { 'ip_address': ip_address, 'local_user': local_user, 'remote_user': remote_user, 'access_time': access_time,
             'request_type': request_type, 'resource_url': resource_url, 'document': document, 'query': query, 'query_string': query_string,
             'status': status, 'bytes_sent': bytes_sent, 'referer': referer, 'user_agent': user_agent }

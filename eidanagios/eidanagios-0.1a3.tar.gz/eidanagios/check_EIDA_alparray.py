#!/usr/bin/env python3
#
# Nagios plugin to check if Alparray data is accessible
#
# Copyright (C) 2020 Javier Quinteros, GEOFON team
# <javier@gfz-potsdam.de>
#
# ----------------------------------------------------------------------

"""Nagios plugin to check if Alparray data is accessible

   :Platform:
       Linux
   :Copyright:
       GEOFON, Helmholtz-Zentrum Potsdam - Deutsches GeoForschungsZentrum GFZ
       <geofon@gfz-potsdam.de>
   :License:
       GNU General Public License, Version 3, 29 June 2007

   This program is free software; you can redistribute it and/or modify it
   under the terms of the GNU General Public License as published by the Free
   Software Foundation; either version 3, or (at your option) any later
   version. For more information, see http://www.gnu.org/

.. moduleauthor:: Javier Quinteros <javier@gfz-potsdam.de>, GEOFON, GFZ Potsdam
"""

import requests
import os
import sys
import time
import datetime
import random
import argparse
from requests.auth import HTTPDigestAuth


def nagios_output(service, status, message, perfvalues):
    print('%s %s: %s | %s' % (service, status, message, perfvalues))


def check_EIDA_Alparray(url, payload, timeout=9, token=None):
    """ Check if Alparray data is accessible at the node specified by url

        A file containing a token is expected in the home folder
        of the user running this script with filename '.eidatoken'
        Return 0: OK; 1: WARNING; 2: CRITICAL
    """

    # Default location for token
    if token is None:
        token = os.path.expanduser('~/.eidatoken')

    # Save starting time to measure performance
    start_time = time.time()

    username, password = authenticate(url, timeout=timeout,
                                      token=token)

    urlreq = url.replace('/auth', '/queryauth').replace('https://', 'http://')

    r = requests.get(urlreq, payload, auth=HTTPDigestAuth(username, password))
    if r.status_code != 200:
        nagios_output('ALPARRAY', 'FAILED', '%s returned a %s HTTP error code' % (urlreq, r.status_code),
                      'time=%fs' % (time.time() - start_time))
        return 2

    nagios_output('ALPARRAY', 'OK', '%s returned %d bytes' % (urlreq, len(r.content)),
                  'time=%fs' % (time.time() - start_time))
    return 0


def authenticate(url, timeout=9, token=None):
    """ Use the token passed in the parameter to get a username and password

        A file containing a token is expected in the home folder
        of the user running this script with filename '.eidatoken'
        Return a tuple of strings (username, password)
    """

    # Default location for token
    if token is None:
        token = os.path.expanduser('~/.eidatoken')

    # This is actually a critical part. A token is expected in the home folder
    # of the user running this script with filename '.eidatoken'
    files = {'file': open(token, 'rb')}
    r = requests.post(url, files=files, timeout=timeout)
    if r.status_code != 200:
        raise Exception('Authentication returned a %s HTTP Error code' % r.status_code)

    resp = r.text.split(':')
    if len(resp) != 2:
        raise Exception('Authentication returned a wrong response format:\n%s' % r.text)

    return resp


def main():
    """Nagios plugin to check if Alparray data is accessible

    Following Nagios specifications, the value returned can be
    0: OK
    1: WARNING
    2: CRITICAL
    3: UNKNOWN
    and the output line is something like

    ALPARRAY OK: https://eida.bgr.de/fdsnws/dataselect/1/queryauth | time=0.133321s
    """

    version = '0.1a3'

    urls = dict()
    urls['ETH'] = 'https://eida.ethz.ch/fdsnws/dataselect/1/auth'
    urls['GFZ'] = 'https://geofon.gfz-potsdam.de/fdsnws/dataselect/1/auth'
    urls['INGV'] = 'https://webservices.ingv.it/fdsnws/dataselect/1/auth'
    urls['LMU'] = 'https://erde.geophysik.uni-muenchen.de/fdsnws/dataselect/1/auth'
    urls['ODC'] = 'https://www.orfeus-eu.org/fdsnws/dataselect/1/auth'
    urls['RESIF'] = 'https://ws.resif.fr/fdsnws/dataselect/1/auth'

    reqs = dict()
    reqs['ETH'] = {'net': 'Z3', 'sta': 'A291A', 'start': datetime.datetime(2018, 1, 1)}
    reqs['GFZ'] = {'net': 'Z3', 'sta': 'A434A', 'start': datetime.datetime(2017, 10, 1)}
    reqs['INGV'] = {'net': 'Z3', 'sta': 'A319A', 'start': datetime.datetime(2018, 1, 1)}
    reqs['LMU'] = {'net': 'Z3', 'sta': 'A369A', 'start': datetime.datetime(2018, 1, 1)}
    reqs['ODC'] = {'net': 'Z3', 'sta': 'A339A', 'start': datetime.datetime(2018, 1, 1)}
    reqs['RESIF'] = {'net': 'Z3', 'sta': 'A429A', 'start': datetime.datetime(2017, 10, 1)}

    desc = 'Nagios plugin to check if Alparray data is accessible from endpoints\n\nIf no arguments are passed all EIDA nodes are tested.'
    parser = argparse.ArgumentParser(description=desc)

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-H', '--hostname', default=None, choices=urls.keys(),
                       help='Hostname providing the "auth" method at the default location.')
    parser.add_argument('-t', '--timeout', default=9, type=int,
                        help='Number of seconds to be used as a timeout for the HTTP calls.')
    parser.add_argument('-a', '--authentication', default=os.path.expanduser('~/.eidatoken'),
                        help='File containing the token to use during the authentication process')
    parser.add_argument('-V', '--version', action='version', version='%(prog)s ' + version,
                        help='Show version information.')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    args = parser.parse_args()

    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    # Select an offset within one week (in hours)
    offset = random.sample(range(24*7), 1)[0]

    # Save starting time to measure performance
    start_time = time.time()

    if args.hostname is not None:
        payload = reqs[args.hostname].copy()
        auxstart = payload['start'] + datetime.timedelta(hours=offset)
        payload['start'] = auxstart.isoformat()
        payload['end'] = (auxstart + datetime.timedelta(minutes=10)).isoformat()

        sys.exit(check_EIDA_Alparray(urls[args.hostname], payload,
                                     timeout=args.timeout,
                                     token=args.authentication))

    retcode = 0
    for dc, url in urls.items():
        payload = reqs[dc].copy()
        auxstart = payload['start'] + datetime.timedelta(hours=offset)
        payload['start'] = auxstart.isoformat()
        payload['end'] = (auxstart + datetime.timedelta(minutes=10)).isoformat()

        retcode = max(retcode, check_EIDA_Alparray(url, payload=payload, timeout=args.timeout,
                                                   token=args.authentication))

    sys.exit(retcode)


if __name__ == '__main__':
    main()

#!python

"""
hetzner_set_dns_txt_record.py

Copyright (C) 2020 NeuroForge GmbH & Co.KG <https://neuroforge.de/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from typing import Optional

import dns
import argparse

from easyzone import easyzone
from hetzner_set_dns_txt_record import api


parser = argparse.ArgumentParser(description='Set DNS A TXT record')
parser.add_argument('--basedomain', type=str, help='the base domain (i.e. zone)', required=True)
parser.add_argument('--domain', type=str, help='the domain to set the TXT record for', required=True)
parser.add_argument('--record', type=str, help='the record to set', required=True)
value_group = parser.add_mutually_exclusive_group(required=True)
value_group.add_argument('--value', type=str, help='the value to set the record to')
value_group.add_argument('--delete', action='store_true', help='delete the value in the TXT record')
parser.add_argument('--user', type=str, help='the Hetzner robot user', required=True)
parser.add_argument('--password', type=str, help='the Hetzner robot password', required=True)
parser.add_argument('--ttl', type=int, help='TTL setting', default='86400')
parser.add_argument('--roboturl', type=str, help='Hetzner Robot URL', default=api.DEFAULT_ROBOT_URL)
parser.add_argument('--accounturl', type=str, help='Hetzner Robot URL', default=api.DEFAULT_ACCOUNT_URL)
parser.add_argument('--verbose', action='store_true')

args = vars(parser.parse_args())

user: str = args['user']
password: str = args['password']
domain: str = args['domain']
base_domain: str = args['basedomain']
record: str = args['record']
value: Optional[str]
if 'value' in args:
    value = args['value']
else:
    # if none, we automatically delete anyways
    value = None
ttl: int = args['ttl']
robot_url: str = args['roboturl']
account_url: str = args['accounturl']
verbose: bool = False
if 'verbose' in args:
    verbose = True

print("Logging into Hetzner...")
session = api.login(user=user, password=password, robot_url=robot_url, account_url=account_url)

_zone_id = api.get_zone_id(session=session, zone=base_domain)
_zone_file, _csrf_token = api.get_zone_file(session=session, zone_id=_zone_id)

if verbose:
    print('============================')
    print('Got original zonefile:')
    print(_zone_file)
    print('============================')

_zone = easyzone.Zone(domain=base_domain)
_zone.zone = dns.zone.Zone(domain)
_zone._zone = dns.zone.from_text(_zone_file, base_domain, relativize=False)

print('successfully parsed existing zone from hetzner')

_name=f'{record}.{domain}.'
print(f'using zone record: {_name}')

_existing_txt_records = api.get_txt_records(_zone, name=f'{record}.{domain}.')

if verbose:
    print('============================')
    print('Got existing txt records:')
    print(_existing_txt_records)
    print('============================')

api.set_txt_record_zone(zone=_zone, name=_name, txt_record=value)

_modified_txt_records = api.get_txt_records(_zone, name=f'{record}.{domain}.')

if verbose:
    print('============================')
    print('TXT records after modification:')
    print(_modified_txt_records)
    print('============================')

_complete_zone_file_after_changes = api.zone_to_string(_zone, ttl=ttl)

if verbose:
    print('============================')
    print('will modify Hetzner zone file now')
    print(_complete_zone_file_after_changes)
    print('============================')

api.save_zone(session, zone_id=_zone_id, zone_file=_complete_zone_file_after_changes, csrf_token=_csrf_token)

_zone_file_after_hetzner_call, _csrf_token = api.get_zone_file(session=session, zone_id=_zone_id)

if verbose:
    print('============================')
    print('Got zonefile after changes (might be inaccurate due to delays in processing at Hetzner!):')
    print(_zone_file_after_hetzner_call)
    print('============================')

print('success... DNS entry should be updated in a bit.')
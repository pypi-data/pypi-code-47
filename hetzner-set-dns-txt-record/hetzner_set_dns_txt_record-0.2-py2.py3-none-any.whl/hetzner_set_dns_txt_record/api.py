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

import re
from time import strftime, localtime, time
from typing import List, Dict, Optional, Tuple

import bs4
import requests
from easyzone import easyzone

DEFAULT_ROBOT_URL = "https://robot.your-server.de"
DEFAULT_ACCOUNT_URL = "https://accounts.hetzner.com"


class HetznerSession(object):
    session: requests.Session
    robot_url: str
    account_url: str

    def __init__(self, session: requests.Session, robot_url: str, account_url: str):
        super().__init__()
        self.session = session
        self.robot_url = robot_url
        self.account_url = account_url


def auth(csrf: str, user: str, password: str):
    return {
        '_username': user,
        '_password': password,
        '_csrf_token': csrf
    }


def login(user: str, password: str, robot_url: str = DEFAULT_ROBOT_URL, account_url: str = DEFAULT_ACCOUNT_URL) -> HetznerSession:
    session = requests.session()
    res = session.get(f"{account_url}/login")
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    csrf = soup.select_one('input[name="_csrf_token"]')["value"]

    assert csrf is not None

    response = session.post(f"{account_url}/login_check", data=auth(csrf=csrf, user=user, password=password))
    response.raise_for_status()
    return HetznerSession(session=session, robot_url=robot_url, account_url=account_url)


def get_zone_id(session: HetznerSession, zone: str) -> str:
    res = session.session.post(f"{session.robot_url}/dns")
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    x = soup.findAll(text=zone)[0].findParents('table')[0]["onclick"]

    zone_ids: List[str] = list(set(re.findall('\d{6}', x)))
    assert len(zone_ids) == 1
    return zone_ids[0]


def get_zone_file(session: HetznerSession, zone_id: str) -> Tuple[str, str]:
    res = session.session.get(f"{session.robot_url}/dns/update/id/{zone_id}")

    res.raise_for_status()

    zone_fragment = bs4.BeautifulSoup(res.text, "html.parser")
    zone_file_element_contents = zone_fragment.select_one('textarea[name="zonefile"]').contents
    csrf_token = zone_fragment.select_one('input[name="_csrf_token"]')["value"]

    assert len(zone_file_element_contents) == 1

    zone_file = zone_file_element_contents[0]

    return zone_file, csrf_token


def save_zone(session: HetznerSession, zone_id: str, zone_file: str, csrf_token: str):
    res = session.session.post(f"{session.robot_url}/dns/update", data={'id': zone_id, 'zonefile': zone_file, '_csrf_token': csrf_token})
    res.raise_for_status()


def get_txt_records(zone: easyzone.Zone, name: str) -> Optional[List[str]]:
    names: Dict[str, easyzone.Name] = zone.get_names()

    if name in names:
        _name_obj: easyzone.Name = names[name]
        return _name_obj.records('TXT').items

    return []


def set_txt_record_zone(zone: easyzone.Zone, name: str, txt_record: Optional[str]) -> None:
    zone.add_name(name=name)

    names: Dict[str, easyzone.Name] = zone.get_names()

    assert name in names

    _name_obj: easyzone.Name = names[name]

    records: easyzone.Records = _name_obj.records('TXT', create=True)

    # bug in easyzone for creation and deletion, work around it
    for item in records.items:
        item = item[1:-1]
        rd = easyzone._new_rdata(records.type, [item.encode('UTF-8')])
        records._rdataset.remove(rd)

    if txt_record is not None:
        if txt_record.startswith('"') and txt_record.endswith('"'):
            # strip quotes off both ends; dns module will add them automatically
            txt_record = txt_record[1:-1]

        encoded = [txt_record.encode('UTF-8')]

        rd = easyzone._new_rdata(records.type, encoded)
        records._rdataset.add(rd)


def zone_to_string(zone: easyzone.Zone, ttl: int) -> str:
    soa = zone.root.soa
    new_serial = int(strftime('%Y%m%d00', localtime(time())))
    if new_serial <= soa.serial:
        new_serial = soa.serial + 1
    soa.serial = new_serial
    return f"""
$TTL {ttl}
{zone._zone.to_text().decode('UTF-8')}
"""

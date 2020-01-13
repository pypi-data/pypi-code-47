import array
import datetime
import logging
import re

import requests

from .const import commands, dict_channel_list, urls
from pyskycontrol import Helper

_LOGGER = logging.getLogger(__name__)


class SkyDevice:
    """Sky Control Class"""

    def __init__(
        self,
        host: str,
        ctrl_url: str,

    ) -> None:
        """Create a new SmartDevice instance.
        :param str host: host name or ip address on which the device listens.
        :param str ctrl_url: control url to control th box.
        """

        self.host = host
        self.ctrl_url = ctrl_url

    def get_status(self, host, ctrl_url):
        """Send soap command to the Sky Q box to get status"""
        test = Helper.request(request_type="GET",
                              response_type="JSON",
                              target=host,
                              request_url=urls["info_url"])

        if test["activeStandby"] != True:
            command = "GetTransportInfo"
            response = Helper.soap_request(command, ctrl_url)
            return response.find('CurrentTransportState').string
        else:
            response = 'STOPPED'
            return response

    def channel_epg(self, host):
        """Get the Sky EPG"""
        channel_list = {}
        request = Helper.request(request_type="GET",
                                 response_type="JSON",
                                 target=host,
                                 request_url=urls["channel_epg"])
        channels = request['services']
        for channel in channels:
            if channel["t"] not in channel_list:
                channel_list.update({channel["t"]: channel})
        channel_list.update({'Recording': {'sid': '0', 't': 'Recording'}})
        dict_channel_list = channel_list
        return channel_list

    def current_program(self, host, ctrl_url):
        """Get the current channel"""
        data = {}
        ps = None
        prog_type = None
        ch = None
        channel = None
        desc = None
        command = "GetMediaInfo"

        response = Helper.soap_request(command, ctrl_url)
        soap_result = response.find('CurrentURI').string

        if soap_result is None:
            data.update({'pvr_sid': 'off'})
            return data
        elif 'xsi' in soap_result:
            prog_type = 'Channel'
            ps = str(int(re.split('\\bxsi://\\b', soap_result)[-1], 16))
            data.update({'pvr_sid': ps})
            data.update({'type': prog_type})
        elif 'pvr' in soap_result:
            prog_type = 'Recording'
            ps = "P" + re.split('\\bfile://pvr/\\b', soap_result)[-1].lower()
            data.update({'pvr_sid': ps})
            data.update({'type': prog_type})

        if prog_type == 'Channel':
            d = datetime.datetime.now()
            d_date = d.strftime('%Y%m%d')
            response = Helper.request(request_type='GET',
                                      response_type='JSON',
                                      target="N/A",
                                      request_url=urls["chn_list"].format(d_date, ps))
            p_list = response["schedule"][0]["events"]
            current_epoch = Helper.epochtime(
                datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
                None, 'to_epoch')
            for prog in p_list:
                if prog["st"] + prog["d"] > current_epoch:
                    ch = prog
                    break

            for cha in dict_channel_list:
                if ps == dict_channel_list[cha]["sid"]:
                    channel = dict_channel_list[cha]['t']
                    data.update({"channel": channel})
                    break

        elif prog_type == 'Recording':
            response = Helper.request(request_type='GET',
                                      response_type='JSON',
                                      target=host,
                                      request_url=urls["rec_list"])
            p_list = response["pvrItems"]
            for rec in p_list:
                if rec["pvrid"] == ps:
                    ch = rec
                    if 'cn' in ch:
                        channel = ch['cn']
                        data.update({"channel": channel})
                    if 'osid' in ch:
                        ps = ch['osid']
                    break

        if ch is not None:
            if 't' in ch:
                title = ch['t']
                data.update({"title": title})
            if 'sy' in ch:
                desc = ch['sy']
                if ':' in desc:
                    s_t = desc.split(":")
                    series_title = s_t[0]
                    data.update({'series_title': series_title})
            if 'seasonnumber' in ch and 'episodenumber' in ch:
                season = ch['seasonnumber']
                episode = ch['episodenumber']
                data.update({"season": season})
                data.update({"episode": episode})
                source_type = 'TV'
                data.update({"source_type": source_type})
            else:
                source_type = 'Video'
                data.update({"source_type": source_type})
            if 'programmeuuid' in ch:
                programmeuuid = ch['programmeuuid']
                imageurl = urls['metadata_url'].format(
                    str(programmeuuid), str(ps))
                data.update({"imageurl": imageurl})

        _LOGGER.debug(data)
        return data

        def remote(self, host, command):
            """Send a button press to the sky box."""

import re
import socket
from typing import Dict

from pyskycontrol import Helper, SkyDevice


class Discover:
    """Discover Sky TV devices on the network."""

    def boxes(
        timeout: int = 30
    ) -> Dict[str, SkyDevice]:
        """
        Search for Sky Q Boxes on local network.

        :rtype: dict
        :return: Array of json objects {"ip", "port", "sys_info"}
        """
        device = {}
        devices = {}

        # UDP message.
        msg = \
            'M-SEARCH * HTTP/1.1\r\n' \
            'HOST:239.255.255.250:1900\r\n' \
            'ST:upnp:rootdevice\r\n' \
            'MX:2\r\n' \
            'MAN:"ssdp:discover"\r\n' \
            '\r\n'

        # Set up UDP socket.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                          socket.IPPROTO_UDP)
        s.settimeout(timeout)
        s.sendto(msg.encode(), ('239.255.255.250', 1900))

        try:
            while True:
                data, addr = s.recvfrom(65507)
                data_text = data.decode("utf-8")
                url = re.search("(?P<url>https?://[^\s]+)",
                                data_text).group("url")
                if "Sky" in data_text:
                    if addr[0] not in device:
                        device[addr[0]] = []
                    device[addr[0]].append(url)
        except socket.timeout:
            pass

        compl = []
        for IP in device:
            for url in device[IP]:
                if IP in compl:
                    break
                else:
                    try:
                        headers = {
                            'USER-AGENT': 'SKY_skyplus',
                            'CONTENT-TYPE': 'text/xml; charset="utf-8"'
                        }
                        request = Helper.request.get(url=url, data=None,
                                                     headers=headers)
                        response = Helper.xml(request)
                        base_url = response.find(
                            'URLBase').string[:-1]
                        for node in response.find_all('service'):
                            service = node.serviceType.string
                            ctrl_url = base_url + node.controlURL.string
                            scpd_url = base_url + node.SCPDURL.string

                            if "SkyPlay:2" in service and \
                                    "player_avt.xml" in scpd_url:
                                result = self.request(request_type="GET",
                                                      response_type='JSON',
                                                      target=IP,
                                                      request_url=self.urls[
                                                          "info_url"])
                                name = result["btID"]
                                devices[IP] = {"IP": IP,
                                               "PORT": self.port,
                                               "NAME": name,
                                               "XML_URL": url,
                                               "CONTROL_URL": ctrl_url,
                                               "SCPD_URL": scpd_url,
                                               "SERVICE_TYPE": service}
                                compl.append(IP)
                    except:
                        pass

        return devices

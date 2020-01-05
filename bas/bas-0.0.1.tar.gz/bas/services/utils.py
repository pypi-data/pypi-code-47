from xml.etree import ElementTree as ET
import requests

def parse_response(resp):
    if resp.status_code != 200:
        raise Exception(resp.text)
    element = ET.fromstring(resp.text)
    success = element.findtext('./success')
    if success == 'false':
        message = element.findtext('./message')
        raise Exception(message)
    url = element.findtext('./downloadLink')
    return requests.get(url).text
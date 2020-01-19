from lxml import etree
from result import Result, ListResult, SearchResult
from status import Status
from datetime import datetime
import re


class Parser:
    """Parser Class"""
    def __init__(self):
        """Initialize Parser class"""
        self.regex = re.compile(r'\n* +')

    def parse(self, xml_text: bytes) -> Result:
        """Parse XML returned from J-STAGE API

        Parse XML document (as bytes object) into Result object.
        This function may raise Error or Warning.
        If that error starts with Jstage, that error was occurred by J-STAGE.

        Args:
            xml_text: raw xml text's bytes encoded by UTF-8
        Returns:
            Result object which contains meta data and contents.
        Raises:
            JstageError: error depending on j-stage api
            JstageWarning: warning depending on j-stage api
        """
        result = Result()

        root = etree.fromstring(xml_text)
        result.xmlns = root.nsmap
        result.xmlns['xml'] = 'http://www.w3.org/XML/1998/namespace'
        result.xml_lang = root.find('[@xml:lang]', result.xmlns).attrib.values()[0]
        result.xml_version = etree.ElementTree(root).docinfo.xml_version
        result.encoding = etree.ElementTree(root).docinfo.encoding
        result.servicecd = int(root.find('./servicecd', result.xmlns).text)
        result.title = root.find('./title', result.xmlns).text
        result.link = self.regex.sub('', root.find('./link', result.xmlns).attrib['href'])
        result.id = self.regex.sub('', root.find('./id', result.xmlns).text)
        result.updated = datetime.fromisoformat(root.find('./updated', result.xmlns).text)
        result.total_results = int(root.find('./opensearch:totalResults', result.xmlns).text)
        result.start_index = int(root.find('./opensearch:startIndex', result.xmlns).text)
        result.items_per_page = int(root.find('./opensearch:itemsPerPage', result.xmlns).text)
        result.entries = list(root.findall('./entry', result.xmlns))
        result.status = root.find('./result/status', result.xmlns).text
        result.message = root.find('./result/message', result.xmlns).text
        Status.divide(result.status, result.message)
        if result.servicecd == 2:
            rresult = ListResult(result)
        elif result.servicecd == 3:
            rresult = SearchResult(result)
        else:
            raise Exception('Undefined service code')

        return rresult

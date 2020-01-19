from typing import Dict, Optional, List
import re
from datetime import datetime
from entry import ListEntry, SearchEntry
from lxml import etree


class Result:
    """Base class for Result
    Attributes:
        encoding: Document encoding, it may always be utf-8.
        xml_version: XML version.
        xmlns: What namespaces does this document refer.
        xml_lang: What language is this document written in.
        status: Status code.
        message: Status message.
        title: returned title
        link: returned link
        id: document id, it is always same as link value.
        servicecd: API service code, 2 is list and 3 is search.
        updated: When was this document updated.
        total_results: How many results did API return.
        start_index: What index do results starts.
        items_per_page: How many items does a page contain.
        entries: Entries API returned.
    """
    def __init__(self):
        self.encoding: Optional[str] = None
        self.xml_version: Optional[str] = None
        self.xmlns: Dict[str, str] = {}
        self.xml_lang: Optional[str] = None
        self.status: str = Optional[None]
        self.message: Optional[str] = None
        self.title: Optional[str] = None
        self.link: Optional[str] = None
        self.id: Optional[str] = None
        self.servicecd: Optional[str] = None
        self.updated: Optional[datetime] = None
        self.total_results: Optional[int] = None
        self.start_index: Optional[int] = None
        self.items_per_page: Optional[int] = None
        self.entries: List[etree] = []
        self.entries_temp: List[etree] = []

    def __finish_setup(self):
        """remove unused temporary attribute"""
        del self.entries_temp

    def __str__(self):
        return str(self.__dict__.items())


class SearchResult(Result):
    """Search Result Class

    Attributes:
        encoding: Document encoding, it may always be utf-8.
        xml_version: XML version.
        xmlns: What namespaces does this document refer.
        xml_lang: What language is this document written in.
        status: Status code.
        message: Status message.
        title: returned title
        link: returned link
        id: document id, it is always same as link value.
        servicecd: API service code, 2 is list and 3 is search.
        updated: When was this document updated.
        total_results: How many results did API return.
        start_index: What index do results starts.
        items_per_page: How many items does a page contain.
        entries: Entries API returned.
    """
    def __init__(self, result: Result):
        """Initialize SearchResult class

        Args:
            result: Result object
        """
        super().__init__()
        self.encoding = result.encoding
        self.xml_version = result.xml_version
        self.xmlns = result.xmlns
        self.xml_lang = result.xml_lang
        self.status = result.status
        self.message = result.message
        self.title = result.title
        self.link = result.link
        self.id = result.id
        self.servicecd = result.servicecd
        self.updated = result.updated
        self.total_results = result.total_results
        self.start_index = result.start_index
        self.items_per_page = result.items_per_page
        self.entries_temp = result.entries
        self.entries = []

        regex = re.compile(r'{.+\}')
        for e in self.entries_temp:
            ent = SearchEntry()
            ent.article_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./article_title', self.xmlns)
            }
            ent.article_link = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./article_link', self.xmlns)
            }
            ent.author = {
                regex.sub('', t.tag): list(t)[0].text.replace('\n', '').strip() for t in e.find('./author', self.xmlns)
            }
            ent.article_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./article_title', self.xmlns)
            }
            ent.cdjournal = e.find('./cdjournal', self.xmlns).text.replace('\n', '').strip()
            ent.material_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./material_title', self.xmlns)
            }
            ent.issn = e.find('./prism:issn', self.xmlns).text.replace('\n', '').strip()
            ent.eissn = e.find('./prism:eIssn', self.xmlns).text.replace('\n', '').strip()
            ent.volume = int(e.find('./prism:volume', self.xmlns).text.replace('\n', '').strip())
            ent.number = int(e.find('./prism:number', self.xmlns).text.replace('\n', '').strip())
            ent.starting_page = int(e.find('./prism:startingPage', self.xmlns).text.replace('\n', '').strip())
            ent.ending_page = int(e.find('./prism:endingPage', self.xmlns).text.replace('\n', '').strip())
            ent.pubyear = e.find('./pubyear', self.xmlns).text.replace('\n', '').strip()
            ent.doi = e.find('./prism:doi', self.xmlns).text.replace('\n', '').strip()
            ent.systemcode = int(e.find('./systemcode', self.xmlns).text.replace('\n', '').strip())
            ent.systemname = e.find('./systemname', self.xmlns).text.replace('\n', '').strip()
            ent.title = e.find('./title', self.xmlns).text.replace('\n', '').strip()
            ent.link = e.find('./link', self.xmlns).attrib['href'].replace('\n', '').strip()
            ent.id = e.find('./id', self.xmlns).text.replace('\n', '').strip()
            ent.updated = datetime.fromisoformat(e.find('./updated', self.xmlns).text.replace('\n', '').strip())
            self.entries.append(ent)
        self.__finish_setup()


class ListResult(Result):
    """List Result Class

    Attributes:
        encoding: Document encoding, it may always be utf-8.
        xml_version: XML version.
        xmlns: What namespaces does this document refer.
        xml_lang: What language is this document written in.
        status: Status code.
        message: Status message.
        title: returned title
        link: returned link
        id: document id, it is always same as link value.
        servicecd: API service code, 2 is list and 3 is search.
        updated: When was this document updated.
        total_results: How many results did API return.
        start_index: What index do results starts.
        items_per_page: How many items does a page contain.
        entries: Entries API returned.
    """
    def __init__(self, result: Result = None):
        """Initialize ListResult class

        Args:
            result: Result object
        """
        super().__init__()
        self.encoding = result.encoding
        self.xml_version = result.xml_version
        self.xmlns = result.xmlns
        self.xml_lang = result.xml_lang
        self.status = result.status
        self.message = result.message
        self.title = result.title
        self.link = result.link
        self.id = result.id
        self.servicecd = result.servicecd
        self.updated = result.updated
        self.total_results = result.total_results
        self.start_index = result.start_index
        self.items_per_page = result.items_per_page
        self.entries_temp = result.entries
        self.entries = []

        regex = re.compile(r'{.+\}')
        for e in self.entries_temp:
            ent = ListEntry()
            ent.vols_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./vols_title', self.xmlns)
            }
            ent.vols_link = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./vols_link', self.xmlns)
            }
            ent.issn = e.find('./prism:issn', self.xmlns).text.replace('\n', '').strip()
            ent.eissn = e.find('./prism:eIssn', self.xmlns).text.replace('\n', '').strip()
            ent.publisher_name = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip()
                for t in e.find('./publisher/name', self.xmlns)
            }
            ent.publisher_url = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip()
                for t in e.find('./publisher/url', self.xmlns)
            }
            ent.cdjournal = e.find('./cdjournal', self.xmlns).text.replace('\n', '').strip()
            ent.material_title = {
                regex.sub('', t.tag): t.text.replace('\n', '').strip() for t in e.find('./material_title', self.xmlns)
            }
            ent.volume = int(e.find('./prism:volume', self.xmlns).text.replace('\n', '').strip())
            ent.number = int(e.find('./prism:number', self.xmlns).text.replace('\n', '').strip())
            ent.starting_page = int(e.find('./prism:startingPage', self.xmlns).text.replace('\n', '').strip())
            ent.pubyear = e.find('./pubyear', self.xmlns).text.replace('\n', '').strip()
            ent.systemcode = int(e.find('./systemcode', self.xmlns).text.replace('\n', '').strip())
            ent.systemname = e.find('./systemname', self.xmlns).text.replace('\n', '').strip()
            ent.title = e.find('./title', self.xmlns).text.replace('\n', '').strip()
            ent.link = e.find('./link', self.xmlns).attrib['href'].replace('\n', '').strip()
            ent.id = e.find('./id', self.xmlns).text.replace('\n', '').strip()
            ent.updated = datetime.fromisoformat(e.find('./updated', self.xmlns).text.replace('\n', '').strip())
            self.entries.append(ent)
        self.__finish_setup()

from result import Result
from parser import Parser
from service import Service
from order import ListOrder, SearchOrder
from urllib.parse import quote
from typing import List, Union
import requests


class Pyjstage:
    """Pyjstage Class

    Attributes:
        domain: J-STAGE API domain
        parser: Parser object
    """
    def __init__(self, domain: str = 'http://api.jstage.jst.go.jp/searchapi/do?'):
        """Initialize Pyjstage class

        Args:
            domain: (Optional) J-STAGE API domain
        """
        self.domain: str = domain
        self.parser: Parser = Parser()

    def list(
            self,
            pubyearfrom: int = None,
            pubyearto: int = None,
            material: Union[str, List[str]] = None,
            issn: str = None,
            cdjournal: str = None,
            volorder: ListOrder = None
    ) -> Result:
        """Access LIST API

        Access LIST API and parse result as ListResult Object.
        Union[xxx, List[xxx]] arguments can multiple value as list object.
        If you set that argument as list, Search as 'AND'

        Args:
            pubyearfrom: (Optional) Year you want to search when papers were published from.
            pubyearto: (Optional) Year you want to search when papers were published to.
            material: (Optional) Keyword journal should contain.
            issn: (Optional) ISSN you want to search.
            cdjournal: (Optional) Journal code you want to search.
            volorder: (Optional) How order are responses sorted.
        Returns:
            ListResult object which contains meta data and contents
        Raises:
            JstageError: Error caused by J-STAGE API
            JstageWarning: Warning caused by J-STAGE API
        """
        url = self.build_query(
            service=Service.LIST.value,
            pubyearfrom=pubyearfrom,
            pubyearto=pubyearto,
            material=material,
            issn=issn,
            cdjournal=cdjournal,
            volorder=volorder.value)
        response = requests.get(url)
        return self.parser.parse(response.text.encode('utf-8'))

    def search(
            self,
            pubyearfrom: int = None,
            pubyearto: int = None,
            material: Union[str, List[str]] = None,
            article: Union[str, List[str]] = None,
            author: Union[str, List[str]] = None,
            affile: Union[str, List[str]] = None,
            keyword: Union[str, List[str]] = None,
            abst: Union[str, List[str]] = None,
            text: Union[str, List[str]] = None,
            issn: str = None,
            cdjournal: str = None,
            sortfig: SearchOrder = None,
            vol: int = None,
            no: int = None,
            start: int = None,
            count: int = None
    ) -> Result:
        """Access SEARCH API

        Access SEARCH API and parse result as SearchResult Object.
        Union[xxx, List[xxx]] arguments can multiple value as list object.
        If you set that argument as list, Search as 'AND'

        Args:
            pubyearfrom: (Optional) Year you want to search when papers were published from.
            pubyearto: (Optional) Year you want to search when papers were published to.
            material: (Optional) Keyword journal should contain.
            article: Keyword document's title should contain.
            author: Keyword document's author name should contain.
            affile: Keyword document's author's affile name should contain.
            keyword: Keyword document's keyword should contain.
            abst: Keyword document's abstract should contain.
            text: Keyword document's body should contain
            issn: (Optional) ISSN you want to search.
            cdjournal: (Optional) Journal code you want to search.
            sortfig: How order are responses sorted.
            vol: What volume is document contained in journal
            no: What number is document contained in journal
            start: How many offsets you want to set, default 0.
            count: How many results you want to fetch, max & default is 1000.
        Returns:
            SearchResult object which contains meta data and contents
        Raises:
            xxxError: xxx
        """
        url = self.build_query(
            service=Service.SEARCH.value,
            pubyearfrom=pubyearfrom,
            pubyearto=pubyearto,
            material=material,
            article=article,
            author=author,
            affile=affile,
            keyword=keyword,
            abst=abst,
            text=text,
            issn=issn,
            cdjournal=cdjournal,
            sortfig=sortfig.value if sortfig else None,
            vol=vol,
            no=no,
            start=start,
            count=count
        )
        response = requests.get(url)
        result = self.parser.parse(response.text.encode('utf-8'))
        return result

    def build_query(self, **kwargs):
        """Build url with queries

        Args:
            kwargs: key-value pairs for querying. If multiple values, use list.
        Returns:
            URL-string which can access J-STAGE API
        """
        return self.domain + '&'.join(
            [
                f'{quote(k, encoding="utf8")}={quote(str(v) if type(v) is not list else " ".join(v), encoding="utf8")}'
                for k, v in kwargs.items() if v is not None
            ]
        )

if __name__ == '__main__':
    pj = Pyjstage()
    ret = pj.search(text=['統合失調症', '精神分裂病'], count=10)
    print(ret)

class Entry:
    """Base class for Entry

    Attributes:
        issn: ISSN
        eissn: eISSN
        cdjournal: journal name
        material_title: journal title
        volume: journal volume
        number: journal number
        starting_page: starting page this document is.
        pubyear: Published year.
        systemcode: System code
        systemname: System name
        title: Title
        link: Link
        id: ID, it is always the same as link parameter.
        updated: updated date
    """
    def __init__(self):
        """Initialize Entry class"""
        self.issn = None
        self.eissn = None
        self.cdjournal = None
        self.material_title = None
        self.volume = None
        self.number = None
        self.starting_page = None
        self.pubyear = None
        self.systemcode = None
        self.systemname = None
        self.title = None
        self.link = None
        self.id = None
        self.updated = None

    def __str__(self):
        return str(self.__dict__.items())


class ListEntry(Entry):
    """Entry class for List API

    Attributes:
        vols_title: volumes title
        vols_link: volumes link
        publisher_name: publisher name
        publisher_url: publisher url
    """
    def __init__(self):
        """Initialize ListEntry class"""
        super().__init__()
        self.vols_title = {}
        self.vols_link = {}
        self.publisher_name = None
        self.publisher_url = {}


class SearchEntry(Entry):
    """Entry class for Search API

    Attributes:
        article_title: article title
        article_link: article link
        author: article author
        ending_page: ending page
        doi: DOI
    """
    def __init__(self):
        """Initialize SearchEntry class"""
        super().__init__()
        self.article_title = {}
        self.article_link = None
        self.author = None
        self.ending_page = None
        self.doi = None

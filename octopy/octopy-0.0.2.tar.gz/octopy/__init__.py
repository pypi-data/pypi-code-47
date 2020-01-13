from .modules import *


class OctopyClient:
    URL = "https://api.github.com"

    def __init__(self, token=None, bearer=None):
        self._headers = {}
        if token:
            self._headers["Authorization"] = f"token {token}"
        if bearer:
            self._headers["Authorization"] = f"Bearer {bearer}"

        self.activity = Activity(self.URL, self._headers)
        self.apps = App(self.URL, self._headers)
        self.checks = Check(self.URL, self._headers)
        self.data = GitData(self.URL, self._headers)
        self.gists = Gist(self.URL, self._headers)
        self.interactions = Interaction(self.URL, self._headers)
        self.issues = Issue(self.URL, self._headers)
        self.marketplace = MarketPlace(self.URL, self._headers)
        self.migrations = Migration(self.URL, self._headers)
        self.miscellaneous = Miscellaneous(self.URL, self._headers)
        self.organizations = Organization(self.URL, self._headers)
        self.projects = Project(self.URL, self._headers)
        self.pull_requests = PullRequest(self.URL, self._headers)
        self.reactions = Reaction(self.URL, self._headers)
        self.repositories = Repository(self.URL, self._headers)
        self.search = Search(self.URL, self._headers)
        self.teams = Team(self.URL, self._headers)
        self.scim = Scim(self.URL, self._headers)
        self.users = User(self.URL, self._headers)

    @property
    def token(self):
        return

    @token.setter
    def token(self, access_token):
        self._headers["Authorization"] = f"token {access_token}"

    @property
    def jwt(self):
        return

    @jwt.setter
    def jwt(self, access_token):
        self._headers["Authorization"] = f"Bearer {access_token}"
        self.apps = App(self.URL, self._headers)

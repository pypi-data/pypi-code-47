import requests


class authenticate(object):

    """
        Authenticate Class Object will provide user authentication based on the Username and Password, Api operations
        related to the authentication should be extended in this class.

        This Class is initialized with hostname and defaults to McAfee API Port.
    """

    def __init__(self, hostname, port, https=True):
        self.session = None
        self.target = None
        self.hostname = hostname
        self.port = port
        self.https = https


    def createSession(self, username, password):
        """
            createSession will create login session for a specific user/account that require access to MWG servers.
            Looks inside cache Dir for previous Authentication if nothing available generates new SessionID based
            on User Credentials.
        :param username: userinput or functional
        :param password: userinput or functional
        :return: generates a user session with sessionID.
        """
        self.createTargetURL()
        url = self.createAppendURL(string='/login')
        self.session = requests.Session()
        gen = self.session.post(url, data={'userName': username, 'pass': password}, verify=False)
        if not 'JSESSIONID' in gen.cookies:
            print("Authentication Error. Try Again Later..")
            raise Exception(gen.text)
        return gen.cookies


    def destroySession(self):
        """
         destroySession will destroy the created session for the user/account in the MWG Server
        :return: response status
        """
        url = self.createAppendURL(string='/logout')
        self.session.get(url)



    def createTargetURL(self):
        """
            createTargetURL stores the API end-point created in the self.target for portability.
        :return: None.
        """
        url = '{}://{}:{}/Konfigurator/REST/'
        http = 'http'
        if self.https:
            http = 'https'
        url = url.format(http, self.hostname, self.port)
        self.target = url


    def createAppendURL(self, string):
        """
            createAppendURL creates added parameter API end-point based on the string requested.
        :param string: parameters
        :return: Full API URL with added string.
        """
        self.createTargetURL()
        out = self.target + string
        return out
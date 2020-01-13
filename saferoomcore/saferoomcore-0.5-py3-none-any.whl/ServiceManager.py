# Import section
import json
from saferoomcore.SafeExceptions import SaferoomException
import saferoomcore.safevars as GLOBALS
import saferoomcore.messages as MESSAGES

# Class section
class ServiceManager(object):

    def __init__(self,id,service,access_token):
        self.id = id
        self.service = service
        self.access_token = access_token
        self.items = []

    def set_request_url(self,url):
        """
            Method is used to set the URL for the API call. It's not needed for some services (Evernote and etc.),
            but mandatory for others

            For example: https://graph.microsoft.com/me/onenote/pages

        """
        self.url = url

    def set_prefix(self,prefix):

        """
            Method is used to set prefix while creating or updating the page.
            For example, for Onenote service prefix will be the following:

            <html><head><body></body></head></html>

        """

        self.prefix = prefix

    def set_config(self,config):

        """ Method is used to initialize the configuration parameters """

        # Checking the configuration for specific mandatory parameters
        if "key_notebooks" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_notebooks")
        if "key_sections" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_sections")
        if "key_pages" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_pages")
        if "key_page" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_page")
        if "redis_expires" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "redis_expires")

        # Setting the configuration
        self.config = config


    def set_redis_store(self,redis_store):

        """ Method is used to configure the REDIS interface """
        self.redis_store = redis_store


    def connect(self):

        """ Method is used to connect to specific service. Some services may not need this and thus will be left empty"""

        if not self.access_token:
            raise SaferoomException(MESSAGES.ACCESS_TOKEN_NOTFOUND,[])


    def cache(self,keyname,guid=""):

        """ This method is used to cache data in REDIS store for faster access """
        try:

            # Generating Key name
            if id:
                key = self.config[keyname] % self.id
            else:
                key = self.config[keyname] % guid

            # Caching the item
            self.redis_store.set(self.config[type] % (self.id), json.dumps(data))

        except Exception as e:
            raise SaferoomException(MESSAGES.CACHE_ERROR % str(e))

    @staticmethod
    def create_manager(id,service,access_token):

        # Initializing the manager
        manager = None

        # Based on specified service initialize specific Service Manager
        if service == GLOBALS.SERVICE_EVERNOTE:
            manager = EvernoteManager(id,service,access_token)
            manager.set_prefix(GLOBALS.PREFIX_EVERNOTE)
        elif service == GLOBALS.SERVICE_ONENOTE:
            manager = OnenoteManager(id,service,access_token)
            manager.set_prefix(GLOBALS.PREFIX_ONENOTE)
        else:
            raise SaferoomException(MESSAGES.SERVICE_UNKNOWN,[])

        return manager



###############################################
#           Onenote Manager                   #
###############################################

class OnenoteManager(ServiceManager):

    # Constructor
    def __init__(self,id,service,access_token):
        super(self.__class__, self).__init__(id,service,access_token)

    # Connecting to Onenote service
    def connect(self):
        super().connect()
        print("Connecting to Onenote")

    #####################################################
    #           Getting notebooks                       #
    #####################################################

    def get_notebooks(self,refresh=False,term=""):

        if forceRefresh:
            self._load_notebooks()
        else:
            # Checking if notebooks are cached
            try:
                # Getting the list of notebooks
                result = self.redis_store.get(self.config['key_notebooks'] % self.id)
                if not result:
                    self._load_notebooks(term)
                else:
                    self.items = json.loads(result)
            except Exception as e:
                self._load_notebooks(term)


    def _load_notebooks(self,term=""):

        # Setting the headers
        headers = {"Authorization": "Bearer %s" % self.access_token, "Content-Type":"application/json"}

        # Sending POST request
        r = request.get(self.url,headers=headers)
        if r.ok == False:
            self._handle_onenote_error(r.text)

        # Checking the response
        response = json.loads(r.text)
        if not response:
            raise SaferoomException(MESSAGES.JSON_PARSE_ERROR % ("get_notebooks",r.text))

        # Getting the data
        for notebook in response['value']:
            self.items.append({
                "name":notebook['displayName'],
                "guid":notebook['id'],
                "created":notebook['createdDateTime'],
                "shared":notebook['isShared'],
                "service":self.service
            })

        # Caching items
        self.cache("key_notebooks")


    #####################################################
    #           Getting sections                        #
    #####################################################

    def get_sections(self,guid,refresh=False,term=""):

        if forceRefresh:
            self._load_sections(guid,term)
        else:
            # Checking if sections are cached
            try:
                # Getting the list of notebooks
                result = self.redis_store.get(self.config['key_sections'] % (self.id,self.guid))
                if not result:
                    self._load_sections(guid,term)
                else:
                    self.items = json.loads(result)
            except Exception as e:
                self._load_sections(guid,term)


    def _load_sections(self,guid,term=""):

        # Setting the headers
        headers = {"Authorization": "Bearer %s" % self.access_token, "Content-Type":"application/json"}

        # Sending POST request
        r = request.get(self.url.replace(":id",guid),headers=headers)
        if r.ok == False:
            self._handle_onenote_error(r.text)

        # Checking the response
        response = json.loads(r.text)
        if not response:
            raise SaferoomException(MESSAGES.JSON_PARSE_ERROR % ("get_sections",r.text))

        # Getting the data
        for section in response['value']:
            self.items.append({
                "name":section['displayName'],
                "guid":section['id'],
                "created":section['createdDateTime']
            })

        # Caching items
        self.cache("key_sections",guid)


    #####################################################
    #           Getting pages                        #
    #####################################################

    def get_pages(self,guid,refresh=False,term=""):

        if forceRefresh:
            self._load_pages(guid,term)
        else:
            # Checking if sections are cached
            try:
                # Getting the list of notebooks
                result = self.redis_store.get(self.config['key_pages'] % (self.id,self.guid))
                if not result:
                    self._load_pages(guid,term)
                else:
                    self.items = json.loads(result)
            except Exception as e:
                self._load_pages(guid,term)

    def _load_sections(self,guid,term=""):

        # Setting the headers
        headers = {"Authorization": "Bearer %s" % self.access_token, "Content-Type":"application/json"}

        # Sending POST request
        r = request.get(self.url.replace(":id",guid),headers=headers)
        if r.ok == False:
            self._handle_onenote_error(r.text)

        # Checking the response
        response = json.loads(r.text)
        if not response:
            raise SaferoomException(MESSAGES.JSON_PARSE_ERROR % ("get_pages",r.text))

        # Getting the data
        for section in response['value']:
            self.items.append({
                "title":page['title'],
                "guid":page['id'],
                "created":page['createdDateTime'],
                "updated":page['lastModifiedDateTime']
            })

        # Caching items
        self.cache("key_pages",guid)


    #####################################################
    #           Error Handling                          #
    #####################################################

    def _handle_onenote_error(self,response):

        # Parsing the ERROR
        try:
            error = json.loads(response)
            message = error['error']['message']
        except ValueError:
            message = response

        raise SaferoomException(message,[])




###############################################
#           Evernote Manager                  #
###############################################

class EvernoteManager(ServiceManager):

    # Constructor
    def __init__(self,id,service,access_token):
        super(self.__class__, self).__init__(id,service,access_token)
        self.store = None # Initializing the Evernote store object

    # Connecting to Evernote service
    def connect(self):
        super().connect()
        print("Connecting to Evernote")

# Import section
import json
from saferoomcore.SafeExceptions import SaferoomException
from saferoomcore.Safenote import Safenote
import saferoomcore.safevars as GLOBALS
import saferoomcore.messages as MESSAGES
from saferoomcore.functions import md5_data
import requests
from bs4 import BeautifulSoup

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
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_notebooks",[])
        if "key_sections" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_sections",[])
        if "key_pages" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_pages",[])
        if "key_page" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "key_page",[])
        if "redis_expires" not in config:
            raise SaferoomException(MESSAGES.NO_MANDATORY_KEY % "redis_expires",[])

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
            if not guid:
                key = self.config[keyname] % self.id
            else:
                key = self.config[keyname] % guid
            print(key)

            # Caching the item
            self.redis_store.set(key, json.dumps(self.items))

        except Exception as e:
            raise SaferoomException(MESSAGES.CACHE_ERROR % str(e),[])

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

        if refresh:
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
        r = requests.get(self.url,headers=headers)
        if r.ok == False:
            self._handle_onenote_error(r.text)

        # Checking the response
        response = json.loads(r.text)
        if not response:
            raise SaferoomException(MESSAGES.JSON_PARSE_ERROR % ("get_notebooks",r.text),[])

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

        if refresh:
            self._load_sections(guid,term)
        else:
            # Checking if sections are cached
            try:
                # Getting the list of notebooks
                result = self.redis_store.get(self.config['key_sections'] % (self.guid))
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
        r = requests.get(self.url.replace(":id",guid),headers=headers)
        if r.ok == False:
            self._handle_onenote_error(r.text)

        # Checking the response
        response = json.loads(r.text)
        if not response:
            raise SaferoomException(MESSAGES.JSON_PARSE_ERROR % ("get_sections",r.text),[])

        # Getting the data
        self.items = []
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

    def get_notes(self,guid,refresh=False,term=""):

        if refresh:
            self._load_notes(guid,term)
        else:
            # Checking if sections are cached
            try:
                # Getting the list of notebooks
                result = self.redis_store.get(self.config['key_pages'] % (self.id,self.guid))
                if not result:
                    self._load_notes(guid,term)
                else:
                    self.items = json.loads(result)
            except Exception as e:
                self._load_notes(guid,term)

    def _load_notes(self,guid,term=""):

        # Setting the headers
        headers = {"Authorization": "Bearer %s" % self.access_token, "Content-Type":"application/json"}

        # Sending POST request
        r = requests.get(self.url.replace(":id",guid),headers=headers)
        if r.ok == False:
            self._handle_onenote_error(r.text)

        # Checking the response
        response = json.loads(r.text)
        if not response:
            raise SaferoomException(MESSAGES.JSON_PARSE_ERROR % ("get_pages",r.text),[])

        # Getting the data
        for page in response['value']:
            self.items.append({
                "title":page['title'],
                "guid":page['id'],
                "created":page['createdDateTime'],
                "updated":page['lastModifiedDateTime']
            })

        # Caching items
        self.cache("key_pages",guid)


    #####################################################
    #           Getting specific page                   #
    #####################################################

    def get_note(self,guid,refresh):

        # Setting up the headers
        headers = {
            "Authorization":"Bearer "+self.access_token,
            "Content-Type":"application/json"
        }

        # Sending request to get the list of sections
        r = requests.get(self.url,headers=headers)
        if r.ok == False:
            self._handle_onenote_error(r.text)
        response = r.text

        # Initializing the note
        note = Safenote()
        note.guid = guid

        # Getting title
        soup = BeautifulSoup(response,"html.parser")
        if soup.title:
            note.title = soup.title.text
        else:
            note.title = ""

        # Getting note content
        note.content = ''.join(['%s' % x for x in soup.body.contents])
        #note.content = note.content.replace(" ","\r\n")

        # Getting all the attachments
        attachments = []
        images = soup.find_all("img")
        for image in images:

            if "src" in image and "data-src-type" in image and "src" in image:
                attachments.append({
                "name":md5_string(image['src']),
                "type":image['data-src-type'],
                "link":image['src']
            })

        objects = soup.find_all("object")
        for obj in objects:
            attachments.append({
                "name":obj['data-attachment'],
                "type":obj['type'],
                "link":obj['data']
            })

        # Downloading files into temporary folder
        binary_data = None
        hash = None
        resources = []
        tmp_file = os.path.join(self.path_cache,"tmp.download")
        headers = {"Authorization":"Bearer "+self.access_token}

        for attachment in attachments:

            # Sending request to download the file
            r = requests.get(attachment['link'],headers=headers,stream=True)
            if r.ok:

                # Writing data to temporary file
                with open(tmp_file,"wb") as f:
                    for block in r.iter_content(512):
                        f.write(block)

                # Calculating hash
                with open(tmp_file,"rb") as f:
                    binary_data = f.read()
                hash = md5_data(binary_data)

                # Initializing the data
                data = Data()
                data.size = len(binary_data)
                data.bodyHash = hash
                data.body = binary_data

                # Adding data to resource
                resource = Resource()
                resource.mime = attachment['type']
                resource.data = data

                # Creating attributes
                attributes = ResourceAttributes()
                attributes.fileName = os.path.basename(attachment['name'])
                resource.attributes = attributes
                resources.append(resource)

        note.resources = resources
        return note


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

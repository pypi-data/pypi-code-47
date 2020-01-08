import requests
from re import sub
from urllib.parse import unquote, urlencode
from ssdp import SimpleServiceDiscoveryProtocol, ST_DIAL
from xmlparse import XMLFile


def discover(timeout:int=3) -> list:
    '''
    Scans network for dial compatible devices and returns a list.
    '''
    SimpleServiceDiscoveryProtocol.settimeout(timeout)
    ssdp = SimpleServiceDiscoveryProtocol(ST_DIAL)
    return ssdp.broadcast()


class DIscoveryAndLaunch:

    def __init__(self, address: str):
        self.bind(address)
        self.instance_url = None
        self.refresh_url = None

    def __getitem__(self, prop):
        return self.__getattribute__(prop)

    def __enter__(self):
        self._session = requests.Session()
        return self

    def __exit__(self, *args):
        self._session.close()

    @property
    def request(self):
        '''
        I should have just had this class inherit requests.Session() and
        run self.post, etc. instead but such is life. Perhaps I'll update 
        it in the future or perhaps I won't. ¯\_(ツ)_/¯
        '''
        try:
            return self._session
        except:
            return requests

    def _build_app_url(self, app_name=None) -> str:
        '''
        Simple helper function to build app urls.
        '''
        return '/'.join([self.address, app_name])

    def bind(self, addr:str) -> None :
        '''
        A function called on __init__ to bind to a specific device.
        '''
        resp = self.request.get(addr)
        self.address = resp.headers.get('Application-URL')
        xml = XMLFile(resp.text)
        key = lambda element: '_'.join(sub('([a-z])([A-Z])', r'\1 \2', element).split()).lower().replace('-', '_')
        value = lambda element: xml.find(element).text
        tag_name = lambda element: element.tag.replace(xml.namespace, '')

        for element in [tag_name(el) for el in xml.find('device')]:
            try:
                k = key(element)
                v = value(element)
            except TypeError as e:
                print (e)
            finally:
                setattr(self, k, v) if v != "\n" else None
    
    def launch_app(self, app_name, callback=None, **kwargs) -> None:
        '''
        Launches specified application.
        '''
        url = self._build_app_url(app_name)
        data = unquote(urlencode(kwargs))
        headers = {'Content-Type':'text/plain; charset=utf-8'} if kwargs else {'Content-Length': "0"}
        resp = self.request.post(url, data=data, headers=headers)
        if resp.status_code in [200, 204]:
            self.refresh_url = unquote(resp.text)
            self.instance_url = resp.headers.get('location')
        else:
            raise Exception(f"{app_name} is not found, is it installed onto the device?")
        callback(resp) if callback else None

    def kill_app(self, app_name=None, callback=None) -> None:
        '''
        This will kill any active application tracked by this 
        instance if one exists and will return True if successful 
        otherwise it will return False.
        '''
        if app_name:
            app_url = self._build_app_url(app_name) + '/run'
        elif not app_name and not self.instance_url:
            raise Exception("There is no instance found to kill.")
        else:
            app_url = self.instance_url
        resp = self.request.delete(app_url)
        if resp.status_code in [200, 204]:
            self.instance_url = None
            self.refresh_url = None
        elif resp.status_code == 404:
            raise Exception(f"There is no running {app_name} instance.")
        callback(resp) if callback else None

    def get_app_status(self, app_name:str) -> dict:
        '''
        Makes a request to the DIAL device with a application name parameter and returns
        a dictionary including the supported DIAL version, app name and state.
        State examples: running, stopped or installable
        '''
        url = self._build_app_url(app_name)
        resp = self.request.get(url, headers={'Content-Type': 'text/plain'})
        xml = XMLFile(resp.text)
        return {
            'version': xml.find('service').attrib.get('dialVer'),
            'name': xml.find('name').text,
            'state': xml.find('state').text
        }

    def refresh_instance(self, inplace:bool=False)-> str:
        '''
        Makes a request using the refresh_url stored in the instance
        of this class.
        '''
        if not self.refresh_url:
            raise Exception('No refresh_url found in the dial instance.')
        resp = self.request.post(self.refresh_url)
        instance_url = resp.headers.get('location')
        if inplace:
            self.instance_url = instance_url
        else:
            return instance_url

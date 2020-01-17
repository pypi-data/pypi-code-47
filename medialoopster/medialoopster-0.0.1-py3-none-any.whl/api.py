from requests import Session
from requests.auth import HTTPBasicAuth


class Medialoopster(object):
    def __init__(self, url, user=None, password=None):
        self.session = Session()
        self.session.verify = False

        if user and password:
            self.session.auth = HTTPBasicAuth(user, password)

        self.url = url

    def __enter__(self):
        """Enable context management."""
        return self

    def __exit__(self, *args):
        """Clean up."""
        self.close()

    def ping(self):
        return self.session.get(self.url + "ping/")

    def asset_import(self, production=None, type=None, move_asset=False, name=None, description=None, approval=0,
                     path_file=None, meta_field_store={}):
        request = {
            "production": production,
            "type": type,
            "move_asset": move_asset,
            "asset": {
                "asset_meta": {
                    "name": name,
                    "description": description,
                    "approval": approval,
                    "path_file": path_file,
                    "meta_field_store": meta_field_store
                }
            }
        }

        response = self.session.post(self.url + "asset/import/", json=request).json()

        return response.get('asset_import_id', None)

    def get_productions(self):
        return self.get_from_api(type="productions")

    def get_from_api(self, type="videoassets", url=None):
        if not url:
            try:
                r = self.session.get(url=self.url)
                url = r.json().get(type, None)
            except ConnectionError:
                return None

        while url:
            try:
                r = self.session.get(url=url)
            except ConnectionError:
                continue

            if r.links:
                url = r.links.get("next", dict()).get("url", None)
            else:
                url = None

            yield r.json()

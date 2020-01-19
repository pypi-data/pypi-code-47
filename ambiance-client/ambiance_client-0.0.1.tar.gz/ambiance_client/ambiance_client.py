import requests

class AmbianceClient:
    """Client API for interacting with an Ambiance server"""

    def __init__(self, base_url):
        self._url = f"{base_url}/api/entities"

    def get_entities(self):
        return requests.get(self._url).json()

    def turn_on(self, entity_id):
        """Instruct a light to turn on."""
        requests.patch(f'{self._url}/{entity_id}', json = {"is_on": True})

    def turn_off(self, entity_id):
        """Instruct a light to turn off."""
        requests.patch(f'{self._url}/{entity_id}', json = {"is_on": False})

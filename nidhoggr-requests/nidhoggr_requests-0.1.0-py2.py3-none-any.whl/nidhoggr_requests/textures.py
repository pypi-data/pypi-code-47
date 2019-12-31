import requests
from typing import Dict

from nidhoggr.bl import BaseTextureRepo
from nidhoggr.models.texture import TextureType, TextureItem


class RequestsTextureRepo(BaseTextureRepo):
    def __init__(self, api_url: str, bearer_token: str):
        self.api_url = api_url
        self.bearer_token = bearer_token

    def get(self, *, uuid: str) -> Dict[TextureType, TextureItem]:
        result = requests.post(f'{self.api_url}/texture/get', json={'uuid': uuid}, headers={
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json'
        })

        if result.status_code != 200:
            return {}

        result_json = result.json()
        if not result_json:
            return {}

        response = {}
        for texture in result_json:
            response[TextureType(texture)] = TextureItem(url=result_json[texture])

        return response

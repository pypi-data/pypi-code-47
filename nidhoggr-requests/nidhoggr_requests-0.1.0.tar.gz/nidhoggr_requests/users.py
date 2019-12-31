import requests
from typing import Dict, Optional
from nidhoggr.bl import BaseUserRepo, User


class RequestsUserRepo(BaseUserRepo):
    def __init__(self, api_url: str, bearer_token: str):
        self.api_url = api_url
        self.bearer_token = bearer_token

    def get_user(self, **kw: Dict[str, str]) -> Optional[User]:
        result = requests.post(f'{self.api_url}/user/get', json=kw, headers={
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json'
        })

        if result.status_code != 200:
            return None

        result_json = result.json()
        if not result_json:
            return None

        return User.parse_obj(result_json)

    def check_password(self, *, clean: str, uuid: str) -> bool:
        result = requests.post(f'{self.api_url}/user/check_password', json={'uuid': uuid, 'password': clean}, headers={
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json'
        })

        if result.status_code != 200:
            return False

        result_json = result.json()
        if 'authenticated' not in result_json:
            return False

        return result_json['authenticated']

    def save_user(self, *, user: User) -> bool:
        result = requests.post(f'{self.api_url}/user/save', json=user.dict(), headers={
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json'
        })

        if result.status_code != 200:
            return False

        result_json = result.json()
        if 'saved' not in result_json:
            return False

        return result_json['saved']

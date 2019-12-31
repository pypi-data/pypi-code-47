from typing import Dict

from nidhoggr_core.repository import BaseTextureRepo
from nidhoggr_core.texture import TextureType, TextureItem

from nidhoggr_requests.core import RequestsRepo


class RequestsTextureRepo(BaseTextureRepo, RequestsRepo):

    def get(self, *, uuid: str) -> Dict[TextureType, TextureItem]:
        payload = {'uuid': uuid}
        result = self.fetch(endpoint='/texture/get', payload=payload)
        if result is not None:
            return {
                TextureType(kind): TextureItem(url=url)
                for kind, url
                in result.items()
            }
        return {}

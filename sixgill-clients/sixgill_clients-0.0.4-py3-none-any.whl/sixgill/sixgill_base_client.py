from typing import List, Dict, Any
from abc import abstractmethod
import json

from sixgill.sixgill_request_classes.sixgill_auth_request import SixgillAuthRequest
from sixgill.sixgill_request_classes.sixgill_base_request import SixgillBaseRequest
from sixgill.sixgill_exceptions import BadResponseException, AuthException
from sixgill.sixgill_utils import get_logger
from sixgill.sixgill_constants import VALID_STATUS_CODES
import traceback


class SixgillBaseClient(object):

    def __init__(self, client_id, client_secret, channel_code, logger=None, bulk_size=1000):
        self.client_id = client_id
        self.client_secret = client_secret
        self.channel_code = channel_code
        self.logger = get_logger(self.__class__.__name__) if logger is None else logger
        self.bulk_size = bulk_size
        self.digested_ids = []

    @staticmethod
    def _get_item_id(item) -> str:
        return item.get('id', "")

    @abstractmethod
    def _mark_as_digested(self, digested_ids: List[str]) -> Dict[str, Any]:
        raise NotImplemented()

    def _send_http_request(self, sixgill_api_request: SixgillBaseRequest):
        try:
            response = sixgill_api_request.send()

            if response.status_code not in VALID_STATUS_CODES:
                self.logger.error(f'Error in API call [{response.status_code}] - {response.reason}')
                raise BadResponseException(status_code=response.status_code, reason=response.reason, url=response.url,
                                           method=response.request.method)

            return response.json()

        except json.decoder.JSONDecodeError as e:
            self.logger.error(f'Failed parsing response {e}')
            raise

        except Exception as e:
            self.logger.error(f'Error {e}, traceback: {traceback.format_exc()}')
            raise

    def _get_access_token(self) -> str:
        try:
            response = SixgillAuthRequest(self.channel_code, self.client_id, self.client_secret).send()

            if response.status_code not in VALID_STATUS_CODES:
                raise AuthException(status_code=response.status_code, reason=response.reason, url=response.url,
                                    method=response.request.method)

            json_response = response.json()
            return json_response.get('access_token')

        except Exception as e:
            self.logger.error(f'Failed getting access token: {e}, traceback: {traceback.format_exc()}')
            raise

    def mark_digested_item(self, item):
        try:
            doc_id = self._get_item_id(item)

        except Exception as e:
            self.logger.error(f'Failed extracting doc_id: {item}, message {e}, traceback: {traceback.format_exc()}')
            raise

        self.digested_ids.append(doc_id)
        self.logger.debug(f'Marked id: {doc_id} as digested')

    def submit_digested_items(self, force: bool = False):
        if (len(self.digested_ids) >= self.bulk_size or force) and len(self.digested_ids) > 0:
            try:
                response = self._mark_as_digested(self.digested_ids)

            except Exception as e:
                self.logger.error(f'Failed marking items as digested {e}, traceback: {traceback.format_exc()}')
                raise

            if response.get("status") in VALID_STATUS_CODES:
                self.digested_ids = []

            self.logger.info(f'{response.get("message")}')

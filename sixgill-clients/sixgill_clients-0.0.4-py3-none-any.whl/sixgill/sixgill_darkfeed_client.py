from typing import List, Dict, Any

from sixgill.sixgill_base_client import SixgillBaseClient
from sixgill.sixgill_request_classes.sixgill_darkfeed_digested_request import SixgillDarkFeedDigestedRequest
from sixgill.sixgill_request_classes.sixgill_darkfeed_request import SixgillDarkFeedRequest
from sixgill.sixgill_utils import streamify


class SixgillDarkFeedClient(SixgillBaseClient):

    def _get_incidents(self, include_delivered_items: bool) -> List[Dict[str, Any]]:
        return self._send_http_request(SixgillDarkFeedRequest(self.channel_code, self._get_access_token(),
                                                              include_delivered_items, self.bulk_size))

    def _mark_as_digested(self, digested_ids: List[str]) -> Dict[str, Any]:
        return self._send_http_request(SixgillDarkFeedDigestedRequest(self.channel_code, self._get_access_token(),
                                                                      digested_ids))

    @streamify
    def get_incidents(self, include_delivered_items: bool = False) -> List[Dict[str, Any]]:
        self.submit_digested_items(force=True)
        return self._get_incidents(include_delivered_items)

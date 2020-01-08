from typing import List, Dict, Any

from sixgill.sixgill_base_client import SixgillBaseClient
from sixgill.sixgill_request_classes.sixgill_alerts_digested_request import SixgillAlertsDigestedRequest
from sixgill.sixgill_request_classes.sixgill_alerts_request import SixgillAlertsRequest
from sixgill.sixgill_utils import streamify


class SixgillAlertClient(SixgillBaseClient):

    def _get_alerts(self, offset: int, is_read: bool):
        return self._send_http_request(SixgillAlertsRequest(self.channel_code, self._get_access_token(), self.bulk_size,
                                                            is_read, offset))

    def _mark_as_digested(self, digested_ids: List[str]) -> Dict[str, Any]:
        return self._send_http_request(SixgillAlertsDigestedRequest(self.channel_code, self._get_access_token(),
                                                                    digested_ids))

    @streamify
    def get_alerts(self, offset: int = 0, is_read: bool = False) -> List[Dict[str, Any]]:
        self.submit_digested_items(force=True)
        return self._get_alerts(offset, is_read)

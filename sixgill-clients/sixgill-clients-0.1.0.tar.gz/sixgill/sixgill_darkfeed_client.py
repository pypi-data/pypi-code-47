from typing import List, Dict, Any
import traceback

from sixgill.sixgill_base_client import SixgillBaseClient
from sixgill.sixgill_request_classes.sixgill_darkfeed_digested_request import SixgillDarkFeedDigestedRequest
from sixgill.sixgill_request_classes.sixgill_darkfeed_request import SixgillDarkFeedRequest
from sixgill.sixgill_utils import streamify, is_indicator


class SixgillDarkFeedClient(SixgillBaseClient):

    def get_bundle(self) -> Dict[str, Any]:
        return self._send_request(SixgillDarkFeedRequest(self.channel_id, self._get_access_token(), self.bulk_size))

    def _mark_as_digested(self) -> int:
        return self._send_request(SixgillDarkFeedDigestedRequest(self.channel_id, self._get_access_token()))

    @streamify
    def get_indicator(self) -> List[Dict[str, Any]]:
        """
        This function is wrapped using a streamify decorator,
        which creates an iterator out of the list and returns item by item until server has nothing to return
        """
        self.commit_indicators()
        indicators = self.get_bundle().get("objects", [])
        return list(filter(is_indicator, indicators))

    def commit_indicators(self):
        try:
            response = self._mark_as_digested()

        except Exception as e:
            self.logger.error(f'Failed submitting {e}, traceback: {traceback.format_exc()}')
            raise

        if response <= 0:
            self.logger.info(f'Nothing committed')
        else:
            self.logger.info(f'Committed {response} indicators')

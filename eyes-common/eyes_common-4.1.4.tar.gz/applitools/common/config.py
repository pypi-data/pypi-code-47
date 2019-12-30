import uuid
from copy import copy
from datetime import datetime
from typing import TYPE_CHECKING

import attr

from applitools.common.geometry import RectangleSize
from applitools.common.match import ImageMatchSettings, MatchLevel
from applitools.common.server import FailureReports, SessionType
from applitools.common.utils import UTC, argument_guard
from applitools.common.utils.general_utils import get_env_with_prefix
from applitools.common.utils.json_utils import JsonInclude

if TYPE_CHECKING:
    from typing import TYPE_CHECKING, Dict, List, Optional, Text, TypeVar
    from applitools.common.utils.custom_types import ViewPort

    Self = TypeVar("Self", bound="Configuration")  # typedef

__all__ = ("BatchInfo", "Configuration")

MINIMUM_MATCH_TIMEOUT_MS = 600
DEFAULT_MATCH_TIMEOUT_MS = 2000  # type: int
DEFAULT_SERVER_REQUEST_TIMEOUT_MS = 60 * 5 * 1000
DEFAULT_SERVER_URL = "https://eyesapi.applitools.com"


@attr.s
class BatchInfo(object):
    """
    A batch of tests.
    """

    name = attr.ib(
        factory=lambda: get_env_with_prefix("APPLITOOLS_BATCH_NAME"),
        metadata={JsonInclude.THIS: True},
    )  # type: Optional[Text]
    started_at = attr.ib(
        factory=lambda: datetime.now(UTC), metadata={JsonInclude.THIS: True}
    )  # type: datetime
    sequence_name = attr.ib(
        init=False,
        factory=lambda: get_env_with_prefix("APPLITOOLS_BATCH_SEQUENCE"),
        metadata={JsonInclude.NAME: "batchSequenceName"},
    )  # type: Optional[Text]
    id = attr.ib(
        init=False,
        converter=str,
        factory=lambda: get_env_with_prefix("APPLITOOLS_BATCH_ID", str(uuid.uuid4())),
        metadata={JsonInclude.THIS: True},
    )  # type: Text

    def with_batch_id(self, id):
        # type: (Text) -> BatchInfo
        argument_guard.not_none(id)
        self.id = str(id)
        return self


@attr.s
class Configuration(object):
    batch = attr.ib(default=None)  # type: Optional[BatchInfo]
    branch_name = attr.ib(
        factory=lambda: get_env_with_prefix("APPLITOOLS_BRANCH", None)
    )  # type: Optional[Text]
    parent_branch_name = attr.ib(
        factory=lambda: get_env_with_prefix("APPLITOOLS_PARENT_BRANCH", None)
    )  # type: Optional[Text]
    baseline_branch_name = attr.ib(
        factory=lambda: get_env_with_prefix("APPLITOOLS_BASELINE_BRANCH", None)
    )  # type: Optional[Text]
    agent_id = attr.ib(default=None)  # type: Optional[Text]
    baseline_env_name = attr.ib(default=None)  # type: Optional[Text]
    environment_name = attr.ib(default=None)  # type: Optional[Text]
    save_diffs = attr.ib(default=None)  # type: bool
    app_name = attr.ib(default=None)  # type: Optional[Text]
    test_name = attr.ib(default=None)  # type: Optional[Text]
    viewport_size = attr.ib(
        default=None, converter=attr.converters.optional(RectangleSize.from_)
    )  # type: Optional[RectangleSize]
    session_type = attr.ib(default=SessionType.SEQUENTIAL)  # type: SessionType
    host_app = attr.ib(default=None)  # type: Optional[Text]
    host_os = attr.ib(default=None)  # type: Optional[Text]
    properties = attr.ib(factory=list)  # type: List[Dict[Text, Text]]
    match_timeout = attr.ib(default=DEFAULT_MATCH_TIMEOUT_MS)  # type: int # ms
    match_level = attr.ib(
        default=MatchLevel.STRICT, converter=MatchLevel
    )  # type: MatchLevel
    is_disabled = attr.ib(default=False)  # type: bool
    ignore_displacements = attr.ib(default=False)  # type: bool
    save_new_tests = attr.ib(default=True)  # type: bool
    save_failed_tests = attr.ib(default=False)  # type: bool
    failure_reports = attr.ib(default=FailureReports.ON_CLOSE)  # type: FailureReports
    send_dom = attr.ib(default=True)  # type: bool
    use_dom = attr.ib(default=False)  # type: bool
    enable_patterns = attr.ib(default=False)  # type: bool
    default_match_settings = attr.ib(
        default=ImageMatchSettings()
    )  # type: ImageMatchSettings
    stitch_overlap = attr.ib(default=5)  # type: int

    api_key = attr.ib(
        factory=lambda: get_env_with_prefix("APPLITOOLS_API_KEY", None)
    )  # type: Optional[Text]
    server_url = attr.ib(
        factory=lambda: get_env_with_prefix("APPLITOOLS_SERVER_URL", DEFAULT_SERVER_URL)
    )  # type: Text
    _timeout = attr.ib(default=DEFAULT_SERVER_REQUEST_TIMEOUT_MS)  # type: int # ms

    def set_batch(self, batch):
        # type: (Self, BatchInfo) -> Self
        argument_guard.is_a(batch, BatchInfo)
        self.batch = batch
        return self

    def set_branch_name(self, branch_name):
        # type: (Self, Text) -> Self
        self.branch_name = branch_name
        return self

    def set_agent_id(self, agent_id):
        # type: (Self, Text) -> Self
        self.agent_id = agent_id
        return self

    def set_parent_branch_name(self, parent_branch_name):
        # type: (Self, Text) -> Self
        self.parent_branch_name = parent_branch_name
        return self

    def set_baseline_branch_name(self, baseline_branch_name):
        # type: (Self, Text) -> Self
        self.baseline_branch_name = baseline_branch_name
        return self

    def set_baseline_env_name(self, baseline_env_name):
        # type: (Self, Text) -> Self
        self.baseline_env_name = baseline_env_name
        return self

    def set_environment_name(self, environment_name):
        # type: (Self, Text) -> Self
        self.environment_name = environment_name
        return self

    def set_save_diffs(self, save_diffs):
        # type: (Self, bool) -> Self
        self.save_diffs = save_diffs
        return self

    def set_app_name(self, app_name):
        # type: (Self, Text) -> Self
        self.app_name = app_name
        return self

    def set_test_name(self, test_name):
        # type: (Self, Text) -> Self
        self.test_name = test_name
        return self

    def set_viewport_size(self, viewport_size):
        # type: (Self, ViewPort) -> Self
        self.viewport_size = viewport_size
        return self

    def set_session_type(self, session_type):
        # type: (Self, SessionType) -> Self
        self.session_type = session_type
        return self

    @property
    def ignore_caret(self):
        # type: () -> bool
        ignore = self.default_match_settings.ignore_caret
        return True if ignore is None else ignore

    def set_ignore_caret(self, ignore_caret):
        # type: (Self, bool) -> Self
        self.default_match_settings.ignore_caret = ignore_caret
        return self

    def set_host_app(self, host_app):
        # type: (Self, Text) -> Self
        self.host_app = host_app
        return self

    def set_host_os(self, host_os):
        # type: (Self, Text) -> Self
        self.host_os = host_os
        return self

    def set_match_timeout(self, match_timeout):
        # type: (Self, int) -> Self
        self.match_timeout = match_timeout
        return self

    def set_match_level(self, match_level):
        # type: (Self, MatchLevel) -> Self
        self.match_level = match_level
        return self

    def set_ignore_displacements(self, ignore_displacements):
        # type: (Self, bool) -> Self
        self.ignore_displacements = ignore_displacements
        return self

    def set_save_new_tests(self, save_new_tests):
        # type: (Self, bool) -> Self
        self.save_new_tests = save_new_tests
        return self

    def set_save_failed_tests(self, save_failed_tests):
        # type: (Self, bool) -> Self
        self.save_failed_tests = save_failed_tests
        return self

    def set_failure_reports(self, failure_reports):
        # type: (Self, FailureReports) -> Self
        self.failure_reports = failure_reports
        return self

    def set_send_dom(self, send_dom):
        # type: (Self, bool) -> Self
        self.send_dom = send_dom
        return self

    def set_use_dom(self, use_dom):
        # type: (Self, bool) -> Self
        self.use_dom = use_dom
        return self

    def set_enable_patterns(self, enable_patterns):
        # type: (Self, bool) -> Self
        self.enable_patterns = enable_patterns
        return self

    def set_stitch_overlap(self, stitch_overlap):
        # type: (Self, int) -> Self
        self.stitch_overlap = stitch_overlap
        return self

    def set_api_key(self, api_key):
        # type: (Self, Text) -> Self
        self.api_key = api_key
        return self

    def set_server_url(self, server_url):
        # type: (Self, Text) -> Self
        self.server_url = server_url
        return self

    @match_timeout.validator
    def _validate1(self, attribute, value):
        if 0 < value < MINIMUM_MATCH_TIMEOUT_MS:
            raise ValueError(
                "Match timeout must be at least {} ms.".format(MINIMUM_MATCH_TIMEOUT_MS)
            )

    @viewport_size.validator
    def _validate2(self, attribute, value):
        if value is None:
            return None
        if isinstance(value, RectangleSize) or (
            isinstance(value, dict)
            and "width" in value.keys()
            and "height" in value.keys()
        ):
            return None

        raise ValueError("Wrong viewport type settled")

    @property
    def is_send_dom(self):
        # type: () -> bool
        return self.send_dom

    def clone(self):
        # type: () -> Configuration
        return copy(self)

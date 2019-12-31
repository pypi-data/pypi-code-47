import os
from typing import ClassVar, Dict, Iterator, List, Optional, Set

import attr
import backoff
import requests
import singer

from .version import __version__

LOGGER = singer.get_logger()


def is_fatal_code(e: requests.exceptions.RequestException) -> bool:
    '''Helper function to determine if a Requests reponse status code
    is a "fatal" status code. If it is, the backoff decorator will giveup
    instead of attemtping to backoff.'''
    return 400 <= e.response.status_code < 500 and e.response.status_code != 429


@attr.s
class PivotalTrackerStream(object):
    tap_stream_id: ClassVar[Optional[str]] = None

    api_token: str = attr.ib()
    config: Dict = attr.ib(repr=False)
    config_path: str = attr.ib()
    state: Dict = attr.ib()
    base_url: str = attr.ib(init=False)
    schema: Dict = attr.ib(repr=False, init=False)
    api_version: str = attr.ib(default="v5", validator=attr.validators.instance_of(str))
    params: Dict = attr.ib(init=False, default=None)

    def __attrs_post_init__(self):
        self.base_url = f"https://www.pivotaltracker.com/services/{self.api_version}"

        if self.tap_stream_id is not None:
            self.schema = self._load_schema()

        if self.config.get("streams") is None:
            self.params = {}
        else:
            self.params = self.config.get("streams").get(self.tap_stream_id, {})
            if not isinstance(self.params, dict):
                raise TypeError("Stream parameters must be supplied as JSON.")
            else:
                for key in self.params.keys():
                    if key not in self.valid_params:
                        raise ValueError(f"{key} is not a valid parameter for stream {self.tap_stream_id}")

        if self.schema is not None:
            self.params.update({"fields": ','.join(self.schema.get("properties").keys())})

    @classmethod
    def from_args(cls, args):
        return cls(api_token=args.config.get("api_token"),
                   api_version=args.config.get("api_version"),
                   config=args.config,
                   config_path=args.config_path,
                   state=args.state)

    def _get_abs_path(self, path: str) -> str:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)

    def _load_schema(self) -> Dict:
        '''Loads a JSON schema file for a given
        Dayforce resource into a dict representation.
        '''
        schema_path = self._get_abs_path("schemas")
        return singer.utils.load_json(f"{schema_path}/{self.tap_stream_id}.json")

    def _construct_headers(self) -> Dict:
        '''Constructs a standard set of headers for HTTPS requests.'''
        headers = requests.utils.default_headers()
        headers["User-Agent"] = f"python-pivotal-tracker-tap/{__version__}"
        headers["X-TrackerToken"] = self.api_token
        headers["Date"] = singer.utils.strftime(singer.utils.now(), '%a, %d %b %Y %H:%M:%S %Z')
        return headers

    @singer.utils.ratelimit(limit=300, every=60)
    @backoff.on_exception(backoff.fibo,
                          requests.exceptions.HTTPError,
                          max_time=120,
                          giveup=is_fatal_code,
                          logger=LOGGER)
    @backoff.on_exception(backoff.fibo,
                          (requests.exceptions.ConnectionError,
                           requests.exceptions.Timeout),
                          max_time=120,
                          logger=LOGGER)
    def _get(self, endpoint: str, params: Dict = None) -> Dict:
        '''Constructs a standard way of making
        a GET request to the Pivotal Tracker REST API.
        '''
        url = self.base_url + endpoint
        headers = self._construct_headers()
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def _yield_records(self, entity: str, params: Optional[Dict] = None) -> Iterator[Dict]:
        '''Yeild individual records for a given entity.'''
        if params is not None:
            params.update({
                "envelope": "true"
            })
        response = self._get(endpoint=f"/{entity}", params=params)
        for record in response.get("data"):
            yield record

        # Pagination
        pagination_data = response.get("pagination")
        if pagination_data is not None:
            total_returned = pagination_data.get("returned")
            current_offset = pagination_data.get("offset")
            while total_returned < pagination_data.get("total"):
                current_offset += pagination_data.get("returned")
                if params is not None:
                    params.update({"offset": current_offset})
                response = self._get(endpoint=f"/{entity}", params=params)
                for record in response.get("data"):
                    yield record

                pagination_data = response.get("pagination")
                total_returned += pagination_data.get("returned")

    def write_schema_message(self):
        '''Writes a Singer schema message.'''
        return singer.write_schema(stream_name=self.tap_stream_id, schema=self.schema, key_properties=self.key_properties)

    def write_state_message(self):
        '''Writes a Singer state message.'''
        return singer.write_state(self.state)


@attr.s
class AccountsStream(PivotalTrackerStream):
    tap_stream_id: ClassVar[str] = 'accounts'
    key_properties: ClassVar[List[str]] = ["id"]
    bookmark_properties: ClassVar[List[str]] = []
    replication_method: ClassVar[str] = 'FULL_TABLE'
    valid_params: ClassVar[Set[str]] = set()

    def sync(self):
        with singer.metrics.job_timer(job_type=f"sync_{self.tap_stream_id}"):
            with singer.metrics.record_counter(endpoint=self.tap_stream_id) as counter:
                for record in self._yield_records(entity=self.tap_stream_id, params=self.params):
                    with singer.Transformer() as transformer:
                        transformed_record = transformer.transform(data=record, schema=self.schema)
                        singer.write_record(stream_name=self.tap_stream_id, time_extracted=singer.utils.now(), record=transformed_record)
                        counter.increment()


@attr.s
class ProjectsStream(PivotalTrackerStream):
    tap_stream_id: ClassVar[str] = 'projects'
    key_properties: ClassVar[List[str]] = ["id"]
    bookmark_properties: ClassVar[List[str]] = []
    replication_method: ClassVar[str] = 'FULL_TABLE'
    valid_params: ClassVar[Set[str]] = {
        "account_ids"
    }

    def sync(self):
        with singer.metrics.job_timer(job_type=f"sync_{self.tap_stream_id}"):
            with singer.metrics.record_counter(endpoint=self.tap_stream_id) as counter:
                for record in self._yield_records(entity=self.tap_stream_id, params=self.params):
                    with singer.Transformer() as transformer:
                        transformed_record = transformer.transform(data=record, schema=self.schema)
                        singer.write_record(stream_name=self.tap_stream_id, time_extracted=singer.utils.now(), record=transformed_record)
                        counter.increment()


@attr.s
class ProjectMembershipsStream(PivotalTrackerStream):
    tap_stream_id: ClassVar[str] = 'project_memberships'
    key_properties: ClassVar[List[str]] = ["id"]
    bookmark_properties: ClassVar[List[str]] = []
    replication_method: ClassVar[str] = 'FULL_TABLE'
    valid_params: ClassVar[Set[str]] = {
        "role",
        "email",
        "name",
        "initials",
        "project_color",
        "favorite"
    }

    def sync(self):
        with singer.metrics.job_timer(job_type=f"sync_{self.tap_stream_id}"):
            with singer.metrics.record_counter(endpoint=self.tap_stream_id) as counter:
                project_params = self.config.get("streams", {}).get("projects", {})
                project_params.update({"fields": "id"})
                for project in self._yield_records(entity='projects', params=project_params):
                    for record in self._yield_records(entity=f"projects/{project.get('id')}/memberships", params=self.params):
                        with singer.Transformer() as transformer:
                            transformed_record = transformer.transform(data=record, schema=self.schema)
                            singer.write_record(stream_name=self.tap_stream_id, time_extracted=singer.utils.now(), record=transformed_record)
                            counter.increment()


@attr.s
class LabelsStream(PivotalTrackerStream):
    tap_stream_id: ClassVar[str] = 'labels'
    key_properties: ClassVar[List[str]] = ["id"]
    bookmark_properties: ClassVar[List[str]] = []
    replication_method: ClassVar[str] = 'FULL_TABLE'
    valid_params: ClassVar[Set[str]] = set()

    def sync(self):
        with singer.metrics.job_timer(job_type=f"sync_{self.tap_stream_id}"):
            with singer.metrics.record_counter(endpoint=self.tap_stream_id) as counter:
                project_params = self.config.get("streams", {}).get("projects", {})
                project_params.update({"fields": "id"})
                for project in self._yield_records(entity='projects', params=project_params):
                    for record in self._yield_records(entity=f"projects/{project.get('id')}/labels", params=self.params):
                        with singer.Transformer() as transformer:
                            transformed_record = transformer.transform(data=record, schema=self.schema)
                            singer.write_record(stream_name=self.tap_stream_id, time_extracted=singer.utils.now(), record=transformed_record)
                            counter.increment()


@attr.s
class StoriesStream(PivotalTrackerStream):
    tap_stream_id: ClassVar[str] = 'stories'
    key_properties: ClassVar[List[str]] = ["id"]
    bookmark_properties: ClassVar[str] = "updated_at"
    api_bookmark_param: ClassVar[str] = "updated_after"
    replication_method: ClassVar[str] = 'INCREMENTAL'
    expand_endpoints: ClassVar[Set[str]] = {
        "tasks",
        "comments",
        "blockers"
    }
    valid_params: ClassVar[Set[str]] = {
        "with_label",
        "with_story_type",
        "with_state",
        "after_story_id",
        "before_story_id",
        "accepted_before",
        "accepted_after",
        "created_before",
        "created_after",
        "updated_before",
        "updated_after",
        "deadline_before",
        "deadline_after",
        "limit",
        "filter"
    }

    def sync(self):
        current_bookmark_str = singer.bookmarks.get_bookmark(state=self.state,
                                                             tap_stream_id=self.tap_stream_id,
                                                             key=self.bookmark_properties)

        if current_bookmark_str is not None:
            self.params.update({self.api_bookmark_param: current_bookmark_str})

        singer.bookmarks.write_bookmark(state=self.state,
                                        tap_stream_id=self.tap_stream_id,
                                        key=self.bookmark_properties,
                                        val=singer.utils.strftime(singer.utils.now()))

        with singer.metrics.job_timer(job_type=f"sync_{self.tap_stream_id}"):
            with singer.metrics.record_counter(endpoint=self.tap_stream_id) as counter:
                project_params = self.config.get("streams", {}).get("projects", {})
                project_params.update({"fields": "id"})
                for project in self._yield_records(entity='projects', params=project_params):
                    # Reset the offset after each Project iteration.
                    self.params.update({"offset": 0})
                    for story in self._yield_records(entity=f"projects/{project.get('id')}/stories", params=self.params):
                        for endpoint in self.expand_endpoints:
                            records = [record for record in self._yield_records(entity=f"projects/{project.get('id')}/stories/{story.get('id')}/{endpoint}", params={})]
                            story[endpoint] = records
                        with singer.Transformer() as transformer:
                            transformed_record = transformer.transform(data=story, schema=self.schema)
                            singer.write_record(stream_name=self.tap_stream_id, time_extracted=singer.utils.now(), record=transformed_record)
                            counter.increment()

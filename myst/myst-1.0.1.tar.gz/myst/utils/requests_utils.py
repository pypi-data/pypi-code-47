"""This module contains various utility functions related to requests."""
import datetime
import logging
import random
import time

import pytz
from requests import Session
from six.moves import urllib

import myst
from myst.exceptions import MystAPIError

# Define request retry configuration.

_DEFAULT_MAX_BACKOFF_TIMEOUT = 64
_DEFAULT_MAX_RETRIES = 3
_DEFAULT_BACKOFF_FACTOR = 1.0
_DEFAULT_RETRYABLE_HTTP_STATUSES = {
    429,  # Too Many Requests
    500,  # Internal Server Error
    502,  # Bad Gateway
    503,  # Service Unavailable
    504,  # Gateway Timeout
}

logger = logging.getLogger(__name__)


def _compute_retry_timeout(retry_count, backoff_factor, max_backoff_timeout=_DEFAULT_MAX_BACKOFF_TIMEOUT):
    """Computes a timeout for retrying requests by exponentially backing off.

    Args:
        retry_count (int): current retry count
        backoff_factor (float): factor used in backoff algorithm
        max_backoff_timeout (int, optional): max number of seconds to back off for before retrying

    Returns:
        backoff_timeout (float): backoff timeout
    """
    backoff_timeout = float(min(backoff_factor * (2 ** (retry_count - 1)), max_backoff_timeout))
    return backoff_timeout


def _make_request(
    request_url,
    method="GET",
    session=None,
    auth=None,
    headers=None,
    data=None,
    max_retry_count=_DEFAULT_MAX_RETRIES,
    backoff_factor=_DEFAULT_BACKOFF_FACTOR,
    max_backoff_timeout=_DEFAULT_MAX_BACKOFF_TIMEOUT,
    retryable_status_codes=None,
):
    """Makes a request to the specified url with the given method.

    Handles retry-logic and error handling for HTTP requests.

    Args:
        request_url (str): the url used to fetch the JSON content
        method (str, optional): HTTP request method (e.g. GET, POST, PUT, etc.)
        session (requests.Session, optional): session to make request with
        auth (tuple, optional): auth tuple to enable Basic/Digest/Custom HTTP Auth
        headers (dict of str:str, optional): HTTP header key:value pairs
        data (str, optional): request body (for a POST request)
        max_retry_count (int, optional): number of times to retry if request fails
        max_backoff_timeout (int, optional): max number of seconds to back off for before retrying
        backoff_factor (float, optional): backoff factor used to determine timeouts between retries
        retryable_status_codes (set, optional): status codes to retry; if not specified, a sensible default will be used

    Returns:
        response (requests.Response): fetched HTTP response
    """
    # If no session was given, construct a default session to use.
    if session is None:
        session = Session()

    # If specific retryable status codes were not given, use a sensible default.
    if retryable_status_codes is None:
        retryable_status_codes = _DEFAULT_RETRYABLE_HTTP_STATUSES

    logger.debug("Sending a {} request to {}.".format(method, request_url))

    # Make requests so long as we have enough retries available.
    retry_count = 0
    while True:

        # Use the session to make the request. Using the context manager ensures that the session closes any sockets
        # after use.
        with session:
            response = session.request(method=method, url=request_url, headers=headers, data=data, auth=auth)

        # If the response is OK, we're done and we can return the response.
        if response.ok:
            break

        # Otherwise, retry if we've received a retryable status code and still have retries left to use.
        elif response.status_code in retryable_status_codes and retry_count < max_retry_count:
            logger.debug("Received an invalid response to {} request to {}. Retrying.".format(method, request_url))
            logger.debug("Retrying to send a {} request to {}.".format(method, request_url))

            # Increment retry count and sleep, incorporating back off and jitter.
            retry_count += 1
            retry_timeout = _compute_retry_timeout(
                retry_count=retry_count, backoff_factor=backoff_factor, max_backoff_timeout=max_backoff_timeout
            )
            time.sleep(retry_timeout + random.random())

        # We are out of retries or were returned a status code that we shouldn't retry so raise a descriptive error.
        else:
            raise IOError(
                "Unable to request the specified url {url} after {retry_count} retries. "
                "The last request response code is {code} (`{reason}`) with content `{content}`.".format(
                    url=request_url,
                    retry_count=retry_count,
                    code=response.status_code,
                    reason=response.reason,
                    content=response.content,
                )
            )

    return response


def fetch_json_content(
    request_url,
    session=None,
    auth=None,
    headers=None,
    max_retry_count=_DEFAULT_MAX_RETRIES,
    backoff_factor=_DEFAULT_BACKOFF_FACTOR,
    max_backoff_timeout=_DEFAULT_MAX_BACKOFF_TIMEOUT,
    retryable_status_codes=None,
):
    """Fetches JSON content using the passed request url.

    Args:
        request_url (str): the url used to fetch the JSON content
        session (requests.Session, optional): session to make request with
        auth (tuple, optional): auth tuple to enable Basic/Digest/Custom HTTP Auth
        headers (dict, optional): request headers to be passed
        max_retry_count (int, optional): number of times to retry if request fails
        max_backoff_timeout (int, optional): max number of seconds to back off for before retrying
        backoff_factor (float, optional): backoff factor used to determine timeouts between retries
        retryable_status_codes (set, optional): status codes to retry; if not specified, a sensible default will be used

    Returns:
        json_content (dict): fetched JSON content
    """
    response = _make_request(
        request_url,
        session=session,
        auth=auth,
        headers=headers,
        max_retry_count=max_retry_count,
        backoff_factor=backoff_factor,
        max_backoff_timeout=max_backoff_timeout,
        retryable_status_codes=retryable_status_codes,
    )

    try:
        json_content = response.json()
    except ValueError as error:
        raise MystAPIError(
            http_status_code=response.status_code,
            code=response.status_code,
            message=str.format(
                "Failed to decode json response content. Error message: {error_message}. "
                "Response content: {response_content}.",
                error_message=str(error),
                response_content=response.content,
            ),
        )

    return json_content


def build_resource_url(resource_name, resource_uuid=None):
    """Builds the Myst API URL for a resource.

    Args:
        resource_name (str): resource name to build URL for
        resource_uuid (str, optional): resource instance uuid; if None, this function will just return the resource
            class url

    Returns:
        resource_url (str): resource url
    """
    api_base = urllib.parse.urljoin("{api_host}/".format(api_host=myst.api_host), myst.api_version)
    resource_url = urllib.parse.urljoin("{api_base}/".format(api_base=api_base), resource_name)
    if resource_uuid is not None:
        resource_url = urllib.parse.urljoin("{resource_url}/".format(resource_url=resource_url), resource_uuid)
    return resource_url


def encode_url(base_url, params):
    """Encodes the base url using the passed get parameters.

    Args:
        base_url (str): base url
        params (list of tuple): parameters to be used in the encoded url; note that even though `urllib.parse.urlencode`
            can take `params` in dictionary form, a list of tuple preserves order, whereas a dictionary does not

    Returns:
        encoded_url (str): encoded url
    """
    # Format any special parameter types that need to be formatted.
    formatted_params = []
    for param, value in params:
        if isinstance(value, datetime.datetime):
            value = format_timestamp(value)
        formatted_params.append((param, value))

    encoded_url = "{base_url}?{params}".format(base_url=base_url, params=urllib.parse.urlencode(formatted_params))
    return encoded_url


def format_timestamp(timestamp):
    """Formats the passed timestamp according to the RFC 3339 standard.

    Args:
        timestamp (datetime.datetime): timestamp to be formatted

    Returns:
        formatted_timestamp (str): formatted timestamp
    """
    if timestamp.tzinfo is None or timestamp.tzinfo is pytz.UTC:
        formatted_timestamp = "{}Z".format(timestamp.replace(tzinfo=None).isoformat())
    else:
        formatted_timestamp = timestamp.isoformat()
    return formatted_timestamp

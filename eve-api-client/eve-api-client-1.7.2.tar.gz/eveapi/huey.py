import datetime
import json
import logging
from json.decoder import JSONDecodeError

import redis
import requests
from django.conf import settings
from django.utils import timezone
from huey.exceptions import RetryTask

from eveapi.esi.errors import ESIPageCacheRefresh

TIMEOUT = 30

SESSION = requests.Session()
ADAPTER = requests.adapters.HTTPAdapter(pool_connections=1000, pool_maxsize=1000, max_retries=3)
SESSION.mount('https://', ADAPTER)

logger = logging.getLogger(__name__)
redis = redis.StrictRedis(connection_pool=settings.REDIS_POOL)

HUEY = settings.EVEAPI_HUEY_INSTANCE


def log_data_age(r):
    """
    Logs data age and expiry time in seconds.
    Age is time since last modified, expiry is the time until the esi refreshes the cache.
    """
    age = -1
    expires = -1
    if 'Last-Modified' in r.headers:
        age = datetime.datetime.now() \
              - datetime.datetime.strptime(r.headers['Last-Modified'], '%a, %d %b %Y %H:%M:%S %Z')
        age = round(age.total_seconds())

    if 'Expires' in r.headers:
        expires = datetime.datetime.strptime(r.headers['Expires'], '%a, %d %b %Y %H:%M:%S %Z') - datetime.datetime.now()
        expires = round(expires.total_seconds())

    logger.debug('ESI data is {} seconds old, new ESI data in {} seconds'.format(age, expires),
                 extra={'esi_type': 'data_age', 'age': age, 'expires': expires})

    return age, expires


def get_cache_url(url, params):
    """
    Appends the parameters to the url.
    This is used to cache urls with specific parameters.
    Parameters are sorted by key names since parameters are unordered.

    This may not generate valid urls, this should only be used for redis keys.
    """
    params = map(lambda param: str(param[0]) + '=' + str(param[1]), params.items())  # join param key/value pairs
    params = '&'.join(sorted(params))  # sort since dicts can be in any order, sort by key
    return url + '?' + params


def error_limit_retry(delay=settings.ESI_RETRY, **kwargs):
    """
    Schedule another esi task after the esi error limit reset ends then return the result.
    """
    return esi.schedule(
        kwargs=kwargs,
        delay=delay,
    ).get(timeout=90, blocking=True)


def cache_response(endpoint, expires, data):
    if expires:
        cached_until = timezone.make_aware(datetime.datetime.strptime(expires, '%a, %d %b %Y %H:%M:%S %Z'))
        time_delta = cached_until - timezone.now()
        seconds = int(time_delta.total_seconds())
    else:
        seconds = 300  # default to 5 minutes

    if seconds > 0:
        data = json.dumps(data)
        redis.setex(endpoint, seconds, data)

        return True


@HUEY.task(retries=3, retry_delay=5)
def esi(method, url, headers, params, data, fetch_pages, cache, raise_error,
        page=None, parent_expires=None, auth_callback=None):
    """
    ESI call method.
    This calls the esi, aggregates pages, and caches results.
    On errors this function will be rerun
    """

    def kwargs_with(**kwargs_):
        return {
            'method': method,
            'url': url,
            'headers': headers,
            'params': params,
            'data': data,
            'fetch_pages': fetch_pages,
            'cache': cache,
            'raise_error': raise_error,
            'page': page,
            'parent_expires': parent_expires,
            'auth_callback': auth_callback,
            **kwargs_,
        }

    # set page number
    if page:
        params['page'] = page  # unspecified gives the first page in esi

    cache_url = get_cache_url(url, params)

    # log route info
    logger.debug('({}) {}'.format(method, cache_url),
                 extra={'esi_type': 'esi_route_info', 'method': method, 'cache_url': cache_url})

    # check for cached request
    cached = redis.get(cache_url)
    if method == 'GET' and cached:  # return cached get response
        logger.debug('Cached ESI call', extra={'esi_type': 'cached_call'})
        return json.loads(cached.decode('utf-8'))

    # check for esi_api_client.lock to esi rate limit
    delay = redis.ttl('esi_api_client.lock')
    if delay and delay > 0:
        message = redis.get('esi_api_client.lock')
        logger.warning('esi locked due to "{}", retrying in {}'.format(message, delay),
                       extra={'esi_type': 'error_limit_hit', 'delay': delay})
        return error_limit_retry(**kwargs_with())

    # make request
    r = SESSION.request(method, url, params=params, headers=headers, data=data, timeout=TIMEOUT)
    logger.debug('got response in {} seconds'.format(r.elapsed.seconds),
                 extra={'esi_type': 'esi_response', 'duration': r.elapsed.seconds})

    # check ESI error rate limiting
    if 'X-Esi-Error-Limit-Remain' in r.headers and int(r.headers['X-Esi-Error-Limit-Remain']) <= 20:
        delay = r.headers.get('X-Esi-Error-Limit-Reset', settings.ESI_RETRY)
        redis.setex('esi_api_client.lock', delay, delay)

    if 200 <= r.status_code < 300:  # is 2xx
        age, expires = log_data_age(r)
        logger.info('esi 2xx response', extra={
            'esi_type': '2xx_response',
            'status': r.status_code,
            'age': age,
            'expires': expires,
            'url': cache_url,
            'duration': r.elapsed.seconds
        })

        if 'application/json' not in r.headers.get('Content-Type', ''):
            return True

        if parent_expires and r.headers.get('Expires', None) != parent_expires:
            # return (not raise) an exception, since we want the parent call (page 1) to retry
            return ESIPageCacheRefresh()

        try:
            response_data = r.json()
        except JSONDecodeError:
            raise RetryTask()

        # load multiple pages if able to
        total_pages = int(r.headers.get('x-pages', 1))
        if fetch_pages and total_pages > 1:
            logger.debug('got {} pages, fetching all'.format(total_pages),
                         extra={'esi_type': 'fetching_pages', 'pages': total_pages})
            pages = [
                esi(**kwargs_with(
                    fetch_pages=False,
                    page=p + 2,
                    parent_expires=r.headers.get('Expires', None)
                ))
                for p in range(total_pages - 1)  # +2 since pages are 1-based indexed
            ]
            for page_request in pages:
                page_data = page_request.get(blocking=True, timeout=300)  # block to get result

                if isinstance(page_data, ESIPageCacheRefresh):
                    logger.warning(page_data, extra={'esi_type': 'fetch_page_error'})
                    for p in pages:
                        p.revoke()

                    # retry this task
                    raise RetryTask()

                response_data.extend(page_data)  # assume both are lists

        # cache response if get request
        if method == 'GET' and cache:  # assume fetch_pages and save the full data list for page=false
            cache_response(get_cache_url(url, params), r.headers.get('Expires', None), response_data)

        return response_data

    else:
        try:
            data = r.json()
        except JSONDecodeError:
            data = {}

        error_limit = r.headers.get('X-ESI-Error-Limit-Remain', 100)
        error_message = data.get('error', '')
        sso_status = data.get('sso_status', '')

        logger.info('esi 200 response'.format(r.elapsed.seconds),
                    extra={'esi_type': 'response', 'status': r.status_code,
                           'url': cache_url,
                           })
        logger.error('ESI request {} error: {} - {}, {}'.format(
            r.url,
            r.status_code,
            r.content,
            error_limit
        ), extra={
            'esi_type': 'request_error',
            'url': cache_url,
            'status': r.status_code,
            'esi_error_content': r.content,
            'esi_error_message': error_message,
            'sso_status': sso_status,
            'error_limit': error_limit,
            'duration': r.elapsed.seconds
        })

        # remake request if token was expired
        if error_message == 'expired':
            raise RetryTask()

        # error refreshing token, so refresh the token again
        if error_message == 'invalid character \'<\' looking for beginning of value':
            redis.setex('esi_api_client.lock', 60, 'invalid character, refreshing token and auth header')
            headers_ = headers.copy()
            headers_['Authorization'] = auth_callback(force=True)
            logger.info('refreshed token and auth header: {}'.format(headers_['Authorization']))
            error_limit_retry(**kwargs_with(headers=headers_, delay=60))

        # retry request in 5 minutes after TQ is back up
        if error_message == 'The datasource tranquility is temporarily unavailable':
            return error_limit_retry(**kwargs_with(delay=60 * 5))

        # log error for esi rate limiting
        if error_limit == 0:
            logger.error('ESI error limit hit 0', extra={'esi_type': 'error_limit_hit_0'})
            delay = redis.ttl('esi_api_client.lock')
            return error_limit_retry(**kwargs_with(delay=delay + 10))

        if raise_error == r.status_code:
            return r
        elif raise_error is True:
            return r

        raise RetryTask()

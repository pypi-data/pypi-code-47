import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from uuid import UUID

bb_api_root = 'https://api.bitbucket.org'


def create(key, secret, repository, title, description, head, base='master', reviewer=None, close_source_branch=False,
           *_):
    if not reviewer:
        reviewer = []
    auth_headers = bb_authenticate(key, secret)
    reviewer_uuids = [{
        'uuid': bb_user_to_uuid(auth_headers, r),
    } for r in reviewer]
    payload = {
        'title': title,
        'description': description,
        'source': {'branch': {'name': head}},
        'destination': {'branch': {'name': base}},
        'reviewers': reviewer_uuids,
        'close_source_branch': close_source_branch,
    }
    url = '{}/2.0/repositories/{}/pullrequests'.format(bb_api_root, repository)
    requests.post(
        url=url,
        json=payload,
        headers=auth_headers,
    )


def bb_authenticate(key, secret):
    client = BackendApplicationClient(client_id=key)
    oauth = OAuth2Session(client=client)
    ft = oauth.fetch_token(
        token_url='https://bitbucket.org/site/oauth2/access_token',
        client_id=key,
        client_secret=secret
    )
    at = ft['access_token']
    return {'Authorization': 'Bearer {}'.format(at)}


def bb_user_to_uuid(headers, user):
    if isinstance(user, dict):
        return user['uuid']
    if is_uuid(user):
        return user
    r = requests.get(
        url='{}/2.0/users/{}'.format(bb_api_root, user),
        headers=headers,
    )
    user_info = r.json()
    return user_info['uuid']


def is_uuid(arg):
    try:
        uuid = UUID(arg)
    except ValueError:
        return False
    return arg == uuid

import logging
import os
import urllib3

from seeq.sdk import *
from seeq.sdk.rest import ApiException

from . import _common, _config
from ._common import Status

from urllib3.connectionpool import MaxRetryError

client = None  # type: ApiClient
user = None  # type: UserOutputV1
https_verify_ssl = True
https_key_file = None
https_cert_file = None

AUTOMATIC_PROXY_DETECTION = '__auto__'


def login(username=None, password=None, *, url=None, directory='Seeq', ignore_ssl_errors=False,
          proxy=AUTOMATIC_PROXY_DETECTION, credentials_file=None, auth_token=None, quiet=False,
          status=None, auth_provider=None):
    """
    Establishes a connection with Seeq Server and logs in with a set of
    credentials. At least one set of credentials must be provided.
    Applicable credential sets are:
        - username + password + directory
        - credentials_file + directory
        - auth_token

    Parameters
    ----------
    username : str, optional
        Username for login purposes. See credentials_file argument for
        alternative.

    password : str, optional
        Password for login purposes. See credentials_file argument for
        alternative.

    url : str, default 'http://localhost:34216'
        Seeq Server url. You can copy this from your browser and cut off
        everything to the right of the port (if present).
        E.g. https://myseeqserver:34216

    directory : str, default 'Seeq'
        The authentication directory to use. You must be able to supply a
        username/password, so some passwordless Windows Authentication
        (NTLM) scenarios will not work. OpenID Connect is also not
        supported. If you need to use such authentication schemes, set up
        a Seeq Data Lab server.

    ignore_ssl_errors : bool, default False
        If True, SSL certificate validation errors are ignored. Use this
        if you're in a trusted network environment but Seeq Server's SSL
        certificate is not from a common root authority.

    proxy : str, default '__auto__'
        Specifies the proxy server to use for all requests. The default
        value is "__auto__", which examines the standard HTTP_PROXY and
        HTTPS_PROXY environment variables. If you specify None for this
        parameter, no proxy server will be used.

    credentials_file : str, optional
        Reads username and password from the specified file. If specified, the
        file should be plane text and contain two lines, the first line being
        the username, the second being the user's password.

    auth_token : str, optional
        Provide an authorization token directly from a browser session of Seeq
        Workbench.

    quiet : bool, default False
        If True, suppresses progress output.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    auth_provider : str, deprecated
        Use directory instead.
    """
    _common.validate_argument_types([
        (username, 'username', str),
        (password, 'password', str),
        (url, 'url', str),
        (directory, 'directory', str),
        (ignore_ssl_errors, 'ignore_ssl_errors', bool),
        (proxy, 'proxy', str),
        (credentials_file, 'credentials_file', str),
        (auth_token, 'auth_token', str),
        (quiet, 'quiet', bool),
        (status, 'status', _common.Status)
    ])

    status = Status.validate(status, quiet)

    if auth_provider is not None:
        raise RuntimeError('"auth_provider" argument has been renamed to "directory"')

    # Annoying warnings are printed to stderr if connections fail
    logging.getLogger("requests").setLevel(logging.FATAL)
    logging.getLogger("urllib3").setLevel(logging.FATAL)
    urllib3.disable_warnings()

    if url:
        _config.set_seeq_url(url)

    api_client_url = _config.get_api_url()

    cert_file = _config.get_seeq_cert_path()
    if os.path.exists(cert_file):
        Configuration().cert_file = cert_file
    key_file = _config.get_seeq_key_path()
    if os.path.exists(key_file):
        Configuration().key_file = key_file

    Configuration().verify_ssl = not ignore_ssl_errors

    if proxy == AUTOMATIC_PROXY_DETECTION:
        if api_client_url.startswith('https') and 'HTTPS_PROXY' in os.environ:
            Configuration().proxy = os.environ['HTTPS_PROXY']
        elif 'HTTP_PROXY' in os.environ:
            Configuration().proxy = os.environ['HTTP_PROXY']
    elif proxy is not None:
        Configuration().proxy = proxy

    global client, https_verify_ssl, https_key_file, https_cert_file
    client = ApiClient(api_client_url)
    https_verify_ssl = not ignore_ssl_errors
    https_key_file = key_file
    https_cert_file = cert_file

    if auth_token:
        if username or password or credentials_file:
            raise ValueError('username, password and/or credentials_file cannot be provided along with auth_token')

        client.auth_token = auth_token
    else:
        auth_api = AuthApi(client)
        auth_input = AuthInputV1()

        if credentials_file:
            if username is not None or password is not None:
                raise ValueError('If credentials_file is specified, username and password must be None')

            try:
                with open(credentials_file) as f:
                    lines = f.readlines()
            except Exception as e:
                raise RuntimeError('Could not read credentials_file "%s": %s' % (credentials_file, e))

            if len(lines) < 2:
                raise RuntimeError('credentials_file "%s" must have two lines: username then password')

            username = lines[0].strip()
            password = lines[1].strip()

        if not username or not password:
            raise ValueError('Both username and password must be supplied')

        auth_input.username = username
        auth_input.password = password

        status.update('Logging in to <strong>%s</strong> as <strong>%s</strong>' % (
            api_client_url, username), Status.RUNNING)

        directories = dict()
        try:
            auth_providers_output = auth_api.get_auth_providers()  # type: AuthProvidersOutputV1
        except MaxRetryError as e:
            raise RuntimeError(
                '"%s" could not be reached. Is the server or network down?\n%s' % (api_client_url, e))

        for datasource_output in auth_providers_output.auth_providers:  # type: DatasourceOutputV1
            directories[datasource_output.name] = datasource_output

        if directory not in directories:
            raise RuntimeError('directory "%s" not recognized. Possible directory(s) for this server: %s' %
                               (directory, ', '.join(directories.keys())))

        datasource_output = directories[directory]
        auth_input.auth_provider_class = datasource_output.datasource_class
        auth_input.auth_provider_id = datasource_output.datasource_id

        try:
            auth_api.login(body=auth_input)
        except ApiException as e:
            if e.status == 401:
                raise RuntimeError(
                    '"%s" could not be logged in with supplied credentials, check username and password.' %
                    auth_input.username)
            else:
                raise
        except MaxRetryError as e:
            raise RuntimeError(
                '"%s" could not be reached. Is the server or network down?\n%s' % (api_client_url, e))
        except Exception as e:
            raise RuntimeError('Could not connect to Seeq"s API at %s with login "%s".\n%s' % (api_client_url,
                                                                                               auth_input.username, e))

    users_api = UsersApi(client)

    global user
    user = users_api.get_me()  # type: UserOutputV1

    user_string = user.username
    user_profile = ''
    if user.first_name:
        user_profile = user.first_name
    if user.last_name:
        user_profile += ' ' + user.last_name
    if user.is_admin:
        user_profile += ' [Admin]'
    if len(user_profile) > 0:
        user_string += ' (%s)' % user_profile.strip()

    status.update('Logged in to <strong>%s</strong> successfully as <strong>%s</strong>' % (
        api_client_url, user_string), Status.SUCCESS)


def logout(quiet=False, status=None):
    """
    Logs you out of your current session.

    Parameters
    ----------

    quiet : bool, default False
        If True, suppresses progress output.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    """

    status = Status.validate(status, quiet)
    global client  # type: ApiClient
    if client is None:
        status.update('No action taken because you are not currently logged in.', Status.FAILURE)

    auth_api = AuthApi(client)
    auth_api.logout()

    client.logout()

    status.update('Logged out.', Status.SUCCESS)


def find_user(query):
    """
    Finds a user by using Seeq's user/group autocomplete functionality. Must result in exactly one match or a
    RuntimeError is raised.
    :param query: A user/group fragment to use for the search
    :return: The identity of the matching user.
    :rtype: UserOutputV1
    """
    users_api = UsersApi(client)

    if _common.is_guid(query):
        user_id = query
    else:
        identity_preview_list = users_api.autocomplete_users_and_groups(query=query)  # type: IdentityPreviewListV1
        if len(identity_preview_list.items) == 0:
            raise RuntimeError('User "%s" not found' % query)
        if len(identity_preview_list.items) > 1:
            raise RuntimeError('Multiple users found that match "%s":\n%s' % (
                query, '\n'.join([('%s (%s)' % (u.username, u.id)) for u in identity_preview_list.items])))

        user_id = identity_preview_list.items[0].id

    return users_api.get_user(id=user_id)

# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

# See the Rebrickable API documentation at https://rebrickable.com/api/v3/docs/

from . import config
from .request import request, assert_user_token


def get_token(username, password, api_key=None):
    """
    Generates user token to be used for authorizing actions.
    
    Args:
        username: str
            Rebrickable registration username or email.
        
        password: str
            Rebrickable registration password.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'username': username,
        'password': password,
        'key': api_key}
    
    path = config.API_USERS_URL + "_token/"
    
    return request(path, parameters, post=True)


def get_build(set_id, user_token=None, api_key=None):
    """
    Finds out how many parts the user needs to build specific set.
    
    Args:
        set_id: str or int
            Rebrickable set ID.
        
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    if '-' not in str(set_id):
        set_id = "%s-1" % set_id
    
    parameters = {'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/build/%s/" % (user_token, set_id)
    
    return request(path, parameters)


def get_lost_elements(page=None, page_size=None, ordering=None, user_token=None, api_key=None):
    """
    Gets details for all user's lost elements.
    
    Args:
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/lost_parts/" % user_token
    
    return request(path, parameters)


def get_partlist(list_id, user_token=None, api_key=None):
    """
    Gets details about specific user's part list.
    
    Args:
        list_id: str or int
            Rebrickable part list ID.
        
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/partlists/%s/" % (user_token, list_id)
    
    return request(path, parameters)


def get_partlists(page=None, page_size=None, ordering=None, user_token=None, api_key=None):
    """
    Gets details for all available user's parts lists.
    
    Args:
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/partlists/" % user_token
    
    return request(path, parameters)


def get_partlist_elements(list_id, page=None, page_size=None, ordering=None, user_token=None, api_key=None):
    """
    Gets details about all elements of specific user's part list.
    
    Args:
        list_id: str or int
            Rebrickable part list ID.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/partlists/%s/parts/" % (user_token, list_id)
    
    return request(path, parameters)


def get_partlist_element(list_id, part_id, color_id, user_token=None, api_key=None):
    """
    Gets details about specific part/color combination in user's part list.
    
    Args:
        list_id: str or int
            Rebrickable part list ID.
        
        part_id: str or int
            Rebrickable part ID.
        
        color_id: str or int
            Rebrickable color ID.
        
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/partlists/%s/parts/%s/%s" % (user_token, list_id, part_id, color_id)
    
    return request(path, parameters)


def get_parts(search=None, part_id=None, part_cat_id=None, color_id=None, page=None, page_size=None, ordering=None, user_token=None, api_key=None):
    """
    Gets details for all available user's parts with optional filters.
    
    Args:
        search: str, int or None
            Search term e.g. part ID or name.
        
        part_id: str, int or None
            Rebrickable part ID.
        
        part_cat_id: str, int or None
            Rebrickable category ID.
        
        color_id: str, int or None
            Rebrickable color ID.
        
        page: int or None
            A page number within the paginated result set.
        
        page_size: int or None
            Number of results to return per page.
        
        ordering: str or None
            Specifies the field to use for results ordering.
        
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {
        'search': search,
        'part_num': part_id,
        'part_cat_id': part_cat_id,
        'color_id': color_id,
        'page': page,
        'page_size': page_size,
        'ordering': ordering,
        'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/parts/" % user_token
    
    return request(path, parameters)


def get_profile(user_token=None, api_key=None):
    """
    Gets details about the user.
    
    Args:
        user_token: str or None
            Rebrickable user token. If set to None the one set by
            rebrick.init() is used.
        
        api_key: str or None
            Rebrickable API access key. If set to None the one set by
            rebrick.init() is used.
    
    Returns:
        http.client.HTTPResponse
            Server response.
    """
    
    parameters = {'key': api_key}
    
    user_token = assert_user_token(user_token)
    path = config.API_USERS_URL + "%s/profile/" % user_token
    
    return request(path, parameters)

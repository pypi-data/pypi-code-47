# Copyright (c) 2019 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import qumulo.lib.request as request

# Statically defined roles
ADMINISTRATOR_ROLE_NAME = 'Administrators'
ADMIN_OBSERVER_ROLE_NAME = 'Observers'

@request.request
def list_roles(conninfo, credentials):
    method = 'GET'
    uri = '/v1/auth/roles/'
    return request.rest_request(conninfo, credentials, method, uri)

@request.request
def list_role(conninfo, credentials, role_name):
    method = 'GET'
    uri = '/v1/auth/roles/{}'.format(role_name)
    return request.rest_request(conninfo, credentials, method, uri)

@request.request
def add_member(conninfo, credentials, role_name, **attrs):
    '''
    Add a member to role @p role_name. At least one argument other
    than @p domain must be specified. If multiple are specified, they must
    represent the same identity.
    @p role_name The name of the role being assigned to.
    @p domain The domain the identity is in.  LOCAL_DOMAIN, WORLD_DOMAIN,
        POSIX_USER_DOMAIN, POSIX_GROUP_DOMAIN, or AD_DOMAIN.
    @p auth_id The identifier used internally by qsfs.
    @p uid A posix UID
    @p gid A posix GID
    @p sid A SID.
    @p name A name of a cluster-local, AD, or LDAP user.  May be an unqualified
        login name, qualified with netbios name (e.g. DOMAIN\user), a
        universal principal name (e.g. user@domain.example.com), or an LDAP
        distinguished name (e.g CN=John Doe,OU=users,DC=example,DC=com).
    '''
    method = 'POST'
    uri = '/v1/auth/roles/{}/add-member'.format(role_name)
    return request.rest_request(conninfo, credentials, method, uri, body=attrs)

@request.request
def remove_member(conninfo, credentials, role_name, **attrs):
    '''
    Remove a member from role @p role_name. At least one argument other
    than @p domain must be specified. If multiple are specified, they must
    represent the same identity.
    @p role_name The name of the role being assigned to.
    @p domain The domain the identity is in.  LOCAL_DOMAIN, WORLD_DOMAIN,
        POSIX_USER_DOMAIN, POSIX_GROUP_DOMAIN, or AD_DOMAIN.
    @p auth_id The identifier used internally by qsfs.
    @p uid A posix UID
    @p gid A posix GID
    @p sid A SID.
    @p name A name of a cluster-local, AD, or LDAP user.  May be an unqualified
        login name, qualified with netbios name (e.g. DOMAIN\user), a
        universal principal name (e.g. user@domain.example.com), or an LDAP
        distinguished name (e.g CN=John Doe,OU=users,DC=example,DC=com).
    '''
    method = 'POST'
    uri = '/v1/auth/roles/{}/remove-member'.format(role_name)
    return request.rest_request(conninfo, credentials, method, uri, body=attrs)

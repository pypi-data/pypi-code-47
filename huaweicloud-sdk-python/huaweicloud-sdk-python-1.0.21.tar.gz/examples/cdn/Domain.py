# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

import os
import time
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE',
                      'xxxxxxxxxxx')  # CDN API url,example:https://cdn.myhuaweicloud.com/v1.0/

# token Auth
# username = "xxxxxxxxxxx"  # IAM User Name
# password = "xxxxxxxxxxx"  # IAM User Password
# projectId = "xxxxxxxxxxx"  # Project ID of cn-north-1
# userDomainId = "xxxxxxxxxxx"  # Account ID
# auth_url = "xxxxxxxxxxx"  # IAM auth url,example: https://iam.myhuaweicloud.com/v3
#
# conn = connection.Connection(
#     auth_url=auth_url,
#     user_domain_id=userDomainId,
#     project_id=projectId,
#     username=username,
#     password=password
# )


# AKSK Auth
projectId = "xxxxxxxxxxx"  # Project ID of cn-north-1
cloud = "xxxxxxxxxxx"  # cdn use: cloud = "myhuaweicloud.com"
region = "xxxxxxxxxxx"  # example: region = "cn-north-1"
AK = "xxxxxxxxxxx"
SK = "xxxxxxxxxxx"

conn = connection.Connection(
    project_id=projectId,
    cloud=cloud,
    region=region,
    ak=AK,
    sk=SK)


def domain_create(domain_name):
    print('Create a new acceleration domain name: ')
    attrs = {
        'domain_name': domain_name,
        'business_type': 'web',
        'sources': [
            {
                'ip_or_domain': 'X.X.X.X',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1  # 1 means this source is active
            }
        ]
    }
    domain = conn.cdn.create_domain(**attrs)
    print(domain)


def domain_create_by_enterprise_project_id(domain_name, enterprise_project_id):
    print('Create a new acceleration domain name: ')
    attrs = {
        'domain_name': domain_name,
        'business_type': 'web',
        'sources': [
            {
                'ip_or_domain': 'X.X.X.X',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1  # 1 means this source is active
            }
        ],
        'enterprise_project_id': enterprise_project_id
    }
    domain = conn.cdn.create_domain(**attrs)
    print(domain)


def domains_query():
    print('List all domains:')
    for domain in conn.cdn.domains():
        print(domain)

    # Also support filtering by some attributes
    print('List all domains in "online" status: ')
    for domain in conn.cdn.domains(domain_status='online'):
        print(domain)

    print('List all domains of type "web": ')
    for domain in conn.cdn.domains(business_type='web'):
        print(domain)

    # You can list domains by page.
    print('List domains by page: ')
    for domain in conn.cdn.domains(page_size=2, page_number=1):
        print(domain)


def domains_query_by_enterprise_project_id(_enterprise_project_id):
    print('List all domains:')
    for domain in conn.cdn.domains(enterprise_project_id='ALL'):
        print(domain)

    # Also support filtering by some attributes
    print('List domains by enterprise_project_id in "online" status: ')
    for domain in conn.cdn.domains(enterprise_project_id=_enterprise_project_id, domain_status='online'):
        print(domain)

    print('List all domains of type "web": ')
    for domain in conn.cdn.domains(enterprise_project_id='ALL', business_type='web'):
        print(domain)

    # You can list domains by page.
    print('List domains by page: ')
    for domain in conn.cdn.domains(enterprise_project_id='ALL', page_size=10, page_number=1):
        print(domain)


def domain_query_detail(domain_id):
    print('Get the domain detail:')
    domain = conn.cdn.get_domain(domain_id)
    print(domain)


def domain_query_detail_by_enterprise_project_id(domain_id, enterprise_project_id='ALL'):
    print('Get the domain detail:')
    domain = conn.cdn.get_domain_detail_by_enterprise_project_id(domain_id, enterprise_project_id)
    print(domain)
    print(domain.sources)


def domain_disable(domain_id):
    print('Delete the domain: ')
    conn.cdn.disable_domain(domain_id)


def domain_disable_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('Disable the domain: ')
    conn.cdn.disable_domain_by_enterprise_project_id(domain_id, enterprise_project_id)


def domain_delete(domain_id):
    print('Deleted the domain.')
    conn.cdn.delete_domain(domain_id)


def domain_delete_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('Delete the domain: ')
    conn.cdn.delete_domain_by_enterprise_project_id(domain_id, enterprise_project_id)


def domain_enable(domain_id):
    print('enable the domain: ')
    # Enable the domain
    conn.cdn.enable_domain(domain_id)


def domain_enable_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('enable the domain: ')
    # Enable the domain
    conn.cdn.enable_domain_by_enterprise_project_id(domain_id, enterprise_project_id)


def get_domain_origin_host(domain_id):
    print('get domain origin host: ')
    domain = conn.cdn.get_domain_origin_host(domain_id)
    print(domain)


def get_domain_origin_host_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('get domain origin host: ')
    domain = conn.cdn.get_domain_origin_host_by_enterprise_project_id(domain_id, enterprise_project_id)
    print(domain)


def set_domain_origin_host(domain_id):
    print('set domain origin host: ')
    attrs = {
        'origin_host_type': 'accelerate',
        'customize_domain': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_origin_host(domain_id, **attrs)


def set_domain_origin_host_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('set domain origin host: ')
    attrs = {
        'origin_host_type': 'accelerate',
        'customize_domain': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_origin_host_by_enterprise_project_id(domain_id, enterprise_project_id, **attrs)


def get_domain_referer(domain_id):
    print('get domain referer:')
    domain = conn.cdn.get_domain_referer(domain_id)
    print(domain)


def get_domain_referer_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('get domain referer:')
    domain = conn.cdn.get_domain_referer_by_enterprise_project_id(domain_id, enterprise_project_id)
    print(domain)


def set_domain_referer(domain_id):
    print('set domain referer:')
    attrs = {
        'referer_type': 1,
        'referer_list': 'xxxxxxxxxxx',
        'include_empty': False
    }
    conn.cdn.set_domain_referer(domain_id, **attrs)


def set_domain_referer_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('set domain referer:')
    attrs = {
        'referer_type': 1,
        'referer_list': 'xxxxxxxxxxx',
        'include_empty': False
    }
    conn.cdn.set_domain_referer_by_enterprise_project_id(domain_id, enterprise_project_id, **attrs)


def get_domain_cache_rules(domain_id):
    print('get domain cache rules:')
    domain = conn.cdn.get_domain_cache_rules(domain_id)
    print(domain)


def get_domain_cache_rules_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('get domain cache rules:')
    domain = conn.cdn.get_domain_cache_rules_by_enterprise_project_id(domain_id, enterprise_project_id)
    print(domain)


def set_domain_cache_rules(domain_id):
    print('set domain cache rules:')
    attrs = {
        'ignore_url_parameter': False,
        'rules': [
            {
                'rule_type': 1,
                'content': '.jpg;.png',
                'ttl': 21,
                'ttl_type': 3,
                'priority': 1
            }
        ]
    }
    conn.cdn.set_domain_cache_rules(domain_id, **attrs)


def set_domain_cache_rules_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('set domain cache rules:')
    attrs = {
        'ignore_url_parameter': False,
        'rules': [
            {
                'rule_type': 1,
                'content': '.jpg;.png;.zip',
                'ttl': 22,
                'ttl_type': 3,
                'priority': 1
            }
        ]
    }
    conn.cdn.set_domain_cache_rules_by_enterprise_project_id(domain_id, enterprise_project_id, **attrs)


def get_domain_https(domain_id):
    print('get domain https:')
    domain = conn.cdn.get_domain_https(domain_id)
    print(domain)


def get_domain_https_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('get domain https:')
    domain = conn.cdn.get_domain_https_by_enterprise_project_id(domain_id, enterprise_project_id)
    print(domain)


def set_domain_https(domain_id):
    print('set domain https:')
    attrs = {
        'force_redirect_https': 0,
        'https_status': 2,
        'cert_name': 'xxxxxxxxxxx',
        'certificate': 'xxxxxxxxxxx',
        'private_key': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_https(domain_id, **attrs)


def set_domain_https_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('set domain https:')
    attrs = {
        'force_redirect_https': 0,
        'https_status': 2,
        'cert_name': 'xxxxxxxxxxx',
        'certificate': 'xxxxxxxxxxx',
        'private_key': 'xxxxxxxxxxx'
    }
    conn.cdn.set_domain_https_by_enterprise_project_id(domain_id, enterprise_project_id, **attrs)


def set_domain_sources(domain_id):
    print('set domain sources: ')
    attrs = {
        'sources': [
            {
                'ip_or_domain': 'xxxxxxxxxxx',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1
            }
        ]
    }
    conn.cdn.set_domain_sources(domain_id, **attrs)


def set_domain_sources_by_enterprise_project_id(domain_id, enterprise_project_id):
    print('set domain sources: ')
    attrs = {
        'sources': [
            {
                'ip_or_domain': 'xxxxxxxxxxx',
                'origin_type': 'xxxxxxxxxxx',
                'active_standby': 1
            }
        ]
    }
    conn.cdn.set_domain_sources_by_enterprise_project_id(domain_id, enterprise_project_id, **attrs)


if __name__ == "__main__":
    domain_name_sample = 'xxxxxxxxxxx'
    domain_id_sample = 'xxxxxxxxxxx'
    enterprise_project_id_sample = 'xxxxxxxxxxx'

    domain_create(domain_name_sample)

    domains_query()

    domain_query_detail(domain_id_sample)

    domain_disable(domain_id_sample)

    domain_delete(domain_id_sample)

    domain_enable(domain_id_sample)

    get_domain_origin_host(domain_id_sample)

    set_domain_origin_host(domain_id_sample)

    get_domain_referer(domain_id_sample)

    set_domain_referer(domain_id_sample)

    get_domain_cache_rules(domain_id_sample)

    set_domain_cache_rules(domain_id_sample)

    get_domain_https(domain_id_sample)

    set_domain_https(domain_id_sample)

    set_domain_sources(domain_id_sample)

    domain_create_by_enterprise_project_id(domain_name_sample, enterprise_project_id_sample)

    domains_query_by_enterprise_project_id(enterprise_project_id_sample)

    domain_query_detail_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    domain_disable_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    domain_delete_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    domain_enable_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    get_domain_origin_host_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    set_domain_origin_host_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    get_domain_referer_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    set_domain_referer_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    get_domain_cache_rules_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    set_domain_cache_rules_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    get_domain_https_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    set_domain_https_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

    set_domain_sources_by_enterprise_project_id(domain_id_sample, enterprise_project_id_sample)

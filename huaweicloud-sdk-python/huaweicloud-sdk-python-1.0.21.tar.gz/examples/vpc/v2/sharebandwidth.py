# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
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

from openstack import connection

auth_url = '******'
userDomainId = '******'
projectId = '******'
username = '******'
password = os.getenv('get_secret_code')

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


# Create a BandWidth
def create_sharebandwidth(_conn):
    data = {
        "name": "xxxxxx",
        "size": 8
    }
    obj = _conn.vpc.create_sharebandwidth(**data)
    print(obj)


# Batch Create BandWidth
def create_batch_sharebandwidth(_conn):
    data = {
        "name": "xxxxxx",
        "size": 9,
        "count": 2
    }
    obj = _conn.vpc.create_batch_sharebandwidth(**data)
    print(obj)


# Delete a BandWidth
def delete_sharebandwidth(_conn):
    bandwidth_id = 'xxxxxx'
    obj = _conn.vpc.delete_sharebandwidth(bandwidth_id)
    print(obj)


# Insert ip into BandWidth
def insert_ip_to_bandwidth(_conn):
    bandwidth_id = 'xxxxxx'
    data = {
        "publicip_info": [
            {
                "publicip_id": "xxxxxx"
            },
            {
                "publicip_id": "xxxxxx"
            }
        ]
    }
    obj = _conn.vpc.insert_ip_to_bandwidth(bandwidth_id, **data)
    print(obj)


# Remove ip into BandWidth
def remove_ip_from_bandwidth(_conn):
    bandwidth_id = 'xxxxxx'
    data = {
        "publicip_info": [
            {
                "publicip_id": "xxxxxx"
            },
            {
                "publicip_id": "xxxxxx"
            }
        ],
        "charge_mode": "bandwidth",
        "size": 12
    }
    obj = _conn.vpc.remove_ip_from_bandwidth(bandwidth_id, **data)
    print(obj)


# Update a BandWidth
def modify_bandwidth(_conn):
    bandwidth_id = 'xxxxxx'
    data = {
        "bandwidth":
            {
                "name": "xxxxxx",
                "size": 100
            },
        "extendParam":
            {
                "is_auto_pay": "false"
            }
    }

    obj = conn.vpc.update_bandwidth_ext(bandwidth_id=bandwidth_id, **data)
    print(obj)


if __name__ == '__main__':
    create_sharebandwidth(conn)
    create_batch_sharebandwidth(conn)
    delete_sharebandwidth(conn)
    insert_ip_to_bandwidth(conn)
    remove_ip_from_bandwidth(conn)
    modify_bandwidth(conn)

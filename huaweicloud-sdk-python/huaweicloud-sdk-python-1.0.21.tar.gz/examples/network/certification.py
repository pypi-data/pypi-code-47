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

import sys
from openstack import connection
from openstack import utils

# utils.enable_logging(debug=True, stream=sys.stdout)

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxx"
userDomainId = "xxxxxxxxxx"
auth_url = "xxxxxxxxxx"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)


def test_get_all_certificate():
    cers = list(conn.network.certificates())
    for cer in cers:
        print(cer)


def test_get_certificate(cf_id):
    print(conn.network.get_certificate(cf_id))


def test_create_certificate():
    cf = {
        'name': 'create-certificate-test',
        'description': 'this is a test',
        'type': 'server',
        'domain': 'www.elb.com',
        'private_key': '''-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwZ5UJULAjWr7p6FVwGRQRjFN2s8tZ/6LC3X82fajpVsYqF1x
qEuUDndDXVD09E4u83MS6HO6a3bIVQDp6/klnYldiE6Vp8HH5BSKaCWKVg8lGWg1
UM9wZFnlryi14KgmpIFmcu9nA8yV/6MZAe6RSDmb3iyNBmiZ8aZhGw2pI1YwR+15
MVqFFGB+7ExkziROi7L8CFCyCezK2/oOOvQsH1dzQ8z1JXWdg8/9Zx7Ktvgwu5PQ
M3cJtSHX6iBPOkMU8Z8TugLlTqQXKZOEgwajwvQ5mf2DPkVgM08XAgaLJcLigwD5
13koAdtJd5v+9irw+5LAuO3JclqwTvwy7u/YwwIDAQABAoIBACU9S5fjD9/jTMXA
DRs08A+gGgZUxLn0xk+NAPX3LyB1tfdkCaFB8BccLzO6h3KZuwQOBPv6jkdvEDbx
Nwyw3eA/9GJsIvKiHc0rejdvyPymaw9I8MA7NbXHaJrY7KpqDQyk6sx+aUTcy5jg
iMXLWdwXYHhJ/1HVOo603oZyiS6HZeYU089NDUcX+1SJi3e5Ke0gPVXEqCq1O11/
rh24bMxnwZo4PKBWdcMBN5Zf/4ij9vrZE+fFzW7vGBO48A5lvZxWU2U5t/OZQRtN
1uLOHmMFa0FIF2aWbTVfwdUWAFsvAOkHj9VV8BXOUwKOUuEktdkfAlvrxmsFrO/H
yDeYYPkCgYEA/S55CBbR0sMXpSZ56uRn8JHApZJhgkgvYr+FqDlJq/e92nAzf01P
RoEBUajwrnf1ycevN/SDfbtWzq2XJGqhWdJmtpO16b7KBsC6BdRcH6dnOYh31jgA
vABMIP3wzI4zSVTyxRE8LDuboytF1mSCeV5tHYPQTZNwrplDnLQhywcCgYEAw8Yc
Uk/eiFr3hfH/ZohMfV5p82Qp7DNIGRzw8YtVG/3+vNXrAXW1VhugNhQY6L+zLtJC
aKn84ooup0m3YCg0hvINqJuvzfsuzQgtjTXyaE0cEwsjUusOmiuj09vVx/3U7siK
Hdjd2ICPCvQ6Q8tdi8jV320gMs05AtaBkZdsiWUCgYEAtLw4Kk4f+xTKDFsrLUNf
75wcqhWVBiwBp7yQ7UX4EYsJPKZcHMRTk0EEcAbpyaJZE3I44vjp5ReXIHNLMfPs
uvI34J4Rfot0LN3n7cFrAi2+wpNo+MOBwrNzpRmijGP2uKKrq4JiMjFbKV/6utGF
Up7VxfwS904JYpqGaZctiIECgYA1A6nZtF0riY6ry/uAdXpZHL8ONNqRZtWoT0kD
79otSVu5ISiRbaGcXsDExC52oKrSDAgFtbqQUiEOFg09UcXfoR6HwRkba2CiDwve
yHQLQI5Qrdxz8Mk0gIrNrSM4FAmcW9vi9z4kCbQyoC5C+4gqeUlJRpDIkQBWP2Y4
2ct/bQKBgHv8qCsQTZphOxc31BJPa2xVhuv18cEU3XLUrVfUZ/1f43JhLp7gynS2
ep++LKUi9D0VGXY8bqvfJjbECoCeu85vl8NpCXwe/LoVoIn+7KaVIZMwqoGMfgNl
nEqm7HWkNxHhf8A6En/IjleuddS1sf9e/x+TJN1Xhnt9W6pe7Fk1
-----END RSA PRIVATE KEY-----''',
        'certificate': '''-----BEGIN CERTIFICATE-----
MIIDpTCCAo2gAwIBAgIJAKdmmOBYnFvoMA0GCSqGSIb3DQEBCwUAMGkxCzAJBgNV
BAYTAnh4MQswCQYDVQQIDAJ4eDELMAkGA1UEBwwCeHgxCzAJBgNVBAoMAnh4MQsw
CQYDVQQLDAJ4eDELMAkGA1UEAwwCeHgxGTAXBgkqhkiG9w0BCQEWCnh4QDE2My5j
b20wHhcNMTcxMjA0MDM0MjQ5WhcNMjAxMjAzMDM0MjQ5WjBpMQswCQYDVQQGEwJ4
eDELMAkGA1UECAwCeHgxCzAJBgNVBAcMAnh4MQswCQYDVQQKDAJ4eDELMAkGA1UE
CwwCeHgxCzAJBgNVBAMMAnh4MRkwFwYJKoZIhvcNAQkBFgp4eEAxNjMuY29tMIIB
IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwZ5UJULAjWr7p6FVwGRQRjFN
2s8tZ/6LC3X82fajpVsYqF1xqEuUDndDXVD09E4u83MS6HO6a3bIVQDp6/klnYld
iE6Vp8HH5BSKaCWKVg8lGWg1UM9wZFnlryi14KgmpIFmcu9nA8yV/6MZAe6RSDmb
3iyNBmiZ8aZhGw2pI1YwR+15MVqFFGB+7ExkziROi7L8CFCyCezK2/oOOvQsH1dz
Q8z1JXWdg8/9Zx7Ktvgwu5PQM3cJtSHX6iBPOkMU8Z8TugLlTqQXKZOEgwajwvQ5
mf2DPkVgM08XAgaLJcLigwD513koAdtJd5v+9irw+5LAuO3JclqwTvwy7u/YwwID
AQABo1AwTjAdBgNVHQ4EFgQUo5A2tIu+bcUfvGTD7wmEkhXKFjcwHwYDVR0jBBgw
FoAUo5A2tIu+bcUfvGTD7wmEkhXKFjcwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0B
AQsFAAOCAQEAWJ2rS6Mvlqk3GfEpboezx2J3X7l1z8Sxoqg6ntwB+rezvK3mc9H0
83qcVeUcoH+0A0lSHyFN4FvRQL6X1hEheHarYwJK4agb231vb5erasuGO463eYEG
r4SfTuOm7SyiV2xxbaBKrXJtpBp4WLL/s+LF+nklKjaOxkmxUX0sM4CTA7uFJypY
c8Tdr8lDDNqoUtMD8BrUCJi+7lmMXRcC3Qi3oZJW76ja+kZA5mKVFPd1ATih8TbA
i34R7EQDtFeiSvBdeKRsPp8c0KT8H1B4lXNkkCQs2WX5p4lm99+ZtLD4glw8x6Ic
i1YhgnQbn5E0hz55OLu5jvOkKQjPCW+8Kg==
-----END CERTIFICATE-----'''
    }
    certificate = conn.network.create_certificate(**cf)
    return certificate


def test_update_certificate(cf_id):
    cf = {'name' : 'update-cf-test'}
    cf_new = conn.network.update_certificate(cf_id, **cf)
    return cf_new


def test_delete_certificate(cf_id):
    conn.network.delete_certificate(cf_id)


if __name__ == "__main__":
    cf = test_create_certificate()
    cf_new = test_update_certificate(cf.id)
    test_get_certificate(cf_new.id)
    test_get_all_certificate()
    test_delete_certificate(cf_new.id)
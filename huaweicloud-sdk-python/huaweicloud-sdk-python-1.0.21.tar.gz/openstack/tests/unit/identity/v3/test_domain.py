# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import testtools

from openstack.identity.v3 import domain

IDENTIFIER = 'IDENTIFIER'
EXAMPLE = {
    'description': '1',
    'enabled': True,
    'id': IDENTIFIER,
    'links': {'self': 'http://example.com/identity/v3/domains/id'},
    'name': '4',
}


class TestDomain(testtools.TestCase):

    def test_basic(self):
        sot = domain.Domain()
        self.assertEqual('domain', sot.resource_key)
        self.assertEqual('domains', sot.resources_key)
        self.assertEqual('/domains', sot.base_path)
        self.assertEqual('identity', sot.service.service_type)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_get)
        self.assertTrue(sot.allow_update)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)
        self.assertTrue(sot.patch_update)

    def test_make_it(self):
        sot = domain.Domain(**EXAMPLE)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertTrue(sot.is_enabled)
        self.assertEqual(EXAMPLE['id'], sot.id)
        self.assertEqual(EXAMPLE['links'], sot.links)
        self.assertEqual(EXAMPLE['name'], sot.name)

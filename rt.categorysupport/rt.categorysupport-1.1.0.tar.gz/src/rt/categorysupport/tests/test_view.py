# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from rt.categorysupport.testing import RT_CATEGORYSUPPORT_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class TestView(unittest.TestCase):
    """Test taxonomies-info view"""

    layer = RT_CATEGORYSUPPORT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.folder = api.content.create(
            container=self.portal, type='Folder', title='Folder'
        )
        self.doc1 = api.content.create(
            container=self.folder,
            type='Document',
            title='First Document',
            subject=['subj1', 'subj2'],
            taxonomies=['taxonomy1'],
        )
        self.doc2 = api.content.create(
            container=self.folder,
            type='Document',
            title='Second Document',
            taxonomies=['taxonomy1'],
        )
        self.doc3 = api.content.create(
            container=self.folder,
            type='Document',
            title='Third Document',
            subject=['subj1'],
            taxonomies=['taxonomy1', 'taxonomy2'],
        )
        self.view = api.content.get_view(
            name='taxonomies-info', context=self.folder, request=self.request
        )

    def test_get_taxonomies(self):
        taxonomies = self.view.get_taxonomies()
        self.assertIn('taxonomy1', taxonomies)
        self.assertIn('taxonomy2', taxonomies)
        self.assertEqual(taxonomies['taxonomy1'], 3)
        self.assertEqual(taxonomies['taxonomy2'], 1)

    def test_get_subjects(self):
        subjects = self.view.get_subjects()
        self.assertIn('subj1', subjects)
        self.assertIn('subj2', subjects)
        self.assertEqual(subjects['subj1'], 2)
        self.assertEqual(subjects['subj2'], 1)

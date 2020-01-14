# Imports ##############################################################################################################
import os

from django.test import TestCase

from pixelforest_drf.countries.models import Region, SubRegion, Country


# Tests ################################################################################################################

class TestMigrations(TestCase):
    """
    Test the data migration adding the necessary Countries, SubRegions and Regions
    """
    def test_nbr_obj(self):
        self.assertEqual(Region.objects.count(), 5)
        self.assertEqual(SubRegion.objects.count(), 17)
        self.assertEqual(Country.objects.count(), 249)

    def test_image_upload(self):
        fr = Country.objects.get(name="France")
        self.assertTrue(os.path.isfile(fr.flag.file.name))

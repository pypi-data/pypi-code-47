# Imports ##############################################################################################################
from django.core.exceptions import ValidationError
from django.db.models.constraints import UniqueConstraint
from django.test import TestCase

from ..models import Region, SubRegion, Country


# Tests ################################################################################################################

class SubRegionTestCase(TestCase):
    """
    Tests on the SubRegion Model & Lock of the uniqueness constraints.
    """
    def test_uniqueness_constraints(self):
        # Constraint on sub_Region + name
        self.assertEqual(len([c for c in SubRegion._meta.constraints
                              if isinstance(c, UniqueConstraint) and c.fields == ('region', 'name')]), 1)
        # Constraint on sub_Region + abbreviation
        self.assertEqual(len([c for c in SubRegion._meta.constraints
                              if isinstance(c, UniqueConstraint) and c.fields == ('region', 'abbreviation')]), 1)

    def test_cannot_add_empty_subregion(self):
        with self.assertRaises(ValidationError):
            SubRegion.objects.create(name=None)

    def test_cannot_add_existing_subregion(self):
        SubRegion.objects.create(name="Test")
        with self.assertRaises(ValidationError):
            SubRegion.objects.create(name="Test")

    def test_subregion_by_default_inactive(self):
        sub_region = SubRegion.objects.create(name="SubRegionName")
        self.assertFalse(sub_region.is_active)


class TestRegionModel(TestCase):
    """
    Tests on the Region Model & Lock of the uniqueness constraints.
    """
    def test_uniqueness(self):
        # Constraint on Region name
        self.assertEqual(len([c for c in Region._meta.constraints
                              if isinstance(c, UniqueConstraint) and c.fields == ('name',)]), 1)
        # Constraint on Region abbreviation
        self.assertEqual(len([c for c in Region._meta.constraints
                              if isinstance(c, UniqueConstraint) and c.fields == ('abbreviation',)]), 1)

    def test_cannot_add_empty_region(self):
        with self.assertRaises(ValidationError):
            Region.objects.create(name=None)

    def test_cannot_add_existing_region(self):
        Region.objects.create(name="Test")
        with self.assertRaises(ValidationError):
            Region.objects.create(name="Test")

    def test_region_by_default_inactive(self):
        region = Region.objects.create(name="RegionName")
        self.assertFalse(region.is_active)


class TestCountryModel(TestCase):
    """
    Tests on the Country Model & Lock of the uniqueness constraints.
    """
    def test_uniqueness_constraints(self):
        self.assertEqual(len([c for c in Country._meta.constraints
                              if isinstance(c, UniqueConstraint) and c.fields == ('sub_region', 'name')]), 1)

    def test_cannot_add_empty_country(self):
        with self.assertRaises(ValidationError):
            Country.objects.create(name=None)

    def test_cannot_change_country_name(self):
        c = Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)
        with self.assertRaisesMessage(ValidationError, "{'name': ['This field cannot be modified']}"):
            c.name = "This is another name"
            c.save()

    def test_cannot_change_country_iso2(self):
        c = Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)
        with self.assertRaisesMessage(ValidationError, "{'iso_alpha_2': ['This field cannot be modified']}"):
            c.iso_alpha_2 = "YY"
            c.save()

    def test_cannot_change_country_iso3(self):
        c = Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)
        with self.assertRaisesMessage(ValidationError, "{'iso_alpha_3': ['This field cannot be modified']}"):
            c.iso_alpha_3 = "YYY"
            c.save()

    def test_cannot_change_country_isonum(self):
        c = Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)
        with self.assertRaisesMessage(ValidationError, "{'iso_num': ['This field cannot be modified']}"):
            c.iso_num = "001"
            c.save()

    def test_cannot_add_existing_country(self):
        Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)
        with self.assertRaises(ValidationError):
            Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)

    def test_country_by_default_inactive(self):
        country = Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)
        self.assertFalse(country.is_active)

    def test_country_iso2_length(self):
        with self.assertRaises(ValidationError):
            country = Country.objects.create(name="NewCountry", iso_alpha_2="X", iso_alpha_3="XXX", iso_num=999)
        with self.assertRaises(ValidationError):
            country = Country.objects.create(name="NewCountry", iso_alpha_2="XXX", iso_alpha_3="XXX", iso_num=999)
        Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)

    def test_country_iso3_length(self):
        with self.assertRaises(ValidationError):
            country = Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XX", iso_num=999)
        with self.assertRaises(ValidationError):
            country = Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXXX", iso_num=999)
        Country.objects.create(name="NewCountry", iso_alpha_2="XX", iso_alpha_3="XXX", iso_num=999)


class LinkedCountryTestCase(TestCase):
    """
    Tests of the LocObject.linked_countries method, that will return the countries linked to any LocObject (it is an
    abstract method that should be overwritten)
    """
    def setUp(self):
        # Create fake data for testing
        # Region
        self.europe = Region.objects.create(name="Europe1")
        self.americas = Region.objects.create(name="America1")
        self.groenland = Region.objects.create(name="Oceania1")
        # SubRegion
        self.emea = SubRegion.objects.create(name="EMEA")
        self.west_eu = SubRegion.objects.create(name="Western Europe1", region_id=self.europe.pk)
        self.nort_eu = SubRegion.objects.create(name="Northern Europe1", region_id=self.europe.pk)
        self.sout_eu = SubRegion.objects.create(name="Southern Europe1", region_id=self.europe.pk)
        self.cal = SubRegion.objects.create(name="California1", region_id=self.americas.pk)

        # Country
        self.fr = Country.objects.create(name="France1", sub_region_id=self.west_eu.pk,
                                         iso_alpha_2="XA", iso_alpha_3="XAA", iso_num=990)
        self.bl = Country.objects.create(name="Belgium1", sub_region_id=self.west_eu.pk,
                                         iso_alpha_2="XB", iso_alpha_3="XBB", iso_num=991)
        self.dn = Country.objects.create(name="Denmark1", sub_region_id=self.nort_eu.pk,
                                         iso_alpha_2="XC", iso_alpha_3="XCC", iso_num=992)
        self.pt = Country.objects.create(name="Portugal1", sub_region_id=self.sout_eu.pk,
                                         iso_alpha_2="XD", iso_alpha_3="XDD", iso_num=993)
        self.sp = Country.objects.create(name="Spain1", sub_region_id=self.sout_eu.pk,
                                         iso_alpha_2="XE", iso_alpha_3="XEE", iso_num=994)
        self.gr = Country.objects.create(name="Greece1", sub_region_id=self.sout_eu.pk,
                                         iso_alpha_2="XF", iso_alpha_3="XFF", iso_num=995)

    def test_country_linked_countries(self):
        self.assertQuerysetEqual(self.fr.linked_countries, [repr(self.fr)], ordered=False)
        self.assertQuerysetEqual(self.bl.linked_countries, [repr(self.bl)], ordered=False)


    def test_sub_region_linked_countries(self):
        self.assertQuerysetEqual(self.cal.linked_countries, [], ordered=False)
        self.assertQuerysetEqual(self.nort_eu.linked_countries, [repr(self.dn)], ordered=False)
        self.assertQuerysetEqual(self.west_eu.linked_countries, [repr(self.fr), repr(self.bl)], ordered=False)
        self.assertQuerysetEqual(self.sout_eu.linked_countries, [repr(self.pt), repr(self.sp), repr(self.gr)],
                                 ordered=False)

    def test_region_linked_countries(self):
        self.assertQuerysetEqual(self.americas.linked_countries, [], ordered=False)
        self.assertQuerysetEqual(self.europe.linked_countries, [repr(self.pt), repr(self.sp), repr(self.gr),
                                                                repr(self.fr), repr(self.bl), repr(self.dn)],
                                 ordered=False)

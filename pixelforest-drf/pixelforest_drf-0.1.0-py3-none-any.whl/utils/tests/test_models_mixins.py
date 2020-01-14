# Imports ##############################################################################################################
from django.db import models

from ..models import AbrModelMixin, NotModifiableFieldsModelMixin
from ..testcase import ModelMixinTestCase, CountSaveModelMixin

from django.core.exceptions import ValidationError


# Fake models ##########################################################################################################

class ModelWithNameField(AbrModelMixin, models.Model):
    name = models.CharField(max_length=100)


class SaveCounterWithName(CountSaveModelMixin):
    name = models.CharField(max_length=100)


class BadSaveImplementation(SaveCounterWithName):
    def save(self, *args, **kwargs):
        """ Bad implementation that will call .save() multiple times """
        if not self._state.adding:
            super().save(*args, **kwargs)
        super().save(*args, **kwargs)


class ModelWithNotModifiableFields(NotModifiableFieldsModelMixin):
    name = models.CharField(max_length=10)
    description = models.TextField()

    not_modifiable_fields = ['name']

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


# Tests ################################################################################################################

class ModelWithNameFieldAbrModelMixinTests(ModelMixinTestCase):
    """ Test the Mixin with a name field """
    mixins = [ModelWithNameField]

    def test_without_abbreviation(self):
        instance = self.ModelWithNameField.objects.create(name="This is the name")
        self.assertEqual(instance.get_name_or_abbreviation(), instance.name)
        self.assertEqual(instance.__str__(), instance.name)

    def test_with_abbreviation(self):
        instance = self.ModelWithNameField.objects.create(name="This is the name", abbreviation="abr")
        self.assertEqual(instance.get_name_or_abbreviation(), instance.abbreviation)
        self.assertEqual(instance.__str__(), instance.abbreviation)


class ModelWithoutNameFieldAbrModelMixinTests(ModelMixinTestCase):
    """ Test the Mixin without a name field """
    mixins = [AbrModelMixin]

    def test_without_abbreviation(self):
        instance = self.AbrModelMixin.objects.create()
        self.assertEqual(instance.get_name_or_abbreviation(), None)
        self.assertEqual(instance.__str__(), "")

    def test_with_abbreviation(self):
        instance = self.AbrModelMixin.objects.create(abbreviation="abr")
        self.assertEqual(instance.get_name_or_abbreviation(), instance.abbreviation)
        self.assertEqual(instance.__str__(), instance.abbreviation)


class CountSaveModelMixinTests(ModelMixinTestCase):
    """ Test the Mixin with a simple models class """
    mixins = [SaveCounterWithName]

    def test_simple_save(self):
        # Instance creation will call save once
        instance = self.SaveCounterWithName.objects.create(name="Name")
        self.assertEqual(instance.save_count, 1)
        # save_count will be updated if the object was changed and saved
        instance.name = "New name"
        instance.save()
        self.assertEqual(instance.save_count, 2)
        # save_count will be updated if the object wasn't changed and saved
        instance.save()
        self.assertEqual(instance.save_count, 3)


class BadSaveImplementationTests(ModelMixinTestCase):
    """ Test the Mixin with a bad models class """
    mixins = [BadSaveImplementation]

    def test_simple_save(self):
        # Instance creation will call save once
        instance = self.BadSaveImplementation.objects.create(name="Name")
        self.assertEqual(instance.save_count, 1)
        # .save() was called twice and will be counted twice if the object was changed and saved
        instance.name = "New name"
        instance.save()
        self.assertEqual(instance.save_count, 3)
        # .save() was called twice and will be counted twice if the object wasn't changed and saved
        instance.save()
        self.assertEqual(instance.save_count, 5)


class ModelWithNotModifiableFieldsModelMixinTests(ModelMixinTestCase):
    """ Verify that the mixin will work with a name field that cannot be modified """
    mixins = [ModelWithNotModifiableFields]

    def test_raise_error_for_bad_field(self):
        self.ModelWithNotModifiableFields.not_modifiable_fields = ['not_existing_field']
        with self.assertRaisesMessage(ValidationError, '["One or more field names in not_modifiable_fields do not '
                                                       'exists in the __TestModel__ModelWithNotModifiableFields '
                                                       'model ([\'not_existing_field\'])"]'):
            instance = self.ModelWithNotModifiableFields(name="Blog #1", description="This is a simple post")
            instance.save()

    def test_can_create_with_modifiable_field(self):
        # Save the object
        instance = self.ModelWithNotModifiableFields(name="Blog #1", description="This is a simple post")
        instance.save()
        # Compare it to it's db representation
        in_db = self.ModelWithNotModifiableFields.objects.get(pk=instance.pk)
        self.assertEqual(instance, in_db)

    def test_can_create_with_already_set_pk(self):
        """ This test is done because if using self.pk is None to know if an object is new it wouldn't work """
        # Save the object
        instance = self.ModelWithNotModifiableFields(pk=1, name="Blog #1", description="This is a simple post")
        instance.save()
        # Compare it to it's db representation
        in_db = self.ModelWithNotModifiableFields.objects.get(pk=instance.pk)
        self.assertEqual(instance, in_db)

    def test_can_modify_field_before_creation(self):
        # Save the object
        instance = self.ModelWithNotModifiableFields(name="Blog #1", description="This is a simple post")
        instance.name = "Blog #0"
        instance.save()
        # Compare it to it's db representation
        in_db = self.ModelWithNotModifiableFields.objects.get(pk=instance.pk)
        self.assertEqual(instance, in_db)

    def test_can_modify_other_fields_after_creation(self):
        # Save the object
        instance = self.ModelWithNotModifiableFields(name="Blog #1", description="This is a simple post")
        instance.save()
        # Modify a modifiable field
        instance.description = "This is a complex post"
        instance.save()
        # Compare it to it's db representation
        in_db = self.ModelWithNotModifiableFields.objects.get(pk=instance.pk)
        self.assertEqual(instance, in_db)

    def test_cant_modify_field_after_creation(self):
        # Save the object
        instance = self.ModelWithNotModifiableFields(name="Blog #1", description="This is a simple post")
        instance.save()
        # Compare it to it's db representation
        with self.assertRaisesMessage(ValidationError, "{'name': ['This field cannot be modified']}"):
            instance.name = "Blog #0"
            instance.save()

    def test_errors_are_stacking(self):
        # Save the object
        instance = self.ModelWithNotModifiableFields(name="Blog #0", description="This is the first post")
        instance.save()
        # Compare it to it's db representation
        with self.assertRaisesMessage(ValidationError, "{'name': ['This field cannot be modified', "
                                                       "'Ensure this value has at most 10 characters (it has 23).']}"):
            instance.name = "This string is too long"
            instance.save()

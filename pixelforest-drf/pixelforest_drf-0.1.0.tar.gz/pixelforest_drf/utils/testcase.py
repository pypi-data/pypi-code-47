# Imports ##############################################################################################################
from django.test import TestCase
from django.db import connection, models
from django.db.models.base import ModelBase


# TestCase #############################################################################################################

class ModelMixinTestCase(TestCase):
    """
    Base class for tests of model mixins. To use, subclass and specify the 'mixins' class variable.
    This should be a list of models to instantiate.
    The models using this mixin will be made available in self

    ex:
    class ModelMixinTestCase(TestCase):
        mixins = [ModelWithNameField]

        def test_mixin_stuff(self):
            self.ModelWithNameField.objects.create(name="This is a test")

    """
    mixins = []

    @classmethod
    def setUpClass(cls):
        if not cls.mixins:
            raise ValueError("No mixins where specified, please set 'mixins' in your ModelMixinTestCase")

        for mixin in cls.mixins:
            # Verify that there isn't a property with the name in question in self
            if hasattr(cls, mixin.__name__):
                raise ValueError("A mixin specified in ModelMixinTestCase.mixins is already a property of self and "
                                 "cannot be overwritten ({})".format(mixin.__name__))
            # Create a dummy model which extends the mixin
            setattr(cls, mixin.__name__, ModelBase('__TestModel__' + mixin.__name__, (mixin,),
                                                   {'__module__': mixin.__module__}))

        # Create the schema for  our test model
        with connection.schema_editor() as schema_editor:
            for mixin in cls.mixins:
                schema_editor.create_model(getattr(cls, mixin.__name__))

        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        # Delete the schema for the tests models
        with connection.schema_editor() as schema_editor:
            for mixin in cls.mixins:
                schema_editor.delete_model(getattr(cls, mixin.__name__))

        super().tearDownClass()


class CountSaveModelMixin(models.Model):
    """
    This class will count the number of time an object was saved.
    It is used for unit-testing purposes
    """

    @property
    def save_count(self):
        return self._save_count

    def __init__(self, *args, **kwargs):
        """ Add a save counter to the model """
        super().__init__(*args, **kwargs)
        self._save_count = 0

    def save(self, *args, **kwargs):
        """ Increment the save counter on every call """
        super().save(*args, **kwargs)
        self._save_count += 1

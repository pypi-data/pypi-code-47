# Imports ##############################################################################################################
from django.db import models
from django.forms.models import model_to_dict
from django.core.exceptions import ValidationError


# Model Mixins #########################################################################################################

class NotModifiableFieldsModelMixin(models.Model):
    """
    This mixin add the ability to create fields that can only be changed before the object is added in database

    It was created because we expected 'editable=False' to have this behaviour, but this field option only remove the
    field from any ModelForm (such as the admin) AND also remove validation on it
    (https://docs.djangoproject.com/en/2.2/ref/models/fields/#editable).

    Note that this doesn't alter the behaviour of the manager, so fields can still be updated by a bulk_update
    Note that this mixin does not overwrite .save() to call .full_clean() at the save stage for compatibility

    To add a field to the list of fields that cannot be modified, add the name of your field in the
    'not_modifiable_fields' list of your model.
    """
    @classmethod
    def nm_fields(cls):
        if hasattr(cls, "not_modifiable_fields"):
            return cls.not_modifiable_fields
        return []

    def __init__(self, *args, **kwargs):
        """ Override the init to keep the original value """
        # Call the init from the model
        super().__init__(*args, **kwargs)

        # Verify that all fields in not_modifiable_fields are fields of your model
        not_a_field = [f for f in self.nm_fields() if f not in [f.name for f in self._meta.fields]]
        if not_a_field:
            raise ValidationError("One or more field names in not_modifiable_fields do not exists in the {} model ({})"
                                  .format(self.__class__.__name__, not_a_field))

        # Keep the original values of the fields
        self.original_fields = model_to_dict(self, fields=[f for f in self.nm_fields()])

    def clean_fields(self, exclude=None):
        """
        For all fields in not_modifiable_fields, if the call to .save() is not an insert, do the validation
        """
        # If you are not creating a new object
        errors = {}
        if not self._state.adding:
            # Change exclude to empty list if None
            exclude = [] if exclude is None else exclude
            for f in self.nm_fields():
                if f in exclude:
                    continue
                if getattr(self, f) != self.original_fields[f]:
                    error = "This field cannot be modified"
                    errors[f] = errors[f] + [error] if f in errors.keys() else [error]

        # Get a dictionary of errors from clean_fields
        try:
            super().clean_fields(exclude=exclude)
        except ValidationError as e:
            errors = e.update_error_dict(errors)

        if errors:
            raise ValidationError(errors)

    class Meta:
        abstract = True


class AbrModelMixin(models.Model):
    """ Augmented model mixin with an abbreviation field """
    abbreviation = models.CharField(max_length=5, null=True, blank=True)

    def get_name_or_abbreviation(self):
        """ Either return the abbreviation (if specified), the name (if specified), or None """
        if self.abbreviation:
            return self.abbreviation
        if hasattr(self, "name") and self.name:
            return self.name
        return None

    def __str__(self):
        str_repr = self.get_name_or_abbreviation()
        return str_repr if str_repr is not None else ""

    class Meta:
        abstract = True

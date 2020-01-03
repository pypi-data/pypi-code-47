from typing import Any, Callable, Optional

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import QuerySet

from easyaudit.models import CRUDEvent


class ExtensibleModel(object):
    """ Allow injection of code from AlekSIS apps to extend model functionality.

    After all apps have been loaded, the code in the `model_extensions` module
    in every app is executed. All code that shall be injected into a model goes there.

    :Example:

    .. code-block:: python

       from datetime import date, timedelta

       from aleksis.core.models import Person

       @Person.property
       def is_cool(self) -> bool:
           return True

       @Person.property
       def age(self) -> timedelta:
           return self.date_of_birth - date.today()

    For a more advanced example, using features from the ORM, see AlekSIS-App-Chronos
    and AlekSIS-App-Alsijil.

    :Date: 2019-11-07
    :Authors:
        - Dominik George <dominik.george@teckids.org>
    """

    @classmethod
    def _safe_add(cls, obj: Any, name: Optional[str]) -> None:
        # Decide the name for the attribute
        if name is None:
            prop_name = obj.__name__
        else:
            if name.isidentifier():
                prop_name = name
            else:
                raise ValueError("%s is not a valid name." % name)

        # Verify that property name does not clash with other names in the class
        if hasattr(cls, prop_name):
            raise ValueError("%s already used." % prop_name)

        # Add function wrapped in property decorator if we got here
        setattr(cls, prop_name, obj)

    @classmethod
    def property(cls, func: Callable[[], Any], name: Optional[str] = None) -> None:
        """ Adds the passed callable as a property. """

        cls._safe_add(property(func), func.__name__)

    @classmethod
    def method(cls, func: Callable[[], Any], name: Optional[str] = None) -> None:
        """ Adds the passed callable as a method. """

        cls._safe_add(func, func.__name__)


class CRUDMixin(models.Model):
    class Meta:
        abstract = True

    @property
    def crud_events(self) -> QuerySet:
        """Get all CRUD events connected to this object from easyaudit."""

        content_type = ContentType.objects.get_for_model(self)

        return CRUDEvent.objects.filter(
            object_id=self.pk, content_type=content_type
        ).select_related("user")

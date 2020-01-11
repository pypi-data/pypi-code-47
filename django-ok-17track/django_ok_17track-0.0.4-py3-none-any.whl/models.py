from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'Track17Country',
    'Track17Carrier'
)


class Track17Country(models.Model):
    key = models.CharField(
        _('Key'),
        max_length=15
    )
    title = models.CharField(
        _('Title'),
        max_length=255
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self) -> str:
        return self.title


class Track17Carrier(models.Model):
    key = models.CharField(
        _('Key'),
        max_length=15
    )
    title = models.CharField(
        _('Title'),
        max_length=255
    )
    country = models.ForeignKey(
        Track17Country,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Country'),
    )
    url = models.CharField(
        _('Url'),
        max_length=255,
        blank=True
    )
    can_track = models.BooleanField(
        _('Can track'),
        default=False
    )

    class Meta:
        verbose_name = _('Carrier')
        verbose_name_plural = _('Carriers')

    def __str__(self) -> str:
        return self.title

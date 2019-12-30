from datetime import timedelta

import pytz
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class TokensExceededBase(Exception):
    whatfor = None

    def __init__(self, time_available):
        self.time_available = time_available

    def __str__(self, tz=None):
        return self.get_message(tz)

    @property
    def message(self):
        return self.get_message()

    def get_message(self, tz=None):
        if tz is None:
            tz = pytz.timezone(settings.TIME_ZONE)
        time_available = self.time_available.astimezone(tz)
        if time_available.date() != timezone.now().date():
            time_format = '%Y-%m-%d %H:%M'
        else:
            time_format = '%H:%M:%S'

        time_str = time_available.strftime(time_format)

        if self.whatfor is not None:
            return _('Limit for {} reached. Please wait until {}.').format(
                self.whatfor, time_str)
        return _('Limit reached. Please wait until {}').format(time_str)


class TokenBucket(models.Model):
    identifier = models.CharField(max_length=30)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    foreign_object = GenericForeignKey()
    max_tokens = models.IntegerField()
    fill_rate = models.FloatField()
    tokens = models.FloatField(default=0.0)
    last_updated = models.DateTimeField()

    class Meta:
        unique_together = ('identifier', 'object_id', 'content_type')

    def consume(self, num_tokens, save=True):
        """Remove num_tokens from the bucket.

        If there are not enough tokens available it will not remove any
        token but raise a TokensExceeded exception.

        It saves the state of the bucket to the database unless ``save``
        is set to False.
        """
        now = timezone.now()
        total_tokens = self._calc_tokens(now)
        wait_seconds = self.wait_seconds(num_tokens, total_tokens)
        if wait_seconds != 0:
            raise self.TokensExceeded(now + timedelta(seconds=wait_seconds))
        total_tokens -= num_tokens
        self.tokens = total_tokens
        self.last_updated = now
        if save:
            self.save()

    def wait_seconds(self, num_tokens, total_tokens=None):
        """Return the number of seconds to wait for ``num_tokens``.

        If no waiting is required 0 is returned.
        """
        if num_tokens > self.max_tokens:
            raise ValueError("The bucket capacity is too small.")

        if total_tokens is None:
            now = timezone.now()
            total_tokens = self._calc_tokens(now)

        if num_tokens <= total_tokens:
            return 0
        num_missing = num_tokens - total_tokens
        return num_missing * self.fill_rate

    def _calc_tokens(self, now):
        delta = (now - self.last_updated).total_seconds()
        return min(self.tokens + delta / self.fill_rate, self.max_tokens)

    @classmethod
    def get(cls, identifier, ref_object, max_tokens, fill_rate, whatfor=None):
        """Get a token bucket with specified configuration.

        Always use this function to get a bucket!
        """
        try:
            bucket = cls.objects.get(
                identifier=identifier,
                content_type=ContentType.objects.get_for_model(ref_object),
                object_id=ref_object.id,
            )
        except cls.DoesNotExist:
            bucket = cls(identifier=identifier,
                         foreign_object=ref_object,
                         max_tokens=max_tokens,
                         fill_rate=fill_rate,
                         tokens=max_tokens,
                         last_updated=timezone.now())

        scope_whatfor = whatfor

        class TokensExceeded(TokensExceededBase):
            whatfor = scope_whatfor

        bucket.TokensExceeded = TokensExceeded
        return bucket

    def __str__(self):
        return 'TokenBucket(ref={}, identifier={})'.format(self.foreign_object, self.identifier)

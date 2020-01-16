# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import UniqueIdentifierMixin


class ElectionType(UniqueIdentifierMixin, CivicBaseModel):
    """
    e.g., "General", "Primary"
    """

    natural_key_fields = ["slug"]
    uid_prefix = "electiontype"
    default_serializer = "election.serializers.ElectionTypeSerializer"

    GENERAL = "general"
    PARTISAN_CAUCUS = "partisan-caucus"
    PARTISAN_FIREHOUSE_CAUCUS = "partisan-firehouse-caucus"
    PARTISAN_PRIMARY = "partisan-primary"
    ALL_PARTY_PRIMARY = "all-party-primary"  # Let's not say 'Jungle primary.'
    PRIMARY_RUNOFF = "primary-runoff"
    GENERAL_RUNOFF = "general-runoff"

    TYPES = (
        (GENERAL, "General election"),
        (PARTISAN_CAUCUS, "Caucus"),
        (PARTISAN_FIREHOUSE_CAUCUS, "Firehouse Caucus"),
        (PARTISAN_PRIMARY, "Primary"),
        (ALL_PARTY_PRIMARY, "All-party Primary"),
        (PRIMARY_RUNOFF, "Primary Runoff"),
        (GENERAL_RUNOFF, "General Runoff"),
    )

    slug = models.SlugField(
        blank=True, max_length=255, unique=True, choices=TYPES
    )

    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    ap_code = models.CharField(max_length=1, null=True, blank=True)
    number_of_winners = models.PositiveSmallIntegerField(default=1)
    winning_threshold = models.DecimalField(
        decimal_places=3, max_digits=5, null=True, blank=True
    )

    def __str__(self):
        return self.uid

    def save(self, *args, **kwargs):
        """
        **uid field/identifier**: :code:`electiontype:{slug}`
        """
        self.generate_unique_identifier(always_overwrite_uid=True)

        super(ElectionType, self).save(*args, **kwargs)

    def is_primary(self):
        if self.slug in [
            self.PARTISAN_PRIMARY,
            self.PARTISAN_CAUCUS,
            self.ALL_PARTY_PRIMARY,
        ]:
            return True
        else:
            return False

    def is_runoff(self):
        if self.slug in [self.PRIMARY_RUNOFF, self.GENERAL_RUNOFF]:
            return True
        else:
            return False

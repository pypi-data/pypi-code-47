# Imports from python.
import re


# Imports from Django.
from django.db import models


# Imports from other dependencies.
from civic_utils.models import CivicBaseModel
from civic_utils.models import CommonIdentifiersMixin
from government.models import Party


# Imports from election.
from election.models.election_type import ElectionType


PRIMARY_TYPE = ElectionType.PARTISAN_PRIMARY


class ElectionBallot(CommonIdentifiersMixin, CivicBaseModel):
    """A single statewide ballot, up for election on a single day."""

    natural_key_fields = ["election_event", "party"]
    uid_prefix = "electionballot"
    default_serializer = "election.serializers.ElectionBallotSerializer"

    PRESIDENTIAL_OFFICE = "president"
    ALL_OFFICES = "all"
    DOWNTICKET_OFFICES = "downticket"

    OFFICES_ELECTED_TYPES = (
        (PRESIDENTIAL_OFFICE, "Presidential race"),
        (ALL_OFFICES, "Presidential, Congressional & Statewide races"),
        (DOWNTICKET_OFFICES, "Congressional & Statewide races"),
    )

    election_event = models.ForeignKey(
        "ElectionEvent", related_name="ballots", on_delete=models.PROTECT
    )
    party = models.ForeignKey(
        Party, null=True, blank=True, on_delete=models.PROTECT
    )
    offices_elected = models.SlugField(
        max_length=15,
        choices=OFFICES_ELECTED_TYPES,
        default=DOWNTICKET_OFFICES,
    )

    overall_notes = models.TextField(blank=True, null=True)

    early_vote_start = models.DateField(null=True, blank=True)
    early_vote_close = models.DateField(null=True, blank=True)
    vote_by_mail_application_deadline = models.DateField(null=True, blank=True)
    vote_by_mail_ballot_deadline = models.DateField(null=True, blank=True)
    early_voting_notes = models.TextField(blank=True, null=True)

    online_registration_deadline = models.DateField(null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    poll_closing_time = models.DateTimeField(null=True, blank=True)
    registration_notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("election_event", "party")

    def __str__(self):
        formatted_elex_date = self.election_event.election_day.date.strftime(
            "%Y-%m-%d"
        )

        if self.election_event.division is None:
            return "ASDF 9989"

        if (
            self.party
            and self.offices_elected == self.PRESIDENTIAL_OFFICE
            and self.election_event.election_type.slug == PRIMARY_TYPE
        ):
            return " ".join(
                [
                    f"{self.election_event.division.label}",
                    f"{self.get_party_possessive()} Presidential Primary",
                    f"({formatted_elex_date})",
                ]
            )
        elif (
            self.party
            and self.offices_elected == self.ALL_OFFICES
            and self.election_event.election_type.slug == PRIMARY_TYPE
        ):
            return " ".join(
                [
                    f"{self.election_event.division.label}",
                    f"{self.get_party_possessive()}",
                    "Presidential, Congressional & Statewide Primaries",
                    f"({formatted_elex_date})",
                ]
            )
        elif (
            self.party
            and self.election_event.election_type.slug == PRIMARY_TYPE
        ):
            return " ".join(
                [
                    f"{self.election_event.division.label}",
                    f"{self.get_party_possessive()} Primary",
                    f"({formatted_elex_date})",
                ]
            )

        return f"{self.election_event.label} -- open ballot"

    def save(self, *args, **kwargs):
        """
        **uid field**: :code:`electionevent:{event type}[({party types})]`
        **identifier**: :code:`<division uid>__<election day uid>__<this uid>`
        """
        self.generate_common_identifiers(
            always_overwrite_slug=True, always_overwrite_uid=True
        )

        super(ElectionBallot, self).save(*args, **kwargs)

    def get_uid_base_field(self):
        if self.party:
            return self.party.slug

        return "nonpartisan"

    def get_uid_prefix(self):
        return f"{self.election_event.uid}__{self.uid_prefix}"

    def get_party_possessive(self):
        if self.party:
            return re.sub(r"Party$", "", self.party.organization.name).strip()

        return "Nonpartisan"

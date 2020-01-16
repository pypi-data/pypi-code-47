# Imports from other dependencies.
from civic_utils.serializers import CommandLineListSerializer
from rest_framework import serializers


# Imports from election.
from election.models import ElectionBallot


class ElectionBallotAPISerializer(CommandLineListSerializer):
    party = serializers.SerializerMethodField()
    notes = serializers.SerializerMethodField()

    def get_party(self, obj):
        if obj.party:
            return obj.party.ap_code.lower()
        return None

    def get_notes(self, obj):
        return obj.overall_notes

    class Meta(CommandLineListSerializer.Meta):
        model = ElectionBallot
        fields = ("party", "offices_elected", "notes")

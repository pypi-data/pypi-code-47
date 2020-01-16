# Imports from other dependencies.
from civic_utils.serializers import CommandLineListSerializer
from rest_framework import serializers


# Imports from election.
from election.models import ElectionEvent
from election.serializers.api.election_ballot import (
    ElectionBallotAPISerializer,
)


class ElectionEventAPISerializer(CommandLineListSerializer):
    date = serializers.SerializerMethodField()
    election_type = serializers.SerializerMethodField()
    ballots = serializers.SerializerMethodField()

    def get_date(self, obj):
        return obj.election_day.date.strftime("%Y-%m-%d")

    def get_election_type(self, obj):
        return obj.election_type.slug

    def get_ballots(self, obj):
        return ElectionBallotAPISerializer(obj.ballots.all(), many=True).data

    class Meta(CommandLineListSerializer.Meta):
        model = ElectionEvent
        fields = ("date", "election_type", "ballots", "notes")

from rest_framework import serializers

from movie_selection.models import Nomination, Room, Vote

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

class NominationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomination
        fields = ['id', 'title', 'room']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'vote', 'nomination']

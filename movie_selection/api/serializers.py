from rest_framework import serializers

from movie_selection.models import Nomination, Room, Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['vote']

class NominationSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True)

    class Meta:
        model = Nomination
        fields = ['id', 'title', 'votes']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

class RoomDetailSerializer(serializers.ModelSerializer):
    nominations = NominationSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'nominations']

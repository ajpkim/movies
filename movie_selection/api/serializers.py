from rest_framework import serializers

from movie_selection.models import Nomination, Room, Vote

class VoteSerializer(serializers.ModelSerializer):
    room_name = serializers.ReadOnlyField(source='room.name')
    nomination_title = serializers.ReadOnlyField(source='nomination.title')

    class Meta:
        model = Vote
        fields = ['room_name', 'nomination_title', 'vote']

class NominationSerializer(serializers.ModelSerializer):
    room_name = serializers.ReadOnlyField(source='room.name')
    votes = VoteSerializer(many=True)

    class Meta:
        model = Nomination
        fields = ['id', 'room_name', 'title', 'votes']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

class RoomDetailSerializer(serializers.ModelSerializer):
    lookup_field = 'name'
    nominations = NominationSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'nominations']

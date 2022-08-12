import uuid

from rest_framework import serializers

from movie_selection.models import Nomination, Room, User, Vote

class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.username = user.id
        user.save()
        return user

class VoteSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.id', read_only=True)
    room_name = serializers.ReadOnlyField(source='room.name')
    nomination_title = serializers.ReadOnlyField(source='nomination.title')

    class Meta:
        model = Vote
        fields = ['room_name', 'user', 'nomination_title', 'vote']

class NominationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.id', read_only=True)
    room_name = serializers.ReadOnlyField(source='room.name')
    votes = VoteSerializer(many=True)

    class Meta:
        model = Nomination
        fields = ['id', 'user', 'room_name', 'title', 'votes']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name']

    def create(self, validated_data):
        """TODO: Remove the need to send this empty name data from client."""
        name = str(uuid.uuid4())
        room = Room(name=name)
        room.save()
        return room

class RoomDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.id', read_only=True)
    lookup_field = 'name'
    nominations = NominationSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'user', 'name', 'nominations']

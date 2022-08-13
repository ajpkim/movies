import random

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
        """TODO: Remove the need to send this empty name data ('validated_data') from client."""

        def create_room_name(word_file: str) -> str:
            with open(word_file, 'r') as file:
                words = file.read().split()
            room_words = random.choices(words, k=3)
            return '-'.join(room_words)

        word_file = 'common-5-letter-eng-words.txt'
        name = create_room_name(word_file)
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

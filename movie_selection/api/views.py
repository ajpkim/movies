"""
REST API.
"""

from rest_framework import generics
from rest_framework.views import APIView

from movie_selection.models import Nomination, Room, User, Vote
from movie_selection.api.serializers import RoomDetailSerializer, RoomSerializer, UserSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveAPIView):
    lookup_field = 'name'

    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

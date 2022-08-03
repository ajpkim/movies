from rest_framework import generics
from rest_framework.views import APIView

from movie_selection.models import Nomination, Room, Vote
from movie_selection.api.serializers import RoomDetailSerializer, RoomSerializer

class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomDetail(generics.RetrieveAPIView):
    lookup_field = 'name'

    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

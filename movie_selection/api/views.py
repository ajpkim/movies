from django.http import Http404
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from movie_selection.models import Nomination, Room, Vote
from movie_selection.api.serializers import NominationSerializer, RoomSerializer, VoteSerializer

class RoomList(APIView):
    def get(self, request, format=None):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(id=pk)
        except Room.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        room = self.get_object(pk)
        room_nominations = room.nominations_data
        data = {'room_name': room.name, 'nominations': room_nominations}
        return Response(data)

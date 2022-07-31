from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie_selection.models import Nomination, Room, Vote
from movie_selection.api.serializers import NominationSerializer, RoomSerializer, VoteSerializer

@api_view(['GET', 'POST'])
def room_list(request, format=None):
    """
    List all rooms, or create a new room.
    """
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def room_detail(request, pk, format=None):
    """
    Retrieve, update or delete a room.
    """
    try:
        room = Room.objects.get(pk=pk)
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {'room_name': room.name, 'nominations': room.nominations_data}
        return Response(data)

    elif request.method == 'POST':
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

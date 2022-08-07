import json

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    CreateModelMixin,
    DeleteModelMixin,
    ListModelMixin,
    PatchModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from .models import Nomination, Room, Vote
from movie_selection.api.serializers import RoomDetailSerializer, NominationSerializer, VoteSerializer

class RoomConsumer(RetrieveModelMixin, CreateModelMixin, GenericAsyncAPIConsumer):
    lookup_name = 'name'
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

    ################################################################################
    # NOMINATION
    ################################################################################
    @model_observer(Nomination, serializer_class=NominationSerializer)
    async def nomination_activity_handler(self, data, subscribing_request_ids=[], **kwargs):
        for request_id in subscribing_request_ids:
            data['request_id'] = request_id
            await self.reply(action="subscribe_to_room_nominations", data=data)

    @nomination_activity_handler.groups_for_consumer
    def nomination_activity_handler(self, room=None, **kwargs):
        """Add the consumer to the correct groups given the room context we receive here."""
        if room is not None:
            yield f'-room_name__{room.name}'

    @nomination_activity_handler.groups_for_signal
    def nomination_activity_handler(self, instance: Nomination, **kwargs):
        """Broadcast activity to the correct consumers based on the room-based groups this signal applies to."""
        yield f'-room_name__{instance.room.name}'

    @action()
    async def subscribe_to_room_nominations(self, action: str, room_name: str, request_id: int):
        room = await database_sync_to_async(Room.objects.get)(name=room_name)
        await self.nomination_activity_handler.subscribe(request_id=request_id, room=room)

    ################################################################################
    # VOTE
    ################################################################################
    @model_observer(Vote, serializer_class=VoteSerializer)
    async def vote_activity_handler(self, data, subscribing_request_ids=[], **kwargs):
        for request_id in subscribing_request_ids:
            data['request_id'] = request_id
            await self.reply(action="subscribe_to_room_votes", data=data)

    @vote_activity_handler.groups_for_consumer
    def vote_activity_handler(self, room=None, **kwargs):
        """Add the consumer to the correct groups given the room context we receive here."""
        if room is not None:
            yield f'-room_name__{room.name}'

    @vote_activity_handler.groups_for_signal
    def vote_activity_handler(self, instance: Vote, **kwargs):
        """Broadcast activity to the correct consumers based on the room-based groups this signal applies to."""
        yield f'-room_name__{instance.room.name}'

    @action()
    async def subscribe_to_room_votes(self, action: str, room_name: str, request_id: int):
        room = await database_sync_to_async(Room.objects.get)(name=room_name)
        await self.vote_activity_handler.subscribe(request_id=request_id, room=room)

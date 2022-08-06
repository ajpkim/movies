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
from movie_selection.api.serializers import RoomDetailSerializer, NominationSerializer

class RoomConsumer(RetrieveModelMixin, CreateModelMixin, GenericAsyncAPIConsumer):
    lookup_name = 'name'

    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer

    # @model_observer(Nomination)
    # async def nomination_activity_handler(self, message, observer=None, **kwargs):
    #     breakpoint()
    #     await self.send_json(message)

    # @nomination_activity_handler.groups_for_signal
    # async def nomination_activity_handler(self, instance: Nomination, **kwargs):
    #     print('YOOO')
    #     breakpoint()

    # @action()
    # async def subscribe_to_nomination(self, nomination, **kwargs):
    #     print("subscribe_to_nomination called")
    #     breakpoint()
    #     await self.nomination_activity_handler.subscribe(nomination=nomination)
    #     return {}, 201

    ##################################################

    # @model_observer(Room, serializer_class=RoomDetailSerializer)
    # async def room_activity_handler(self, message, action, name, **kwargs):
    #     print("\n\nTrying to do some room subscription stuff ...\n\n")
    #     await
    #     breakpoint()




    @model_observer(Nomination, serializer_class=NominationSerializer)
    async def nomination_activity_handler(self, data, subscribing_request_ids=[], **kwargs):
        print("\n\nTrying to do some nomination sub stuff...\n\n")
        for request_id in subscribing_request_ids:
            data['request_id'] = request_id
            await self.reply(action="HAHA", data=data)


    # @model_observer(Nomination)
    # async def nomination_activity_handler(
    #         self,
    #         message: NominationSerializer,
    #         observer=None,
    #         subscribing_request_ids=[],
    #         **kwargs
    # ):
    #     breakpoint()
    #     await self.send_json(dict(message.data))

    # @nomination_activity_handler.serializer
    # def nomination_activity_handler(self, instance: Nomination, action, **kwargs) -> NominationSerializer:
    #     """This will return the nomination serializer"""
    #     breakpoint()
    #     return NominationSerializer(instance).data


    # @action()
    # async def subscribe_to_room(self, name, **kwargs):
    #     print("\n\nsubscribe_to_room called\n\n")
    #     # breakpoint()
    #     await self.room_activity_handler.subscribe(name=name)
    #     return {"some DATA": 333}, 201

    @action()
    async def subscribe_to_nomination(self, action: str, room_name: str, title: str, request_id: int):
        """We will use these args later to filter out the specific stuff we care about"""

        print("\n\nsubscribe_to_nomination called\n\n")

        # await self.nomination_activity_handler.subscribe(room_name=room_name, title=title)
        #  await self.nomination_activity_handler.subscribe(request_id=request_id)

        await self.nomination_activity_handler.subscribe(request_id=request_id)




################################################################################
    # Trying to get subscription stuff to work but its breaking when i create a new instance of model

    # @model_observer(Nomination)
    # async def nomination_activity(
    #         self,
    #         message: NominationSerializer,
    #         observer=None,
    #         subscribing_request_ids=[],
    #         **kwargs
    # ):
    #     breakpoint()
    #     await self.send_json(dict(message.data))

    # @nomination_activity.serializer
    # def nomination_activity(self, instance: Nomination, action, **kwargs):
    #     """This will return the Nomination serializer.

    #     Ok to have the same name as method decoratored with @model_observer.
    #     """
    #     breakpoint()
    #     return NominationSerializer(instance)

    # @action()
    # async def subscribe_to_nomination_activity(self, request_id, **kwargs):
    #     breakpoint()
    #     await self.nomination_activity.subscribe(request_id=request_id)


################################################################################

# class MovieSelectionConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = f'group_{self.room_name}'

#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def disconnect(self):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     async def receive_json(self, content, **kwargs):

#         if content['type'] == 'new_nomination':
#             title = content['title']
#             # Add new nomination to DB
#             room = await database_sync_to_async(Room.objects.get)(name=self.room_name)

#             # TODO: VALIDATE THAT THERE ISN"T ALREADY A NOMINATION WITH THIS TITLE IN ROOM
#             nomination = Nomination(title=title, room=room)
#             await database_sync_to_async(nomination.save)()

#             # Send message to room group
#             await self.channel_layer.group_send(
#                 self.room_group_name,
#                 {
#                     'type': 'nomination',
#                     'title': title,
#                     'votes_yes': 0,
#                     'votes_no': 0,
#                 }
#             )

#         if content['type'] == 'vote':
#             await self.channel_layer.group_send(
#                 self.room_group_name,
#                 {
#                     'type': 'vote',
#                     'vote': content['vote'],
#                     'title': content['title']
#                 }
#             )

#     # Receive message from room group
#     async def nomination(self, event):
#         # Send message to WebSocket
#         await self.send_json(content=event)

#     async def vote(self, event):
#         await self.send_json(content=event)

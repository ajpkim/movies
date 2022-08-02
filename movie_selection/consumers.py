import json

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Nomination, Room, Vote


class MovieSelectionConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'group_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

    async def disconnect(self):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive_json(self, content, **kwargs):

        if content['type'] == 'new_nomination':
            title = content['title']
            # Add new nomination to DB
            room = await database_sync_to_async(Room.objects.get)(name=self.room_name)

            # TODO: VALIDATE THAT THERE ISN"T ALREADY A NOMINATION WITH THIS TITLE IN ROOM
            nomination = Nomination(title=title, room=room)
            await database_sync_to_async(nomination.save)()

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'nomination',
                    'title': title,
                    'votes_yes': 0,
                    'votes_no': 0,
                }
            )

        if content['type'] == 'vote':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'vote',
                    'vote': content['vote'],
                    'title': content['title']
                }
            )

    # Receive message from room group
    async def nomination(self, event):
        # Send message to WebSocket
        await self.send_json(content=event)

    async def vote(self, event):
        await self.send_json(content=event)

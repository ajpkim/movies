import json

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer  #, JsonWebsocketConsumer, WebsocketConsumer
from .models import Nomination, Room

class MovieSelectionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WEBSOCKET CONNECTING")

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'group_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json['type'] == 'nomination':
            title = text_data_json['title']
            # Add new nomination to DB
            room = await database_sync_to_async(Room.objects.get)(name=self.room_name)
            nomination = Nomination(name=title, room=room)
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

        if text_data_json['type'] == 'vote':
            print("A VOTEEEEEEE")
        #     title = text_data_json['title']
        #     # Add new nomination to DB
        #     room = await database_sync_to_async(Room.objects.get)(name=self.room_name)
        #     nomination = Nomination(name=title, room=room)
        #     await database_sync_to_async(nomination.save)()

        #     # Send message to room group
        #     await self.channel_layer.group_send(
        #         self.room_group_name,
        #         {
        #             'type': 'nomination',
        #             'title': title,
        #             'voted': 0,
        #             'yes': 0,
        #             'no': 0,
        #         }
        #     )

    # Receive message from room group
    async def nomination(self, event):

        if event['type'] == 'nomination':
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                'type': 'nomination',
                'title': event['title'],
                'votes_yes': event['votes_yes'],
                'votes_no': event['votes_no'],
            }))

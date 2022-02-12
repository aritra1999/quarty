import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from django.contrib.auth.models import User
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
    
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'new_user',
        #         'new_user': self.scope['user'].username,
        #     }
        # )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'user_disconnet',
        #         'new_user': self.scope['user'].username
        #     }
        # )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_from = text_data_json['message_from']
        message_to = text_data_json['message_to']

            
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'message_from': message_from,
                'message_to': message_to
            }
        )


    async def user_disconnet(self, event):
        user = event['new_user']
        await self.send(text_data=json.dumps({
            'meta': "user_disconnect",
            'new_user': user,
        }))

    async def chat_message(self, event):
        message = event['message']
        message_from = event['message_from']
        message_to = event['message_to']

        await record_message(message, message_from, message_to)  
        print('Sending: ', message)

        await self.send(text_data=json.dumps({
            'meta': "new_message",
            'message': message,
            'message_from': message_from,
            'message_to': message_to
        }))

    

@database_sync_to_async
def record_message(message, message_from, message_to):
    Message.objects.create(
        message=message,
        message_from=User.objects.get(username=message_from),
        message_to=User.objects.get(username=message_to),
    )


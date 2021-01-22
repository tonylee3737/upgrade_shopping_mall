import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.utils import timezone


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        # self.id = self.scope['url_route']['kwargs']["gh"]
        self.id = "gwanho"
        self.room_group_name = 'chat_%s' % self.id
        # join room group
        # await self.channel_layer.group_add(
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # accept connection
        # await self.accept()
        self.accept()
    def disconnect(self, close_code):
        # leave room group
        # await self.channel_layer.group_discard(
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    # receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()

        # send message to room group
        # await self.channel_layer.group_send(
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        # self.send(text_data=json.dumps({'message':message}))
        )
    # receive message from room group
    # async def chat_message(self, event):
    def chat_message(self, event):
        # send message to WebSocket
        # await self.send(text_data=json.dumps(event))
        self.send(text_data=json.dumps(event))
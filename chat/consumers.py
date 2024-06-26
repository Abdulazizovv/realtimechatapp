import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from .models import Chats, Messages
from main.models import Profile


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

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

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope['user']

        # Save the message to the database
        chat = await self.get_chat(self.room_name)
        saved_message = await self.save_message(user, chat, message)

        profile_image_url = await self.get_user_image(user)

        # Broadcast the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': saved_message.text,
                'author': saved_message.author.username,
                'image_url': profile_image_url,
                'time': saved_message.created_at.strftime('%H:%M %d-%m-%Y')
            }
        )

    async def chat_message(self, event):
        message = event['message']
        author = event['author']
        image_url = event['image_url']
        time = event['time']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'author': author,
            'image_url': image_url,
            'time': time
        }))

    @database_sync_to_async
    def get_user_image(self, user):
        return user.profile.image.url

    @database_sync_to_async
    def get_chat(self, room_name):
        return Chats.objects.get(id=room_name)

    @database_sync_to_async
    def save_message(self, user, chat, message):
        return Messages.objects.create(author=user, chat=chat, text=message)

from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.exceptions import StopConsumer
from time import sleep
from channels.layers import get_channel_layer
import asyncio
import json
from django.db.models.signals import post_save
from .models import *

class ParkingLotConsumer(WebsocketConsumer):
    def connect(self):
        print('connect!')
        self.room_group_name = self.scope['url_route']['kwargs']['groupid']
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'send_data',
                'message': 'message'
            }
        )
    def send_data(self, event):
        data_receive = event['message']
        parking_lots = parking_lot.objects.all()
        data = [{'name': lot.name, 'status': lot.status} for lot in parking_lots]
        self.send(text_data=json.dumps(data))


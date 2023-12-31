import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import RoomChat
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['uuid']
        self.room_group_name = f"chat_{self.room_id}"


        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        host = text_data_json['host']
        creator = text_data_json['creator']
        room_id = text_data_json['room_id']


        user1=User.objects.get(username=host)
        user2=User.objects.get(username=creator)
        obj=RoomChat.objects.create(message=message,roomId=room_id)
        obj.host=user1
        obj.creator=user2
     
        obj.save()
        print('eta message: ',message)
        print('o hocce msg dice: ',creator)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            { 
                'type':'chat_message',
                'message':message,
                'host':host
            }
            

        )
       
    
    def chat_message(self, event):
        message = event['message']
        host = event['host']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'host':host,
        }))
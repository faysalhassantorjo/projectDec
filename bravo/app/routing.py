from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/(?P<uuid>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
]

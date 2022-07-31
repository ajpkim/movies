from django.urls import re_path

from .consumers import MovieSelectionConsumer

websocket_urlpatterns = [
    re_path(r'(?P<room_name>\w+)/$', MovieSelectionConsumer.as_asgi()),
]

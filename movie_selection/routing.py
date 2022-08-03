from django.urls import re_path

from movie_selection.consumers import RoomConsumer

websocket_urlpatterns = [
    re_path(r'api/(?P<room_name>\w+)/$', RoomConsumer.as_asgi()),
]

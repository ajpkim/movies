from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/movie_selection/(?P<room_name>\w+)/$', consumers.MovieSelectionConsumer.as_asgi()),
]

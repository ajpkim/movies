from django.urls import re_path

from movie_selection.consumers import MovieSelectionConsumer

websocket_urlpatterns = [
    re_path(r'api/(?P<room_name>\w+)/$', MovieSelectionConsumer.as_asgi()),
]

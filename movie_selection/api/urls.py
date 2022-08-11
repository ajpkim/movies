from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from movie_selection.api import views

urlpatterns = [
    path('users/create/', views.UserCreateAPIView.as_view()),
    path('rooms/', views.RoomList.as_view()),
    path('rooms/create/', views.RoomCreateAPIView.as_view()),
    path('rooms/<str:name>/', views.RoomDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

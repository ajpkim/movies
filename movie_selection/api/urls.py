from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from movie_selection.api import views

urlpatterns = [
    path('rooms/', views.room_list),
    path('rooms/<int:pk>/', views.room_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)



# from .views import (
#     NominationListView,
#     NominationDetailView,
#     NominationCreateView,
#     NominationUpdateView,
#     NominationDeleteView,
# )

# app_name = 'movie_selection'

# urlpatterns = [
    # path('', NominationListView.as_view()),
    # path('create/', NominationCreateView.as_view()),
    # path('<pk>', NominationDetailView.as_view()),
    # path('<pk>/update', NominationUpdateView.as_view()),
    # path('<pk>/delete/', NominationDeleteView.as_view()),
# ]

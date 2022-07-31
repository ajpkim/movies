from django.urls import include, path

from .views import (
    NominationListView,
    NominationDetailView,
    NominationCreateView,
    NominationUpdateView,
    NominationDeleteView,
)

app_name = 'movie_selection'

urlpatterns = [
    path('', NominationListView.as_view()),
    path('create/', NominationCreateView.as_view()),
    path('<pk>', NominationDetailView.as_view()),
    path('<pk>/update', NominationUpdateView.as_view()),
    path('<pk>/delete/', NominationDeleteView.as_view()),
]

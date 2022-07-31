# from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    )


from movie_selection.models import Nomination, Room
from .serializers import NominationSerializer, VoteSerializer



class NominationListView(ListAPIView):
    # queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        room_name = self.request.query_params.get('room_name')
        room = Room.objects.get(name=room_name)
        nominations = Nomination.objects.filter(room=room)
        return nominations

class NominationDetailView(RetrieveAPIView):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
    permission_classes = (permissions.AllowAny, )

class NominationCreateView(CreateAPIView):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
    permission_classes = (permissions.AllowAny, )

class NominationUpdateView(UpdateAPIView):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
    permission_classes = (permissions.AllowAny, )

class NominationDeleteView(DestroyAPIView):
    queryset = Nomination.objects.all()
    serializer_class = NominationSerializer
    permission_classes = (permissions.AllowAny, )

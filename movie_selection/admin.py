from django.contrib import admin
from .models import Room, Nomination, Vote

admin.site.register(Room)
admin.site.register(Nomination)
admin.site.register(Vote)

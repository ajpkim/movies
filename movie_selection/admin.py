from django.contrib import admin
from .models import Room, Nomination, User, Vote

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Nomination)
admin.site.register(Vote)

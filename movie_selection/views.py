# from django.shortcuts import render

# from .models import Nomination, Room

# def index(request):
#     return render(request, 'movie_selection/index.html')

# def room(request, room_name):
#     room = Room.objects.filter(name=room_name).first()
#     nominations = []
#     if room:
#         nominations = Nomination.objects.filter(room=room)
#     else:
#         room = Room(name=room_name)
#         room.save()

#     return render(request, 'movie_selection/room.html', {
#         'room_name': room_name,
#         'nominations': nominations,
#     })

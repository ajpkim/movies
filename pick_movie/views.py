from django.shortcuts import render

def index(request):
    return render(request, 'pick_movie/index.html')

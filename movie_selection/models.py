from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Nomination(models.Model):
    name = models.CharField(max_length=100, unique=False)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

class Vote(models.Model):
    yes = models.BooleanField()
    nomination = models.ForeignKey('Nomination', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

import uuid
from collections import Counter

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    # USERNAME_FIELD = 'id'  # Set this in the model create method

    def __str__(self):
        return str(self.id)

class Room(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, unique=True)

    @property
    def nominations(self):
        return Nomination.objects.filter(room=self)

    @property
    def nominations_data(self) -> {str: {str: {int: int}}}:
        """Return dictionay of nominations with vote data for each nomination."""
        return {nom.title: nom.vote_counts for nom in self.nominations}

    def __str__(self):
        return f'<Room: {self.name}>'

class Nomination(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)  #, related_name='room')
    title = models.CharField(max_length=100, unique=False)

    @property
    def votes(self):
        return Vote.objects.filter(nomination=self)

    @property
    def vote_counts(self):
        return Counter([vote.vote for vote in self.votes])

    def __str__(self):
        return f'<Nomination: {self.title}, room={self.room.name}>'

class Vote(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)  #, related_name='room')
    nomination = models.ForeignKey('Nomination', on_delete=models.CASCADE, related_name='nomination')
    vote = models.IntegerField()

    def __str__(self):
        return f'<Vote: {self.vote}, room={self.room.name}, nomination={self.nomination.title}>'

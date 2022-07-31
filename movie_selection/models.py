from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)

    @property
    def nominations(self):
        return Nomination.objects.filter(room=self)

    def __str__(self):
        return f'<Room: {self.name}>'

class Nomination(models.Model):
    title = models.CharField(max_length=100, unique=False)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    @property
    def votes(self):
        votes = Vote.objects.filter(nomination=self)
        votes = [vote.vote for vote in votes]
        return {
            'votes_yes': sum(votes),
            'votes_no': len(votes) - sum(votes)
        }

    def __str__(self):
        return f'<Nomination: {self.title}, room={self.room.name}>'

class Vote(models.Model):
    vote = models.BooleanField()
    nomination = models.ForeignKey('Nomination', on_delete=models.CASCADE)
    # room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'<Vote: {self.vote}, nomination={self.nomination.title}>'

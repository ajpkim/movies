from collections import Counter

from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)

    @property
    def nominations(self):
        return Nomination.objects.filter(room=self)

    @property
    def nominations_data(self) -> {str: {str: {int: int}}}:
        """
        Return data about each nomination attached to room and all the votes for those nominations.

        TODO: Move serializer logic into serializer
        """
        data = []
        for nomination in self.nominations:
            nom_data = {'title': nomination.title}
            nom_data['votes'] =  [{k:v} for k,v in nomination.votes.items()]  # This type of stuff should be in serializer...
            data.append(nom_data)
        return data

    def __str__(self):
        return f'<Room: {self.name}>'

class Nomination(models.Model):
    title = models.CharField(max_length=100, unique=False)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    @property
    def votes(self):
        votes = Vote.objects.filter(nomination=self)
        return Counter([vote.vote for vote in votes])

    def __str__(self):
        return f'<Nomination: {self.title}, room={self.room.name}>'

class Vote(models.Model):
    vote = models.IntegerField()
    nomination = models.ForeignKey('Nomination', on_delete=models.CASCADE)
    # room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'<Vote: {self.vote}, nomination={self.nomination.title}>'


# Create join tables with array aggreation with join using groupby?

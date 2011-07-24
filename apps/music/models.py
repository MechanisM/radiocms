from django.db import models


class Artist(models.Model):

    name = models.CharField(max_length=100)


class Song(models.Model):

    artist = models.ForeignKey('Artist')
    title = models.CharField(max_length=100)



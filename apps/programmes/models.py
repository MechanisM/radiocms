from django.db import models
from django.contrib.auth.models import User, UserManager
from apps.music.models import Song


class Presenter(User):

    preferred_name = models.CharField(max_length=100, blank=True, null=True)

    objects = UserManager()

    class Meta:
        pass

    def __unicode__(self):
        return self.preferred_name


class Show(models.Model):

    title = models.CharField(max_length=100)
    presenters = models.ManyToManyField('Presenter')

    class Meta:
        pass

    def __unicode__(self):
        return self.title


class Episode(models.Model):

    show = models.ForeignKey('Show', related_name='episodes')

    class Meta:
        pass

    def __unicode__(self):
        return self.show


class Instance(models.Model):

    episode = models.ForeignKey('Episode', related_name='instances')

    class Meta:
        pass

    def __unicode__(self):
        return self.episode


class Segment(models.Model):

    start_time = models.TimeField()
    duration = models.IntegerField()

    class Meta:
        pass

    def __unicode__(self):
        return '@todo'


class SongSegment(Segment):

    song = models.ForeignKey(Song)

    def __unicode__(self):
        return self.song


class EventSegment(Segment):

    description = models.CharField(max_length=100)

    class Meta:
        pass

    def __unicode__(self):
        return self.description

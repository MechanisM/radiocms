from django.db import models
from django.contrib.auth.models import User, UserManager
from apps.music.models import Song


class Presenter(User):

    preferred_name = models.CharField(max_length=100, blank=True, null=True)

    objects = UserManager()

    class Meta:
        pass

    def __unicode__(self):
        if self.preferred_name:
            return self.preferred_name
        else:
            return '%s %s' % (self.first_name, self.last_name)


class Show(models.Model):

    title = models.CharField(max_length=100)
    presenters = models.ManyToManyField('Presenter')

    class Meta:
        pass

    def __unicode__(self):
        return self.title


class Episode(models.Model):

    show = models.ForeignKey('Show', related_name='episodes')
    series = models.IntegerField(null=True, blank=True)
    episode = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)

    class Meta:
        pass

    def __unicode__(self):
        return '%s - %s' % (self.show, self.title, )


class Instance(models.Model):

    episode = models.ForeignKey('Episode', related_name='instances')
    tx_time = models.DateTimeField()

    class Meta:
        pass

    def __unicode__(self):
        return '%s' % (self.episode, )


class Segment(models.Model):

    start_time = models.TimeField()
    duration = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '@todo'


class SongSegment(Segment):

    song = models.ForeignKey(Song)

    def __unicode__(self):
        return '%s' % (self.song, )


class EventSegment(Segment):

    description = models.CharField(max_length=100)

    class Meta:
        pass

    def __unicode__(self):
        return self.description

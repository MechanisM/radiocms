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

    # @todo Duration
    show = models.ForeignKey('Show', related_name='episodes')
    series = models.IntegerField(null=True, blank=True)
    episode = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        pass

    def __unicode__(self):
        return '%s - %s' % (self.show, self.title, )

    @models.permalink
    def get_absolute_url(self):
        return ('episode_detail', [str(self.id)])


class Instance(models.Model):

    # @todo Rename to tx_date
    episode = models.ForeignKey('Episode', related_name='instances')
    tx_time = models.DateTimeField()

    class Meta:
        pass

    def __unicode__(self):
        return '%s' % (self.episode, )


class Segment(models.Model):

    start_time_minutes = models.IntegerField()
    start_time_seconds = models.IntegerField()
    duration = models.IntegerField(null=True, blank=True)
    episode = models.ForeignKey('Episode')

    class Meta:
        abstract = True
        ordering = ('start_time_minutes', 'start_time_seconds', )

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

from django.db import models


class Artist(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('artist_detail', [str(self.id)])


class Song(models.Model):

    artist = models.ForeignKey('Artist')
    title = models.CharField(max_length=100)

    class Meta:
        pass

    def __unicode__(self):
        return '%s - %s' % (self.artist, self.title)


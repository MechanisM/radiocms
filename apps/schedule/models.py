from django.db import models


class Presenter(models.Model):
    pass


class Show(models.Model):
    # ManyToMany to Presenter
    pass


class Episode(models.Model):
    # ForeignKey to Show
    pass


class Instance(models.Model):
    # ForeignKey to Episode
    pass


class Segment(models.Model):
    # Time
    pass


class SongSegment(Segment):
    # ForeignKey to music.Song.
    pass


class EventSegment(Segment):
    # Just some text, for now.
    pass

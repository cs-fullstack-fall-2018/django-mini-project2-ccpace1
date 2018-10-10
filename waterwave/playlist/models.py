from django.db import models


class Playlist(models.Model):
    songName = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    duration = models.CharField(max_length=10)
    rating = models.IntegerField(default=1)
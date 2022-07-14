from django.db import models

from common.models import Timestamped


class Tutorial(Timestamped):
    yt_title = models.CharField(max_length=100, null=True)
    trick = models.ForeignKey(
        "tricks.Trick", on_delete=models.CASCADE, related_name="tutorials")
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, related_name='tutorials')
    url = models.URLField()


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, related_name='playlists')


class Author(models.Model):
    name = models.CharField(max_length=15)

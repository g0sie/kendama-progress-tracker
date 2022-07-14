from django.db import models

from common.models import Timestamped


class Tutorial(Timestamped):
    yt_title = models.CharField(max_length=100, null=True)
    trick = models.ForeignKey(
        "tricks.Trick", on_delete=models.CASCADE, related_name="tutorials")
    author = models.CharField(max_length=100)
    url = models.URLField()

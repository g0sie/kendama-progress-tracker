from django.db import models

from common.models import Timestamped


class Tutorial(Timestamped):
    trick = models.ForeignKey("Trick", on_delete=models.CASCADE, related_name="tutorials")
    author = models.CharField(max_length=100)
    url = models.URLField()


class Trick(Timestamped):
    name = models.CharField(max_length=300)
    difficulty = models.CharField(
        max_length=1,
        choices=[
            ('b', 'beginner'),
            ('i', 'intermediate'),
            ('a', 'advanced'),
            ('o', 'other')],
        default='other')
    official = models.BooleanField(default=False)

    def __str__(self):
        return self.name

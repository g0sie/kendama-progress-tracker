from django.db import models


class Trick(models.Model):
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

from django.db import models
from django.core.validators import MaxValueValidator

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


class UserTrick(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="tricks")
    trick = models.ForeignKey('Trick', on_delete=models.CASCADE, related_name="users")
    land_count = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    added = models.DateTimeField(auto_now_add=True)
    passed = models.DateTimeField(blank=True, null=True)

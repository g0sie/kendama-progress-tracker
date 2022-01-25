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
    # official tricks are in official list of tricks
    official = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserTrick(models.Model):
    """defines user's tricks"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="tricks")
    trick = models.ForeignKey('Trick', on_delete=models.CASCADE, related_name="users")
    # how many times user landed the trick
    land_count = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    # when the trick was added
    added = models.DateTimeField(auto_now_add=True)
    # when the trick was passed if was
    passed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"user: {self.user}, trick: {self.trick}, " \
               f"landed: {self.land_count} times{', passed' if self.passed else ''}"

from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    kens = models.PositiveIntegerField(default=0)

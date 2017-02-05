from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Model3d(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user"
    )
    title = models.CharField(help_text="title of the model", max_length=100)
    description = models.TextField(help_text="description of the model")
    path = models.FileField(help_text="Path to model", upload_to="uploads/")
    votes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def update_count(self):
        # count views
        self.views += 1
        self.save()


class Badge(models.Model):
    name = models.CharField(help_text="name", max_length=100)
    description = models.CharField(help_text="description", max_length=200)
    user = models.ManyToManyField(User, related_name="badges")

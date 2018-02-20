from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MeMessages(models.Model):
    name = models.CharField(max_length=50, default="")
    text = models.TextField()
    #author = models.CharField(max_length=50, default="me")
    author = models.ForeignKey('auth.User')
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

class FriendsMessages(models.Model):
    name = models.CharField(max_length=50, default="")
    text = models.TextField()
    #author = models.CharField(max_length=50, default="me")
    author = models.ForeignKey('auth.User')
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

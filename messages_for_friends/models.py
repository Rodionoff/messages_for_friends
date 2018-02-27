from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MeMessages(models.Model):
    name = models.CharField(max_length=50, default="")
    text = models.TextField()
    author = models.CharField(max_length=50, default="myself")
    #author = models.ForeignKey('auth.User', null=True)
    #author = models.ForeignKey(User)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

class FriendsMessages(models.Model):
    name = models.CharField(max_length=50, default="")
    text = models.TextField()
    author = models.CharField(max_length=50, default="myself")
    #author = models.CharField(max_length=50, default="me")
    ##author = models.ForeignKey('auth.User')
    #author = models.ForeignKey(User, null=True)
    #author = models.CharField(max_length=50)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def publish(self):
        self.save()

class Comment(models.Model):
    message = models.ForeignKey("FriendsMessages", related_name="comments")
    author = models.ForeignKey("auth.User")
    text = models.TextField(max_length=550)
    publish_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-publish_date"]

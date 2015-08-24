from django.db import models
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=100)
    sender = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100)
    message = models.TextField()

class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()
    URL1 = models.URLField(max_length=200)
    URL2 = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Apply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    name = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
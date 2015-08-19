from django.db import models
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=100)
    sender = models.EmailField(blank=True, null=True)
    phone = models. CharField(max_length=100)
    message = models.TextField()


class Apply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    name = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    sender = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=100)
    message = models.TextField()


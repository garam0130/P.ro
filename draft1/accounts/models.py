from django.db import models
from django.contrib.auth.models import User
import datetime
from uuid import uuid4

# Create your models here.


class EmailToken(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(max_length=255)
    token = models.CharField(max_length=64, unique=True)
    key_expires = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     self.token = str(uuid4())
    #     super(EmailToken, self).save(*args, **kwargs)
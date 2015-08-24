from django.conf import settings
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=100)
    sender = models.EmailField(blank=True, null=True)
    phone = models. CharField(max_length=100)
    message = models.TextField()


class Apply(models.Model):

    MAN = 'M'
    WOMAN = 'F'
    GENDER_CHOICES = (
        (MAN, '남'),
        (WOMAN, '여'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=WOMAN)
    phone = models.CharField(max_length=20)
    birthdate = models.DateField(default=timezone.now)
    email = models.EmailField()
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=1)
    content1 = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    content4 = models.TextField()
    content5 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    final_submit = models.BooleanField(default=False)

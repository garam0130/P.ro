# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='messeage',
            new_name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='sender',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]

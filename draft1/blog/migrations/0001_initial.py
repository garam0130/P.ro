# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sender', models.EmailField(max_length=254, null=True, blank=True)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]

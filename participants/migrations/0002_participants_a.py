# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-10 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participants',
            name='a',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

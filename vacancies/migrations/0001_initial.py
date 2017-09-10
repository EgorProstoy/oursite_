# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='vacphoto')),
                ('name', models.CharField(max_length=50)),
                ('organization', models.CharField(max_length=50)),
                ('href', models.TextField()),
            ],
        ),
    ]
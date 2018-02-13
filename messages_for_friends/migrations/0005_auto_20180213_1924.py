# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-13 16:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messages_for_friends', '0004_messages_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

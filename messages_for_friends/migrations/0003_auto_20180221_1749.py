# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-21 14:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messages_for_friends', '0002_auto_20180221_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendsmessages',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='memessages',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

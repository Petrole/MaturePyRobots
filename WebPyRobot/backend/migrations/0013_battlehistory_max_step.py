# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20171125_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlehistory',
            name='max_step',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
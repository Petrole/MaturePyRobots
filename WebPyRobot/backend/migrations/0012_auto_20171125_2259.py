# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20171125_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlehistory',
            name='result_stats',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='battlehistory',
            name='status',
            field=models.CharField(default='Fini', max_length=10),
        ),
        migrations.AddField(
            model_name='battlehistory',
            name='step',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

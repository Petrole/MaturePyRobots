# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-03 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_battlehistory_championship_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='symbol',
            field=models.CharField(default='import_contacts', help_text='Material Icons', max_length=50, null=True),
        ),
    ]

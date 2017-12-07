# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171121_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'man'), ('female', 'women')], default='female', max_length=6),
        ),
    ]
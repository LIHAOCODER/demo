# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='need_know',
            field=models.CharField(default='', max_length=100, verbose_name='\u8bfe\u7a0b\u987b\u77e5'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=100, verbose_name='\u8bfe\u7a0b\u9884\u5907'),
        ),
    ]
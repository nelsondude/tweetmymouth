# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 22:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='text',
            new_name='content',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 04:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course',
        ),
    ]

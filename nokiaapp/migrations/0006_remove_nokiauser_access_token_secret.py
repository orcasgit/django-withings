# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-09-11 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nokiaapp', '0005_migrate_oauth_tokens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nokiauser',
            name='access_token_secret',
        ),
    ]
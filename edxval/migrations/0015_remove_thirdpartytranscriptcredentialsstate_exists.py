# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-06 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edxval', '0014_transcript_credentials_state_retype_exists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdpartytranscriptcredentialsstate',
            name='exists',
        ),
    ]

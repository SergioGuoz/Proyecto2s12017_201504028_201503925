# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170429_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar',
            old_name='desc',
            new_name='descripcion',
        ),
    ]
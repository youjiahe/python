# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-04 19:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops_tools1', '0002_ansimod_modargs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosts',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='modargs',
            old_name='mod_id',
            new_name='mod',
        ),
    ]
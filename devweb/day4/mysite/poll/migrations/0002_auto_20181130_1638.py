# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-30 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='q',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='question_tesxt',
            new_name='question_text',
        ),
    ]

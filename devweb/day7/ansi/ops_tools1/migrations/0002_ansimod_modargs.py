# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-04 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ops_tools1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsiMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulename', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ModArgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arg_text', models.CharField(max_length=300)),
                ('mod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops_tools1.AnsiMod')),
            ],
        ),
    ]

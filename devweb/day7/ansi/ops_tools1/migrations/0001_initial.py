# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-04 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True)),
                ('ipaddr', models.CharField(max_length=15, unique=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops_tools1.HostGroup')),
            ],
        ),
    ]
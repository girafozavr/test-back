# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-08-19 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Params',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limiter', models.CharField(default='ET', max_length=2, unique=True)),
                ('cpu', models.FloatField()),
                ('ram', models.FloatField()),
                ('disc', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('is_enabled', models.BooleanField()),
                ('is_started', models.BooleanField()),
                ('enable_action', models.CharField(blank=True, choices=[('', ''), ('EE', 'enable'), ('DE', 'disable')], default='', max_length=2)),
                ('launch_action', models.CharField(blank=True, choices=[('', ''), ('ST', 'start'), ('SP', 'stop'), ('RT', 'restart')], default='', max_length=2)),
            ],
        ),
    ]

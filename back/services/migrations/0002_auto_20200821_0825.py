# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-08-21 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='params',
            name='disc',
        ),
        migrations.AlterField(
            model_name='params',
            name='cpu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='params',
            name='ram',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.TextField(),
        ),
    ]
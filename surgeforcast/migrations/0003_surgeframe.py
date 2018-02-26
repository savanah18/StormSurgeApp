# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-11 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surgeforcast', '0002_auto_20180211_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurgeFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('customFile', models.CharField(max_length=200)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surgeforcast.SurgeEvent')),
            ],
        ),
    ]

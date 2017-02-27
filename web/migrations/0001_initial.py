# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-13 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('publication_date', models.DateTimeField()),
            ],
        ),
    ]

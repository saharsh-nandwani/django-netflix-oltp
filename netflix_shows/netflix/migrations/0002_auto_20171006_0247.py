# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('castName', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Puppy',
        ),
    ]
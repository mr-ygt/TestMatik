# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-28 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('sınıf', models.IntegerField()),
                ('ders', models.CharField(max_length=100)),
                ('konu', models.CharField(max_length=100)),
                ('zorluk', models.IntegerField()),
                ('soru', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['sınıf'],
            },
        ),
    ]
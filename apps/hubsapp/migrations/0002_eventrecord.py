# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-23 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='Title')),
                ('slug', models.SlugField(max_length=400, verbose_name='Slug')),
                ('full_description', models.TextField(blank=True, null=True, verbose_name='Full description')),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='Logo')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers', verbose_name='Cover Image')),
                ('type', models.CharField(blank=True, choices=[('offline', 'Offline'), ('online', 'Online'), ('both', 'Online and Offline')], max_length=100, null=True, verbose_name='Type')),
                ('cost', models.CharField(blank=True, choices=[('free', 'Free'), ('paid', 'Paid')], max_length=100, null=True, verbose_name='Cost')),
                ('phone1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone 1')),
                ('phone2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone 2')),
                ('phone3', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone 3')),
                ('website', models.CharField(blank=True, max_length=4000, null=True, verbose_name='Website')),
                ('address', models.CharField(blank=True, max_length=400, null=True, verbose_name='Address')),
                ('email', models.CharField(blank=True, max_length=400, null=True, verbose_name='E-mail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('cities', models.ManyToManyField(blank=True, related_name='eventsapp_city', to='hubsapp.City', verbose_name='Cities')),
                ('tags', models.ManyToManyField(blank=True, related_name='eventsapp_tag', to='hubsapp.Tag', verbose_name='Теги')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
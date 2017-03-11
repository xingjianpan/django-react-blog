# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'settings'},
        ),
        migrations.AlterField(
            model_name='settings',
            name='about',
            field=models.TextField(blank=True, default='', null=True, verbose_name='About page (markdown)'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='analytics',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='Google Analytics tracking nuber (UA-XXXXXXXX).'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='author',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='description',
            field=models.TextField(blank=True, max_length=512, verbose_name='Google results description (ideally under 160 characters)'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='image_social',
            field=models.ImageField(default='/media/img/social-card.png', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
    ]
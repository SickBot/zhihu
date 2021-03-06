# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-15 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_page', '0012_auto_20170114_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='like_or',
            field=models.CharField(default='normal', max_length=10),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user_vote',
            field=models.ManyToManyField(blank=True, related_name='user_vote_answer', to='site_page.UserProfile'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-26 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_page', '0016_comment_child'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='child',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='site_page.Comment'),
        ),
    ]

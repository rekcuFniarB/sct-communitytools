# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 20:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sphboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boarduserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='extendedcategoryconfig',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sphboard.Category'),
        ),
        migrations.AlterField(
            model_name='postannotation',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='annotation', to='sphboard.Post'),
        ),
    ]
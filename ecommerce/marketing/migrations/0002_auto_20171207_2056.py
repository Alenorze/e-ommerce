# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketingpreference',
            old_name='update',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='marketingpreference',
            name='mailchimp_subscribed',
            field=models.NullBooleanField(),
        ),
    ]

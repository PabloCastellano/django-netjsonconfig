# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0002_config_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='last_ip',
            field=models.GenericIPAddressField(blank=True, help_text='indicates the last ip from which the configuration was downloaded from (except downloads from this page)', null=True),
        ),
    ]

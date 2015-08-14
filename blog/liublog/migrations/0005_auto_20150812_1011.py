# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liublog', '0004_auto_20150808_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'IP',
                'verbose_name_plural': 'IP',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['index', 'id'], 'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
    ]

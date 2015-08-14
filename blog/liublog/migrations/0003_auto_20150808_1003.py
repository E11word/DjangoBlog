# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liublog', '0002_auto_20150808_0948'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='catagory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='links',
            name='description',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x8f\x8b\xe6\x83\x85\xe9\x93\xbe\xe6\x8e\xa5\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
    ]

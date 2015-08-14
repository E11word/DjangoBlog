# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liublog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='index',
            field=models.IntegerField(default=999, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\x9a\x84\xe6\x8e\x92\xe5\xba\x8f'),
        ),
    ]

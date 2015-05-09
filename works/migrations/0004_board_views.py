# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_remove_board_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

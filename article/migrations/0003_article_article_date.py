# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_remove_article_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(default=datetime.date(2014, 10, 21)),
            preserve_default=False,
        ),
    ]

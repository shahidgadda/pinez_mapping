# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0002_auto_20150626_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadgets',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gadgets',
            name='image',
            field=models.ImageField(upload_to=b'media/images/'),
        ),
    ]

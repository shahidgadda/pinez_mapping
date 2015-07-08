# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0003_auto_20150626_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadgets',
            name='image',
            field=models.ImageField(upload_to=b'media/pictures/'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gadgets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(null=True, blank=True)),
                ('category', models.CharField(max_length=1, choices=[(b'0', b'laptops'), (b'1', b'desktops'), (b'2', b'tablets')])),
                ('price', models.FloatField(null=True)),
                ('image', models.ImageField(upload_to=b'static/media/products/images')),
            ],
        ),
    ]

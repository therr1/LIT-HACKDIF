# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athand', '0002_userprofile_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentableObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

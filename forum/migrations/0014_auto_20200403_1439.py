# Generated by Django 2.2.11 on 2020-04-03 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_auto_20200403_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 14, 39, 45, 23990)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 14, 39, 45, 23270)),
        ),
    ]

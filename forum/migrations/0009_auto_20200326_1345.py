# Generated by Django 2.2.11 on 2020-03-26 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20200326_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 13, 45, 9, 454202)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 13, 45, 9, 453557)),
        ),
    ]

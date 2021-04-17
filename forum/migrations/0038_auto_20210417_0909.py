# Generated by Django 3.1.7 on 2021-04-17 13:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0037_auto_20210416_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='postsignature',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 9, 9, 39, 933617)),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='member_since',
            field=models.DateField(default=datetime.datetime(2021, 4, 17, 13, 9, 39, 931621, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 9, 9, 39, 932619)),
        ),
        migrations.AlterField(
            model_name='post',
            name='editted_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 9, 9, 39, 932619)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 9, 9, 39, 931621)),
        ),
    ]

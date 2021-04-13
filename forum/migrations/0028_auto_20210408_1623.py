# Generated by Django 3.1.7 on 2021-04-08 20:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0027_auto_20210408_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='editted_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 16, 23, 5, 877661)),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='member_since',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 20, 23, 5, 876662, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 16, 23, 5, 877661)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 16, 23, 5, 877661)),
        ),
    ]
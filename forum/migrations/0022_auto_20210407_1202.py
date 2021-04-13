# Generated by Django 3.1.7 on 2021-04-07 16:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_auto_20210407_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.thread'),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='member_since',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 16, 2, 32, 109064, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 12, 2, 32, 111060)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 12, 2, 32, 110062)),
        ),
    ]
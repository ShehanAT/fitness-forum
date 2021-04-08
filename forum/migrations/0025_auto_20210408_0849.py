# Generated by Django 3.1.7 on 2021-04-08 12:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0024_auto_20210407_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='started_by',
        ),
        migrations.AddField(
            model_name='thread',
            name='started_by_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='member_since',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 12, 49, 21, 211983, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 8, 49, 21, 213978)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 8, 49, 21, 212980)),
        ),
    ]

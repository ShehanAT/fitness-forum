# Generated by Django 3.2 on 2021-05-09 01:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0051_auto_20210508_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 463340)),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='member_since',
            field=models.DateField(default=datetime.datetime(2021, 5, 9, 1, 9, 38, 461348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 464338)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 466332)),
        ),
        migrations.AlterField(
            model_name='post',
            name='editted_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 466332)),
        ),
        migrations.AlterField(
            model_name='postsignature',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 468326)),
        ),
        migrations.AlterField(
            model_name='postvote',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 468326)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 465335)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='latest_post_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 21, 9, 38, 465335)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='started_by_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.forumuser'),
        ),
    ]

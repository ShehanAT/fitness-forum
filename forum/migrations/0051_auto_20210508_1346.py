# Generated by Django 3.1.7 on 2021-05-08 17:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0050_auto_20210508_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 479141)),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='member_since',
            field=models.DateField(default=datetime.datetime(2021, 5, 8, 17, 46, 38, 478144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 482133)),
        ),
        migrations.AlterField(
            model_name='post',
            name='editted_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 482133)),
        ),
        migrations.AlterField(
            model_name='postsignature',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 483130)),
        ),
        migrations.AlterField(
            model_name='postvote',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 484127)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 480138)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='latest_post_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 480138)),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateField(default=datetime.datetime(2021, 5, 8, 13, 46, 38, 480138))),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.category')),
            ],
        ),
    ]
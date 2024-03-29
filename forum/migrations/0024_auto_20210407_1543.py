# Generated by Django 3.1.7 on 2021-04-07 19:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0023_auto_20210407_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessprofile',
            name='profile_user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='member_since',
            field=models.DateField(default=datetime.datetime(2021, 4, 7, 19, 43, 12, 586906, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 15, 43, 12, 587902)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 15, 43, 12, 587902)),
        ),
        migrations.CreateModel(
            name='PostSignature',
            fields=[
                ('signature_id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('signature_picture', models.ImageField(blank=True, null=True, upload_to='signature_pics/%Y/%m/%d')),
                ('signature_for_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

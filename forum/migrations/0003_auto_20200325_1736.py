# Generated by Django 2.2.11 on 2020-03-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200325_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='forum_id',
            new_name='category',
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-06 19:03

import datetime
from django.db import migrations, models


FITNESSGOAL = [
        ('build_muscle', 'build_muscle'),
        ('lose_fat', 'lose_fat'),
        ('improve_sport', 'improve_sport'),
        ('endurance', 'endurance'),
        ('flexibility', 'flexibility'),
        ('other', 'other')
]

class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0015_auto_20210406_1139')
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='post',
        #     name='posted_by_id',

        # ),

        # migrations.AddField(
        #     model_name='post',
        #     name='posted_by_id',
        #     field=models.ForeignKey(to='django.contrib.auth.models.User', null=True, on_delete=models.CASCADE)
        # ),

        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 15, 3, 52, 148616)),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 15, 3, 52, 148616)),
        ),
    
    
        migrations.CreateModel(
            name='fitness_profile',
            fields=[
                ('fitness_profile_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='fitness_profile_id')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('body_fat_percentage', models.DecimalField(max_digits=2, decimal_places=2)),
                ('fitness_goal', models.CharField(max_length=100, choices=FITNESSGOAL))
            ]
        ),

        # migrations.AddField(
        #     model_name='fitness_profile',
        #     name='user_id_fk',
        #     field=models.ForeignKey(to='django.contrib.auth.models.User', null=False, on_delete=models.CASCADE)
        # )
    ]

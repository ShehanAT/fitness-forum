from django.db import models
from datetime import datetime
from django.conf import settings 
from enum import Enum 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import logging 

logger = logging.getLogger()
class ForumUser(User):

    class Gender(models.TextChoices):
        male = 'M', _('Male')
        female = 'F', _('Female')

    member_since = models.DateField(default=timezone.now())
    gender = models.CharField(max_length=1, choices=Gender.choices)
    rep_points = models.IntegerField()

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name 

class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    started_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    views = models.IntegerField()
    replies = models.IntegerField()
    created_on = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return "Topic: " + self.subject + "Started By: " + self.started_by

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    # add default to posted_by_id
    posted_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    # reply_to_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    first_reply_to_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='first_reply')
    second_reply_to_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='second_reply')
    rep_count = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=datetime.now())
    editted_on = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return "Posted by: " + self.posted_by_id + ", On: " + str(self.created_on)
    
    def set_first_reply_message(self):
        first_reply_post = Post.objects.get(post_id=self.first_reply_to_id.post_id)
        reply_to_msg = first_reply_post.message
        self.first_reply_message = reply_to_msg
        return first_reply_post

    def set_second_reply_message(self, first_reply_post):
        try:
            second_reply_post = Post.objects.get(post_id=first_reply_post.first_reply_to_id.post_id)
            self.second_reply_message = second_reply_post.message 
        except ObjectDoesNotExist as e:
            logger.error(e)
        except AttributeError as e:
            logger.error(e)


class FitnessProfile(models.Model):

    class FitnessGoals(models.TextChoices):
        build_muscle = 'build_muscle', _('build_muscle')
        lose_fat = 'lose_fat', _('lose_fat')
        improve_sport = 'improve_sport', _('improve_sport')
        endurance = 'endurance', _('endurance')
        flexibility = 'flexibility', _('flexibility')
        other = 'other', _('other')

    fitness_profile_id = models.AutoField(primary_key=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    body_fat_percentage = models.DecimalField(max_digits=2, decimal_places=2)
    fitness_goal = models.CharField(max_length=100, choices=FitnessGoals.choices)
    profile_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class PostSignature(models.Model):
    signature_id = models.AutoField(primary_key=True)
    signature_for_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    message = models.TextField()
    signature_picture = models.ImageField(blank=True, null=True, upload_to='signature_pics/%Y/%m/%d')


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
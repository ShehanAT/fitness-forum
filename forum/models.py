from django.db import models
from datetime import datetime
from django.conf import settings 
from enum import Enum 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.constraints import UniqueConstraint
from ckeditor.fields import RichTextField
import logging 

logger = logging.getLogger()
class ForumUser(User):
    class Gender(models.TextChoices):
        male = 'M', _('Male')
        female = 'F', _('Female')
    forum_user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    profile_pic = models.ImageField(null=True, blank=True, upload_to='')
    profile_pic_path = ''
    member_since = models.DateField(default=timezone.now())
    gender = models.CharField(max_length=1, choices=Gender.choices)
    rep_points = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default='')
    about = models.TextField(max_length=2000, default='')

class UserFollowing(models.Model):
    user_id = models.ForeignKey(ForumUser, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(ForumUser, related_name="followers", on_delete=models.CASCADE)
    # Automatically set the field to now when the object is first created
    created_on = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name 

class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    started_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    views = models.IntegerField()
    replies = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    created_on = models.DateTimeField(default=datetime.now())
    latest_post_on = models.DateTimeField(default=datetime.now())
    
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return "Topic: " + self.subject + "Started By: " + self.started_by
    

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    thread_id = models.ForeignKey(Thread, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=1000, null=True)
    message = RichTextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    posted_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    first_reply_to_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='first_reply')
    second_reply_to_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='second_reply')
    rep_count = models.IntegerField(default=0)
    vote_value = ""
    voted_previous = False 
    signature = False 
    original_post = models.BooleanField(default=False) 
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
    message = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.now())

class PostVote(models.Model):
    vote_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(ForumUser, null=True, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now())
    class VoteValueChoice(models.IntegerChoices):
        upvote = 1, _('upvote')
        downvote = -1, _('downvote')
    vote_value = models.IntegerField(choices=VoteValueChoice.choices)

    def __str__(self):
        return "Vote Id: " + str(self.vote_id) + ", Post id: " + str(self.post_id) + ", User id: " + str(self.user_id)
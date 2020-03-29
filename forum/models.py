from django.db import models
from datetime import datetime

class Category(models.Model):
    category_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name 

class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    started_by = models.CharField(max_length=30)
    views = models.IntegerField()
    replies = models.IntegerField()
    created_on = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return "Topic: " + self.subject + "Started By: " + self.started_by

def get_foo():
    return Thread.objects.filter(thread_id=1).values()[0]["thread_id"]

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, default=get_foo)
    posted_by = models.CharField(max_length=30)
    message = models.CharField(max_length=2000)
    reply_to = models.IntegerField(default=0)
    reply_message = models.CharField(max_length=2000, blank=True, default="")
    created_on = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "Posted by: " + self.posted_by + ", On: " + self.date
    
    def replying_message(self):
        orignal_post_message = Post.objects.filter(post_id=self.reply_to).values()[0]["message"]
        self.reply_message = orignal_post_message

# Create your models here.

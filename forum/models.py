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
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    posted_by = models.CharField(max_length=30)
    message = models.CharField(max_length=2000)
    created_on = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return "Posted by: " + self.posted_by + ", On: " + self.date

# Create your models here.

from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name 

class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    started_by = models.CharField(max_length=30)
    views = models.IntegerField()
    replies = models.IntegerField()

    def __str__(self):
        return "Topic: " + self.topic + "Started By: " + self.started_by


# Create your models here.

from rest_framework import serializers
from .models import Category, Thread, Post, ForumUser, PostVote, PostSignature, Tag
import humanize 
from datetime import datetime, timezone
from django.utils.timesince import timesince

class ForumUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumUser 
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = "__all__"

class ThreadSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()
    class Meta:
        model = Thread 
        fields = ["thread_id", "category_id", "subject", "started_by_id", "views", "replies", "created_on"]

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return timesince(value)

class PostSerializer(serializers.ModelSerializer):
    thread_id = ThreadSerializer()
    created_on = TimestampField()
    def get_content(self, instance):
        from django.utils.safestring import mark_safe
        return mark_safe(instance.message)
   
    class Meta: 
        model = Post 
        fields = ('post_id', 'thread_id', 'title', 'message', 'tags', 'posted_by_id', 'rep_count', 'created_on', 'editted_on')


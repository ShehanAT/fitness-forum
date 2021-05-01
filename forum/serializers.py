from rest_framework import serializers
from .models import Category, Thread, Post, ForumUser, PostVote, PostSignature, Tag
import humanize 
from datetime import datetime, timezone
from django.utils.timesince import timesince


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
    # created_on = serializers.DateTimeField(format="%F-%d-%Y %H:%M:%S")
    created_on = TimestampField()
    def get_content(self, instance):
        from django.utils.safestring import mark_safe
        return mark_safe(instance.message)
    # def to_representation(self, instance):
    #     representation = super(PostSerializer, self).to_representation(instance)
    #     timedelta = (datetime.now(timezone.utc) - representation['created_on'])
    #     timedelta = humanize.naturaldelta(timedelta)
    #     representation['created_on'] = timedelta
    #     return representation
    # def FORMAT(self):
    #    from django.utils.timesince import timesince
    #    return timesince(self.created_on)
   
    class Meta: 
        model = Post 
        fields = ('post_id', 'thread_id', 'title', 'message', 'tags', 'posted_by_id', 'rep_count', 'created_on', 'editted_on')


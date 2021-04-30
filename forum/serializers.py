from rest_framework import serializers
from .models import Category, Thread, Post, ForumUser, PostVote, PostSignature, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category 
        fields = "__all__"

class ThreadSerializer(serializers.ModelSerializer):
    category_id = CategorySerializer()
    class Meta:
        model = Thread 
        fields = ["thread_id", "category_id", "subject", "started_by_id", "views", "replies", "created_on"]

class PostSerializer(serializers.ModelSerializer):
    thread_id = ThreadSerializer()

    def get_content(self, instance):
        from django.utils.safestring import mark_safe
        return mark_safe(instance.message)
    class Meta: 
        model = Post 
        fields = ('post_id', 'thread_id', 'title', 'message', 'tags', 'posted_by_id', 'rep_count', 'created_on', 'editted_on')


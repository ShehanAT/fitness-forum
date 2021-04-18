from django.contrib import admin
from .models import Category, Thread, Post
# Register your models here.

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)
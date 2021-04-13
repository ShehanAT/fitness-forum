
import os
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fitness_forum.settings")
django.setup()

from django.core.management import call_command

from django_seed import Seed 
import random
from forum.models import Category, Thread, Post
from django_seed import Seed 
from django.contrib.auth.models import User 
seeder = Seed.seeder()

category_num = 10
thread_num = 50
post_num = 100
# seeder.add_entity(Category, category_num)
# seeder.execute()


# seeder.add_entity(Thread, thread_num, {
#     'category_id': Category.objects.get(category_id=1),
#     'started_by_id': User.objects.get(id=1)
# })
# seeder.execute() 

# for i in range(thread_num):
#     thread = Thread.objects.get(thread_id=i+1)
#     thread.category_id = Category(category_id=random.randint(1, 10))
#     thread.started_by_id = User.objects.get(id=random.randint(1, 4))
#     thread.save()

# seeder.add_entity(Post, 100, {
#     'thread_id': Thread.objects.get(thread_id=1),
#     'posted_by_id': User.objects.get(id=1),
#     'first_reply_to_id': None,
#     'second_reply_to_id': None
# })
# seeder.execute()

# for i in range(post_num):
#     post = Post.objects.get(post_id=i+1)
#     post.thread_id = Thread.objects.get(thread_id=random.randint(1, 50))
#     post.posted_by_id = User.objects.get(id=random.randint(1, 4))
#     post.reply_to_id = Post.objects.get(post_id=random.randint(1, 100))
#     post.save()

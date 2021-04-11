from django.http import HttpResponseRedirect
from django.shortcuts import render 
from datetime import datetime
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.sessions.backends.db import SessionStore 
from django.shortcuts import redirect
from .forms import AddCategoryForm, AddThreadForm, SignUpForm, AddPostForm, ForumUserForm, ProfilePicForm
from .models import Category, Thread, Post, ForumUser
from django.core.files.uploadedfile import SimpleUploadedFile
import logging 

logger = logging.getLogger(__name__)
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            user = ForumUser.objects.create_user(username, email, password1)
            user.save()
            # redirect to /login
            return redirect("/login")
            # return render(request, "login.html", {"signup_success_msg": "Thanks for registering! Please login using your new credentials..."})
    else:
        form = SignUpForm()
    return render(request, "signup_view.html", {'signupForm': form})

def login_view(request):
    s = SessionStore()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        request.session['username'] = username
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session['logged_in'] = True
            categories = Category.objects.all().values()
            return redirect("/")
        else:
            return render(request, "login_view.html", {"errors": "Incorrect username/password combo"})
    else:
        request.session['logged_in'] = False 
        return render(request, "login_view.html", {})

def logout_view(request):
    logout(request)
    categories = Category.objects.all().values()
    return redirect("/")

def profile_view(request):
    forum_user = ForumUser.objects.get(id=request.user.id)
    profile_pic_form = ProfilePicForm(request.POST, request.FILES)
    if request.method == "POST":
        if "update_profile" in request.POST:
            pass 
        if "upload_profile_pic" in request.POST:
            if profile_pic_form.is_valid():
                avatar = profile_pic_form.cleaned_data.get('profile_pic')
                forum_user.profile_pic = avatar 
                forum_user.save()
    return render(request, "profile_view.html", {"user": forum_user, "profile_pic_form": profile_pic_form})

def forum_list_view(request):
    categories = Category.objects.all().values()
    for c in categories:
        threadCount = Thread.objects.filter(category_id=c['category_id']).count()
        threads = Thread.objects.filter(category_id=c['category_id'])
        postCounter = 0
        for i in threads:
            postCount = Post.objects.filter(thread_id=i.thread_id).count()
            postCounter += postCount
        c["threadNum"] = threadCount
        c["postNum"] = postCounter 
    
    return render(request, 'forum_list_view.html', {'categories': categories})

def add_category_view(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category_description = form.cleaned_data['category_description']
            category = Category(name=category_name, description=category_description)
            category.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'add_category_view.html', {})
    else:
        return render(request, 'add_category_view.html')

def category_detail_view(request, category_id):
    category = Category.objects.filter(category_id=category_id)
    threads = Thread.objects.filter(category_id=category_id).values()
    try:
        for thread in threads:
            posts = Post.objects.filter(thread_id=thread["thread_id"]).order_by("created_on")
            posted_user_id = posts.first().posted_by_id.id
            username = User.objects.get(id=posted_user_id).get_username()
            thread["started_by"] = username 
            print("Thread Subject", thread["subject"],"Views: ", thread["views"])
    except AttributeError as e:
        logger.error("ERROR: " + str(e))
    return render(request, "category_detail_view.html", {"category": category.values()[0], "category_id": category_id, "threads": threads})

def add_thread_view(request, category_id):
    category = Category.objects.filter(category_id=category_id).values()
    if request.method == "POST":
        form = AddThreadForm(request.POST)
        if form.is_valid():
            thread_subject = form.cleaned_data['subject']
            thread_message = form.cleaned_data['message']
            new_thread = Thread(subject=thread_subject, category_id=category_id, views=0, replies=0)
            new_thread.save()
            new_post = Post(message=thread_message, posted_by="ShehanTest", thread_id=new_thread.thread_id)
            new_post.save()
        redirect_url = "/category/" + str(category_id)
        return redirect(redirect_url)
    else:
        return render(request, "add_thread_view.html", {"category_name": category[0]['name']})

def thread_detail_view(request, category_id, thread_id):
    posts = Post.objects.filter(thread_id=thread_id).order_by("created_on")
    category_name = Category.objects.get(category_id=category_id).name
    thread_name = Thread.objects.get(thread_id=thread_id).subject
    thread = Thread.objects.get(thread_id=thread_id)
    thread.views = thread.views + 1
    thread.save()
    for post in posts:
        if post.first_reply_to_id != None and post.first_reply_to_id.post_id > 0:
            first_reply_post = post.set_first_reply_message()
            post.set_second_reply_message(first_reply_post)
    return render(request, "thread_detail_view.html", {"posts":  posts, "category_id": category_id, "thread_id": thread_id, "thread_name": thread_name, "category_name": category_name})

def add_post_view(request, category_id, thread_id):
    category_name = Category.objects.filter(category_id=category_id).values()[0]["name"]
    thread = Thread.objects.get(thread_id=thread_id)
    thread_subject = thread.subject
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post_message = form.cleaned_data["message"]
            new_post = Post(message=post_message, posted_by_id=user, thread_id=thread, created_on=datetime.now(), reply_to_id=None)
            new_post.save()
        redirect_url = "/category/" + str(category_id) + "/thread/" + str(thread_id)
        return redirect(redirect_url)
    else:
        return render(request, "add_post_view.html", {"category_name": category_name, "thread_name": thread_subject })

def add_reply_post_view(request, category_id, thread_id, post_id):
    category_name = Category.objects.filter(category_id=category_id).values()[0]["name"]
    thread = Thread.objects.get(thread_id=thread_id)
    thread_subject = thread.subject
    user = User.objects.get(id=request.user.id)
    reply_post = Post.objects.get(post_id=post_id)
    reply_post_id = reply_post.post_id
    reply_post_message = reply_post.message
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            thread = Thread.objects.get(thread_id=thread_id)
            thread.replies = thread.replies + 1
            thread.save()
            post_message = form.cleaned_data["message"]
            new_post = Post(message=post_message, posted_by_id=user, thread_id=thread, created_on=datetime.now(), first_reply_to_id=reply_post, second_reply_to_id=reply_post.first_reply_to_id)
            new_post.save()
        redirect_url = "/category/" + str(category_id) + "/thread/" + str(thread_id)
        return redirect(redirect_url)
    else:
        return render(request, "add_reply_post_view.html", {"category_name": category_name, "category_id": category_id, "thread_subject": thread_subject, "reply_post_message": reply_post_message, "thread_id": thread_id})

def test_view(request):
    request.session["login_status"] = "Thanks for registering! Please login using your new credentials..."
    return render(request, "login_view.html", {})

def image_upload_view(request):
    '''Process images uploaded by users'''
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance 
            return render (request, "test_image_upload.html", {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, "test_image_upload.html", {'form': form})
from django.http import HttpResponseRedirect
from django.shortcuts import render 
from datetime import datetime
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.sessions.backends.db import SessionStore 
from django.shortcuts import redirect
from .forms import AddCategoryForm, AddThreadForm, SignUpForm, AddPostForm 
from .models import Category, Thread, Post 

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            user = User.objects.create_user(username, email, password1)
            user.save()
            return render(request, "signup.html", {"signupForm": form})
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'signupForm': form})
def Login(request):
    s = SessionStore()
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            categories = Category.objects.all().values()
            return redirect("/")
        else:
            return render(request, "login.html", {"errors": "Incorrect username/password combo"})
    else:
        return render(request, "login.html", {})

def Logout(request):
    logout(request)
    categories = Category.objects.all().values()
    return redirect("/")

def Profile(request):
    user = request.user
    return render(request, "profileView.html", {"user": user})

def ForumListView(request):
    categories = Category.objects.all().values()
    for c in categories:
        threads = Thread.objects.filter(category_id=c['category_id']).count()
        c["threadNum"] = threads
    return render(request, 'forumListView.html', {'categories': categories})

def ForumAddCategoryView(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category_description = form.cleaned_data['category_description']
            category = Category(name=category_name, description=category_description)
            category.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'forumAddCategory.html', {})
    else:
        return render(request, 'forumAddCategory.html')

def categorydetail(request, category_id):
    category = Category.objects.filter(category_id=category_id)
    threads = Thread.objects.filter(category_id=category_id).values()
    return render(request, "categoryDetailView.html", {"category": category.values()[0], "category_id": category_id, "threads": threads})

def addThread(request, category_id):
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
        return render(request, "addThreadView.html", {})
    else:
        return render(request, "addThreadView.html", {"category_name": category[0]['name']})

def threadDetail(request, category_id, thread_id):
    posts = Post.objects.filter(thread_id=thread_id).order_by("created_on")
    category_name = Category.objects.filter(category_id=category_id).values()[0]["name"]
    thread_name = Thread.objects.filter(thread_id=thread_id).values()[0]["subject"]
    for post in posts:
        if post.reply_to > 0:
            print("The post message is ", post.message)
            post.replying_message()
            # post.reply_message = post.replying_message()
            # print("The replying message is ", post.reply_message)
            # post["replying_to"] = orignal_post_message
            # print(post.message, " is a reply to post id:", post.reply_to)
    return render(request, "threadDetailView.html", {"posts":  posts, "category_id": category_id, "thread_id": thread_id, "thread_name": thread_name, "category_name": category_name})

def addpost(request, category_id, thread_id):
    category_name = Category.objects.filter(category_id=category_id).values()[0]["name"]
    thread_subject = Thread.objects.filter(thread_id=thread_id).values()[0]["subject"]
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post_message = form.cleaned_data["message"]
            new_post = Post(message=post_message, posted_by=request.user, thread_id=thread_id, created_on=datetime.now())
            new_post.save()
        redirect_url = "/category/" + str(category_id) + "/thread/" + str(thread_id)
        return redirect(redirect_url)
    else:
        return render(request, "addPostView.html", {"category_name": category_name, "thread_subject": thread_subject })

def addreplypost(request, category_id, thread_id, post_id):
    category_name = Category.objects.filter(category_id=category_id).values()[0]["name"]
    thread_subject = Thread.objects.filter(thread_id=thread_id).values()[0]["subject"]
    reply_post = Post.objects.filter(post_id=post_id).values()[0]
    reply_post_id = reply_post["post_id"]
    reply_post_message = reply_post["message"]
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            post_message = form.cleaned_data["message"]
            new_post = Post(message=post_message, posted_by=request.user, thread_id=thread_id, created_on=datetime.now(), reply_to=reply_post_id)
            new_post.save()
        redirect_url = "/category/" + str(category_id) + "/thread/" + str(thread_id)
        return redirect(redirect_url)
    else:
        return render(request, "addReplyPostView.html", {"category_name": category_name, "category_id": category_id, "thread_subject": thread_subject, "reply_post_message": reply_post_message, "thread_id": thread_id})
# Create your views here.

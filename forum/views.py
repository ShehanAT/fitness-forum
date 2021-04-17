from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render 
from datetime import datetime
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.sessions.backends.db import SessionStore 
from django.shortcuts import redirect
from .forms import AddCategoryForm, AddThreadForm, SignUpForm, AddPostForm, ForumUserForm, ProfilePicForm, UpdateProfileForm, ChangePasswordForm, PostSignatureForm
from .models import Category, Thread, Post, ForumUser, PostVote, PostSignature 
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ObjectDoesNotExist
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
    try:
        forum_user = ForumUser.objects.get(id=request.user.id)
        user = User.objects.get(id=request.user.id)
    except ObjectDoesNotExist as e:
        logger.error(e)
        request.session["status_msg"] = "Password reset successfully! Please login using your new password..."
        return redirect("/login")
    profile_pic_form = ProfilePicForm(request.POST, request.FILES)
    post_signature_form = PostSignatureForm(request.POST)
    if request.method == "POST":
        if "update_profile" in request.POST:
            update_profile_form = UpdateProfileForm(data=request.POST, instance=forum_user)
            if update_profile_form.is_valid():
                update_profile_form.save()
                return redirect("/profile") 
            return render(request, "profile_view.html", {"user": forum_user, "profile_pic_form": profile_pic_form, "update_profile_form": update_profile_form, "change_password_form": ChangePasswordForm(user=user), "post_signature_form": post_signature_form})
        elif "upload_profile_pic" in request.POST:
            if profile_pic_form.is_valid():
                avatar = profile_pic_form.cleaned_data.get('profile_pic')
                forum_user.profile_pic = avatar 
                forum_user.save()
            return render(request, "profile_view.html", {"user": forum_user, "profile_pic_form": profile_pic_form, "update_profile_form": UpdateProfileForm(instance=forum_user), "change_password_form": ChangePasswordForm(user=user), "post_signature_form": post_signature_form})
        elif "update_password" in request.POST:
            change_password_form = ChangePasswordForm(data=request.POST, user=user)
            if change_password_form.is_valid():
                change_password_form.save() 
                return redirect("/profile")
            return render(request, "profile_view.html", {"user": forum_user, "profile_pic_form": profile_pic_form, "update_profile_form": UpdateProfileForm(instance=forum_user), "change_password_form": change_password_form, "post_signature_form": post_signature_form})
        elif "upload_post_signature" in request.POST:
            if post_signature_form.is_valid():
                user = User.objects.get(id=request.user.id)
                post_signature = PostSignature()
                post_signature.signature_for_id = user 
                post_signature.message = post_signature_form.cleaned_data["content"]
                post_signature.save()
            return render(request, "profile_view.html", {"user": forum_user, "profile_pic_form": profile_pic_form, "update_profile_form": UpdateProfileForm(instance=forum_user), "change_password_form": ChangePasswordForm(user=user), "post_signature_form": post_signature_form})

    else:
        return render(request, "profile_view.html", {"user": forum_user, "profile_pic_form": profile_pic_form, "update_profile_form": UpdateProfileForm(instance=forum_user), "change_password_form": ChangePasswordForm(user=user), "post_signature_form": post_signature_form})

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
        if len(PostVote.objects.filter(post_id=post.post_id, user_id=request.user.id)) > 0:
            # vote found, user is not allowed to vote on this post 
            post.vote = False 
        else:
            # vote not found, user is allowed to vote on this post 
            post.vote = True 
        # get post signature is user uploaded it 
        try:
            post_signature = PostSignature.objects.filter(signature_for_id=post.posted_by_id.id).latest('created_on')
            post.signature = post_signature 
        except ObjectDoesNotExist: 
            post.signature = None 
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
            new_post = Post(message=post_message, posted_by_id=user, thread_id=thread, created_on=datetime.now())
            new_post.save()
        redirect_url = "/category/" + str(category_id) + "/thread/" + str(thread_id)
        return redirect(redirect_url)
    else:
        form = AddPostForm()
        return render(request, "add_post_view.html", {"category_name": category_name, "thread_name": thread_subject, "form": form })

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

def vote(request):
    if request.method == "POST":
        user = ForumUser.objects.get(id=request.user.id)
        # second param in request.GET.get is the default value if required param is not found
        category_id = request.POST.get('category_id', '')
        thread_id = request.POST.get('thread_id', '')
        vote_value = int(request.POST.get('vote_value', ''))
        post = Post.objects.get(post_id=request.POST.get('post_id', ''))
        response_data = {}
        post.rep_count += vote_value
        new_vote = PostVote.objects.create(post_id=post, user_id=user, vote_value=1)
        posted_by_user = ForumUser.objects.get(id=post.posted_by_id.id)
        if posted_by_user.id != user.id:
            # current user is not the original poster of current post so increment/decrement their rep_points by 1 
            posted_by_user.rep_points += vote_value 
        post.save() 
        new_vote.save()
        posted_by_user.save()
        response_data['post_rep_count'] = post.rep_count
        return JsonResponse(response_data)
    else:
        return redirect("/category/" + category_id + "/thread/" + thread_id)

def test_view(request):
    request.session["login_status"] = "Thanks for registering! Please login using your new credentials..."
    return render(request, "login_view.html", {})
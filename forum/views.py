from django.http import HttpResponseRedirect
from django.shortcuts import render 
from datetime import datetime
from .forms import AddCategoryForm, AddThreadForm, SignUpForm
from .models import Category, Thread, Post 


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'signupForm': form})

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
            new_post = Post(message=thread_message, posted_by="ShehanTest")
            new_post.save()
        return render(request, "addThreadView.html", {})
    else:
        return render(request, "addThreadView.html", {"category_name": category[0]['name']})
# Create your views here.

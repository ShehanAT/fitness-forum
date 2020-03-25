from django.http import HttpResponseRedirect
from django.shortcuts import render 

from .forms import AddCategoryForm
from .models import Category
def ForumListView(request):
    categories = Category.objects.all()
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


# Create your views here.

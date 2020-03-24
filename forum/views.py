from django.shortcuts import render


def ForumListView(request):
    return render(request, 'forumListView.html', {})

# Create your views here.

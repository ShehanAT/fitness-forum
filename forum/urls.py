from django.urls import path 
from forum import views 

urlpatterns = [
    path('', views.ForumListView, name='forum'),
    path('addCategory/', views.ForumAddCategoryView)
]
from django.urls import path 
from forum import views 

urlpatterns = [
    path('', views.ForumListView, name='forum'),
    path('signup', views.SignUp),
    path('addCategory/', views.ForumAddCategoryView),
    path('category/<int:category_id>/', views.categorydetail),
    path('category/<int:category_id>/addThread', views.addThread)
]
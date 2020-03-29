from django.urls import path 
from forum import views 

urlpatterns = [
    path('', views.ForumListView, name='forum'),
    path('signup', views.SignUp),
    path('login', views.Login),
    path('logout', views.Logout),
    path('addCategory/', views.ForumAddCategoryView),
    path('category/<int:category_id>/', views.categorydetail),
    path('category/<int:category_id>/addThread', views.addThread),
    path('category/<int:category_id>/thread/<int:thread_id>', views.threadDetail),
    path('category/<int:category_id>/thread/<int:thread_id>/addPost', views.addpost),
    path('category/<int:category_id>/thread/<int:thread_id>/replyPost/<int:post_id>', views.addreplypost)
]
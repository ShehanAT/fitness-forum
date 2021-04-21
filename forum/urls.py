from django.urls import path, include
from django.contrib.auth import views as auth_views  
from forum import views 

urlpatterns = [
    path('', views.index_view),
    path('categories', views.index_view),
    path('signup', views.signup_view),
    path('login', views.login_view),
    # url(r'^login/$', auth_views.login, {'template_name': 'static/page-login.html'} , name='login'),
    path('logout', views.logout_view),
    path('profile', views.profile_view),
    path('add_category', views.add_category_view),
    path('category/<int:category_id>/', views.category_detail_view),
    path('category/<int:category_id>/add_thread', views.add_thread_view),
    path('category/<int:category_id>/thread/<int:thread_id>', views.thread_detail_view),
    path('category/<int:category_id>/thread/<int:thread_id>/add_post', views.add_post_view),
    path('category/<int:category_id>/thread/<int:thread_id>/reply_post/<int:post_id>', views.add_reply_post_view),
    path('test', views.test_view),
    path('test-login', views.test_login),
    path('post_vote', views.vote),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
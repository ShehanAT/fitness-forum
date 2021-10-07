from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views  
from forum import views 
from fitness_forum import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

app_name = 'forum'

urlpatterns = [
    path('', views.index_view),
    path('categories', views.index_view),
    path('signup', views.signup_view, name="signup"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view),
    path('profile', views.profile_view, name="profile"),
    path('profile/show_profile', views.show_profile_view),
    path('profile/show_profile/following', views.show_profile_following_view),
    path('profile/show_profile/unfollow', views.show_profile_unfollow_view),
    path('profile/show_profile/followers', views.show_profile_followers_view),
    path('profile/update_profile', views.update_profile_view),
    path('profile/change_password', views.change_password_view),
    path('add_category', views.add_category_view, name="add_category"),
    path('category/<int:category_id>', views.category_detail_view),
    path('category/<int:category_id>/add_thread', views.add_thread_view),
    path('category/<int:category_id>/thread/<int:thread_id>', views.thread_detail_view),
    path('category/<int:category_id>/thread/<int:thread_id>/add_post', views.add_post_view),
    path('category/<int:category_id>/thread/<int:thread_id>/reply_post/<int:post_id>', views.add_reply_post_view),
    path('category/<int:category_id>/thread/<int:thread_id>/edit_post/<int:post_id>', views.edit_post_view),
    path('test', views.test_view),
    path('test-login', views.test_login),
    path('post_vote', views.vote),
    path('trending', views.trending_view),
    path('about', views.about_view),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact_us', views.contact_us_view)
]
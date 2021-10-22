from django.contrib.sessions.backends.base import SessionBase
import pytest
from django.urls import reverse 
from django.test.client import RequestFactory
from forum.forms import ProfilePicForm
from forum.views import login_view, signup_view, show_profile_view
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from http.cookies import SimpleCookie
import requests 
from django.middleware import csrf
from django.test import TestCase
from forum.models import ForumUser
from tests.conftest import ConfTest
   
   
class TestProfilePage(TestCase):
    @pytest.mark.django_db
    def test_GET_show_profile_page_appears_after_login(self):
        ConfTest.test_register_success(self)
        forum_user = ForumUser.objects.get(username="admin")
        
        show_profile_url = reverse("forum:show_profile")

        # show_profile_data = dict(
        #     user=forum_user,
        # )
        # profile_pic_form = ProfilePicForm()
        self.client.force_login(forum_user)    
        response = self.client.get(show_profile_url)
        print(response.context)
        # print(response.content)
        assert response.status_code == 200
        assert response.context['all_activity'] != None 


    @pytest.mark.django_db 
    def test_GET_show_profile_following_page_appears_after_login(self):
        ConfTest.test_register_success(self)
        forum_user = ForumUser.objects.get(username="admin")
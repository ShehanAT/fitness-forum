from django.contrib.sessions.backends.base import SessionBase
import pytest
from django.urls import reverse 
from django.test.client import RequestFactory
from forum.views import login_view, signup_view, show_profile_view
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from http.cookies import SimpleCookie
import requests 
from django.middleware import csrf
from django.test import TestCase
from forum.models import ForumUser
from .conftest import ConfTest

class TestAuthentication(TestCase):

    @pytest.mark.django_db
    def test_index_page_appears_after_login(self):
        # test_register_success(self)
        ConfTest.test_register_success(self)
        login_url = reverse("forum:login")

        login_data = dict(
            username="admin",
            password="Archimedes123",
        )
    
        response = self.client.post(login_url, data=login_data)
        print(response);
        assert response.status_code == 302
        assert response.url == "/"

    @pytest.mark.django_db
    def test_profile_page_appears_after_login(self):
        ConfTest.test_register_success(self)
        forum_user = ForumUser.objects.get(username="admin")
        
        profile_url = reverse("forum:profile")

        profile_data = dict(
            user=forum_user,
            # profile_pic=
        )

        self.client.force_login(forum_user)    
        response = self.client.get(profile_url, data=profile_data)
        # , data=show_profile_data
        # print("ForumUser count: " + str(ForumUser.objects.all()[0]))
        # print(response);
        # assert response.status_code == 200
        # assert response.url == "/"


from django.contrib.sessions.backends.base import SessionBase
import pytest
from django.urls import reverse 
from django.test.client import RequestFactory
from forum.views import login_view, signup_view
from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware
from http.cookies import SimpleCookie
import requests 
from django.middleware import csrf
from django.test import TestCase 
from forum.models import ForumUser


class TestAuthentication(TestCase):
    @pytest.mark.django_db
    def test_login_fail(self):
        # rf = RequestFactory()
        login_url = reverse("forum:login")

        login_data = dict(
            username="adminasdf",
            password="secret",
        )
    
        response = self.client.post(login_url, data=login_data)


        # login_request = rf.post(login_url, {"username": "failed_login", "password": "failed_login"})
        # login_response = login_view(login_request)
        # response_content = login_response.content.decode("utf-8")
    
        assert response.status_code == 200
        assert response.context['errors'] == ["Invalid Username/Password combination"]
        # assert response_content.find("Invalid Username/Password combination") != -1


    @pytest.mark.django_db
    def test_register_fail_empty_email(self):
        rf = RequestFactory()
        signup_url = reverse("forum:signup")
        signup_request = rf.post(signup_url, {"username": "abc", "email": "abc", "password1": "abc", "password2": "abc"})
        signup_response = signup_view(signup_request)
        response_content = signup_response.content.decode("utf-8")
        # print(response_content)
        assert signup_response.status_code == 200
        assert response_content.find("Enter a valid email address") != -1

    @pytest.mark.django_db
    def test_register_fail_password_errors(self):
        rf = RequestFactory()
        signup_url = reverse("forum:signup")
        signup_request = rf.post(signup_url, {"username": "abc", "email": "abc", "password1": "abc", "password2": "abc"})
        signup_response = signup_view(signup_request)
        response_content = signup_response.content.decode("utf-8")
        # print(response_content)
        assert signup_response.status_code == 200
        assert response_content.find("The password is too similar to the username") != -1
        assert response_content.find("This password is too short. It must contain at least 8 characters") != -1
        assert response_content.find("This password is too common") != -1

    @pytest.mark.django_db
    def test_login_success(self):
        register_url = reverse("forum:signup")
        register_data = {
            "username": "admin",
            "email": "admin@gmail.com",
            "password1": "Archimedes123",
            "password2": "Archimedes123"
        }
        register_response = self.client.post(register_url, register_data)
        print(register_response.context)
        print(register_response.content)

        login_url = reverse("forum:login")
  
        request = requests.session()

        login_data = dict(
            username="admin",
            password="Archimedes123",
    
        )
    
        response = self.client.post(login_url, data=login_data)


        print(response.context, end="\n")
        print(response.content, end="\n")

        assert response.status_code == 302
        assert ForumUser.objects.count() > 0
    



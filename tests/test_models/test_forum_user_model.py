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



class TestForumUserModel(TestCase):

    @pytest.mark.django_db
    def test_forum_user_(self):
        forum_user = ForumUser();
        assert forum_user is True 
        
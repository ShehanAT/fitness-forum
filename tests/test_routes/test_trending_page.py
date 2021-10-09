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
from .conftest import ConfTest



class TestTrendingPage(TestCase):
    @pytest.mark.django_db 
    def test_trending_page_appears_after_login(self):
        ConfTest.test_register_success(self)
        forum_user = ForumUser.objects.get(username="admin")

        trending_url = reverse("forum:trending")

        self.client.force_login(forum_user)
        response = self.client.get(trending_url)
        assert response.status_code == 200
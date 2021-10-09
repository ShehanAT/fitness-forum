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


class TestIndexPage(TestCase):
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
        assert response.status_code == 302
        assert response.url == "/"

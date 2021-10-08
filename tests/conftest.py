import pytest 
import factory
from pytest_factoryboy import register
from rest_framework.test import APIClient, APIRequestFactory 
from django.contrib.auth import get_user_model 
from forum.models import ForumUser
from django.contrib.auth.hashers import make_password
from django import VERSION as DJANGO_VERSION
from django.test import TestCase 
from django.urls import reverse 


class ConfTest(TestCase):

    @pytest.mark.django_db
    def test_register_success(self):
        register_url = reverse("forum:signup")
        register_data = {
            "id": 1,
            "username": "admin",
            "email": "admin@gmail.com",
            "password1": "Archimedes123",
            "password2": "Archimedes123"
        }
        register_response = self.client.post(register_url, register_data)
        assert register_response.status_code == 302
        assert ForumUser.objects.count() > 0


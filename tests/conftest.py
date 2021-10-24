import pytest 
import factory
from pytest_factoryboy import register
from rest_framework.test import APIClient, APIRequestFactory 
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User  
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

    @pytest.mark.django_db 
    def create_test_user(self):
        test_user = User.objects.create(
            username="test_user",
            email="test_user@test_user.com",
            password="test_user"
        )
        test_user.save()

        return test_user 

    @pytest.mark.django_db 
    def create_test_forum_user(self, username="", email=""):
        test_user = None 
        if username != "" and email != "":
            print("USERNAME AND EMAIL ENTERED" + username + ", " + email)
            test_user = User.objects.create(
                username=username,
                email=email,
                password="test_user"
            )
            test_user.save() 
        else:
            test_user = User.objects.create(
                username="test_user",
                email="test_user@test_user.com",
                password="test_user"
            )
            test_user.username = "test_user"
            test_user.email = "test_user@test_user.com"
            test_user.save()

        test_forum_user = ForumUser.objects.create(
            forum_user=test_user,
            gender="M",
        )

        test_forum_user.save()

        return test_forum_user

   



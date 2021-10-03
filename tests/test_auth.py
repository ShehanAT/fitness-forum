import pytest
from django.urls import reverse 
from django.test.client import RequestFactory
from forum.views import login_view, signup_view


@pytest.mark.django_db
def test_login_fail():
    rf = RequestFactory()
    login_url = reverse("forum:login")
    login_request = rf.post(login_url, {"username": "failed_login", "password": "failed_login"})
    login_response = login_view(login_request)
    response_content = login_response.content.decode("utf-8")
    # print(response_content.find("Invalid Username/Password combiasdfa"))
    # print(response_content.find("Invalid Username/Password combination"))
    assert login_response.status_code == 200
    assert response_content.find("Invalid Username/Password combination") != -1


@pytest.mark.django_db
def test_register_fail_empty_email():
    rf = RequestFactory()
    signup_url = reverse("forum:signup")
    signup_request = rf.post(signup_url, {"username": "abc", "email": "abc", "password1": "abc", "password2": "abc"})
    signup_response = signup_view(signup_request)
    response_content = signup_response.content.decode("utf-8")
    # print(response_content)
    assert signup_response.status_code == 200
    assert response_content.find("Enter a valid email address") != -1

@pytest.mark.django_db
def test_register_fail_password_errors():
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
def test_login_success(registered_user):
    # TO-DO, status: Need to have registered_user populated with assigned values in registered_user() fixture
    rf = RequestFactory()
    login_url = reverse("forum:login")
    login_request = rf.post(login_url, 
    {
        "username": registered_user.username, 
        "password": "secret"
    })
    login_response = login_view(login_request)
    response_content = login_response.content.decode("utf-8")
    print("username: " + registered_user.username)
    print("email: " + registered_user.email)
    print("password: " + registered_user.password)
    # print(response_content.find("Invalid Username/Password combiasdfa"))
    # print(response_content.find("Invalid Username/Password combination"))
    assert login_response.status_code == 200
    # assert response_content.find("Invalid Username/Password combination") == -1



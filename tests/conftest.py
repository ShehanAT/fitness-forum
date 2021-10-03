import pytest 
import factory
from pytest_factoryboy import register
from rest_framework.test import APIClient, APIRequestFactory 
from django.contrib.auth import get_user_model 
from forum.models import ForumUser
from django.contrib.auth.hashers import make_password
from django import VERSION as DJANGO_VERSION

@pytest.fixture
def session():
    engine = import_module(setting.SESSION_ENGINE)
    session = engine.SessionStore()
    session.create()
    return session 


@pytest.fixture 
def api_client():
    api_client = APIClient()
    return api_client 

@pytest.fixture
def api_rf():
    api_rf = APIRequestFactory()
    return api_rf 

# @pytest.fixture
# def registered_user():
#     user = ForumUserFactory(
#         username="admin",
#         email='admin@example.com', 
#         password=make_password('secret'), 
#         is_superuser=False,
#         first_name="admin",
#         last_name="admin",
#         is_active=True,
#         date_joined="2017-03-18 08:21:36.175627+07",
#         last_login="2017-03-20 08:21:36.175627+07"
#         )
#     registered_user = ForumUserFactory(user=user)
#     assert isinstance(registered_user, ForumUser)
#     return registered_user

@pytest.fixture
def registered_forum_user():
    registered_forum_user = ForumUserFactory(
        username="admin",
        email='admin@example.com', 
        password=make_password('secret'), 
        is_superuser=False,
        first_name="admin",
        last_name="admin",
        is_active=True,
        date_joined="2017-03-18 08:21:36.175627+07",
        last_login="2017-03-20 08:21:36.175627+07"
    )
    # registered_forum_user = ForumUserFactory(user=user)
    assert isinstance(registered_forum_user, ForumUser)
    return registered_forum_user


@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta: 
        model = get_user_model()

    @classmethod 
    def create(cls, **kwargs):
        user = super(UserFactory, cls).create(**kwargs)
        assert isinstance(user, get_user_model())
        if DJANGO_VERSION < (2,):
            assert user.is_authenticated() is True 
        else:
            assert user.is_authenticated is True 
        return user 
    username = factory.Sequence(lambda n: 'uid-{}'.format(n))
    password = 'secret'


@register 
class ForumUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ForumUser 

    @classmethod 
    def create(cls, **kwargs):
        forum_user = super(ForumUserFactory, cls).create(**kwargs)
        assert isinstance(forum_user, ForumUser)
        assert forum_user.is_authenticated is True 
        # assert forum_user.is_registered is True 
        return forum_user 

    # user = factory.SubFactory(UserFactory)


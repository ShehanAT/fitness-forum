import pytest 
import factory.fuzzy 
from rest_framework.test import APIClient, APIRequestFactory 
from django.contrib.auth import get_user_model 
from forum.models import ForumUser

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
        assert forum_user.is_registered is True 
        return forum_user 

    user = factory.SubFactory(UserFactory)


from forum.models import UserFollowing 
from django.test import TestCase 
import pytest 
from django.db.utils import IntegrityError 
from tests.conftest import ConfTest

class TestUserFollowingModel(TestCase):

    @pytest.mark.django_db
    def test_user_following_without_user_id_should_not_persist(self):
        user_following = UserFollowing()
        # user_following.user_id = ConfTest.create_test_forum_user(self)
        user_following.following_user_id = ConfTest.create_test_forum_user(self)
        with self.assertRaises(IntegrityError):
            user_following.save()

    @pytest.mark.django_db
    def test_user_following_without_following_user_id_should_not_persist(self):
        user_following = UserFollowing()
        user_following.user_id = ConfTest.create_test_forum_user(self)
        # user_following.following_user_id = ConfTest.create_test_forum_user(self)
        with self.assertRaises(IntegrityError):
            user_following.save()

    @pytest.mark.django_db
    def test_user_following_with_all_not_null_fields_should_persist(self):
        user_following = UserFollowing()

        user_1 = ConfTest.create_test_forum_user(self)
        user_following.user_id = user_1
        user_following.following_user_id = user_1
        
        user_following.save()
        assert UserFollowing.objects.count() > 0

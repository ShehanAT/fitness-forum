from forum.models import PostSignature, UserFollowing 
from django.test import TestCase 
import pytest 
from django.db.utils import IntegrityError 
from tests.conftest import ConfTest

class TestPostSignatureModel(TestCase):

    @pytest.mark.django_db
    def test_post_signature_persists(self):
        post_signature = PostSignature()
        post_signature.save()

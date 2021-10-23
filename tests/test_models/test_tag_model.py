from forum.models import Tag 
from django.test import TestCase 
import pytest



class TestTagModel(TestCase):

    @pytest.mark.django_db 
    def test_tag_persists(self):
        tag = Tag()
        tag.save() 
        assert Tag.objects.count() > 0
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render 
from datetime import datetime, timezone
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.sessions.backends.db import SessionStore 
from django.shortcuts import redirect
from .forms import AddCategoryForm, AddThreadForm, SignUpForm, AddPostForm, ProfilePicForm, UpdateProfileForm, ChangePasswordForm, PostSignatureForm
from .models import Category, Thread, Post, ForumUser, PostVote, PostSignature, Tag, UserFollowing
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ObjectDoesNotExist
import logging 
import humanize
from itertools import chain
from django.db.models import Q 
from django.core import serializers
from .serializers import PostSerializer, ForumUserSerializer
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class ViewPaginatorMixin(object):
    min_limit = 1 
    max_limit = 10 

    def paginate(self, object_list, page=1, limit=10, **kwargs):
        try:
            page = int(page)
            if page < 1:
                page = 1 
        except (TypeError, ValueError):
            page = 1 

        try: 
            limit = int(limit)
            if limit < self.min_limit:
                limit = self.min_limit 
            if limit > self.max_limit:
                limit = self.max_limit 
        except (ValueError, TypeError):
            limit = self.max_limit 

        paginator = Paginator(object_list, limit)
        try: 
            objects = paginator.page(page)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
        data = {
            'previous_page': objects.has_previous() and objects.previous_page_number() or None,
            'next_page': objects.has_next() and objects.next_page_number() or None, 
            'data': list(objects)
        }
        return data 
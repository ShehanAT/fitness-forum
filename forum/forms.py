from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Image, ForumUser
from django.core.validators import validate_email
from django.contrib.auth.validators import ASCIIUsernameValidator



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')


class AddCategoryForm(forms.Form):
    category_name = forms.CharField(label='New Form Category', max_length=100)
    category_description = forms.CharField(label='New Form Description', max_length=500)
    
class AddThreadForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', max_length=500)
    
class AddPostForm(forms.Form):
    message = forms.CharField(label='Message', max_length=500)

class ForumUserForm(forms.Form):
    '''Form for the image model'''
    profic_pic = forms.ImageField(label='Profilc Picture') 

class MultiEmailField(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        return value.split(',')
    
    def validate(self, value):
        super().validate(value)
        for email in value:
            validate_email(email)

class UpdateProfileForm(UserChangeForm):
    password = None
    
    class Meta:
        model = ForumUser 
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )
    # username = ASCIIUsernameValidator()
    # email = MultiEmailField()
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # if not username:
    #     self.add_error('username', )


class ProfilePicForm(forms.Form):
    profile_pic = forms.ImageField(label='Profile Picture Upload')